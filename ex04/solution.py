num = int(input("Please enter a number: "))

#makes sures it in between 1 and the number inputted
for elem in range(1, num + 1): 
    if num % elem == 0:
        print(elem)
    
