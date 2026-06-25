#include <stdio.h>
#include <math.h>

int main()
{
    double loanAmount;
    double annualInterestRate;
    int loanYears;

    double monthlyRate;
    int months;
    double emi;

    printf("Loan Amount: ");
    scanf("%lf", &loanAmount);

    printf("Annual Interest Rate: ");
    scanf("%lf", &annualInterestRate);

    printf("Loan Term (Years): ");
    scanf("%d", &loanYears);

    monthlyRate = annualInterestRate / (12 * 100);

    months = loanYears * 12;

    emi = (loanAmount * monthlyRate * pow(1 + monthlyRate, months))
          / (pow(1 + monthlyRate, months) - 1);

    printf("\nMonthly EMI: %.2lf\n", emi);

    return 0;
}