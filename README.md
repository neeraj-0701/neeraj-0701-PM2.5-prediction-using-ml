<<<<<<< HEAD
# AIR QUALITY PM2.5 PREDICTION MODEL USING MACHINE LEARNING AND FLASK WEB APP
## 1. Project Title / Headline
🌫️ **Air Quality PM2.5 Prediction Web App**  
A Flask-based, interactive web application that predicts PM2.5 levels in the environment using machine learning, helping users monitor air pollution trends in real-time.

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

## 6. Screenshots 📸

### 🔹 Home Page Part-1
![Home Page](https://github.com/neeraj-0701/neeraj-0701-PM2.5-prediction-using-ml/blob/main/Snapshot%20Of%20Home%20Page1.png)



### 🔹 Home Page Part-2
![Home Page](https://github.com/neeraj-0701/neeraj-0701-PM2.5-prediction-using-ml/blob/main/Snapshot%20of%20Homepage(2).png)


### 🔹 Prediction Result
![Prediction Result](https://github.com/neeraj-0701/neeraj-0701-PM2.5-prediction-using-ml/blob/main/Snapshot%20of%20Prediction%20Result.png)

=======
# neeraj-0701-PM2.5-prediction-using-ml
mlproject\Scripts\activate
pip install flask scikit-learn numpy pandas matplotlib
git add README.md pm2.5_model.pkl "PM2.5 PREDICTION.ipynb"
git commit -m "Added README, notebook, model file, and requirements"
git push origin main
>>>>>>> 57a88c4 (Save all local changes before pull)
