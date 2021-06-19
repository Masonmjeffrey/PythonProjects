import random
import gameState as gS


def game_intro():
    print('Hi there welcome to my first text based game')
    print('Welcome to the game of Colorado Trail')
    print("")
    player_name = input(" What's your character's name? ")
    print("Hmmmmmm, " + player_name + ", that's a good name")
    print("Welcome to the Colorado Trail, " + player_name + ", the goal of this game is to travel across the state of "
                                                            "Colorado.\n We want to go all the way from Grand Junction"
                                                            "across the mountains to Denver\n")
    print(" __                      \n"
          "<__>____________________________\n"
          " |  |                           |\n "
          "|  |         _..._             |\n "
          "|  |_______,'  _  `.___________|\n "
          "|  |       | .' `.-'           |\n "
          "|  |_______| '._.'-____________|\n "
          "|  |        `.____.'           |\n "
          "|  |___________________________|\n "
          "|  |                            \n ")


def advance_game_time(num_days):
    gS.day = gS.day + num_days
    gS.totalDays += num_days
    if gS.day > 30:
        gS.month += 1
        gS.day = 1


def miles_remaining():
    print("You have traveled " + str(gS.totalDistance - gS.miles_traveled) + " miles.")


def food_remaining():
    print("You started with " + str(gS.beginning_food) + " food, you now have " + str(gS.food) + " food remaining\n")


def handle_rest():
    print("Let's take a quick break the mountains are tiring\n")
    daysRest = random.randint(1, 4)
    print("You rested for " + str(daysRest) + " days, time to get back on the trail\n")
    gS.totalDays += daysRest
    gS.health += random.randint(1, 3)


def handle_hunt():
    print("We are getting pretty hungry we should eat soon, unfortunately their aren't many restaurants nearby\n")
    daysHunt = random.randint(1, 4)
    foodCaught = random.randint(25, 300)
    print("You spent " + str(daysHunt) + " days hunting, and caught " + str(foodCaught) + " food nice job.\n")
    gS.totalDays += daysHunt
    hurtFromHunt = random.randint(0, 4)
    ## is what I used as how much food consumed on the hunt
    foodConsumed = daysHunt * gS.huntFactor
    gS.food -= foodConsumed
    gS.food += foodCaught
    if hurtFromHunt > 0:
        print("Hunting is tough and the mountains in Colorado contain a diverse catalogue of wildlife. Some of that"
              "wildlife is better left alone.\n You got took some hits but we should see the other guy, big oof \n")
        print("Your health has been depleted by " + str(hurtFromHunt) + ".\n")
        gS.health -= hurtFromHunt
    else:
        print("Hunting is tough but this time you were tougher. You escape the hunt unscathed and even catch some extra"
              "food. Nice Job!\n")
        gS.food += 50


def handle_travels():
    minMilesperTurn = gS.totalDistance/gS.minTurns
    maxMilesperTurn = gS.totalDistance/gS.maxTurns
    milesTraveledTurn = random.randint(minMilesperTurn, maxMilesperTurn)
    ## maybe I'll change this 10 to something else
    daysTraveled = milesTraveledTurn / 10
    gS.miles_traveled += milesTraveledTurn
    gS.totalDays += daysTraveled
    foodConsumed = daysTraveled * gS.travelFactor
    gS.food -= foodConsumed
    print("You traveled " + str(milesTraveledTurn) + " miles over the course of " + str(daysTraveled) + ".\n")
    print("During that traveled you consumed " + str(foodConsumed) + " food.\n")


def handle_status():
    miles_remaining()
    food_remaining()
    print("You have " + str(gS.health) + " health remaining")


def get_action():
    action = input("Choose an action: ")
    if action == "travel" or action == "t":
        handle_travels()
    elif action == "hunt" or action == "h":
        handle_hunt()
    elif action == "rest" or action == "a":
        handle_rest()
    elif action == "quit" or action == "q":
        quit()
    elif action == "status" or action == "s":
        ## status should always call get action again
        handle_status()
        get_action()
    else:
        print("Invalid action: remember you can press h or help for information\n"
              "                or you can press q or quit to quit\n")
        get_action()
    ## after we complete our action we need to check and see if the game is over
    if game_over():
        gS.playState = False


def game_over():
    if gS.health < 0:
        return True
    elif gS.food < 0:
        return True
    elif gS.totalDays > gS.maxDays:
        return True
    elif gS.miles_traveled >= gS.totalDistance:
        return True


def win_state():
    if gS.miles_traveled >= gS.totalDistance:
        return True


def quit_game():
    gS.playing = False


def reset_game_state():
    gS.miles_traveled = 0
    gS.food = 1000
    gS.health = 100
    gS.month = 1
    gS.day = 1
    gS.sickness = 0
    gS.player_name = None
    gS.profession = None
    gS.totalDays = 1
    gS.playState = True
    gS.userMoney = 500








