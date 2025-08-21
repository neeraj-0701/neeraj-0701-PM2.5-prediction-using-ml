import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

# Initialize Flask app
app = Flask(__name__)

# Load only model
model = pickle.load(open('pm2.5_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        features = [float(x) for x in request.form.values()]
        final_input = np.array(features).reshape(1, -1)

        prediction = model.predict(final_input)[0]

        return render_template(
            "result.html",
            prediction_text=f"Predicted PM2.5 Concentration: {prediction:.2f} µg/m³"
        )
    except Exception as e:
        return render_template("result.html", prediction_text=f"Error: {str(e)}")

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
