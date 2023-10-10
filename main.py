import turtle as T
from random import randint
import time


def print_message(message, font_size, position, color):
    msg_turtle = T.Turtle()
    msg_turtle.hideturtle()
    msg_turtle.penup()
    msg_turtle.color(color)
    msg_turtle.goto(position)
    msg_turtle.write(message, align='center', font=('Arial', font_size, 'bold'))
    T.update()
    time.sleep(1)
    msg_turtle.clear()


def print_end(message, font_size, position, color):
    msg_turtle = T.Turtle()
    msg_turtle.hideturtle()
    msg_turtle.penup()
    msg_turtle.color(color)
    msg_turtle.goto(position)
    msg_turtle.write(message, align='center', font=('Arial', font_size, 'bold'))


screen = T.Screen()
screen.bgcolor('lightgreen')
screen.setup(width=650, height=450)

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'black', 'grey', 'pink']
y_position = [-100, -70, -40, -10, 20, 50, 80, 110]
all_turtles = []
user_bet = ''

check = False
while not check:
    user_bet = screen.textinput(
        title="Make your bet", prompt="Pick a turtle, enter its color: ")
    for i in range(len(colors)):
        if user_bet == colors[i]:
            check = True
            break


# create turtles for race
for turtle_index in range(0, len(colors)):
    turtle = T.Turtle('turtle')
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-315, y=y_position[turtle_index])
    all_turtles.append(turtle)

print_message("Get ready for a race!", font_size=15, position=(0, 190), color='black')

end_race = False
while not end_race:
    for turtle in all_turtles:
        if turtle.xcor() > 295:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print_end(f"Congratulation, you've won! The {winning_color} turtle is the winner", font_size=15, position=(0, 190), color='black')
            else:
                print_end(f"Unfortunately, you've lost! The {winning_color} turtle is the winner", font_size=15, position=(0, 190), color='black')
            end_race = True
        turtle.forward(randint(0, 10))

screen.exitonclick()
