import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import os


def preprocess_data(file_path):
    df = pd.read_csv(file_path)

    print("\nPreprocessing Dataset...")



    df = df.dropna()

   
    categorical_columns = [
         "Gender",
    "Marital_Status",
    "Education_Level",
    "Employment_Type",
    "Company_Type",
    "Loan_Purpose",
    "Credit_History"
    ]

    label_encoders = {}

    for column in categorical_columns:
        encoder = LabelEncoder()
        df[column] = encoder.fit_transform(df[column])

        label_encoders[column] = encoder

    X = df.drop("Loan_Status", axis=1)
    y = df["Loan_Status"]


    scaler = StandardScaler()
    print(X.select_dtypes(include="object").columns)
    X_scaled = scaler.fit_transform(X)

    
    os.makedirs("model", exist_ok=True)
    joblib.dump(scaler, "model/scaler.pkl")
    joblib.dump(label_encoders, "model/encoders.pkl")

    print("Preprocessing Completed Successfully.")
    return X_scaled, y


if __name__ == "__main__":
    X, y = preprocess_data("loan_data.csv")