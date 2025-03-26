# Interrupt the flow eg ZeroDivisionError, TypeError, ValueError
# 1. try, 2. except, 3. finally

try:
    number = input("Enter a number:")
    print(1/number)
    
# except Exception - catches all exceptions
except ZeroDivisionError:
    print ("You cant divide by zero")
except ValueError:
    print("You must enter a number")  
except Exception:
    print("Other error")
    
# always executes   
finally:
    print("Program break")

