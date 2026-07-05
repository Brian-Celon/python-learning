#Simple Interest Calculator 

principal = float(input("How much was your principal?: "))
interest_rate = float(input("What was the interest rate?: "))
number_years = int(input("How many years?: "))

interest = principal * (interest_rate/100)  * number_years
total_amount = principal + interest
print(f"The total amount of profit is: {total_amount:.2f}")