def add (num1,num2):
    return "Added value is:",num1+num2

def sub (num1,num2):
    return "Subtracted value is:",num1-num2


print("Enter 1.Add,.Sub:")
choice=int((input("Enter 1 or 2:")))
num1=int((input("Enter number:")))
num2=int((input("Enter number:")))

if choice == 1:
    print(add(num1,num2))
elif choice == 2:
    print(sub(num1,num2))
else:
    print("Hmm Whaaaaaaaaat!? Actually I don't know")