#Lambda fxn = small fxn for one time use. They take a number of args but only have one expression. Helps to keep the namespace clean - (you dont have to think of a name for the function) and is useful with higher order functions e.g. sort(), map(), filter(), reduce()
#lambda parameteres: expression

#example:
# map(lambda x: x*2, numbers)
double = lambda x: x * 2
add = lambda x, y: x + y
max_value = lambda x, y: x if x > y else y
is_even = lambda x: x%2==0

print (double(2))
print(add(2,4))
print(max_value(7, 8))
print(is_even(4))