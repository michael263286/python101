from random import randint

def coin_toss():
  flips = randint(0,1)
  if flips == 1:
    print('Heads!')
  else:
    print ('Tails!')

