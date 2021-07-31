print("Calculator!")

valone: int = input("Enter your value one: ")
valtwo: int = input("Enter your value two: ")
print("1 ADDITION!")
print("SUBTRACTION!")
print("3 MULTIPLICATION!")
print("4 DIVISION!")
print("5 EXPONENTIATION!")

while True:
    choice = int(input("Enter your OPERATION Choice 1 to 5: "))
    print("your choice is:" + str(choice))

    if choice == 1:
     print(int(valone) + int(valtwo))
    elif choice == 2:
     print(int(valone) - int(valtwo))

    elif choice == 3:
     print(int(valone) * int(valtwo))
    elif choice == 4:
     print(int(valone) / int(valtwo))
    elif choice == 5:
     print(int(valone) ** int(valtwo))
    else:
     print("enter the correct choice")
