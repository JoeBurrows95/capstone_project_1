"""
This program is able to calculate simple or complex interest for a given investment, and it can also calculate the monthly 
repayment of a given bond.
The user provides input to determine what path they want to follow, as well as providing pertinent information for the calculations.
The program then provides output to inform the user either what interest they will receive on their investment, or what their monthly 
repayment will be on a bond.
"""

import math

# Introductory message to provide the user with the options available to them
print("""investment - to calculate the amount of interest you'll earn on your investment
bond\t   - to calculate the amount you'll have to pay on a home loan""")

# collecting input from the user based on the options provided - they should enter either 'investment' or 'bond'
# their input will be converted to lower case to handle any variations such as 'Investment' or 'BOND'
decision = (input("\nEnter either 'investment' or 'bond' from the menu above to proceed:\n").lower())

# I've added some unhappy path handling here, for if the user doesn't enter either 'investment' or 'bond'
# They'll be able to re-enter a value 5 more times. If they enter 'investment' or 'bond' at any point, the while loop will 
# stop and the subsequent code will execute
# After 5 unsuccessful retries, the while loop will break and the user will be asked to restart the program
decision_retries = 0
while decision != "investment" and decision != "bond":
    decision = (input("Sorry, your entry wasn't recognised. Please enter either 'investment' or 'bond' from the menu above "
                      "to proceed:\n").lower())
    decision_retries += 1
    if decision_retries == 5:
        break

# if the user enters 'investment', the below code will execute. It will take input from the user in order to calculate the total 
# amount of interest for their investment
# the following block of code collects all the inputs needed from the user to calculate their interest
if decision == "investment":
    print("You have selected 'investment'. Please provide the following information:")
    deposit = float((input("How much money are you depositing?\n")).strip("£").replace(",", ""))
    investment_interest_rate = float((input("What is the interest rate?\n")).strip("%"))
    investment_interest_rate_calculation = investment_interest_rate / 100
    investment_years = int(input("How many years do you plan on investing for?\n"))
    interest = (input("How would you like the interest to be calculated? Please enter 'simple' or 'compound'\n").lower())

    # I've added some unhappy path handling here, for if the user doesn't enter either 'simple' or 'compound'
    # They'll be able to re-enter a value 5 more times. If they enter 'simple' or 'compound' at any point, the while loop will stop 
    # and the subsequent code will execute
    # After 5 retries, the while loop will break and the user will be asked to restart the program
    interest_retries = 0
    while interest != "simple" and interest != "compound":
        interest = (input("Sorry, your entry wasn't recognised. Please enter either 'simple' or 'compound' to proceed:\n").lower())
        interest_retries += 1
        if interest_retries == 5:
            break

    # if the user wants a simple interest calculation, this code will make that calculation and then print the output
    if interest == "simple":
        simple_interest = deposit * (1 + (investment_interest_rate_calculation * investment_years))
        print(f"At an interest rate of {investment_interest_rate}%, over a period of {investment_years} years, your "
              f"investment will be worth £{simple_interest:.2f}")

    # if the user wants a complex interest calculation, this code will make that calculation and then print the output
    elif interest == "compound":
        compound_interest = deposit * math.pow((1 + investment_interest_rate_calculation), investment_years)
        print(f"At an interest rate of {investment_interest_rate}%, over a period of {investment_years} years, your investment "
              f"will be worth £{compound_interest:.2f}")

    # I believe all scenarios are covered by the code above, but in case I've missed anything, the below else statement will 
    # print an error message
    else:
       print("Sorry, your entries weren't recognised. You'll need to restart the program to continue.")

# if the user enters 'bond', the below code will execute. It will take input from the user in order to calculate the monthly 
# repayments for their bond
# the following block of code collects all the inputs needed from the user to calculate their monthly repayments
elif decision == "bond":
    print("You have selected 'bond'. Please provide the following information:")
    present_value = float(input("What is the present value of the house?\n").strip("£").replace(",", ""))
    bond_interest_rate = float(input("What is the interest rate?\n").strip("%"))
    bond_interest_rate_calculation = (bond_interest_rate / 100) / 12
    bond_repayment_months = int(input("How many months do you plan to take to repay the bond?\n"))

    # the calculation of the monthly repayment is in the code below, the output of which is then printed for the user to see
    bond_repayment = (bond_interest_rate_calculation * present_value) / (1 - (1 + bond_interest_rate_calculation) ** (- bond_repayment_months))
    print(f"At an interest rate of {bond_interest_rate}%, for a repayment period of {bond_repayment_months} months, your monthly "
          f"repayment will be £{bond_repayment:.2f}")

# I believe all scenarios are covered by the code above, but in case I've missed anything, the below else statement will 
# print an error message
else:
    print("Sorry, your entries weren't recognised. You will need to restart the program to continue.")