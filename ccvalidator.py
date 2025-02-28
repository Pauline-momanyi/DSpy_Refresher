odd_sum = 0
even_sum = 0
sum_total = 0

user_input = input("Enter credit card number:" )
user_input = user_input.replace(" ", "").replace("-", "")
user_input = user_input[::-1]
print(user_input)

for x in user_input[::2]:
    odd_sum += int(x)
print (odd_sum)
    
for x in user_input[1::2]:
    x = int(x)*2
    if int(x) >= 10:
        x = 1 + int(x)%10
        even_sum += int(x)
    else: 
        even_sum += int(x)
print (even_sum)
sum_total = odd_sum + even_sum
if sum_total%10 == 0:
    print ("Card number is valid")
else: 
    print ("Invalid Card")  
  
# for index, char in enumerate(user_input_string):
#     if index%2 == 1:
#         odd_sum += int(char)
# print (f"odd sum is: {odd_sum}")
        
# for index, char in enumerate(user_input_string):
#     if index%2 == 0:
#         double = int(char)*2
#         # print(f"is {double}")
#         if len(str(double))==1:
#             even_sum += double
#         else: 
#             new_double = str(double)
#             add_new_double = int(new_double[0])+int(new_double[1])
#             # print(add_new_double)
#             even_sum += int(add_new_double)
            
# print (even_sum)

# sum_total = even_sum + odd_sum 
# if sum_total%10 == 0:
#     print ("Card number is valid")
# else: 
#     print ("Invalid Card")
            

# def ccvalidator(card_num):