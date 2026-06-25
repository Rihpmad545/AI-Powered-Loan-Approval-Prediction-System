import pandas as pd
import numpy as np
import random

np.random.seed(42)

rows = 10000

data = {
    "Age": np.random.randint(21, 61, rows),

    "Gender": np.random.choice(
        ["Male", "Female"],
        rows
    ),

    "Marital_Status": np.random.choice(
        ["Single", "Married"],
        rows
    ),

    "Dependents": np.random.randint(0, 6, rows),

    "Education_Level": np.random.choice(
        ["High School", "Graduate", "Post Graduate"],
        rows
    ),

    "Employment_Type": np.random.choice(
        ["Salaried", "Self Employed"],
        rows
    ),

    "Company_Type": np.random.choice(
        ["Private", "Government", "Business"],
        rows
    ),

    "Work_Experience_Years": np.random.randint(0, 35, rows),

    "Monthly_Income": np.random.randint(
        20000,
        300000,
        rows
    ),

    "Annual_Income": np.random.randint(
        240000,
        3600000,
        rows
    ),

    "Existing_Loans": np.random.randint(0, 5, rows),

    "Existing_EMI": np.random.randint(
        0,
        50000,
        rows
    ),

    "Credit_Score": np.random.randint(
        300,
        901,
        rows
    ),

    "Credit_History": np.random.choice(
        ["Good", "Bad"],
        rows,
        p=[0.8, 0.2]
    ),

    "Bank_Balance": np.random.randint(
        10000,
        5000000,
        rows
    ),

    "Loan_Amount_Requested": np.random.randint(
        50000,
        5000000,
        rows
    ),

    "Loan_Purpose": np.random.choice(
        [
            "Home",
            "Car",
            "Education",
            "Business",
            "Personal"
        ],
        rows
    ),

    "Loan_Term_Years": np.random.randint(
        1,
        31,
        rows
    ),

    "Interest_Rate": np.round(
        np.random.uniform(7.0, 18.0, rows),
        2
    )
}

df = pd.DataFrame(data)

# Create realistic loan approval logic
approval_score = (
    (df["Credit_Score"] > 650).astype(int)
    + (df["Monthly_Income"] > 50000).astype(int)
    + (df["Existing_Loans"] < 3).astype(int)
    + (df["Bank_Balance"] > 100000).astype(int)
    + (df["Work_Experience_Years"] > 2).astype(int)
)

df["Loan_Status"] = np.where(
    approval_score >= 4,
    1,
    0
)
df.to_csv("loan_data.csv", index=False)

print("loan_data.csv generated successfully!")
print(f"Total Records: {len(df)}")