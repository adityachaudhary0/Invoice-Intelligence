# AI Powered Invoice Intelligence System

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Regression-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Classification-purple)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![Azure](https://img.shields.io/badge/Azure-Deployment-blue)

---

# AI Powered Invoice Intelligence System

An end-to-end Machine Learning application that helps finance and procurement teams identify freight cost leakage and automatically detect high-risk invoices before payment.

The application is built using **FastAPI** as the backend API, **Streamlit** as the interactive frontend dashboard, and is designed using a production-style modular architecture suitable for deployment on Microsoft Azure.

---

# Live Demo

**Frontend**

> Add Azure Streamlit URL here

**Backend API**

> Add Azure FastAPI URL here

**Swagger Documentation**

> Add Azure Swagger URL here

---

# Project Highlights

- End-to-End Machine Learning Project
- Production-style Project Structure
- FastAPI REST API Backend
- Interactive Streamlit Dashboard
- SQL Feature Engineering using SQLite
- Freight Cost Prediction using Random Forest Regression
- Invoice Risk Detection using XGBoost Classification
- Azure Deployment Ready
- Modular Architecture
- Input Validation using Pydantic
- REST API Integration

---

# Business Problem

Organizations process thousands of purchase invoices every month.

Manually validating freight charges and identifying suspicious invoices is expensive, time-consuming, and prone to human error.

### Invoice Cost Leakage

Freight charges often vary across vendors and purchase orders.

Incorrect freight invoices can lead to:

- Overpayment
- Revenue leakage
- Vendor disputes
- Procurement inefficiencies

Predicting the expected freight cost allows finance teams to identify invoices that require manual review.

---

### Invoice Audit Risk

Finance teams also need to identify invoices that appear unusual before payment.

Examples include:

- Quantity mismatches
- Invoice amount inconsistencies
- Delayed receiving
- Suspicious purchasing behavior

Manual auditing becomes impossible when processing thousands of invoices.

Machine Learning enables automatic identification of invoices that deserve additional investigation.

---

# Solution

This project combines two Machine Learning modules into a single application.

## Module 1 — Freight Cost Prediction

Regression model that predicts the expected freight cost based on invoice and purchase order information.

Business Benefit

- Detect freight overcharging
- Reduce cost leakage
- Improve procurement decisions

---

## Module 2 — Invoice Risk Detection

Classification model that predicts whether an invoice should be considered:

- Normal
- High Risk

Business Benefit

- Reduce manual auditing effort
- Detect suspicious invoices early
- Prioritize audit investigations

---

# Application Architecture

```text
                        Streamlit Dashboard
                               │
                               │ REST API
                               ▼
                         FastAPI Backend
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
      Freight Cost Prediction       Invoice Risk Detection
          Random Forest                 XGBoost
                │                             │
                └──────────────┬──────────────┘
                               ▼
                       Inference Layer
                               │
                               ▼
                     Trained ML Models
```

---

# Data Pipeline

The project uses SQL queries on an SQLite database to generate business-oriented features before training the Machine Learning models.

Feature Engineering includes:

- Purchase Order Aggregation
- Invoice Aggregation
- Total Item Quantity
- Total Item Dollar Amount
- Freight Calculations
- Receiving Delay Calculation
- Purchase Order Statistics

---

# Technology Stack

| Layer | Technology |
|--------|------------|
| Programming Language | Python |
| Machine Learning | Scikit-Learn, XGBoost |
| Backend | FastAPI |
| Frontend | Streamlit |
| API Validation | Pydantic |
| Database | SQLite |
| Data Processing | Pandas |
| Model Serialization | Joblib |
| Deployment | Microsoft Azure |

---

# Machine Learning Models

## Freight Cost Prediction (Regression)

Models Evaluated

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor ✅ Selected
- Support Vector Regression

---

## Invoice Risk Detection (Classification)

Models Evaluated

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine
- XGBoost ✅ Selected

---

# Model Performance

## Freight Cost Prediction

| Model | R² Score |
|--------|-----------|
| Linear Regression | Add Result |
| Decision Tree | Add Result |
| Random Forest | Add Result |
| Support Vector Regression | Add Result |

---

## Invoice Risk Detection

| Model | Accuracy | Precision | Recall | F1 Score |
|--------|-----------|-----------|-----------|-----------|
| Logistic Regression | Add Result | Add Result | Add Result | Add Result |
| Decision Tree | Add Result | Add Result | Add Result | Add Result |
| Random Forest | Add Result | Add Result | Add Result | Add Result |
| XGBoost | Add Result | Add Result | Add Result | Add Result |

---

# Project Structure

```text
project/
│
├── api/
├── frontend/
├── inference/
├── freight_cost_prediction/
├── invoice_flagging/
├── data/
├── docs/
├── notebooks/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

cd YOUR_REPOSITORY
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Train Models

The trained models are intentionally excluded from the repository.

Generate them locally.

```bash
python freight_cost_prediction/train.py

python invoice_flagging/train.py
```

---

# Running FastAPI

```bash
uvicorn main:app --reload
```

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Running Streamlit

```bash
streamlit run frontend/app.py
```

---

# API Endpoints

## GET /

Returns application information.

---

## GET /health

Returns API health status.

---

## POST /predict/freight

Predict expected freight cost.

Request body example:

```json
{
  "invoice_quantity": 100,
  "invoice_dollars": 5000,
  "days_po_to_invoice": 5,
  "total_item_quantity": 100,
  "total_item_dollars": 5000
}
```

---

## POST /predict/invoice

Predict invoice risk.

---

# Screenshots

## Screenshot: Home Page

(Add screenshot here)

---

## Screenshot: Freight Cost Prediction

(Add screenshot here)

---

## Screenshot: Freight Prediction Result

(Add screenshot here)

---

## Screenshot: Invoice Risk Prediction

(Add screenshot here)

---

## Screenshot: Invoice Prediction Result

(Add screenshot here)

---

## Screenshot: FastAPI Swagger Documentation

(Add screenshot here)

---

## Screenshot: Azure Deployment

(Add screenshot here)

---

# Future Improvements

- Docker Support
- Azure Container Apps Deployment
- CI/CD using GitHub Actions
- Authentication using JWT
- Batch Invoice Prediction
- SHAP Explainability
- Model Monitoring
- Automatic Retraining Pipeline
- Azure Blob Storage for Model Artifacts
- Cloud Database Integration
- Logging & Monitoring
- MLflow Integration

---

# Author

**Aditya Chaudhary**

B.Tech Artificial Intelligence & Machine Learning

IMS Engineering College

GitHub

> Add GitHub Profile

LinkedIn

> Add LinkedIn Profile

---

# License

This project is licensed under the MIT License.