import turtle #you have to import it , call the turtle to come here

window = turtle.Screen()    #create a window 
batman = turtle.Turtle()    #create an object 
batman.color("black")       #choosing the color 
batman.shape("turtle")

counter = 0

while counter < 10:
    batman.forward(50)
    batman.left(90)
    batman.forward(50)
    batman.left(90)
    batman.forward(50)
    batman.forward(50)
    batman.right(45)
    batman.forward(50)
    batman.right(45)
    batman.forward(50)
    counter += 2




window.mainloop() #keep the window open
