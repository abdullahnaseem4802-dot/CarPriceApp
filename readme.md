# 🚗 Used Car Price Prediction App

This project is a **web-based application** that predicts the price of used cars based on various features such as manufacturer, model, year, condition, fuel type, transmission, and more. The app uses a **pre-trained machine learning model** to estimate the expected car price, allowing users to quickly evaluate car values.

---

## **Features**

* **Dynamic Dropdowns:** Select manufacturer and model dynamically; models change based on selected manufacturer.
* **Multiple Car Attributes:** Input car condition, cylinders, fuel type, transmission, drive type, size, type, paint color, state, and region.
* **Numeric Inputs:** Specify car year and odometer reading.
* **Price Prediction:** Predict the estimated car price with one click using the trained machine learning model.
* **User-friendly Interface:** Built with Streamlit for an interactive, easy-to-use web interface.

---

## **Dataset & Model**

* **Dataset Source:** The dataset used to train the model was collected from publicly available used car listings.
  *You can access the dataset here:  
  [Used Car Price Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset)*
* **Model:** The pre-trained machine learning regression model is saved as `model.pkl`.
* **Dropdown Values:** Pre-computed dropdown values for all features are saved in `dropdown_values.pkl`.

> **Note:** Users **do not need the original dataset** to run the app — the `model.pkl` and `dropdown_values.pkl` files are included in the repository.

---

## **Tech Stack**

* **Python** (pandas, numpy, scikit-learn, joblib)
* **Streamlit** for interactive web app
* **Machine Learning** for price prediction (pre-trained regression model)

---

## **Getting Started**

### **Prerequisites**

* Python 3.11 or higher
* Git (optional, if cloning the repository)
* Internet browser to view the app

---

## **Installation & Setup**

1. **Clone the repository or download ZIP**

```bash
git clone https://github.com/abdullahnaseem4802-dot/CarPriceApp.git
cd CarPriceApp
```

* Or download the ZIP and extract it.

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

* **Windows (PowerShell):**

```bash
.\venv\Scripts\activate
```

* **macOS/Linux:**

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## **Run the App**

```bash
streamlit run app.py
```

* The app will open in your default browser at:

```
http://localhost:8501
```

---

## **Using the App**

* Select **Manufacturer** → the **model** dropdown updates automatically.
* Fill in other dropdowns and numeric fields (year, odometer).
* Click **Predict Price** → the estimated car price will display.

---

## **Requirements**

`requirements.txt` should include:

```
streamlit>=1.30.0
pandas>=2.1.0
numpy>=1.25.0
scikit-learn>=1.3.0
joblib>=1.3.2
```

---

## **Folder Structure**

```
CarPriceApp/
│
├── app.py                 # Main Streamlit app
├── model.pkl              # Pre-trained ML model
├── dropdown_values.pkl    # Dropdown values for form inputs
├── requirements.txt       # Python dependencies
└── README.md              # Project description & instructions
```

---

## **Notes**

* Make sure `model.pkl` and `dropdown_values.pkl` are in the same folder as `app.py`.
* For Windows users: if Streamlit is not recognized, run with full path:

```bash
C:\Users\RAJA\AppData\Roaming\Python\Python311\Scripts\streamlit.exe run app.py
```

* Use a virtual environment to avoid dependency conflicts.

---

## **Contributing**

* Fork the repository.
* Make your changes or add new features.
* Submit a pull request.

---

## **Author**

Abdullah Naseem
