import turtle
import time

mark_counter = 0
second_counter = 0
minute_counter = 0
number_counter = 1

# takes the hour from the user
set_hour = turtle.textinput("Clock", "Enter the hour")
while not set_hour.isdigit() or int(set_hour) > 12:
    set_hour = (turtle.textinput("Hour", "Enter a correct hour!"))

# takes the minute from the user
set_minute = turtle.textinput("Clock", "Enter the minute")
while not set_minute.isdigit() or int(set_minute) >= 60:
    set_minute = turtle.textinput("Minute", "Enter a correct minute!")

# gives the original angle of the hour and the minute by calculating the rotation angle based on the input
hour_amount = ((int(set_hour) / 12) * 360) + (int(set_minute) * 0.5)
minute_amount = (int(set_minute) / 60) * 360

# declares and sets the initial angle of a turtle that writes the numbers
number = turtle.Turtle()
number.hideturtle()
number.color("blue")
number.penup()
number.speed(1000)
number.left(90)
number.left(150)
number.forward(40)
number.right(150)
number.forward(200)
number.backward(200)
number.backward(0)
number.right(30)

# creates a turtle that draws the circle
draw_circle = turtle.Turtle()
draw_circle.width(5)
draw_circle.hideturtle()

# creates a turtle that draws the minute marks and sets its initial angle
mark_minute = turtle.Turtle()
mark_minute.width(5)
mark_minute.hideturtle()
mark_minute.speed(1000)
mark_minute.left(90)
mark_minute.penup()

# creates a turtle that draws the second hand and sets its initial angle
second_hand = turtle.Turtle()
second_hand.width(3)
second_hand.speed(0)
second_hand.left(90)
second_hand.hideturtle()
second_hand.color("red")

# creates a turtle that draws the minute hand and sets its initial angle
minute_hand = turtle.Turtle()
minute_hand.width(7)
minute_hand.hideturtle()
minute_hand.speed(1000)
minute_hand.left(90)
minute_hand.right(minute_amount)

# creates a turtle that draws the hour hand and sets its initial angle
hour_hand = turtle.Turtle()
hour_hand.width(10)
hour_hand.hideturtle()
hour_hand.speed(1000)
hour_hand.left(90)
hour_hand.right(hour_amount)


# draws the outer circle
def circle():
    draw_circle.speed(1000)
    draw_circle.penup()
    draw_circle.right(90)
    draw_circle.forward(300)
    draw_circle.left(90)
    draw_circle.pendown()
    draw_circle.circle(300)
    draw_circle.penup()
    draw_circle.left(90)
    draw_circle.forward(300)
    draw_circle.right(90)
    draw_circle.pendown()


# draws the minute marks around the circle.
def marks(mn):
    if mn % 5 == 0:
        mark_minute.forward(270)
        mark_minute.pendown()
        mark_minute.forward(30)
        mark_minute.backward(30)
        mark_minute.penup()
        mark_minute.backward(270)
    else:
        mark_minute.forward(290)
        mark_minute.pendown()
        mark_minute.forward(10)
        mark_minute.backward(10)
        mark_minute.penup()
        mark_minute.backward(290)


# prints the numbers around the circle
def numbers():
    if number_counter <= 8:
        number.forward(230)
        number.write(number_counter, font=("normal", 50, "normal"))
        number.backward(230)
        number.backward(0)
        number.right(30)
    elif number_counter <= 12:
        number.forward(230)
        number.write(number_counter, font=("normal", 50, "normal"))
        number.backward(230)
        number.backward(0)
        number.right(28)


# controls the movement of the second, which affects the movement of the minute and hour as well
def second(sc):
    second_hand.forward(220)
    second_hand.backward(240)
    second_hand.backward(0)
    second_hand.forward(20)
    time.sleep(1)
    second_hand.right(6)
    second_hand.clear()
    if sc % 60 == 0:
        minute_hand.clear()
        minute_hand.right(6)
        minute_hand.forward(180)
        minute_hand.backward(200)
        minute_hand.backward(0)
        minute_hand.forward(20)
        hour_hand.clear()
        hour_hand.forward(120)
        hour_hand.backward(140)
        hour_hand.backward(0)
        hour_hand.forward(20)
        hour_hand.right(0.5)


circle()
# draws the minute marks and the numbers around the circle
while mark_counter <= 60:
    marks(mark_counter)
    numbers()
    mark_minute.right(6)
    mark_counter += 1
    number_counter += 1

# draws the initial position of the hour and minute
minute_hand.forward(180)
minute_hand.backward(200)
minute_hand.backward(0)
minute_hand.forward(20)
hour_hand.forward(120)
hour_hand.backward(140)
hour_hand.backward(0)
hour_hand.forward(20)

# begins counting the second
while True:
    second_counter += 1
    second(second_counter)