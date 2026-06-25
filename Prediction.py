import joblib
import pandas as pd


def predict_loan():

    model = joblib.load("model/loan_model.pkl")
    scaler = joblib.load("model/scaler.pkl")
    encoders = joblib.load("model/encoders.pkl")

    print("\nENTER APPLICANT DETAILS\n")

    age = int(input("Age: "))
    gender = input("Gender (Male/Female): ")
    marital_status = input("Marital Status (Single/Married): ")
    dependents = int(input("Number of Dependents: "))
    education = input("Education Level: ")

    employment = input("Employment Type: ")
    company_type = input("Company Type: ")

    work_exp = int(input("Work Experience (Years): "))

    monthly_income = float(input("Monthly Income: "))
    annual_income = monthly_income * 12

    existing_loans = int(input("Existing Loans: "))
    existing_emi = float(input("Existing EMI: "))

    credit_score = int(input("Credit Score: "))
    credit_history = input("Credit History (Good/Bad): ")

    bank_balance = float(input("Bank Balance: "))

    loan_amount = float(input("Loan Amount Requested: "))
    loan_purpose = input("Loan Purpose: ")

    loan_term = int(input("Loan Term (Years): "))
    interest_rate = float(input("Interest Rate: "))

    data = pd.DataFrame([{
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
        data[column] = encoders[column].transform(data[column])

    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)

    if prediction[0] == 1:
        print("\nLoan Approved")
    else:
        print("\nLoan Rejected")


if __name__ == "__main__":
    predict_loan()