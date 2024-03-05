print("1.sum\n2.difference\n3.multiple\n4.divide\n0.exit")
i = input("Type what you wanna do:")


if i == 'sum' :
        x = int(input("Enter U first number:"))
        y = int(input("Enter U second number:"))
        
        sum = x + y
        print("sum :", sum)
elif i == 'difference' :
        x = int(input("Enter U first number:"))
        y = int(input("Enter U second number:"))
        
        difference = x - y
        print("difference : ", difference)
elif i == 'multiple' :
        x = int(input("Enter U first number:"))
        y = int(input("Enter U second number:"))
        
        multiple = x * y
        print("multiple : ",multiple)
elif i == 'divide' :
        x = int(input("Enter U first number:"))
        y = int(input("Enter U second number:"))
        
        divide = x / y
        print("divide : ", divide)
else :
        print("Wrong value!!!!!!")