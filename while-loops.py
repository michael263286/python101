#while loop

#count starts at 1

# count = 0
# while count < 10:
#   #code to run
#   count += 1
#   print(f'number{count}')

# #count starts at 0
# count = 0
# while count < 10:
#   #code to run
  
#   print(f'number{count}')
#   count += 1

# #count starts at 1 ends at 3
# count = 0
# while count < 3:
#   count += 1
#   print(f'number {count}')


# answer = ''
# while answer != 'bye':
#   print('hello')
#   answer = input('')

while True:
  choice = input("""
  Choose an option:
  A) say hello
  B) do a dance
  C) quit
  """)

  if choice == 'A':
    print('Hai!')
  elif choice == 'B':
    print('Im Dancing!')
  elif choice == 'C':
    break
  else:
    print("thats not an option")
print('Bye!')