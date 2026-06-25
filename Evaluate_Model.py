import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

from PreProcess import preprocess_data


def evaluate_model():

    X, y = preprocess_data("loan_data.csv")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("\nCross Validation Results")

    model = DecisionTreeClassifier(random_state=42)

    scores = cross_val_score(
        model,
        X,
        y,
        cv=5
    )

    print("Scores:", scores)
    print("Average Score:", scores.mean())

    print("\nRunning Grid Search...")

    parameters = {
        "max_depth": [3, 5, 10, None],
        "min_samples_split": [2, 5, 10]
    }

    grid_search = GridSearchCV(
        DecisionTreeClassifier(random_state=42),
        parameters,
        cv=5
    )

    grid_search.fit(X_train, y_train)

    print("Best Parameters:")
    print(grid_search.best_params_)

    best_model = grid_search.best_estimator_

    predictions = best_model.predict(X_test)

    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, predictions))

    print("\nClassification Report")
    print(classification_report(y_test, predictions))

    probabilities = best_model.predict_proba(X_test)[:, 1]

    auc_score = roc_auc_score(y_test, probabilities)

    print("\nROC-AUC Score:", auc_score)

    fpr, tpr, thresholds = roc_curve(
        y_test,
        probabilities
    )

    plt.plot(fpr, tpr)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.show()

    joblib.dump(best_model, "model/best_decision_tree.pkl")

    print("\nEvaluation Complete")


if __name__ == "__main__":
    evaluate_model()