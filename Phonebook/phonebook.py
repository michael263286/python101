phone_book = []



while True:

    user_input = int(input("""
        Electronic Phone Book
        =====================
        1. Look up an entry
        2. Set an entry
        3. Delete an entry
        4. List all entries
        5. Quit
        What do you want to do (1-5)? 
        """))
      

  
    if user_input == 1:
      name_searched = input("Who are you looking for?: ")
      for contact in phone_book:
        if name_searched == contact['name']:
          print(f"Phone number: {contact['phone number']}")
    if user_input == 2:
      name_entered = input("What is the person's name: ")
      number_entered = int(input("What is the person's number?: "))
      info_stored = {'name': name_entered, 'phone number':number_entered }
      phone_book.append(info_stored)
      print("Your entry has been saved")
    if user_input == 3:
      del_user = input("Who would you like to delete?: ")
      for contact in phone_book:
        if del_user == contact['name']:
          index = phone_book.index(contact)
          del phone_book[index]
          print("This user has been deleted.")
    if user_input == 4:
      for contact in phone_book:
        print(contact)
    if user_input == 5:
      exit




      print(phone_book)


    

      
  

      