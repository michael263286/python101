from random import randint
def rolls_die():
  user_input = int(input("Pick any number: "))
  roll = randint(1,user_input)
  print(roll)

