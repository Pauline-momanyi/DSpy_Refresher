print (__name__)
def main():
    print("This is the second module")
# print (type(main))
# print (dir(main))   
if __name__ == "__main__":
    main()
else:
    print ("module is called outside")
    
num1 = 11
num2 = num1
print (f"\nnum1 is at {id(num1)}")
print ("num 2 is at", hex(id(num2)))
# print ("\nnum 2 is at" + id(num2))
print ("num 2 is at", id(num2))
print ("num 2 is at", hex(id(num2)))