# def print_evens():
#     num = 2
#     while num<=10:
#         print (num)
#         num+=2
        
# # print_evens()

# array = ['helo ', 'there ', 'you']
# print(array[0]+array[1]+array[2])



# even = map((lambda x: x%2==0), range(11))
# print(list(even))

numbers = range(11)

n_number = [number for number in numbers if number%2==0]
print(n_number)

