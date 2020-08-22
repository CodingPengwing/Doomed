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


label start:

    $ player_score = 0;

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

label go_to_class:
    call breakout_room_1
    call breakout_room_2
    call breakout_room_3
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


    return




























    #
    #
    # "…"
    # "You are the last to join, and the two strangers are already talking."
    # "U: (Hey! How are you guys doing?) , (Ooh.. did I interrupt something?)"
    #
    # "U: Hey! How are you guys doing?"
    # "Josh: Yo dude!"
    # "Brigette: … [scowls]"
    # "Josh: I’m doing great, just a ‘lil bit behind on lectures but nothing a 2am sesh won’t fix."
    # "Brigette: …"
    # "U: Oh! Do you guys know each other? (continue off from below)"
    #
    # "U: Ooh.. did I interrupt something?"
    # "Josh: Yo dude!"
    # "Brigette: Mind your own business. [-10]"
    # "Josh: [chuckles] We went off on a tangent, nothing to worry about!"
    #
    #
    # "U: Oh! Do you guys know each other?"
    # "Josh: Hmm… I dunno her."
    # "Brigette: Hey! [pouts]"
    # "Josh: Joking, joking! I’ve known Bri for like a year, I basically pestered her until she talked to me. "
    # "Brigette: [blushes] Yeah, you were annoying."
    # "Josh: [chuckles] Yeah, yeah, I know. I’m just that annoying guy you know."
    # "Brigette: No you’re n-"
    # "U: (You cut Brigette off to get back on topic.) , (You let Brigette continue, but risk losing time to ask them more questions.)"
    # "U: Ah, look at the time! We should get back on task."
    # "Josh: Yeah man, all good. "
    # "Brigette: [irritated] … ok."
    # "Josh: It sure is cold in here. I’m gonna go turn on the heater real quick. "
    # "Josh disappears from the camera view. His mic is left unmuted."
    # "Brigette: Don’t cut people off next time. [mutters] Jerk."
    # "Brigette turns off her camera, muting herself."
    # "…"
    # "Josh: And… I’m back!"
    # "*Doom chat notif* Brigette: busy rn, continue without me."
    # "U: (Looks like it’s just us two now.) , (Cool guitar you got there!) "
    # "U: Looks like it’s just us two now."
    # "Josh: Yeah, Bri’s been busy lately… I hope she’s okay."
    # "U: (So... what are you majoring in?) , (How’s quarantine?)"
    # "U: So... what are you majoring in?"
    # "Josh: I’m in second year Arts, majoring in Creative Writing! Took me a whole year to decide though."
    # "U: That’s crazy cool!"
    # "Josh: Thanks man! Bri’s major is hella cool though. "
    #
    # "U: You realise that something spicy is brewing here. You remain silent."
    # "Brigette: No you’re not! There’s… more annoying guys out there."
    # "Josh: Ooh. Like who?"
    # "Brigette: [flustered] U-uh..."
    # "She looks away to the side, blushing. Her voice softens."
    # "Brigette: Y-you won’t know them."
    # "Josh: [chuckles] Good. I was gonna fight them haha"
    # "Josh: Hey y/n, you still there?"
    # "…"
    # "U: (Remain silent.) , (Yeah! I just didn’t want to interrupt you guys.)"
    # "Josh: Welp, looks like they’re not there. Maybe connection problems."
    # "Brigette: Yeah, I guess so."
    # "Josh: Oh well. Bri, guess it’s back to storytime."
    # "They continue talking for a minute."
    #
    # "U: Yeah! I just didn’t want to interrupt you guys."
    # "Brigette: [annoyed] Well it’s about time."
    # "Josh: Nah no worries! Just wanted to check if you were still there."
    #
    #
    #
    #
    # "------- cut out ----"
    # "U: (So... what are you guys majoring in?) , (How’s quarantine?)"
    # "U: So... what are you guys majoring in?"
    # "Josh: I’m in second year Arts, majoring in Creative Writing! Took me a whole year to decide though."
    # "U: That’s crazy cool!"
    # "Josh: Thanks man! Bri’s major is hella cool though."
    #
    #
    #
    # "U: (How’s quarantine?)"
    # "Josh: It’s been chill, I"
    #
    #
    #
    #
    #
    # "… Like .. Like …. Mind your own business"
    #
    #
    # "Brigette: "
    # "U: (Looks like it’s just us two now.) , (Cool guitar you got there!) ,"
    #
    #
    #
