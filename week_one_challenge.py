# this is a variable that has a list attatched to it
loan_cost = [500,600,200,1000,450]

# this counts the number of loans in each list
len(loan_cost)

# this adds all loans together 
sum(loan_cost)

# this calculates the average loan price taking the sum of all loans and dividing it by the number of loans avaliable.
average_loan_price = sum(loan_cost) / len(loan_cost)

#this prints the average loan price
print(average_loan_price)

# set loan equal to they variables that are tied to their keys 

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


# this gets the loans future value

loan.get("future_value")

 #this gets the loans remaining_months for loans 

loan.get("remaining_months")


# variables listed with numbers and the present value formula with calculating if the loan is a good buy or not or if its not
##worth the price 

remaining_months = 9
annual_discount_rate = .20
cost_of_loan = 500
future_value = 1000
present_value = future_value/(1 + annual_discount_rate/12)**remaining_months
print(present_value)


if present_value >= cost_of_loan:
    print("loan is worth at least the cost to buy it")
else:
    print("loan is to expensive not worth the price")
    
    
def calculate_present_value(future_value, remaining_months, new_loan):
    
    present_value = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)
    return present_value


    # this gets the loans price 

loan.get("loan_price")

# this gets the loan price 
loan.get("loan_price")

# this is a new variable named inexpensive_loans and setting inexpensive_loans to new loan price and printing new loan. 

inexpensive_loans = []
inexpensive_loans = [loan["loan_price"] for loans in loan if loan["loan_price"] <= 500]
print(inexpensive_loans)

import csv
import dataclasses
with open('path/to/week_one_challenge', 'w') as f:
    writer = csv.writer(f)
    
    writer.writerow(dataclasses)

