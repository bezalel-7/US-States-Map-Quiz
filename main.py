import turtle
from turtle import Turtle
import pandas
screen = turtle.Screen()
missing_states_list ={"states":[]}
img = "blank_states_img.gif"
screen.title("U.S.States_Game Score")
screen.addshape(img)
turtle.shape(img)
w = pandas.read_csv("50_states.csv")
w.to_dict()
states =[]
score =0

def write(answer_state):
    c = (w[w.state == answer_state])
    h = Turtle()
    h.speed("fastest")
    h.hideturtle()
    h.penup()
    h.goto(int(c.x), int(c.y))
    h.write(answer_state)
def guess_answers():
     for i in w.state:
           if i not  in states:
               missing_states_list["states"].append(i)
               write(i)




while score < 50:
  answer_state = screen.textinput(title=f"SCORE = {score}/50",prompt="Guess the another state?")
  answer_state = answer_state.title()
  if answer_state  == "Exit":
      guess_answers()
      break
  lenght  =  len(w[w.state == answer_state])
  if lenght == 1 and answer_state not in states:
      states.append(answer_state)
      write(answer_state)
      score = score +1
t = pandas.DataFrame(missing_states_list)
t.to_csv("states_to_learn")
turtle.mainloop()