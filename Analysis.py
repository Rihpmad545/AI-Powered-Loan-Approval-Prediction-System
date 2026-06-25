import pandas as pd


def analyze_dataset(file_path):
    try:
        print("\nLoading dataset...")

        df = pd.read_csv(file_path)

        print("\n" + "=" * 50)
        print("LOAN DATASET ANALYSIS")
        print("=" * 50)

        print(f"\nRows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        print("\nColumn Names:")
        print(df.columns.tolist())

        print("\nFirst 5 Records:")
        print(df.head())

        print("\nDataset Information:")
        df.info()

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nNumerical Summary:")
        print(df.describe())

        if "Loan_Status" in df.columns:
            print("\nLoan Status Distribution:")
            print(df["Loan_Status"].value_counts())

        print("\nAnalysis Completed Successfully!")

    except FileNotFoundError:
        print("Error: Dataset file not found.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    analyze_dataset("loan_data.csv")