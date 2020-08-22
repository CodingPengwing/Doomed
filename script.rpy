# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Josh = Character("Josh Ong", color = "#00FFFF")
define Brigette = Character("Brigette Simper", color = "#0055FF")
define Shouko = Character("Shouko Oogushi", color = "#00FF22")
define Nine = Character("Nine-One Divoc", color = "#44FF11")
define Alistair = Character("Alistair Moffat", color = "#666600")
define Jessica = Character("Jessica Kim", color = "#666600")

image Josh happy = Image("josh happy.jpg")
image Josh cheeky = Image("josh cheeky.jpg")
image blank = Solid("#000000")
image home space = Image("home space.png")

transform slightleft:
    xalign 0.25
    yalign 1.0

label start:

    $ player_score = 0;
    $ player_chose_Josh = False;
    $ player_chose_Brigette = False;
    $ player_chose_Shouko = False;
    $ player_chose_Nine = False;
    $ player_chose_Alistair = False;
    $ player_chose_Jessica = False;

    scene blank

    # if player_chose_Josh && player_chose_Brigette:
    #
    # if player_chose_Josh && player_chose_Shouko:
    #
    # if player_chose_Josh && player_chose_Nine:
    #
    # if player_chose_Josh && player_chose_Alistair:
    #
    # if player_chose_Josh && player_chose_Jessica:
    #
    #
    # if player_chose_Brigette && player_chose_Shouko:
    #
    # if player_chose_Brigette && player_chose_Nine:
    #
    # if player_chose_Brigette && player_chose_Alistair:
    #
    # if player_chose_Brigette && player_chose_Jessica:
    #
    #
    # if player_chose_Shouko && player_chose_Nine:
    #
    # if player_chose_Shouko && player_chose_Alistair:
    #
    # if player_chose_Shouko && player_chose_Jessica:
    #
    #
    # if player_chose_Nine && player_chose_Alistair:
    #
    # if player_chose_Nine && player_chose_Jessica:
    #
    #
    # if player_chose_Alistair && player_chose_Jessica:


    centered "It's a nice summer day in quarantine."
    centered "You've just woken up, feeling really tired from last night's League grind."
    centered "In fact, you're so tired, you don't remember your own name."
    centered "Wait no for real... what is your name?"
    $ playerName = renpy.input("{i}What is your name?", "Enter name", length=20)

    define player = Character("[playerName]", color = "#666600")

    player "* Ah of course, of course, my name is [playerName]... what a dumbass I am. *"
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
    
    # show Josh happy
    # menu first_convo:
    #     "Tell him about your day"
    #
    #     "My day has been great thanks":
    #         call good_day
    #
    #     "My day has been alright":
    #         call good_day_2
    #
    #     "My day was not too good.":
    #         call bad_day
    #
    # show Josh cheeky
    # menu decision:
    #     "What should we do today?"
    #
    #     "Go to class on Zoom.":
    #         "Woah there are so many people here."
    #         call go_to_class
    #
    #     "Don't go to class, get some food.":
    #         call get_food
    #
    #
    # if got_food:
    #     "I got my usual fish and chips"
    #     "I finished eating my food and felt really good about not going to class"
    # # ------------------------TEST AREA------------------------

    # end game
    return

# ++++++++++++++++++++++++TEST AREA++++++++++++++++++++++++
label to_sleep:
    player "* Arggh, but I can't ditch 3 classes in a row. Damn it! *"
    return

label go_to_class:
    call breakout_room_1
    call breakout_room_2
    call breakout_room_3
    return

label get_food:
    "Go to the kitchen."
    $ got_food = True
    return

label good_day:
    Josh "My day was great too"
label good_day_2:
    Josh "Yeah it's been alright huh"
    return

label bad_day:
    Josh "My day has been kinda shit too"
    return
# ------------------------TEST AREA------------------------


    # scene zoom raw
    # # show jen sprite at slightleft
    # # jen "Woahh.. HIII guys, my name is Jenniferrr uwu. I am the biggest weeb ewer but I also awabsolutely love KPOP! YAYYY! Look at my oppas over there... aww <3"
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
