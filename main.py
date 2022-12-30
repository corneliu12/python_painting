import turtle as tm
import random
# import colorgram

# rgb_colors=[]

# # Extract 6 colors from an image.
# colors = colorgram.extract('picture.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# The list of colors belwo was created using the picture.jpg and the colorgram library (see above commented code)
tm.colormode(255)

colors = [(241, 227, 49), (191, 17, 35), (185, 69, 31), (223, 152, 66), (43, 91, 176), (204, 15, 10), (48, 204, 83), 
        (234, 225, 6), (196, 35, 87), (87, 191, 217), (35, 33, 141), (67, 12, 46), (19, 24, 52), (231, 52, 137), 
        (57, 25, 14), (28, 148, 31), (21, 203, 217), (216, 137, 183), (87, 208, 144), (231, 153, 12), (227, 66, 40), 
        (101, 232, 169), (95, 74, 12), (243, 160, 191), (14, 95, 65), (11, 36, 34)]

# number of dots for the painting
num_dots = 100

brush = tm.Turtle()
brush.penup()
brush.hideturtle()
brush.speed("fastest")

brush.setheading(220)
brush.forward(300)
brush.setheading(0)

for dot_count in range (1, num_dots + 1):
    brush.dot(30, random.choice(colors))
    brush.forward(50)    
    # creating a new row every 10 dots
    if dot_count % 10 == 0:
        brush.setheading(90)
        brush.forward(50)        
        brush.setheading(180)
        brush.forward(500)
        brush.setheading(0)


screen = tm.Screen()
screen.exitonclick()