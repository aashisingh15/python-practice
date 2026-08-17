print("Hello this is your free expense tracker to continue we please enter your name")
name=input("Enter your name: ")
print("Hello", name, "! Welcome to your Expense Tracker.")
expenses={}
choice = 1
while choice == 1:
    x = int(input("Enter 1 to add expense or 2 to view expense: "))
    if x == 1:
        number = int(input("How many expenses do you want to enter? "))
        for i in range(number):
                category = input("Enter category: ")
                amount = int(input("Enter expense: "))
                expenses[category] = amount
            
    elif x == 2:
       print(expenses)
       choice = int(input("Enter 1 to continue or 2 to stop: "))
    else:
        print("Error")
print(expenses)
print("Your total expense is:", sum(expenses.values())) 
