from flask import Flask, render_template, request
import joblib
import pandas as pd
import requests

app = Flask(__name__)

model = joblib.load("model/loan_model.pkl")
scaler = joblib.load("model/scaler.pkl")
encoders = joblib.load("model/encoders.pkl")

def get_ai_analysis(
    result,
    probability,
    credit_score,
    monthly_income,
    bank_balance,
    loan_amount,
    risk_level
):

    prompt = f"""
You are a professional loan analyst.

Loan Decision: {result}
Approval Probability: {probability:.2f}%
Credit Score: {credit_score}
Monthly Income: ₹{monthly_income}
Bank Balance: ₹{bank_balance}
Loan Amount Requested: ₹{loan_amount}
Risk Level: {risk_level}

Provide only:

1. Summary
2. Pros (maximum 3)
3. Cons (maximum 3)

IMPORTANT:
- Use the numerical values provided.
- Do not invent risks.
- Do not state false comparisons.
- If there are no significant cons, say "No major concerns identified."
- Keep response under 150 words.

4. Recommendation
"""

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:latest",
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        return response.json()["response"]

    except Exception as e:

        return f"AI Analysis Unavailable: {str(e)}"

@app.route("/")
def home():
    return render_template("html_temp.html")


@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])

    gender = request.form["gender"].strip()
    marital_status = request.form["marital_status"].strip()

    dependents = int(request.form["dependents"])

    education = request.form["education"].strip()

    employment = request.form["employment"].strip()
    company_type = request.form["company_type"].strip()

    work_exp = int(request.form["work_exp"])

    monthly_income = float(request.form["monthly_income"])
    annual_income = monthly_income * 12

    existing_loans = int(request.form["existing_loans"])
    existing_emi = float(request.form["existing_emi"])

    credit_score = int(request.form["credit_score"])
    credit_history = request.form["credit_history"].strip()

    bank_balance = float(request.form["bank_balance"])

    loan_amount = float(request.form["loan_amount"])
    loan_purpose = request.form["loan_purpose"].strip()

    loan_term = int(request.form["loan_term"])
    interest_rate = float(request.form["interest_rate"])

    applicant = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Marital_Status": marital_status,
        "Dependents": dependents,
        "Education_Level": education,
        "Employment_Type": employment,
        "Company_Type": company_type,
        "Work_Experience_Years": work_exp,
        "Monthly_Income": monthly_income,
        "Annual_Income": annual_income,
        "Existing_Loans": existing_loans,
        "Existing_EMI": existing_emi,
        "Credit_Score": credit_score,
        "Credit_History": credit_history,
        "Bank_Balance": bank_balance,
        "Loan_Amount_Requested": loan_amount,
        "Loan_Purpose": loan_purpose,
        "Loan_Term_Years": loan_term,
        "Interest_Rate": interest_rate
    }])

    categorical_columns = [
        "Gender",
        "Marital_Status",
        "Education_Level",
        "Employment_Type",
        "Company_Type",
        "Loan_Purpose",
        "Credit_History"
    ]

    for column in categorical_columns:
        applicant[column] = encoders[column].transform(
            applicant[column]
        )

    applicant_scaled = scaler.transform(applicant)

    prediction = model.predict(applicant_scaled)[0]

    probability = model.predict_proba(
        applicant_scaled
    )[0][1] * 100

    if prediction == 1:
        result = "Loan Approved"
    else:
        result = "Loan Rejected"

    if probability >= 90:
        risk_level = "Low Risk"
    elif probability >= 70:
        risk_level = "Medium Risk"
    else:
        risk_level = "High Risk"

    analysis = get_ai_analysis(
    result,
    probability,
    credit_score,
    monthly_income,
    bank_balance,
    loan_amount,
    risk_level
)

    monthly_rate = interest_rate / (12 * 100)
    months = loan_term * 12

    emi = (
        loan_amount
        * monthly_rate
        * ((1 + monthly_rate) ** months)
    ) / (
        ((1 + monthly_rate) ** months) - 1
    )

    financial_strength = (
        (monthly_income * 0.0002)
        + (bank_balance * 0.00005)
        - (existing_emi * 0.0005)
    )

    financial_strength = max(
        0,
        min(100, financial_strength)
    )

    return render_template(
        "result.html",
        result=result,
        ai_analysis=analysis,
        probability=round(probability, 2),
        risk_level=risk_level,
        emi=round(emi, 2),
        credit_score=credit_score,
        financial_strength=round(financial_strength, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)