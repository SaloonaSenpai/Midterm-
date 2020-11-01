'''
THIS IS ONLY FOR THE WHILE LOOP THE FOR LOOP WOULD BE IN ANOTHER FILE AND THE TURLE WOULD BE ALSO IN ANOTHER FIEL 
'''



#starts from 1 
print("Class work #1")
counter = 0 
while counter < 10: #counter is the loop control variable
    counter +=1
    print(str(counter) + "  :: INSIDE THE LOOP")
print("OUTSIDE THE LOOP")


#this makes it start from 0 
print("Class work #1.2")
counter = 0
while counter < 10:  # counter is the loop control variable
    print(counter)
    counter += 1
print("OUTSIDE THE LOOP")


#having the counter 10 makes the program ignore the while loop and move to the print since counter is 10 
print("Class work #1.3")
counter = 10
while counter < 10:  # counter is the loop control variable
    print(counter)
    counter += 1
print("OUTSIDE THE LOOP")


#adding another variable 
print("Class work #2")
counter = 0
result = 0
while counter < 10:  # counter is the loop control variable
    counter += 1
    result += counter
    print(f"{counter} : {result}")
print(f"sum is {result}")


#this loop  allows users to input any 6 numbers
#the average should be calculted outside the loop using the counter

print("Classwork #3")
counter = 0
result = 0
while counter < 6:
    num = int(input("Number >>: "))
    result += num
    counter += 1

average = result / counter

print(f"The Sum is: {result}")
print(f"The number of numbers is: {counter}")
print(f"The Avarege is: {average}")



#choosing how many times the loop will go 
print("Classwork #4")
counter = 0
result = 0

#we choose the number itll loop around
N = int(input("N >>: "))

while counter < N:
    num = int(input("Number >>: "))
    result += num
    counter += 1

average = result / counter

print(f"The Sum is: {result}")
print(f"The number of numbers is: {counter}")
print(f"The Avarege is: {average}")



#sum of all even numbers less than 50 
# sum of only even number !
print("class work #5")
counter = 0
result = 0

while counter <= 50:
    number = int(input(">>:: "))
    counter += 2
    # we check if the number is even if it is then we add it to result without overwritting it
    if (number % 2) == 0:
        result += number

print(f"the sum is {result}")



#Multiplication table 

counter = 1
result = 0
number = int(input("Enter a number: "))

while counter <= 10:
    result  = number * counter
    print(f"{number} x {counter} = {result}")
    counter +=1

    
print("THIS IS THE HOMEWORK")