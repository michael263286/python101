from random import randint


def advance_roll():
  user_input1 = int(input("Pick number of dice: "))
  user_input2 = int(input("Pick number of sides: "))
  roll_1 = randint(1,user_input1)
  roll_2 = randint(1,user_input2)



  advance_roll(randint(roll_1,roll_2))
