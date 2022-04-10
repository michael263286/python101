square = []



# square = "*****"
# for i in range(5):
#     print(square)

# for num1 in range (1,11):
#     for num2 in range(1,11):
#       answer = num1 * num2
#       print(f"{num1} * {num2} = {answer}")


Width = int(input("Width: "))
height = int(input("Height: "))

for i in range(height):
  spaces = height - 1 - i
  stars = i * 2 + 1
  print(" " * spaces + "*" * stars)