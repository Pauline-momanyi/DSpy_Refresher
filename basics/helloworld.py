# print ("Hello world!")
# print ("Hello world", end = ("... "))
# print ("hello world")


# #f-string
# dog_name = "Lucy"
# my_number = 20.335
# print(f"my dog is called {dog_name}")
# print(F"Number is {my_number:.2f}")
# print(type(dog_name))
# print(dir(dog_name))
# print ("hello".upper(), end = ". ")
# print ("hello".capitalize(), end = ". ")
# print ("hello".startswith("h"), end = ". ")
# print ("hello".replace("l", "j"), end = ". ")
# # print ("hello".join("world!"), end = ". ")
# print ("hello"+"world", end = ". ")
# words = "one two three"
# print ("hello".split(), end = ". ")
# print ("hello".split(' ',2), end = ". ")
# print ("hello".index("l"), end = ". \n")

# url = ["https://safaricom.com"]
# endpoints = ["api", "v1"]
# print ("/".join(url+endpoints))

# #LISTS
# list_1 = ['a', 'b', 'c']
# print(len(list_1))
# list_11 = list_1.append('e') #add to end of list, return none
# print(list_1)
# print(list_11)

# list_2 = ['d', 'e', 'f']
# list_21 = list_2.insert(1, 'd') #insert at position, return none
# print(list_2)
# print(list_21)

# list_3 = ['g', 'h', 'i', 'h']
# list_31 = list_3.remove('h')  #remove first occurence, return none
# print(list_3)
# print(list_31)

# # list_4 = ['j', 'l', 'k', 'l']
# list_4 = [1, 2, 5, 1]
# list_41 = list_4.pop(1) #remove element at index, or default-last, return the removed
# print(list_4)
# print(list_41)

# list_5 = ['m', 'n', 'o']
# list_51 = list_5.index('n') #index of first occurence - doesn't modify list, return the index
# print(list_5)
# print(list_51)

# list_6 = ['1', '3', '2', '3']
# list_61 = list_6.count('3')  #no.of occurence of element - doesn't modify list, return the no of occur
# print(list_6)
# print(list_61)


# list_7 = ['7', '5', '6']
# list_71 = list_7.sort()  #modifies, returns none
# print(list_7)
# print(list_71)

# list_8 = ['7', '5', '6']
# list_81 = list_8.reverse()  #modifies - by reversing arrangement, returns none
# print(list_8)
# print(list_81)

# list_9 = ['7', '5', '6', 'a', 'b']
# list_91 = list_9[1:3]  #original not modified, returns the new sliced here index 1 & 2
# print(list_9)
# print(list_91)

# list_10 = ['7', '5', '6']
# list_101 = list_10.copy()  #does not modify, returns the copy
# print(list_10)
# print(list_101)

# my_list = list()
# my_list.append('q')
# print(my_list)


# #TUPLES
# my_tuple = tuple([1,2,3])
# print(my_tuple)
# print(my_tuple.count(2))
# print(len(my_tuple))
# print(my_tuple.index(2))
# print(my_tuple[1])
# person = ('popo', 27, 'female')
# name, age, gender = person
# print (f'{name} is {age}')
# print(dir(my_tuple))


#SETS
my_set = {1, 2, 3}
set2 = set([5, 6, 7])
print (my_set)
print (set2)
print (dir(set2))