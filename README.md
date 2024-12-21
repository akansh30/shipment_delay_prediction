# Shipment Delay Prediction Project

![Screenshot 2024-12-22 031054](https://github.com/user-attachments/assets/8d7bb2e4-4a10-4ddc-b41f-dad18ff8f6c0)
![Screenshot 2024-12-22 031821](https://github.com/user-attachments/assets/fb587535-4cdb-4e5d-a1fb-c18d83db0a9a)

## Project Description
This project focuses on predicting shipment delays using machine learning. It includes three main stages:
1. **Data Preparation & Exploration**: Cleaning the dataset, handling missing values, and performing exploratory data analysis (EDA) to identify useful features.
2. **Model Development**: Building a classification model to predict delays and experimenting with at least two machine learning algorithms (e.g., Logistic Regression, Decision Tree, Random Forest). Evaluation is performed using metrics like accuracy, precision, recall, and F1 score.
3. **Deployment**: Creating an API using FastAPI to accept shipment details and return a prediction (Delayed/On Time).

---

## How to Set Up and Run the Project

### Step 1: Clone the Repository
```bash
https://github.com/akansh30/shipment_delay_prediction.git
```
### Step 2: Navigate to the Deployment Folder
```bash
cd shipment_delay_prediction/fastapi_deployment
```
### Step 3: Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/Scripts/activate
```
### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 5: Train and Save the Model

1.Open the shipment.ipynb file in a Jupyter Notebook environment.
2.Train the logistic regression model.
3.Save the trained model as a .pkl file.
4.Create a models folder inside the fastapi_deployment directory.
5.Place the saved model in the models folder.

### Step 6: Start the API Server
```bash
cd fastapi_deployment
uvicorn main:app --reload
```
### You should see the following message:
```bash
{"message":"Welcome to the Shipment Prediction API"}
```

### Access the API at: 
```bash
http://127.0.0.1:8000/
```

### Step 7: Test the API Using Postman

1.Open Postman.
2.Create a new POST request.
3.Set the URL to:
```bash
http://127.0.0.1:8000/predict/
```
4.In the request body (JSON format), provide the following sample data:
```bash
{
    "distance": 1863,
    "delivery_duration": 6,
    "planned_vs_actual_delay": 0
}
```
5.Send the request.
6.You will receive the response:
```bash
{
    "log_reg_prediction": "On Time"
}
```
This indicates a correct prediction by the logistic regression model.
