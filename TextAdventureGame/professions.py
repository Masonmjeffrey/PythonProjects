professionsList = ['Hiker', 'Skier', 'Fisherman', 'Mountain Biker', 'Artist']

def GetProfession():
    print("Many kinds of people visit the beautiful state of Colorado, I myself came from another country and ended up "
          "here.\nPeople come from all over the country to get here and they come for many reasons, "
          "Are you a: ")
    for i in range(len(professionsList)):
        print(professionsList[i] + " \n")
    userProf = input("Which do you feel most like ? ")
    return userProf


def SetProfession(userProf):
    if userProf == "Hiker":
        print("Nice, that was one of my favourite parts about moving here. There are so many great trails to go on. \n"
              "I don't even know if its possible to see all of them but I love going hiking up at El Dorado State Park "
              "\n")
        profession = userProf
    elif userProf == "Skier":
        print("I'm more of a Snowboarder myself, but for snow sports of all kind you can't get much better than Denver."
              "\n There are so many fun places to go skiing just outside the city. \n")
        profession = userProf
    elif userProf == "Fisherman":
        print("Gotta be honest here I don't know a salmon from a tuna. I do know that whenever I drive to go hiking in"
              "the mountains I see people fishing, but that's about it. \n")
        profession = userProf
    elif userProf == "Mountain Biker":
        print("Geez you're a daredevil compared to myself. I see people like you whizzing by whenever I'm on the trails"
              "and it looks like a blast. \n Little too dangerous for me though. \n")
        profession = userProf
    elif userProf == "Artist":
        print("Denver is a super awesome place for artists. Fun fact for ya for every building that is built in Denver"
              "1% of the funding must be dedicated to murals. \n That explains all the really cool local art \n")
        profession = userProf
    return
