# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play, opponent_history=[], counter=[0], win=[0, 0], my_history=[], choice=[0], play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):
    

    if len(my_history) >= 1000:
        win[0] = 0
        win[1] = 0
        choice[0] = 0
        my_history.clear()
        opponent_history.clear()
        for key in play_order[0]:
            play_order[0][key] = 0
    if (my_history):
        if ((prev_play == "R") & (my_history[-1] == "P")) | ((prev_play == "P") & (my_history[-1] == "S")) | ((prev_play == "S") & (my_history[-1] == "R")):
            win[0] += 1
        if (win[0] < 60) & (len(opponent_history) > 100): 
            if (((prev_play == "R") & (my_history[-1] == "P")) | ((prev_play == "P") & (my_history[-1] == "S")) | ((prev_play == "S") & (my_history[-1] == "R"))):
                win[1] += 1
        
    opponent_history.append(prev_play)
    counter[0] += 1
    choices = ["P", "P", "S", "S", "R"]
    guess = choices[counter[0] % len(choices)]

    opp = [0,0,0]
    me = [0,0,0]
    last_two = ""
    if len(my_history) >= 2:
        last_two = "".join(my_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1
    if len(opponent_history) > 100:
        if (len(opponent_history) == 101) & (win[0] >= 60):
            choice[0] = 0
        elif (len(opponent_history) == 101) & (win[0] < 60):
            choice[0] = 1
        elif (len(opponent_history) == 300) & (win[0] < 60):

            choice[0] = 2
        for i in range(100):
            if opponent_history[i] == "R":
                opp[0] += 1
            elif opponent_history[i] == "P":
                opp[1] += 1
            elif opponent_history[i] == "S":
                opp[2] += 1
            if my_history[i] == "R":
                me[0] += 1
            elif my_history[i] == "P":
                me[1] += 1
            elif my_history[i] == "S":
                me[2] += 1
        if (choice[0] == 0):
            ""
        elif choice[0] == 1:
            for i in range(100,len(my_history)):
                if my_history[i] == "R":
                    me[0] += 1
                elif my_history[i] == "P":
                    me[1] += 1
                elif my_history[i] == "S":
                    me[2] += 1
            if (me.index(max(me))) == 2:
                guess = "P"
            elif (me.index(max(me))) == 1:
                guess = "R"
            else:
                guess = "S"       
        else:
            potential_plays = [
                my_history[-1] + "R",
                my_history[-1] + "P",
                my_history[-1] + "S",
            ]

            sub_order = {
                k: play_order[0][k]
                for k in potential_plays if k in play_order[0]
            }

            prediction = max(sub_order, key=sub_order.get)[-1:]

            ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
            guess = ideal_response[prediction]           
        

    my_history.append(guess)

    return guess
