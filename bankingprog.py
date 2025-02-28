def show_balance(current_balance):
    print(f"Your balance is: {current_balance}") 

def deposit():
    amount = input("Enter amount to deposit:")
    if float(amount) < 0:
        amount = input("Enter a valid amount to deposit:")
    return amount 

def withdraw(current_balance):
    amount = input("Enter amount to withdraw:")
    if float(amount) > current_balance:
        amount = input("Insuffcient funds! Enter an amount to withdraw:")
    return amount 
    

def main():
    in_progress = True 
    current_balance = 0
    while in_progress: 
        print("Banking")
        print("1. Show Balance")
        print("2. deposit")
        print("3. Withdraw")
        print("4. Exit") 
        customer_input = input("Please select option 1-4:")
        
        if customer_input=="1":
            show_balance(current_balance)
        elif customer_input=="2":
            current_balance += float(deposit())
            print(f"New balance is: {current_balance}")
        elif customer_input=="3":
            current_balance -= float(withdraw(current_balance))
            print(f"New balance is: {current_balance}")
        elif customer_input=="4":
            in_progress=False
        else:
            print("Please enter the right input")
            customer_input = input("Please select option 1-4:")
    print("Have a nice day!")
    
if __name__ == "__main__":
    main()