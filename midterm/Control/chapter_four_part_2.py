
#basic for loop control structure
'''
(start, End, Incremenent)
0 : start 
15: stop but it wont stop at 15 but 14
1: 1,2,3 :: increments by 1 (adds  1)
if you change the the third number to 2
2: 0,2,4 :: increments by 2
'''
for i in range(0,15,1):
    print(i)

#second basic one 
for i in range(6):
    print(i)

''' 
the default start would be 0 and the default increments would be 1
the range is still 6 BUT DOESNT INCLUDE 6 
0-5
'''

#starts at 100 decreases by 10 till it reaches 10 
for i in range(100,0,-10):
    print(i)

#Loops through string 
name = 'Batman'
for i in name:
    print(i)


#using list 
week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday','friday','saturday']
for i in week:
    print(i)
    print((i).capitalize()) #you can mess with it


#using the break statment

'''
number is 0, the range starts from 0 to 9 and each loop number is increased by one and the number would be printed out

if number is equal to 5 number the loop would be broken and would go outside the loop which contains a print function

'''

number = 0
for i in range(10):
    number += 1
    if number == 5:
        break

    print("Num is " + str(number))
print("OUTSIDE THE FOR LOOP")


#using continue instead of break same example  but different outputs
number = 0
for i in range(10):
    number += 1
    if number == 5:
        print("HELLO FUCKER")
        continue

    print("Num is " + str(number))
print("OUTSIDE THE FOR LOOP")



#making a nested loop 
number = [0,1,2,3,4,5,6,7,8,9]
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

for i in number:
    for j in alpha:
        print(f"{i} : {j}")

print("Outsid the loop")


#program that checks if the number is prime 

number = int(input(">>: "))

if number > 1 : 

    for i in range(2,number):
        #the number starts with 2 and ends with the number before the number if the number is 4 itll end at 3
        if (number % i ) == 0:  #gets the factors 
            print(f"The {number} isnt a prime number")
            break
        else:
            print(f"{number} is prime number")

#less than one isnt a prime number
else:
    print("Number isnt a prime number")


#homework(1):
''' 
factorial is 3! 3x2x1
'''


n = int(input(">>: "))
fact = 1
'''
starts with 1 and ends with number + 1 why n + 1 ?
n+1 because we want it to end at the number 
fact = 1 so starts off 

n = 3

(fact = 1) * (i = 1) = fact = 1 
(fact = 1) * (i = 2)  = fact = 2
(fact  = 2) * (i = 3) = fact = 6


'''

for i in range(1, n+1):
    fact = fact * i

print(f"The factorial of {n} is : ", end="")
print(fact)
