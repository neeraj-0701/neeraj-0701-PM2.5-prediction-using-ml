<<<<<<< HEAD
# neeraj-0701-PM2.5-prediction-using-ml
mlproject\Scripts\activate
pip install flask scikit-learn numpy pandas matplotlib
git add README.md pm2.5_model.pkl "PM2.5 PREDICTION.ipynb"
git commit -m "Added README, notebook, model file, and requirements"
git push origin main
   'BP'
    'RH':
    'WD':,
    'WS': 
    'CO': 
    'NO2': 
    'Ozone':
    'SO2':
    'TEMPARATURE'
    'from_year'
    'from_month',
    'from_day',
    'to_year'
    'to_month'
    'to_day': 
=======

# AIR QUALITY PM2.5 PREDICTION MODEL USING MACHINE LEARNING AND FLASK WEB APP
## 1. Project Title / Headline
🌫️ **Air Quality PM2.5 Prediction Web App**  
A Flask-based, interactive web application that predicts PM2.5 levels in the environment using machine learning, helping users monitor air pollution trends in real-time.

🌐 **Live App:** [Air Quality PM2.5 Prediction](https://neeraj-0701-pm2-5-prediction-using-ml.onrender.com)

---

## 2. Short Description / Purpose
The Air Quality PM2.5 Prediction Web App is designed to provide quick and accurate predictions of PM2.5 levels using user-provided air quality parameters. This tool is intended for environmental analysts, health researchers, urban planners, and citizens who want to understand and respond to air pollution in their area.

---

## 3. Tech Stack
The application was built using the following technologies:  
- 🐍 **Python** – Core programming language  
- 🧠 **Scikit-learn** – Machine learning model development  
- 📊 **Pandas / NumPy** – Data manipulation  
- 📝 **HTML / CSS** – Web interface design  
- 📂 **Flask** – Web framework for the app  
- 📦 **Pickle** – Model serialization  
- ☁️ **Heroku (optional)** – For deployment

---

## 4. Data Source
- **Source:** Central Pollution Control Board (CPCB) and IMD air quality datasets  
- **Data Structure:**  
  - Features include air quality indicators such as PM2.5, PM10, NO2, SO2, CO, temperature, humidity, and wind speed.  
  - Target variable: **PM2.5 concentration**  
  - Stored as CSV (`Air_Quality_Data.csv`) and used to train the ML model (`pm2.5_model.pkl`).

---

## 5. Features / Highlights
- Real-time prediction of PM2.5 levels via a user-friendly web interface.  
- Pre-trained machine learning model for quick and accurate predictions.  
- Interactive HTML templates to input data and view results instantly.  
- Easily deployable on Heroku or any cloud platform.  
- Provides insights for environmental monitoring and pollution mitigation strategies.  

---

## 6. Model Details

Model type: [XGBoost]

Input features: PM10, NO2, SO2, CO, temperature, humidity, wind speed, etc.

Target: PM2.5 concentration

Trained on: Air_Quality_Data.csv

Saved model: pm2.5_model.pkl

## 7. Deployment

The app is deployed on Render and accessible online.

Deployment uses the Procfile and all dependencies listed in requirements.txt.

Users can access the app via the live link below.

## 8.Live Demo

🌐 **Live App:** [Air Quality PM2.5 Prediction](https://neeraj-0701-pm2-5-prediction-using-ml.onrender.com)


## 9. Screenshots 📸

### 🔹 Home Page Part-1
![Home Page](https://github.com/neeraj-0701/neeraj-0701-PM2.5-prediction-using-ml/blob/main/Snapshot%20Of%20Home%20Page1.png)



### 🔹 Home Page Part-2
![Home Page](https://github.com/neeraj-0701/neeraj-0701-PM2.5-prediction-using-ml/blob/main/Snapshot%20of%20Homepage(2).png)


### 🔹 Prediction Result
![Prediction Result](https://github.com/neeraj-0701/neeraj-0701-PM2.5-prediction-using-ml/blob/main/Snapshot%20of%20Prediction%20Result.png)

>>>>>>> 664c3e629d434edc3f1ac2f41ca3710810a1685e
