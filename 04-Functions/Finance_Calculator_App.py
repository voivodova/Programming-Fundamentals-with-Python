def calculate_simple_interest(principal, rate, time):
    interest = principal * rate * time
    return interest

def calculate_compound_interest(principal, rate, time):
    interest = principal * (1 + rate) ** time - principal
    return interest

def calculate_loan_payment(principal, rate, time):
    monthly_rate = rate / 12
    num_payments = time * 12
    payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)
    return payment

def calculate_future_value_of_savings(principal, rate, time, monthly_contribution):
    future_value = principal * (1 + rate) ** time
    future_value += monthly_contribution * (((1 + rate) ** time - 1) / rate)
    return future_value

def main_menu():
    while True:
        print("Financial Calculations Menu")
        print("1. Calculate Simple Interest")
        print("2. Calculate Compound Interest")
        print("3. Calculate Loan Payment")
        print("4. Calculate Future Value of Savings")
        print("5. Quit the application")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the interest rate (as a decimal): "))
            time = float(input("Enter the time period (in years): "))

            interest = calculate_simple_interest(principal, rate, time)
            print("The simple interest is:", interest)
        elif choice == "2":
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the interest rate (as a decimal): "))
            time = float(input("Enter the time period (in years): "))

            interest = calculate_compound_interest(principal, rate, time)
            print("The compound interest is:", interest)
        elif choice == "3":
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the interest rate (as a decimal): "))
            time = float(input("Enter the time period (in years): "))

            payment = calculate_loan_payment(principal, rate, time)
            print("The monthly loan payment is:", payment)
        elif choice == "4":
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the interest rate (as a decimal): "))
            time = float(input("Enter the time period (in years): "))
            monthly_contribution = float(input("Enter the monthly contribution amount: "))

            future_value = calculate_future_value_of_savings(principal, rate, time, monthly_contribution)
            print("The future value of savings is:", future_value)
        elif choice == "5":
            print("Thank you for using the financial calculations application!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

        input("Press Enter to continue...")

main_menu()
