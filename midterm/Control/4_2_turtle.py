import turtle 

#using for loop 

window = turtle.Screen()    # create a window
batman = turtle.Turtle()    # create an object
batman.color("black")       # choosing the color
batman.shape("turtle")

for i in range(0,100,2):
    batman.left(30)
    batman.forward(50)
    batman.left(20)
    batman.forward(10)


window.mainloop()  # keep the window open
