
print("1- selesius be farenhiyt \n 2- farenhiyt be selesius")
i = int(input("Enter U choice : "))

if i == 1 :
    C = int(input("Enter U number : "))
    F = ( C * 1.8 ) + 32
    print("Darageh morede nazar : ", F)
elif i == 2 :
    F = int(input("Enter U number : "))
    C = ( F - 32 )/ 1.8
    print("Darageh morede nazar : ", C)
else :
    print("Wrong number!!!!!")