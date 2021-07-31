
number = int(input("enter the num of values you need to print"))

n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")
if number == 0:
    print(number)
elif number == 1:
    print(str(n1) + '\n' + str(n2))
else:
       print(str(n1) + '\n' + str(n2))
       while count < (number-2):
          c = n1 + n2
          n1 = n2
          n2 = c
          count += 1
          print(n2)





