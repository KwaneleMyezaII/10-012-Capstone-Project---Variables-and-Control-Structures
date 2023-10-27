import math

types = """investment - to calculate the amount of interest you'll earn on your investment 
bond       - to calculate the amount you'll have to pay on a home loan 

"""

print(types)
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:    ").lower()

if choice == "investment" or choice == "bond":
    if choice == "investment":
        amount = int(input("Enter deposit amount: "))
        rate = int(input("Enter interest rate: "))
        duration = int(input("Investment period: "))
        interest = input("simple or compound? ").lower()

        if choice == "simple" or choice == "compound":
            if interest == "simple":
                final_amount = amount * (1 + rate * duration)

            elif interest == "compound":
                final_amount = amount * math.pow((1 + rate), duration)

            print(f"The accumulated amount is R{final_amount}")

        else:
            print("Invalid selection.")

    elif choice == "bond":
        value = int(input("Enter current value: "))
        rate = int(input("Enter interest rate: "))
        duration = int(input("Months? "))

        repayment = (rate * value)/(1 - (1 + rate) ** (-duration))
        print(f"Your repayment amount is R{repayment}")

else:
    print("Invalid selection.")