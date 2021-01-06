# This program shows the simulation of the Monty Hall Problem
import random # random number generator
import matplotlib.pyplot as plt # plotting library
plt.style.use('fivethirtyeight') # style of plotting

# function for door with no prize and was not the player's first choice
def no_prize_door_function(host, num_doors, player_choice):
    i = 1
    while (i == host or i == player_choice):
        i = (i+1)%(num_doors)

    return i # returns a door with no prize and was not the player's first choice

def switch_door_function(shown_door, num_doors, player_choice): # player's switch door
    i = 1
    while (i == shown_door or i == player_choice):
        i = (i+1)%(num_doors)

    return i # returns a door that was the player's switch door

def sim_game(door_switch, num_tests): # a function for simulating the game
    win_switch_count = 0 # count wins that player switch doors
    win_no_switch_count = 0 # count wins that player did not switch doors
    lose_switch_count = 0 # count loss when switching doors
    lose_no_switch_count = 0 # count loss when not switching doors

    doors = [0,1,2] # 3 options for doors
    num_doors = len(doors) # number of doors are 3 ( 1 with prize and 2 goats )

    for i in range(0, num_tests): # number of times the game was played
        door_with_prize = random.randint(0, num_doors-1) # chooses random door
        host = door_with_prize # with prize
        player_choice = random.randint(0, num_doors-1) # chooses random door
        original_player_choice = player_choice
        shown_door = no_prize_door_function(host, num_doors, player_choice) # no prize

        if door_switch ==  True: # if player chooses to switch
            player_choice = switch_door_function(shown_door, num_doors, player_choice)

        if player_choice == door_with_prize and door_switch == False: # win without switching doors
            print('Player Wins! (No switch) - The player chose number #', player_choice, 'Original door choice:', original_player_choice, 'Door with prize:', door_with_prize, 'Shown Door:', shown_door)
            win_no_switch_count = win_no_switch_count + 1

        elif player_choice == door_with_prize and door_switch == True: # win with switching doors
            print('Player Wins! (Switch) - The player chose number #', player_choice, 'Original door choice:', original_player_choice, 'Door with prize:', door_with_prize, 'Shown Door:', shown_door)
            win_switch_count = win_switch_count + 1

        elif player_choice != door_with_prize and door_switch == False: # loss without switching doors
            print('Player Lost :( (No switch) - The player chose number #', player_choice, 'Original door choice:', original_player_choice, 'Door with prize:', door_with_prize, 'Shown Door:', shown_door)
            lost_no_switch_count = lost_no_switch_count + 1

        elif player_choice != door_with_prize and door_switch == True: # loss with switching doors
            print('Player Lost :( (Switch) - The player chose number #', player_choice, 'Original door choice:', original_player_choice, 'Door with prize:', door_with_prize, 'Shown Door:', shown_door)
            lose_switch_count = lose_switch_count + 1
        else:  # something went wrong lol
            print('Error, Try Again')

    return (win_no_switch_count, win_switch_count, lose_no_switch_count, lose_switch_count, num_tests) # return these 4 outcomes and number of tests

x = sim_game(True, 10) # play the game

print ('Win Switch %: ', x[1]/x[4]) # print win switch percentage
print ('Lose Switch %: ', x[3]/x[4]) # print lose switch percentage
print ('Win No Switch %: ', x[0]/x[4]) # print win no switch percentage
print ('Lose No Switch %: ', x[2]/x[4]) # print lose no switch percentage

def sim_game2(door_switch, num_tests): # sim game with no print statements
    win_switch_count = 0
    win_no_switch_count = 0
    lose_switch_count = 0
    lose_no_switch_count = 0

    doors = [0,1,2]
    num_doors = len(doors)

    for i in range(0, num_tests):
        door_with_prize = random.randint(0, num_doors-1)
        host = door_with_prize
        player_choice = random.randint(0, num_doors-1)
        shown_door = no_prize_door_function(host, num_doors, player_choice)

        if door_switch ==  True:
            player_choice = switch_door_function(shown_door, num_doors, player_choice)

        if player_choice == door_with_prize and door_switch == False:
            win_no_switch_count = win_no_switch_count + 1

        elif player_choice == door_with_prize and door_switch == True:
            win_switch_count = win_switch_count + 1

        elif player_choice != door_with_prize and door_switch == False:
            lost_no_switch_count = lost_no_switch_count + 1

        elif player_choice != door_with_prize and door_switch == True:
            lose_switch_count = lose_switch_count + 1

    return (win_no_switch_count, win_switch_count, lose_no_switch_count, lose_switch_count, num_tests)

x = sim_game2(True, 200000) # increase sample size and increase confidence interval

print ('Win Switch %: ', x[1]/x[4])
print ('Lose Switch %: ', x[3]/x[4])
print ('Win No Switch %: ', x[0]/x[4])
print ('Lose No Switch %: ', x[2]/x[4])

num_tests = [] # empty number of tests list
win_percentage = [] # empty win_percentage list
switch2 = True # when switching

for i in range(1, 2001): # for 2,000 tests
    num_tests.append(i) # append the number of tests
    y = sim_game2(switch2, i) # y = sim game 2 with no print statements (runs faster)
    win_percentage.append(y[1]/y[4]) # find win percentage

print('The win percentage for test playing ', y[4], ' games is:', y[1]/y[4] * 100, '%') # print the win percentage

plt.figure(figsize=(20,7)) # plot the figure size
plt.plot(num_tests, win_percentage) # plot the number of tests and win percentage ( x and y )
plt.title('The Monty Hall Problem') # plot title
plt.xlabel('Number of Tests') # plot x label (horizontal)
plt.ylabel('Win Percentage') # plot y label (vertical)
plt.show() # show the graph
