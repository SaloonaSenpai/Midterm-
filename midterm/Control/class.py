'''
The program then outputs the following information about the shape: 

For a rectangle, it outputs the area and perimeter; 

for a circle, it outputs the area and circumference; 

for a cylinder, it outputs the volume and surface area.  

'''

#we need an input to choose the chape 

shape = input("Rec, Circ, Cyli ").lower()
pi = 3.1416

if shape == 'rec':
    height = float(input("Height: "))
    width = float(input("Width: "))
    area= height * width
    print(f"Area of the rectangle is {area}")
    print("Paramter of the rectange is " + str(2*(height + width)))

elif shape == 'circ':
    radius = float(input("Radius: "))
    area = pi * (radius ** 2)
    print(f"Area of the circle is {area}")
    print("Circumference of the circle is " + str(2 * pi * radius))

elif shape == 'cyli':
    radius = float(input("Radius: "))
    height = float(input("Height: "))
    area = pi* (radius **2 ) * height
    print(f"Volume  of the cyli is {area}")
    print("surface area of the cyli is " + str(2 * pi * radius * height + 2 * pi * (radius ** 2.0)))
else:
    print("Incorrect shape or the algorithm doesnt handle that shape")
