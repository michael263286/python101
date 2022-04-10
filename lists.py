#types we've seen so far: String, number (floats, integers), boolean

#empty list

names = []


#list of strings
names = ['tony','steve','tchala']


#list of integers
numbers = [2, 4, 6, 8, 9]

#list of mixed values
#weird = ['pancakes', 10, True]

#print(weird[3]) #indexerror,list is not that long

#print(numbers[-2])


#change value at specific position
names [0] = 'peter'

#.append adds on "tony" to the end
names.append('tony')

#.insert adds on "bruce" before the index number thats indicated
names.insert(0,'bruce')

#.pop removes items in the list from the end, and as you keep adding pop it will keep removing backwards (If you insert certain index it removes that specific item)
names.pop()


#works the same as .pop
#del names

#parenthesis creates a tuple when u set it in this it is permanent
#names = ("tony", "steve", "tchala")
print(names)