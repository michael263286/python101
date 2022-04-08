
#Input accepts user input and returns that value as a string
#Which can be stored in a variable and used later


#User Greeter
#Write a function that accepts two parameters: first_name and last_name. Use those two variables to print a greeting that uses the first_name and last_name variables in the output.

#Call your function after you have defined it and pass in two strings. Do this twice.


from stat import FILE_ATTRIBUTE_SYSTEM


def my_name(first_name, last_name):
  print("Top of the morning to you," + " " + first_name + " " + last_name + "!")


#my_name("Michael", "Nguyen")
#my_name("John", "Doe")


def email(first_name , last_name, domain):
  print(first_name[0].lower() + "." + last_name + domain)

#email("Michael","Nguyen","gmail.com")
#email("Joe","Doe"," gmail.com")

def username(first_name,last_name,):
  print(first_name[0:3].lower() + "_" + last_name[0:5].lower())

#username("Michael", "Nguyen")
#username("John", "Doe")

def contact(first_name, last_name, domain):
  print(f"Welcome to E Corp, {first_name} {last_name}")
  print("Email: ")
  email("Michael", "Nguyen", "domain")
  print ("Username: ")
  username("Michael", "Nguyen")

contact("Michael", "Nguyen", "gmail.com")

















