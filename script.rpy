# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Josh = Character("Josh Ong", color = "#00FFFF")
define Brigette = Character("Brigette Simper", color = "#0055FF")
define Shouko = Character("Shouko Oogushi", color = "#00FF22")
define Nine = Character("Nine-One Divoc", color = "#44FF11")
define Alistair = Character("Alistair Moffat", color = "#666600")
define Jessica = Character("Jessica Kim", color = "#666600")
define professor = Character("Professor X", color = "#FFFFFF")

transform top_left_screen:
    xalign 0.15
    yalign 0.1

transform top_right_screen:
    xalign 0.85
    yalign 0.1

transform bottom_screen:
    xalign 0.35
    yalign 0.70

transform middle:
    xalign 0.5
    yalign 0.5

image blank = Solid("#000000")
image home space = Image("home_space.png")

image Brigette_1 = Image("Brigette_1.jpg")
image Brigette_1b = Image("Brigette_1b.jpg")
image Brigette_2 = Image("Brigette_2.jpg")
image Brigette_2b = Image("Brigette_2b.jpg")
image Brigette_3 = Image("Brigette_3.jpg")
image Brigette_3b = Image("Brigette_3b.jpg")

image Josh_1 = Image("josh_1.jpg")
image Josh_2 = Image("josh_2.jpg")
image Josh_room = Image("josh_room.png")

image Nine_1 = Image("nine_1.jpg")

image blue_screen = Image("blue_screen.jpg")


label start:

    $ player_score = 0;
    $ num_team_members = 0;

    $ Josh_angry = False
    $ Brigette_angry = False
    $ Shouko_angry = False
    $ Nine_angry = False
    $ Alistair_angry = False
    $ Jessica_angry = False

    $ Josh_joined_team = False
    $ Brigette_joined_team = False
    $ Shouko_joined_team = False
    $ Nine_joined_team = False
    $ Alistair_joined_team = False
    $ Jessica_joined_team = False

    scene blank

    centered "It's a nice summer day in quarantine."
    centered "You've just woken up, feeling really tired from last night's League grind."
    centered "In fact, you're so tired, you don't remember your own name."
    centered "Wait no for real... what is your name?"
    $ player_name = renpy.input("{i}What is your name?", "Enter name", length=20)

    define player = Character("[player_name]", color = "#666600")

    player "* Ah of course, of course, my name is [player_name]... what a dumbass I am. *"
    centered "As you start to remind yourself of your own name. You also
    realise that you have to make a very important decision."
    player "* Hmmm my Design of Algorithms tutorial starts in 1 minute. I \
    should get the computer... OR, I could go back to sleep. *"

    menu:
        "Go to back to sleep":
            call to_sleep
            pass
        "Get the computer":
            pass

    player "* Welp, it's gonna be a long day *"

    centered "You open the computer and log in to your online class."

    scene home space

    player "* Ah... everyone's here already. *"

    professor "Alright everyone, this is a very important class. As you already know, we have already released the project."

    call breakout_room_1
    call breakout_room_2
    call breakout_room_3

    # end game
    return


label to_sleep:
    player "* Arggh, but I can't ditch 3 classes in a row. Damn it! *"
    return



























# ------------------------TEST AREA------------------------

    # scene zoom raw
    # # show jen sprite at slightleft
    # # jen "Woahh.. HIII guys"
    # #
    # # show steve sprite
    # # steve "Dude wtf is wrong with her..."
    # #
    # # show crystal sprite
    # # crystal "She's just a lil querky that's all."
    #
    # show 1josh:
    #     xalign 0.02
    #     yalign 0.02
    #
    # show 2josh:
    #     xalign 0.70
    #     yalign 0.02
    #
    # show 3josh:
    #     xalign 0.35
    #     yalign 0.7
    #
    # "You are the last to join, and the two strangers are already talking."







