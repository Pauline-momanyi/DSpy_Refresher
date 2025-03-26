#map(function, collection) = Applies a given fxn to all its collections

def c_to_F(temp):
    return (temp * 9/5) + 32 
    
celcius_temps = [0, 32, 65, 98, 65]


# for temp in celcius_temps:
#     print(c_to_F(temp))

far_temps = map(c_to_F, celcius_temps)
print (far_temps) # returns object location, that is iterable
for temp in far_temps:
    print(temp)
    
# print("\nList option")   
far_temps = list(map(c_to_F, celcius_temps))
# print (far_temps) # returns a list

#you can use a lambda fxn 
far_tempsl = map((lambda temp: (temp * 9/5) + 32), celcius_temps)
# print("Using lambda")
# print (list(far_tempsl))


#Filter(function, collection) = return all elements that pass a condition
grades = [45, 56, 34 ,87 ,98]
good_grades = filter(lambda x: x>50, grades)
print(list(good_grades))


#Reduce(function, colection) = Reduce elements into single value, e.g sum. For loop is better in most cases, Reduce() is better for a functional approach and readability
#reduce fxn hasto be imported

from functools import reduce
prices = [4, 56, 34, 12]
def add(x, y):
    return x + y
total = reduce(add, prices)
total2 = reduce(lambda x, y: x + y, prices)
print (f"Total is ${total}")
print (f"Total is ${total2}")