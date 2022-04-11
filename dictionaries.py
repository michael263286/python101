# #Dictionary syntax
# #Type of data
# #Defined by {}

# #empty
# breakfast_order = {}

# #define data with KEY and VALUE
# breakfast_order = {
#   "main": "short stack",
#   "seat": 3,
#   "table": 10,
#   "paid": False,

# }

# #This will print whatever is in the variable "main"
# # key ="main"
# # print(breakfast_order[key])

# #updating value in key
# # breakfast_order["main"] = "eggs over easy" 
# # print(breakfast_order["main"]) #eggs over easy

# # #adding another value to an object
# # breakfast_order["side"] = "hash brown and bacon"


# # #delete something at a position using its key
# # del breakfast_order["side"]
# # #deleting a value but keeping the key,This makes the value have empty string
# # breakfast_order["side"]["hash brown and bacon"] = ""

# # print(breakfast_order)


# #nesting data inside another dict
# user = {
#   "email": "tony@starkindustries.com",
#   "name": {
#     "first": "Tony",
#     "last": "Stark"

#   }
# }

# #accessing nested data
# print(user['email'])
# print (user['name']['first'])

# print(f'Hello {user["name"]["first"]} {user["name"]["last"]}')


# #The [0] prints whatever is nested inside of "first", which is whatever is the index of the nested item, so this would be "T" in "Tony".
# print(user["name"]["first"][0])


# #looping 
# # for key in user:
#   print(key)
#   print(user[key])




#histogram:looking for some unique
# foods = [
#   'pancakes',
#   'waffles',
#   'bagels'
# ]

# orders = {}

# for food in foods:
#   orders[food] = 1




foods = [
    'pancakes',
    'waffles',
    'bagels',
    'pancakes',
    'waffles'
]

orders = {}

# count occurrances of each food in the list of foods
# loop over each food
for food in foods:
    # if the food has not already been added to the dictionary, add it as a key
    # and set the value to 0
    if food not in orders:
        orders[food] = 0
    # now it is confirmed that the food key exists in the dict because it was
    # either already there or we added it as 0 so now we can  increment it by 1
    orders[food] += 1

print(orders)