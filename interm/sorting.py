#sorting achieved using .sort() - method or sorted()- function depending on wheteher it is a list, tuple or dictionary. sort() is mutable, sorted() is immutable
#list - both
# tuple - no sort() attribute, hence sorted

ages = [6, 7, 4, 18, 2]
agest = (4, 7, 8, 17, 0)
new_agest = (sorted(agest, reverse=True))
print (new_agest)
# agest.sort() #tuples do not have an attribute sort
ages.sort(reverse=True)
print(ages)
print(ages.sort()) #returns none
print(sorted(agest)) #returns a list. You can type cast by doing tuple(sorted(agest))
print(sorted(ages))

print("\n dict")
fruits = {"banana": 9, "kiwi": 6, "apple": 13, "plums": 4}
print (fruits)
print (sorted(fruits)) #sorts according to key
print (sorted(fruits.items())) #tuple for each key value pair
print (dict(sorted(fruits.items()))) 

n_fruits = sorted(fruits.items(), key= lambda item: item[0])
nw_fruits = sorted(fruits.items(), key= lambda item: item[1]) #you can add reverse=True arg
print (f"fruits: {n_fruits}") #same as 20
print (f"fruits2: {nw_fruits}") #same as 20

print("\n Objects")
class Fruit:
    def __init__(self, name, count):
        self.name = name
        self.count = count 
    
    def __repr__(self):
        return f"{self.name}: {self.count}"
    
fruits = [Fruit("banana", 90), Fruit("kiwi", 6), Fruit("apple", 13), Fruit("plums", 4)]
print(fruits) #bts we are calling the __repr__ method
fruits = sorted(fruits, key = lambda fruit: fruit.count, reverse=True)
print(fruits)