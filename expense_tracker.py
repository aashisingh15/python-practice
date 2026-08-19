print("======EXPENSE TRACKER======")
print("1. Add expense")
print("2. View expenses")
print("3. View total")
print("4. Exit")
name=input("Enter your name: ")
print("Hello",name)
expenses={}
choice = 1
while choice == 1:
    x = int(input("Enter 1 to add expense or 2 to view expense or 3 to view total expenses or 4 to stop: "))
    if x == 1:
        number = int(input("How many expenses do you want to enter? "))
        for i in range(number):
                category = input("Enter category: ")
                amount = int(input("Enter expense: "))
                expenses[category] = amount
            
    elif x == 2:
       print(expenses)
    elif x== 3:
        print("Your total expense is:", sum(expenses.values()))
    elif x==4 :
        choice=2
        print("stop")
    else:
        print("Error")


