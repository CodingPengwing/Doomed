# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Josh = Character("Josh Ong", color = "#44DDDD")
define Brigette = Character("Brigette Simper", color = "#44DDDD")
define Shouko = Character("Shouko Oogushi", color = "#44DDDD")
define Nine = Character("Nine-One Divoc", color = "#44DDDD")
define Alistair = Character("Alistair Moffat", color = "#44DDDD")
define Jessica = Character("Jessica Kim", color = "#44DDDD")
define professor = Character("Professor X", color = "#44DDDD")

# Music
#renpy.music.register_channel(name, mixer=None, loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
define audio.music_opening = "audio/opening.mp3"
define audio.music_scary = "<from 5>audio/scary.mp3"
define audio.music_room_one = "audio/room_one.mp3"
define audio.music_room_two = "audio/room_two.mp3"
define audio.music_room_three = "audio/room_three.mp3"

# Brigette pics
image Brigette_one = Image("Brigette_1.jpg")
image Brigette_oneb = Image("Brigette_1b.jpg")
image Brigette_two = Image("Brigette_2.jpg")
image Brigette_twob = Image("Brigette_2b.jpg")
image Brigette_three = Image("Brigette_3.jpg")
image Brigette_threeb = Image("Brigette_3b.jpg")

# Josh pics
image Josh_one = Image("josh_1.jpg")
image Josh_two = Image("josh_2.jpg")
image Josh_room = Image("josh_room.png")

# Nine pics
image Nine_one = Image("nine_1.jpg")

# Shouko pics
image Shouko_one = Image("shouko_1.jpg")

# Jessica pics
image Jessica_one = Image("Jessica_1.jpg")
image Jessica_twoa = Image("Jessica_2a.jpg")
image Jessica_twob = Image("Jessica_2b.jpg")

# Alistair pics


# Image positions
transform top_left_screen:
    xalign 0.1
    yalign 0.1

transform top_right_screen:
    xalign 0.9
    yalign 0.1

transform bottom_screen:
    xalign 0.5
    yalign 0.8

transform middle:
    xalign 0.5
    yalign 0.1

transform center:
    xalign 0.5
    yalign 0.5

# Backgrounds
image bedroom = Image("bedroom.jpg")
image main_room = Image("home_space.png")
image breakout_transition = Image("transition.jpg")
image blue_screen = Image("blue_screen.jpg")
image blank = Solid("#000000")
image teddy_one = Image("teddy_one.jpg")
image teddy_two = Image("teddy_two.jpg")


#-----
# the main program
label start:

    $ num_team_members = 0

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

    $ Alistair_mentioned_recipe = False
    $ Josh_mentioned_guitar = False
    $ Jessica_mentioned_teddy = False
    $ Brigette_mentioned_teddy = False
    $ Shouko_mentioned_teddy = False
    
    call artist_statement
    call disclaimer_scene
    call intro
    call online_class_scene
    call player_instructions

    # breakout room 1
    scene breakout_transition
    centered "You are being moved to outbreak group 1"
    menu:
        "Would you like to join the conversation or skip this group?"

        "Join the conversation":
            call breakout_room_1
            pass
        "Quiet watch the other students like a {i}creepy{/i} ninja (skip)":
            call skip_breakout_1
            pass

    if num_team_members >= 2:
        player "I've got my teammates secured, looks like I can go back to sleep. Stuff the rest of the class."
        call end_game
        return

    # breakout room 2
    scene breakout_transition
    centered "You are being moved to outbreak group 2"
    menu:
        "Would you like to join the conversation or skip this group?"

        "Join the conversation":
            call breakout_room_2
            pass
        "Quietly observe in order to not disturb the natural habitat of awkward university students (skip)":
            call skip_breakout_2
            pass

    if num_team_members >= 2:
        player "I've got my teammates secured, looks like I can go back to sleep. Stuff the rest of the class."
        call end_game
        return

    # breakout room 3
    scene breakout_transition
    centered "You are being moved to outbreak group 3"
    centered "Guess you're going to join the conversation this time... instead of being a mannequin."
    call breakout_room_3
    call end_game

    # finish
    return


#---
# artist statement
label artist_statement:
    scene blank
    centered "{b}{size=30}Quick introduction{/size}{/b}\n
    \n\n
    The purpose of this of the project is to reflect on the current dynamic situation regarding Covid-19 all over the world, and effects it has on our everyday life.
    The pandemic has made the year 2020 one to be remembered for many wrong reasons, with bushfires and natural disasters, as well as political unrest being other causes of concern.
    As university students, we the creators, felt it was fitting that we recreate the struggles of our own online learning experience, and the difficulties related to such communications, in a light-hearted manner.
    Some references in this product will be better understood by university students (especially from the University of Melbourne),
    however, we welcome and encourage students and gamers everywhere to play and enjoy the game.\n
    \n\n
    As most university students would know, the platform Zoom is now used extensively in our everyday communications.
    We took inspiration from this, which is why the game is called Doomed.\n
    \n\n
    Most of the visual elements presented in this visual novel were self-produced, with a few exceptions being listed in the \"About\" section from the menu.\n
    We would like to give very special thanks to our friend Crystal Li for allowing us to feature her amazing artworks in our story. Without her contributions, we would not have any product to offer... it would have been truely doomed."
    return
    
    

#---
# disclaimer for the product
label disclaimer_scene:
    scene blank
    centered "Disclaimer: This work is purely fictional."
    centered "Disclaimer Jr. : Obscene language is mostly censored, but is present in the storyline."
    return


#---
# wake up scene
label intro:
    play music music_opening fadein 2.0
    scene bedroom
    "{i}It's a nice summer day in quarantine."
    "{i}You've just woken up, feeling really tired from last night's League grind."
    "{i}In fact, you're so tired, you don't remember your own name."
    "{i}Wait no for real... what is your name?"
    $ player_name = renpy.input("{i}{b}What is your name?", "Enter name", length=20)

    define player = Character("Me", color = "#666600")

    player "* Ah of course, of course, my name is [player_name]... what a dumbass I am. *"
    "{i}As you remind yourself of your own name. You also start to remember that weird dream you had last night."
    player "* Hmmm, I must've been {b}that{/b} tired huh? That was one of the weirdest dreams I've ever had. *"
    "{i}As always, it takes a while for the entire dream to come back, but it starts with you walking down the supermarket isle, with your surgical mask on of course."
    "{i}Doing the groceries is pretty much a contactless sport nowadays, you try to steer clear of everyone. Wouldn't want to get Covid-19, that would be ugly."
    show teddy_one at center

    "{i}As you turn the corner of the isle, you see a huge teddy bear sitting in the middle of the supermarket floor."
    # Music change here
    stop music fadeout 10.0
    play music music_scary fadein 2.0
    "{i}It was wearing a huge mask too, but it was very annoyed that it had to do so in public."
    "{i}It thought that it was its own teddy right to be free from any social restraints in the name of \"safety\"."
    "{i}It was pissed, ohhh so pissed, it had a pancake on its left hand that it couldn't eat, all because of this stupid mask covering its face."
    "{i}\"Stupid communist politicians!\" - it thought to itself - \"How dare they violate my teddy rights like this?\""
    "{i}It wanted to take the mask off, but didn't know how to, and thus, got really really mad."
    hide teddy_one
    show teddy_two at center
    "{i}It suddenly transformed into a scary looking serial killer teddy. It got up and started running in your direction, screaming \"TAKE THIS MASK OFF OF ME\"."
    "{i}Before you knew it, it was right on top of you, with its right foot hanging in the air right above your face."
    "{i}It said \"Take this! You left-wing narcissist.\" You didn't have any time to react, all you saw was its huge teddy foot coming down on you... "

    # Music change again
    stop music
    play music music_opening fadein 2.0

    hide teddy_two
    "{i}And that's when you woke up."
    "{i}Wow... if there's ever any reason to not love those cuddly teddies..."
    "{i}Bringing yourself back to reality, you realise that you have to make a very important decision."
    player "* Hmmm my Algorithms tutorial starts in 1 minute. I \
    should get the computer... OR, I could go back to sleep. *"

    menu:
        "Go back to sleep":
            player "* Arggh, but I can't ditch 3 classes in a row. Damn it! *"

            pass
        "Get the computer":
            pass

    stop music fadeout 5.0
    player "* Welp, it's gonna be a long day. *"

    "{i}You open the computer and log in to your online class."
    return

#---
# first scene when joining online class
label online_class_scene:
    scene main_room
    player "* Ah... everyone's here already. *"
    professor "Of course! It's the one and only [player_name] who makes us wait again."
    professor "Tell me, [player_name], do you find pleasure in holding us up every single CLASS?"
    menu:
        "Well... kinda":
            professor "I see. We're going to have a very friendly chat after class."
        "No sir, I'm very sorry. It won't happen again.":
            professor "Yeah yeah, same old trick, I've heard enough from you"

    professor "Alright everyone, let's finally start. Today's class is {b}very important{/b}. As you already know, we have already released the project for this semester."
    professor "If you need a quick recap, we're going to make a very basic computer program. You need to implement a polymorphic hash table."
    professor "We may give you numbers as input, we may give you strings as input, heck we may even give you hash tables as input."
    professor "Your task is to make sure that when provided with a valid hash function, your program will work for any given type of input."
    professor "The goal of the project is not only for you to become godlike programmers, but also to allow some of you find some friends... since that's a rare occurrence in the computing world."
    professor "Alright, enough talking, I'm going to put you guys into different outbreak rooms, you will be sent to 3 different breakout rooms, you should talk to one another to find out who you would like to team up with."
    professor "You need exactly 2 teammates for the project. Remember, if you pick the right people, they'll help you get a better mark for the subject. If you pick the wrong people... well, just don't pick the wrong people."
    "{i}Feels like the professor was looking at you when he said that last part... but hey, the camera's turned off, he couldn't have been."
    professor "Okay off you go."
    return


#---
# Instruction screen
label player_instructions:
    scene blank
    centered "{b}{size=40}Instructions{/size}{/b} \n
    \n\n
    1. You will be put into 3 different outbreak rooms, one at a time, each with 2 other students. \n
    2. You are to talk to your peers to learn more about them. \n
    3. At the end of the outbreak room, you may ask them to join your team. \n
    4. You need to invite 2 people into your team, choose wisely... or risk receiving a 50 WAM. \n
    \n\n
    Side note: You can save progress in the menu, if you would like to jump to different sections. \n
    It is recommended that you save progress right here, so you can go back to this starting point without having to redo the intro. \n
    \n\n
    {b}Enjoy!"
    return


#---
# Breakout 1 skip scene
label skip_breakout_1:
    scene blank
    show Josh_one at top_left_screen
    show Brigette_oneb at top_right_screen
    "... ... ... ..."
    Josh "... hehe, check out this cool guitar ...."
    Brigette "... yeah it's so cool... almost as cool as... you ..."
    "... ... ... ... ... ... ... ..."
    return

#---
# Breakout 2 skip scene
label skip_breakout_2:
    scene blank
    show Nine_one at top_left_screen
    show Shouko_one at top_right_screen
    "... ... ... ..."
    Nine "... yeah I'm cool like that ...."
    Shouko "...    ..."
    "... ... ... ... ... .... ... ..."
    return

#---
# outro
label outro:
    scene bedroom
    player "Welp... that was an eventful semester. I guess I could do it again."
    return
