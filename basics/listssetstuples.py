fruits = ["apple", "orange", "kiwi"]
fruits2 = {"apple", "orange", "kiwi"}
# print (fruits[2])
# print (fruits[:2]) #0 to 2, can be 0:2
# print (fruits[::2]) #step
# print (fruits[::-2]) #reverse
# print(dir(fruits)) #print attr and methods
# print(help(fruits)) #description of methods available
# print(fruits.count("apple"))
for fruit in fruits:
    print (fruit) 
    
# fruits.append("grape")
# fruits.remove("grape")
# fruits.append("grape") #last
# fruits.insert(0, "grape")
# print (fruits)

print(len(fruits2))
# print(dir(fruits2))
# print(fruits2.remove("apple"))
print (fruits2)
for fruit in fruits2:
    print(fruit)
    
print(id(fruit[0]))
print(hex(id(fruit[0])))