# def my_func(param):
#     print("hey")
#     return param+1

# func_out=my_func(1)   
# func_out
# print(func_out)

# def say_hi(name):
#     print(f"Hi there, {name}!")

# say_hi('popo')

# # default args:
# def say_hi(name='popo'):
#     print(f"hello, {name}")

# say_hi()
# say_hi('moseti')

# def stylish_painter():
#     best_hairstyle = "Bob Ross"
#     return "Jean-Michel Basquiat"  #after thisnothing is executed
#     return best_hairstyle
#     print(best_hairstyle)

# stylish_painter()

# DECORATORS
def hello(name):
    print("Hello from the hello() function.")

    def greet():
        print("Greetings from the greet() function.")

    # return greet
    # return greet()

hello("Guido")
print(2)
# hello("Guido")()
print ("Hello from py")

def test(name):
    print (f"hello {name}")

test('popo')
print (type('string'))
print (dir('string'))