def show_balance(balance):
    print(f"Your balance is ${balance: .2f}")
    
def deposit():
    amount = float(input("Enter an amount to be deposited: \n"))
 
    if amount < 0:
        print("That's not a valid amount! \n")
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: \n"))
    
    if amount > balance:
        print("InSufficient Balance !! \n")
        return 0
    elif amount < 0 :
        print ("Amount must be greater than 0!! \n") 
        return 0
    else:
        return amount 

def main():  
    balance = 0    
    is_running = True


    while is_running:
        print("**************************")
        print("      Banking Program     ")
        print("**************************")
        print("1.Show Balanace")
        print("2.Deposit Money")
        print("3.Withdraw")
        print("4.Exit")
        
        choice =  input("Enter your chice from above (1-4):")
        
        if choice == '1':
            show_balance(balance)    
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Invalid input \n")
        
            
    print("Thanks you for banking with us :) !! \n")


if __name__ == '__main__':
    main()