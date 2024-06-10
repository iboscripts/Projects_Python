import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                              prompt="What's another state name?").title()
    if answer == "Exit":
        missing_states = [states for states in all_states if states not in guessed_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        guessed_states.append(answer)
        ajma = turtle.Turtle()
        ajma.hideturtle()
        ajma.penup()
        check = states[states.state == answer]
        ajma.goto(int(check.x), int(check.y))
        ajma.color("red")
        ajma.write(answer)

screen.exitonclick()
