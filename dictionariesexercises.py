# phonebook_dict = {}

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# phonebook_dict['Kareem'] = '938-489-1234'
# phonebook_dict['Bob'] = '968-345-2345'

# # # print(phonebook_dict['Elizabeth'])

# # del (phonebook_dict['Alice'])



# # print(phonebook_dict)

# ramit ={}

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     { 'name': 'Jasmine', 'email': 'jasmine@yahoo.com', 'interests': ['photography', 'tennis'] },
#     { 'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': ['movies', 'tv'] }
#   ]
# }

# # Write a python expression that gets the email address of Ramit.
# print(ramit['email'])
# # Write a python expression that gets the first of Ramit's interests.
# print(ramit['interests'][0])
# # Write a python expression that gets the email address of Jasmine.
# print(ramit['friends'][0]['email'])
# # Write a python expression that gets the second of Jan's two interests.
# print(ramit['friends'][1]['interests'][1])



#Letter Histogram





# word = {}
# user_input = input("Please enter a word: ")
# for letter in user_input:
#   if letter not in word:
#     word[letter] = 0
#   word[letter] += 1


#   print(word)




#Word Histogram
#Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing the tally of how many times each word in the alphabet was used in the text. For example:

# sentence = input("Please enter a sentence: ").lower()

# word = {}

# sentence = sentence.split()

# for item in sentence:
#   if item not in word:
#     word[item] = 0
#   word[item] += 1


# print(word)


#Histogram Tally

sentence = input("Please enter a sentence: ").lower()

word = {}

sentence = sorted(sentence.split())

for item in sentence:
  if item not in word:
    word[item] = 0
  word[item] += 1


print(word)

