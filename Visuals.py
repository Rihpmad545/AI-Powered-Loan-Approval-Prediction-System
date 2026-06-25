import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def visualize_data(file_path):
    try:
        df = pd.read_csv(file_path)

        sns.set_theme(style="whitegrid")

       
        sns.countplot(data=df, x="Loan_Status")
        plt.title("Loan Approval Distribution")
        plt.show()


        sns.histplot(data=df, x="Monthly_Income", bins=30, kde=True)
        plt.title("Monthly Income Distribution")
        plt.show()

        sns.histplot(data=df, x="Credit_Score", bins=20, kde=True)
        plt.title("Credit Score Distribution")
        plt.show()

        
        numeric_df = df.select_dtypes(include=["int64", "float64"])

        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )
        plt.title("Correlation Heatmap")
        plt.show()

        print("\nVisualizations Generated Successfully.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    visualize_data("loan_data.csv")