# 🚀 AI Powered Invoice Intelligence System

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Regression-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Classification-purple)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Azure](https://img.shields.io/badge/Azure-Container%20Apps-0078D4)
![Swagger](https://img.shields.io/badge/API-Swagger-success)

---

# AI Powered Invoice Intelligence System

An end-to-end Machine Learning application that helps finance and procurement teams predict freight costs and identify high-risk invoices before payment.

The project follows a production-style architecture using **FastAPI** for the backend, **Streamlit** for the frontend, Docker for containerization, and **Azure Container Apps** for cloud deployment.

---

# 🌐 Live Demo

## Frontend

https://invoice-ui.salmonstone-0528ac00.centralindia.azurecontainerapps.io

## Backend API

https://invoice-api.salmonstone-0528ac00.centralindia.azurecontainerapps.io

## Swagger Documentation

https://invoice-api.salmonstone-0528ac00.centralindia.azurecontainerapps.io/docs

---

# ✨ Features

- Predict expected freight costs using Machine Learning
- Detect high-risk invoices before payment
- Interactive Streamlit dashboard
- RESTful FastAPI backend
- Automatic input validation using Pydantic
- Interactive Swagger documentation
- Dockerized application
- Cloud deployment using Azure Container Apps
- Production-ready modular architecture

---

# 📌 Project Highlights

- End-to-End Machine Learning Project
- Production-style Folder Structure
- FastAPI REST API Backend
- Interactive Streamlit Frontend
- SQL Feature Engineering using SQLite
- Freight Cost Prediction using Random Forest Regression
- Invoice Risk Detection using XGBoost Classification
- Docker Containerization
- Azure Container Apps Deployment
- Azure Container Registry Integration
- Pydantic Request Validation
- REST API Integration

---

# 💼 Business Problem

Organizations process thousands of invoices every month.

Manually validating freight charges and identifying suspicious invoices is expensive, time-consuming, and prone to human error.

## Freight Cost Leakage

Freight invoices often contain inconsistent shipping charges.

Incorrect freight invoices can result in:

- Overpayment
- Revenue leakage
- Vendor disputes
- Procurement inefficiencies

Predicting the expected freight cost allows finance teams to quickly identify invoices requiring manual verification.

---

## Invoice Risk Detection

Finance teams must identify invoices that appear unusual before payment.

Examples include:

- Quantity mismatches
- Invoice amount inconsistencies
- Delayed receiving
- Suspicious purchasing behavior

Manual auditing becomes difficult at scale.

Machine Learning helps automatically prioritize invoices for further investigation.

---

# 💡 Solution

The application combines two Machine Learning modules into one intelligent system.

## Module 1 — Freight Cost Prediction

A regression model that predicts the expected freight cost based on invoice quantity and dollar amount.

### Business Benefits

- Detect freight overcharging
- Reduce procurement cost leakage
- Improve vendor negotiations

---

## Module 2 — Invoice Risk Detection

A classification model predicts whether an invoice should be classified as:

- Normal
- High Risk

### Business Benefits

- Reduce manual auditing effort
- Detect suspicious invoices early
- Prioritize audit investigations

---

# 🏗 Application Architecture

```text
                    Streamlit Dashboard
                           │
                           │ REST API
                           ▼
                     FastAPI Backend
                           │
          ┌────────────────┴────────────────┐
          ▼                                 ▼
 Freight Cost Prediction          Invoice Risk Detection
 Random Forest Regressor           XGBoost Classifier
          │                                 │
          └────────────────┬────────────────┘
                           ▼
                    Inference Layer
                           │
                           ▼
                  Trained Machine Learning Models

☁ Cloud Deployment Architecture

                    Azure Container Apps

             ┌──────────────────────────────┐
             │     Streamlit Frontend       │
             └──────────────┬───────────────┘
                            │ REST API
                            ▼
             ┌──────────────────────────────┐
             │      FastAPI Backend         │
             └──────────────┬───────────────┘
                            │
      ┌─────────────────────┴────────────────────┐
      ▼                                          ▼
Random Forest Regressor                  XGBoost Classifier

              Azure Container Registry (ACR)

📊 Data Pipeline

The project uses SQL queries on an SQLite database to generate business-oriented features before training Machine Learning models.

Feature Engineering includes:

Purchase Order Aggregation
Invoice Aggregation
Total Item Quantity
Total Item Dollar Amount
Freight Calculations
Receiving Delay Calculation
Purchase Order Statistics

🛠 Technology Stack
| Layer                | Technology               |
| -------------------- | ------------------------ |
| Programming Language | Python                   |
| Machine Learning     | Scikit-Learn, XGBoost    |
| Backend              | FastAPI                  |
| Frontend             | Streamlit                |
| API Validation       | Pydantic                 |
| Database             | SQLite                   |
| Data Processing      | Pandas                   |
| Model Serialization  | Joblib                   |
| Containerization     | Docker                   |
| Cloud Platform       | Azure Container Apps     |
| Container Registry   | Azure Container Registry |


🤖 Machine Learning Models
Freight Cost Prediction

Regression Models Evaluated

Linear Regression
Decision Tree Regressor
Random Forest Regressor ✅ Selected
Support Vector Regressor
Invoice Risk Detection

Classification Models Evaluated

Logistic Regression
Decision Tree Classifier
Random Forest Classifier
Support Vector Machine
XGBoost ✅ Selected
## 📈 Model Performance

### Freight Cost Prediction (Linear Regression)

| Metric | Value |
|--------|-------|
| R² Score | 0.9700 |
| MAE | 24.46 |
| MSE | 15482.52 |

### Invoice Risk Detection (XGBoost Classifier)

| Metric | Value |
|--------|-------|
| Accuracy | Add Result |
| Precision | Add Result |
| Recall | Add Result |
| F1 Score | Add Result |
## 📂 Project Structure
## Project Structure

```text
project/
├── api/                          # FastAPI routes
│   ├── routes/
│   │   ├── freight.py           # Freight prediction endpoint
│   │   └── invoice.py           # Invoice prediction endpoint
│   └── schemas.py               # Pydantic models
├── frontend/                     # Streamlit dashboard
│   └── app.py
├── inference/                    # Model inference layer
│   ├── freight.py
│   ├── invoice.py
│   ├── registry.py
│   └── predict_freight.py
├── freight_cost_prediction/      # Freight training pipeline
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   ├── train.py
│   └── models/
├── invoice_flagging/             # Invoice training pipeline
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   ├── train.py
│   └── models/
├── data/                         # Training data
├── docs/                         # Documentation
├── notebooks/                    # Jupyter notebooks
├── main.py                       # FastAPI app entry
├── config.py                     # Configuration
├── requirements.txt              # Python dependencies
├── docker-compose.yml
├── Dockerfile.api
├── Dockerfile.ui
├── .gitignore
└── README.md
```
## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/adityachaudhary0/Invoice-Intelligence.git
cd Invoice-Intelligence
```

### Create Virtual Environment

**Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download Training Database

The `data/inventory.db` file is large (>400 MB) and is not included in the repository.

**Download from Google Drive:**
https://drive.google.com/file/d/1QyEnzPbb0L7zBqMBbNhq-HrxX-FcRi7G/view?usp=sharing

Place the file in the `data/` directory:
```
project/
├── data/
│   └── inventory.db      # Download and place here
└── ...
```
### Running FastAPI Backend

```bash
uvicorn main:app --reload
```

**API Documentation:** http://localhost:8000/docs

### Running Streamlit Frontend

```bash
streamlit run frontend/app.py
```

**Dashboard:** http://localhost:8501
## 🐳 Running with Docker

```bash
docker compose up --build
```

- **Frontend:** http://localhost:8501
- **Backend:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs
## 📡 API Endpoints

### GET /

Returns application information and available endpoints.

### GET /health

Returns API health status and model availability.

### POST /predict/freight

Predict expected freight cost based on invoice quantity and dollar amount.

**Request Body:**

```json
{
  "invoice_quantity": 100,
  "invoice_dollars": 5000
}
```

**Response:**

```json
{
  "predicted_freight_cost": 31.48,
  "features_used": {
    "Quantity": 100,
    "Dollars": 5000
  }
}
```

### POST /predict/invoice

Predict invoice risk flag (0 = normal, 1 = flagged).

**Request Body:**

```json
{
  "invoice_quantity": 100,
  "invoice_dollars": 5000,
  "freight": 50,
  "total_item_quantity": 100,
  "total_item_dollars": 5000
}
```

**Response:**

```json
{
  "flag_invoice": 0,
  "label": "normal",
  "probability": 0.85
}
```

## 📸 Screenshots
- **Home Page** - (Coming soon)
- **Freight Cost Prediction** - (Coming soon)
- **Freight Prediction Result** - (Coming soon)
- **Invoice Risk Prediction** - (Coming soon)
- **Invoice Prediction Result** - (Coming soon)
- **Swagger Documentation** - (Coming soon)
- **Azure Container Apps Deployment** - (Coming soon)

## 🚀 Future Improvements
GitHub Actions CI/CD Pipeline
JWT Authentication
Role-Based Access Control
Batch Invoice Prediction
SHAP Model Explainability
MLflow Integration
Azure Blob Storage
Model Monitoring
Prediction History Dashboard
Cloud Database Integration
## 👨‍💻 Author

**Aditya Chaudhary**

- Education: B.Tech Artificial Intelligence & Machine Learning, IMS Engineering College
- GitHub: https://github.com/adityachaudhary0
- LinkedIn: (Add Your LinkedIn Profile URL)
