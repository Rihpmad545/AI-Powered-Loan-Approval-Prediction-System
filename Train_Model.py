import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from PreProcess import preprocess_data


def train_models():

    X, y = preprocess_data("loan_data.csv")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"\nLogistic Regression Accuracy: {accuracy:.4f}")

    if not os.path.exists("model"):
        os.mkdir("model")

    joblib.dump(model, "model/loan_model.pkl")

    print("\nModel Saved Successfully")


if __name__ == "__main__":
    train_models()