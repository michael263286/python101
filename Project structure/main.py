from flip_coin import coin_toss
from roll_die import rolls_die


def main():
  while True:
    user_input = input("""
    1-flip a coin
    2-roll a die
    3-advanced die
    q-exit
    :                          
    """)

    if user_input == "1":
        coin_toss()
    if user_input == "2":
        rolls_die()
    if user_input == "q":
        exit

main()