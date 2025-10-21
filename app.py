import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Load model
model = pickle.load(open('pm2.5_model.pkl', 'rb'))

def generate_insights(pm25_value):
    """
    Returns actionable insights based on PM2.5 value.
    """
    insights = []

    if pm25_value <= 12:
        insights.append("Air quality is Good. Safe for all outdoor activities.")
        insights.append("Children and elderly can continue daily outdoor routines safely.")
        insights.append("Keep windows open for natural ventilation indoors.")
    elif 12 < pm25_value <= 35.4:
        insights.append("Air quality is Moderate. Sensitive groups should take caution.")
        insights.append("Consider reducing prolonged outdoor exertion if you have respiratory issues.")
        insights.append("Maintain indoor plants to help naturally purify air.")
    elif 35.4 < pm25_value <= 55.4:
        insights.append("Air quality is Unhealthy for Sensitive Groups. Limit prolonged outdoor exposure.")
        insights.append("Use a mask if you need to be outdoors, especially if you have asthma or heart conditions.")
        insights.append("Close windows during high pollution periods and use indoor air purifiers if available.")
    elif 55.4 < pm25_value <= 150.4:
        insights.append("Air quality is Unhealthy. Everyone may experience health effects. Avoid outdoor activities.")
        insights.append("Postpone outdoor exercises and limit exposure to polluted areas.")
        insights.append("Ensure air purifiers or AC filters are clean and functioning indoors.")
    elif 150.4 < pm25_value <= 250.4:
        insights.append("Air quality is Very Unhealthy. Minimize all outdoor activities. Wear a mask if necessary.")
        insights.append("Sensitive individuals should remain indoors and avoid any outdoor exertion.")
        insights.append("Monitor local AQI updates frequently and keep emergency contacts ready if needed.")
    else:
        insights.append("Air quality is Hazardous. Stay indoors and avoid any outdoor activity.")
        insights.append("Use high-quality HEPA air purifiers and wear N95 masks if leaving home is unavoidable.")
        insights.append("Check on vulnerable family members and pets to ensure their safety.")

    # Extra recommendations based on trend and PM2.5 level
    if pm25_value > 50:
        insights.append("Avoid burning wood, incense, or using heavy cooking smoke indoors to reduce indoor pollution.")
    if pm25_value > 100:
        insights.append("Consider using indoor air quality monitors to track PM2.5 levels in real-time.")
    if pm25_value > 150:
        insights.append("Stay hydrated and maintain a healthy diet to help reduce respiratory stress.")

    return insights

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_data = request.form.to_dict()

        # Numeric fields
        numeric_fields = ["BP","RH","WD","WS","CO","NO2","Ozone","SO2","TEMPARATURE"]
        features = [float(form_data[field]) for field in numeric_fields]

        # Convert dates into year, month, day
        from_date = datetime.strptime(form_data["from_date"], "%Y-%m-%d")
        to_date = datetime.strptime(form_data["to_date"], "%Y-%m-%d")
        features.extend([
            float(from_date.year),
            float(from_date.month),
            float(from_date.day),
            float(to_date.year),
            float(to_date.month),
            float(to_date.day)
        ])

        final_input = np.array(features).reshape(1, -1)
        prediction = model.predict(final_input)[0]
        insights = generate_insights(prediction)

        return render_template(
            "result.html",
            prediction_text=f"Predicted PM2.5 Concentration: {prediction:.2f} µg/m³",
            insights=insights
        )
    except Exception as e:
        return render_template("result.html", prediction_text=f"Error: {str(e)}", insights=[])

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = request.json['data']
        new_data = np.array(list(data.values())).reshape(1, -1)
        output = model.predict(new_data)[0]
        return jsonify({"PM2.5_prediction": round(float(output), 2)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)