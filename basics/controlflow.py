age=4

if age < 2:
    is_baby = "baby"
else:
    is_baby = "not baby"
# print (is_baby)

# Conditional Expressions
is_baby = "baby" if age < 2 else "not baby"
# print (is_baby)

# try/except Statements and finally
def division(num1, num2):
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("num2 cant be zero")
    except:
        print ("an error occured")
    finally:
        print ("other error")

division('1',1)
        
dog = "c"

dict_map = {
    'a': 'test',
    'b': 'ho',
    # 'c': 'la',
}

owner = dict_map.get(dog, 'reading')
print(owner)
print ("hello")

#Loops
# height_list = list()
# for height in player_heights:
#     height_n = height*201.168
#     height_list.append(height_n)
# print (height_list)