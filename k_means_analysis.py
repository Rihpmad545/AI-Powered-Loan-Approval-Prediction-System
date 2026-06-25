import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def perform_kmeans():

    print("\nRunning K-Means Clustering...\n")

    df = pd.read_csv("loan_data.csv")

    features = df[
        [
            "Monthly_Income",
            "Credit_Score",
            "Bank_Balance",
            "Loan_Amount_Requested"
        ]
    ]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    df["Cluster"] = kmeans.fit_predict(scaled_features)

    print("Applicants in Each Cluster:\n")
    print(df["Cluster"].value_counts().sort_index())

    summary = df.groupby("Cluster")[
        [
            "Monthly_Income",
            "Credit_Score",
            "Bank_Balance",
            "Loan_Amount_Requested"
        ]
    ].mean()

    print("\nCluster Summary:\n")
    pd.set_option("display.max_columns", None)
    print(summary.round(2))

    plt.figure(figsize=(8, 6))

    for cluster in sorted(df["Cluster"].unique()):

        cluster_data = df[df["Cluster"] == cluster]

        plt.scatter(
            cluster_data["Monthly_Income"],
            cluster_data["Credit_Score"],
            label=f"Cluster {cluster}",
            alpha=0.7
        )

    plt.title("K-Means Customer Segmentation")
    plt.xlabel("Monthly Income")
    plt.ylabel("Credit Score")

    plt.legend()
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    perform_kmeans()