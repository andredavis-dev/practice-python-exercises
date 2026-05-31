number = int(input("Enter a number: "))


if number % 4 == 0:
    print("Number is divisble of 4")
elif number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd.")
    
num = int(input("Give me one number: "))
check = int(input("Give me a second number: "))
if num % check == 0:
    print(str(check) + " divides evenly into " + str(num))
else: 
    print(str(check) + " does not divides evenly into " + str(num))
    
