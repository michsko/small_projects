from turtle import Turtle, Screen
import pandas
turtle = Turtle()
turtle2 = Turtle()
screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []
missing_states = []

good_answers = 0




game_on = True

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{good_answers}/50  Guess state of USA.",
                                    prompt="What's another state's name? If you wanna finish type: 'exit' ")

    if answer_state == "exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break



    if data["state"].str.contains(answer_state.title().strip()).any():
        temp_data = data[data["state"].str.contains(answer_state.title())]
        y_position = int(temp_data["y"])
        x_position = int(temp_data["x"])
        turtle2.color("black")
        turtle2.penup()
        turtle2.goto(x_position, y_position)
        turtle2.write(f"{answer_state.title()}", align="center", font=("Arial", 12, "normal"))
        good_answers += 1








screen.exitonclick()
