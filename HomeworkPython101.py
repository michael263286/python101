# def madlib(noun, verb, name):

#   noun = input("Please enter a noun: ")
#   verb = input("Please enter a verb: ")
#   name = input("Please enter a name: ")

#   print(f"There once was a {noun} that suddenly came to life, called themselves {name} and started {verb} around the town. {name} decided that {verb} was unacceptable and decided to move to the countryside to live a life of solitude.")


# madlib("noun","verb","name")


# def percentageplus(total,tip):
#   tip_amount = total * (tip/100)
#   return(total + tip_amount)

# total = int(input("What is the total bill? "))
# tip = int(input("What percentage would you like to tip? "))


# def tip_calculator(total_bill):
#   return(total_bill)

# total_bill = percentageplus(total,tip)

# tip_calculator("total_bill")

# print(f"Total bill is ${total_bill}")


# Group Tip Calculator (group_tip_calculator.py)
# Write a function called group_tip_calculator that asks the user for the bill total, the tip percentage, and the number of people. Pass the total and percentage values to the percentage_plus function and then divide the result by the number of people in the group. Print the total including the tip as well as the cost per person.


def percentage_plus(total,tip,people):
  tip_amount = total * (tip/100)
  return (total + tip_amount)

total = int(input("What is the total bill? "))
tip = int(input("What percentage would you like to tip? "))
people = int(input("How many people are in the group? "))


def group_tip_calculator(total_bill):
  return(total_bill)

total_bill = percentage_plus(total,tip,people)

group_tip_calculator("total_bill")

print(f"Total bill is ${total_bill}")
print(f"Each person should pay ${total_bill/people:.2f}")
