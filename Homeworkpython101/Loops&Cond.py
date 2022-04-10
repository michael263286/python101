# Coin flip
# Write a function that will "flip a coin" and print the result. There should be a 50/50 chance of getting heads or tails.


#import random


# def coin_toss():
#   print("Flip the coin!")
#   flips = random.randint(0,1)
#   if flips == 1:
#     print('Heads!')
#   else:
#     print ('Tails!')


# coin_toss()


# Even Odd
# Write a function that when given a number as an input will return true if the number is odd and false if the number is even.

# Write a script that asks the user for a number. Pass the number to the function and then print a message to the console that informs the user if the number was even or odd

# count = 0
# enter_num = int(input("Enter a number: "))

# if enter_num % 2 == 1:
#     print ("This number is odd!")
# else:
#     print("This number is even!")


# Dice Roller
# Write a function that takes two numbers as arguments, then returns a random whole number between those two numbers.

# Write a script that tells the user that we are going to roll the dice but we need to know how many sides they have. Ask them for a number between 2 and 20. Pass the number 1 and the number from the user to the function, then print a message that shows the result


import random

print("Let's roll a dice")
def dice(num_1,num_2):
  return random.randrange(num_1,num_2)

num_sides = int(input("How many sides should it have? (2-20): "))

print("It's rolling...")
print(f"It's a {dice(1,num_sides)} !")




