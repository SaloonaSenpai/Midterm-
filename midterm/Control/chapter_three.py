x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

#single if condition

print("Single IF Condition")
if x > y:
    print("First number greater than second number")
else:
    print("Second number is greater than first number")

#multiple condition
print("Multiple conditions")
if x == y == z:
    print("All numbers are the same")
elif x > y & x > z:
    print("First number is greater")
elif y > z:
    print("Second number is the greater")
else:
    print("thrid number is the greates!")


'''
if number 1 greater than both itll be the greatest of them all 
if number 1 isnt greatest it means one of them would be the greatest so we check if number 2 greater than number 3
if all false we move to the else statment!
'''

print("Class work #0") 

check = int(input("Number : "))

if check < 0 :
    check = -(check)
    print(f"Absolute value is {check}")
else:
    print(f"Absolute value is {check}")


'''
if the inputted number is  -ve we make it postive using the -(number) since - times - = +
'''


print("Class work #1")
temp = int(input("Input the temp: "))

if temp > 45:  # if its more than 45
    print("Indoor Activity")
elif temp >= 30 & temp <= 45:  # this will allow it to be between 30 and 45
    print("Just take care")
else:  # if its not greater than 45 or greater than 30 it means its blow 30 so good weather
    print("Go outside you lazy ass")


print("Class work #2")
grade = int(input("Enter your grade: "))

if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade < 90:
    print("B")
elif grade >= 70 and grade < 80:
    print("C")
elif grade >= 60 and grade < 70:
    print("D")
else:
    print("F")


#for some reason this only changes the last character probably from the -1
print("Class work #3")
sentence = input("Enter a sentence  ")

if sentence[len(sentence)-1] == ("a" or "e" or "i" or "o" or "u"):
    print(sentence)
else:
    print(str((sentence[:-1])) + sentence[len(sentence)-1].upper())

    #access all the string but not th last one, the last one is at  + to change it to upper!


print("Class work #4")
sentence2 = input("ENTER A RANDOM SENTENCE: ")

if len(sentence2) >=4: #must be more than 4 
    print(sentence2[0:2] + sentence2[-2:])
else: #if its not more or = to 4
    print(sentence2)

#what this does takes the first 2 character(letter) from the first word and the last 2 character(letter) from the last word and mashes them together!




#focuses here on nested if statement  

var = 100
if var < 200:
    print("Expression value is less than 200")
    if var == 150:
        print("Which is 150")
    elif var == 100:
        print("Which is 100")
    elif var == 50:
        print("Which is 50")
elif var < 50:
    print("Expression value is less than 50")
else:
    print("Could not find true expression")
print("Good bye!")


#this is not a nested if statment :
print("Classwork - NESTED IF STATMENT")

#contains 3 inputs
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))


# we need to check if the 3 input form a triangle
if a + b > c and b + c > a and a + c > b:
    print("Triangle can be formed")
else:
    print("No triangle can be found")


# if its right angle
if ((a+b)**2 == c**2) or ((b+c)**2 == a**2) or ((a+c)**2 == b**2):
    print("Right angle")

else:
    print("Not right Triangle")


#type of traingle

if a == b == c:
    print("Equilateral Triangle")
elif a != b != c:
    print("isosceles triangle")

elif a == b or b == c or c == a:
    print("scalene triangle")


#homework !!!

hours = int(input("Hours worked: "))
rate = int(input("Hourrly rate: "))

Salary = hours * rate

#this calcylatees the total salary but the overtime thats why x - 40 so if you did 20 hours extra itll have a different calculation for the extra 20 hours
# and += meaning it add onto the already calculated salary instead of being overwritten
if hours > 40:
    print(str(1.5 * rate))
    Salary += (hours - 40) * (1.5 * rate)

print(f"final salary is : {Salary}")
