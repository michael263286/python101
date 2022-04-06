#User Greeter
#Define two variables: firstname and lastname. Assign some string values to the variables. You can use your own name or someone else's. Use those two variables to print a greeting that uses the firstname and lastname variables in the output.

firstname = "Michael"
lastname = "Nguyen"

print("How's it going " + firstname + " " + lastname)


#Email Generator
#Using the two variables you set earlier, generate a company email address that follows the pattern: "first initial, period, last name @ company domain". Assign the result to a new variable called email and print the email to the console.

email = firstname[0] + "." + lastname + "@gmail.com"

print("Email: " + email)

#Username Generator
#Using the firstname and lastname variables, generate a username to a new variable and print it to the console. The username should follow this format: first three letters from firstname, underscore, five letters from lastname.

username = firstname[0:3] + "_" + lastname[0:5]

print("Username: " + username)

#New User Contact Information
#Using all the information you have created, print the data in a nice format. That is, generate a "Contact Card" style output that looks better than just printing values.

contactCard =""" "How's it going " + firstname + " " + lastname 
+ "Email: " + email 
+ firstname[0:3] + "_" + lastname[0:5]
"""


print(contactCard)