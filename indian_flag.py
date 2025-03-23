# WRITTEN BY OM [byt-ctrl]
# INDIAN FLAG DRAWING USING PYTHON TURTLE GRAPHICS

import turtle

# For Drawing rectangles
def draw_rectangle(rectangle_color,x,y,rectangle_width,rectangle_height) :  # Required parameters for drawing rectangle
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(rectangle_color)
    turtle.begin_fill()
    
    for _ in range(2) :
        turtle.forward(rectangle_width)
        turtle.right(90)
        turtle.forward(rectangle_height)
        turtle.right(90)
    
    turtle.end_fill()

# For Drawing Ashoka Chakra
def draw_chakra(chakra_radius,chakra_x,chakra_y) : # Required parameters for drawing Ashoka Chakra
    turtle.penup()
    turtle.goto(chakra_x,chakra_y-chakra_radius)  # Going to starting point of the outer circle of the Ashoka Chakra
    turtle.pendown()
    turtle.color("navy") # Set the color to navy blue
    turtle.circle(chakra_radius)  # For drawing the outer circle of the Ashoka Chakra

    # For Drawing 24 spokes of the Ashoka Chakra
    for _ in range(24) :
        turtle.penup()
        turtle.goto(chakra_x,chakra_y)
        turtle.pendown()
        turtle.forward(chakra_radius)
        turtle.backward(chakra_radius)
        turtle.right(15)  # 15 degree angle between each spoke (because 360/24 = 15)



# Setting up the turtle screen
turtle.speed(3)  # This is moderate speed for drawing [speed can be adjusted as per requirement]
turtle.title("Indian Flag")
turtle.bgcolor("black")  # Set background color to black

# Flag Dimensions (in pixels)
flag_width=350
flag_height=200




# drawing the top part of the flag (safron color)
draw_rectangle("orange",-flag_width/2 , flag_height/2 , flag_width , flag_height/3)

# drawing the middle part of the flag (white color)
draw_rectangle("white",-flag_width/2 , flag_height/6 , flag_width , flag_height/  3)

# drawing the bottom part of the flag (green color)
draw_rectangle("green",-flag_width/2 , -flag_height/6 , flag_width , flag_height/3)


# Drawing the Ashoka Chakra in centre of the flag
# The radius of the Ashoka Chakra is 1/6th of the flag height

chakra_radius=30  # We can adjust the radius of the Ashoka Chakra as per requirement
draw_chakra(chakra_radius,0,0)  # Centre of the flag is i.e (0,0)



# Closing the turtle drawing
turtle.hideturtle()
turtle.done()  
# This will keep the turtle window open until we close it manually

# END OF THE PROGRAM
