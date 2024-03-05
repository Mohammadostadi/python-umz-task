money = 0

def variz():
    global money
    varizi = int(input("Enter U money : "))
    money += varizi
    print("add successfully...")
    
    
def bardasht():
    global money
    bardsht = int(input("Enter U money : "))
    money -= bardsht
    print("bardasht successfully...")
    
def mojodi():
    global money
    print("Mojodi", money)
while True :
    userEntry = input  (""" 
                        1- variz
                        2- bardasht
                        3- mojodi
                        4- Exit
                        Enter your choice ?
                        """)
    if(userEntry == "1"):
        print("\n\n")
        variz()
        print("\n\n")
        
    elif(userEntry == "2"):
        print("\n\n")
        bardasht()
        print("\n\n")
        
    elif(userEntry == "3"):
        print("\n\n")
        mojodi()
        print("\n\n")
    elif(userEntry == "0"):
        break    
    else:
        print("system : your choice is not defined")