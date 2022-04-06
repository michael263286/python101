
#Input accepts user input and returns that value as a string
#Which can be stored in a variable and used later


#User Greeter
#Write a function that accepts two parameters: first_name and last_name. Use those two variables to print a greeting that uses the first_name and last_name variables in the output.

#Call your function after you have defined it and pass in two strings. Do this twice.


def my_name(first_name, last_name):
  print("Top of the morning to you," + " " + first_name + " " + last_name + "!")


my_name("Michael", "Nguyen")
my_name("John", "Doe")


def email(first_name , last_name, domain):
  print(first_name[0].lower() + "." + last_name + domain)

email("Michael","Nguyen","gmail.com")
email("Joe","Doe"," gmail.com")






