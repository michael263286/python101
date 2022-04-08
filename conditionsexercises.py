day = input("What day is it today? ").lower()



if day == "Monday" or day == "Tuesday" or day  == "Wednesday" or day == "Thursday" or day == "Friday":
  print("Go to work!")


elif day == "Saturday" or day == "Sunday":
  print("Sleep in!")

else:
  print("Enter a valid day")
