import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage


def perform_hierarchical_clustering():

    print("\nRunning Hierarchical Clustering...\n")

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

    sample_data = scaled_features[:200]

    linked = linkage(
        sample_data,
        method="ward"
    )

    plt.figure(figsize=(12, 6))

    dendrogram(
        linked,
        truncate_mode="lastp",
        p=20,
        leaf_rotation=90,
        leaf_font_size=10
    )

    plt.title("Hierarchical Clustering Dendrogram")
    plt.xlabel("Cluster Groups")
    plt.ylabel("Distance")

    plt.tight_layout()
    plt.show()

    print("Hierarchical Clustering Completed.")


if __name__ == "__main__":
    perform_hierarchical_clustering()