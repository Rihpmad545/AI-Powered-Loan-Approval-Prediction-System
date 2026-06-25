# 🏦 AI-Powered Loan Approval Prediction System

A complete Loan Approval Prediction System built using Machine Learning, Flask, C Programming, and Ollama LLM integration.

The system predicts loan approval status, calculates approval probability, estimates EMI using a C-based module, analyzes financial strength, visualizes loan metrics, and generates AI-powered loan recommendations using Llama 3.2 running locally through Ollama.

---

# 🚀 Features

✅ Loan Approval Prediction

✅ Approval Probability Score

✅ EMI Calculation using C Programming

✅ Financial Strength Analysis

✅ Credit Score Analysis

✅ Interactive Data Visualization

✅ AI-Powered Loan Analysis using Ollama + Llama 3.2

✅ Responsive Corporate UI

✅ Real-Time Loan Decision Support

---

# 🛠 Technologies Used

## Backend

* Python
* Flask
* Pandas
* NumPy
* Joblib
* Requests

## Machine Learning

* Logistic Regression
* Decision Tree
* K-Nearest Neighbors (KNN)
* Bagging Classifier
* Scikit-Learn

## Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

## AI Integration

* Ollama
* Llama 3.2

## Systems Programming

* C Programming
* Python-C Integration

---

# 📂 Project Structure

```text
AI_Project_3
│
├── app.py
├── Prediction.py
├── Train_Model.py
├── Evaluate_Model.py
├── PreProcess.py
│
├── generate_dataset.py
├── loan_data.csv
│
├── Analysis.py
├── Visuals.py
│
├── k_means_analysis.py
├── hierarchy.py
│
├── emi_calculator.c
├── emi_calculator.exe
├── emi_interface.py
│
├── model/
│   ├── loan_model.pkl
│   ├── scaler.pkl
│   ├── encoders.pkl
│   └── best_decision_tree.pkl
│
├── templates/
│   ├── html_temp.html
│   └── result.html
│
├── static/
│   └── style.css
```

---

# ⚙️ System Workflow

1. User enters loan application details.
2. Data is preprocessed and encoded.
3. Machine Learning model predicts approval.
4. Approval probability is calculated.
5. EMI is calculated using a C module.
6. Financial strength score is generated.
7. Graphical analysis is displayed.
8. Llama 3.2 generates AI-powered loan recommendations.

---

# 📊 Input Parameters

* Age
* Gender
* Marital Status
* Dependents
* Education
* Employment Type
* Company Type
* Work Experience
* Monthly Income
* Existing Loans
* Existing EMI
* Credit Score
* Credit History
* Bank Balance
* Loan Amount Requested
* Loan Purpose
* Loan Term
* Interest Rate

---

# 🤖 AI Loan Analysis

The system uses Ollama and Llama 3.2 to generate:

* Summary
* Pros
* Cons
* Recommendation

based on the applicant's financial profile.

---

# 📈 Machine Learning Models Evaluated

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 85%+     |
| Decision Tree       | 99%+     |
| KNN                 | 79%+     |
| Bagging Classifier  | 99%+     |

Logistic Regression is used for probability-based prediction.

---

# 💻 Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Ollama:

```bash
ollama run llama3.2:latest
```

Start Flask:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# 🔮 Future Enhancements

* User Authentication
* Database Integration
* PDF Loan Reports
* Email Notifications
* Explainable AI (SHAP)
* Real Banking Dataset Integration
* Loan Eligibility Dashboard

---

# 👨‍💻 Author

Shreeyash Sawant

Mumbai, India

---

⭐ If you found this project useful, consider giving it a star.
