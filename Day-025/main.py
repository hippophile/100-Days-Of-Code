# This will be a European Union quiz (the course suggests to do a USA quiz...)

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("EU Member States")
screen.setup(width=700, height=600)

image = "eu-states.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("eu_countries.csv")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("darkorange") 

# game loops

def labels_list():

    img_width = 680
    img_height = 520
    
    x_offset = -img_width / 2
    y_offset = img_height / 2

    members_list = []
    for index, row in data.iterrows():
        turtle_x = x_offset + row['x']
        turtle_y = y_offset - row['y']
        
        members_list.append({
            "state": row["state"],
            "x" : turtle_x,
            "y" : turtle_y
        })

    return members_list
        # writer.goto(turtle_x, turtle_y)
        # writer.write(row['state'], align="center", font=("Arial", 8, "bold"))

eu_countries = labels_list()

counter = 0
while counter != 27:
    answer_state = screen.textinput(title=f"{counter}/27",prompt="What's another Member State?" )
    country_found = None

    for member in eu_countries:
        if member['state'] == answer_state:
            country_found = member
            break

    if country_found:
        writer.goto(country_found['x'], country_found['y'])
        writer.write(country_found['state'], align="center", font=("Arial", 8, "bold"))
        print("yay")
        counter += 1
        print(counter)
        eu_countries.remove(country_found)


screen.exitonclick()