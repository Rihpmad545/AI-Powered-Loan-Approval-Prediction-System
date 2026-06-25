import subprocess


def calculate_emi():

    print("\nEMI CALCULATOR")

    loan_amount = input("Enter Loan Amount: ")
    interest_rate = input("Enter Interest Rate (%): ")
    loan_years = input("Enter Loan Term (Years): ")

    user_input = f"{loan_amount}\n{interest_rate}\n{loan_years}\n"

    result = subprocess.run(
    ["emi_calculator.exe"],
        input=user_input,
        text=True,
        capture_output=True
    )

    print("\n========== RESULT ==========")
    print(result.stdout)


if __name__ == "__main__":
    calculate_emi()