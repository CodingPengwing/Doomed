label breakout_room_2:
    $ shouko_message = False
    scene blank
    show Nine_1 at top_left_screen
    show Shouko_1 at top_right_screen

    "You are last to join, no one seems to be talking. The girl appears to be on mute."
    Nine "Finally someone else is here!"
    Nine "Felt like I was talking to a brick wall with Miss Mute over here."
    Shouko "…"

    menu:
        "Miss Mute?":
            call MissMute
            pass
        "What were you guys talking about before?":
            Nine "Oh you know..."
            pass
    Nine "I was just saying how anyone fortunate enough to be on my team would absolutely ace this subject."

    if shouko_message:
        centered "{i}You receive a friend request from \"Shouko Oogushi\""
        menu:
            "Accept friend request":
                pass
            "Decline friend request":
                $ shouko_message = False
                pass

    Nine "Not to brag or anything but I’m 190\% sure I’m the smartest person in this tute."
    Nine "No offence to you or anything,"
    Nine "but you probably won’t do that well just by yourself haha."

    menu:
        "Continue to listen to his rant":
            pass
        "Attempt to cut him off":
            Nine "Uhh okay rude much? So anyways as I was saying..."
            pass

    Nine "Did I mention that I’m f**king loaded?"

    if shouko_message:
        call shouko_message1

    Nine "I kinda got loads of connections here and there…"
    Nine "I mean I’m kinda the greatest aren’t I?"

    if shouko_message:
        call shouko_message2

    Nine "I absolutely carried my team last sem so…"
    Nine "Ugh honestly aren’t I the best?"

    if shouko_message:
        call shouko_message3

    Nine "So what do you say? Team up with me?"

    menu:
        "Yeah for sure!":
            Nine "Nice! Looking forward to it!"
            $ num_team_members += 1
            $ Nine_joined_team = True
            "(Shouko leaves the meeting)"                 # E N D     - TEAM MATE ACQUIRED - NINE
            "{i}You have acquired a team member"

            jump b2_end
            pass
        "I don't know...":
            call Idontknow
            pass
        "Could you shut the f*** up for once":
            call nine_be_angry
            pass

    if shouko_message:
        call shouko_final_moments

    jump b2_end                                      # E N D ------
    return

label b2_end:
    scene blank
    centered "{i}The Outbreak room has ended."

    menu:
        "Will you invite Nine-One to join your team?"
        "Yes":
            call add_Nine
            pass
        "No":
            pass

    menu:
        "Will you invite Shouko to join your team?"
        "Yes":
            call add_Nine
            pass
        "No":
            pass

    # if (num_team_members < 2):
    #     if not Nine_joined_team:
    #         menu:
    #             "Will you invite Nine-One to join your team?"
    #             "Yes":
    #                 if Nine_angry:
    #                     "Nine declined your invitation."
    #                     show Nine_1 at middle
    #                     Nine "F**k off bro."                      # NINE INDIVIDUAL SHOT
    #                     scene blank
    #                 else:
    #                     $ num_team_members += 1
    #                     $ Nine_joined_team = True
    #                     "Nine accepted your invitation."
    #                     "Successfully acquired a new teammate!"
    #                 pass
    #             "No":
    #                 pass
    # if (num_team_members < 2):
    #     if not Shouko_joined_team:
    #         menu:
    #             "Will you invite Shouko to join your team?"
    #             "Yes":
    #                 if Shouko_angry:
    #                     "Shouko declined your invitation"
    #                 else:
    #                     $ num_team_members += 1
    #                     $ Shouko_joined_team = True
    #                     "Shouko accepted your invitation."
    #                     "Successfully acquired a new teammate!"
    #                 pass
    #             "No":
    #                 pass
    return

label MissMute:
    Nine "Yeah that’s my nickname for her."
    Nine "Fitting don’t you think? She hasn’t said a word since I joined lmao"
    "{i}Shouko looks as if to speak but decides against it.{/i}"
    menu:
        "Prompt her to speak.":
            call PromptSpeak
            pass
        "What were you guys talking about before?":
            Nine "Oh you know..."
            return
            pass
    return

label PromptSpeak:
    Shouko "I… uh… {size=-10}My name is...{/size} {size=-15}Shouko{/size}."
    menu:
        "I see that you like anime?":
            "{i}Shouko blushes but remains silent."
            $ shouko_message = True
            pass
        "Sorry, could you speak up?":
            Shouko "..."
            "{i}Shouko seems hurt by your comment."
            pass
        "What were you guys talking about before?":
            Nine "Oh you know..."
            return
            pass
    Nine "So anyways..."
    return
label shouko_message1:
    centered "{i}You have (1) new messages"
    centered "Shouko: Thanks for talking to me! That really made me feel appreciated (> <)"
    menu:
        "No worries at all!":
            pass
        "Lol what's with the weird emoticon?":
            $ shouko_message = False;
            pass
    return


label shouko_message2:
    centered "{i}You have (1) new messages"
    centered "Shouko: I really don’t think you should choose Nine as a teammate… (> <;)"
    menu:
        "I agree.. He seems a bit dodgy":
            pass
        "He seems like a cool dude":
            $ shouko_message = False;
            pass
    return
label shouko_message3:
    centered "{i}You have (1) new messages"
    centered "Shouko: Don’t listen to a word he’s saying XD Apparently last sem he got caught cheating and failed :P"
    menu:
        "Yikes...":
            pass
        "As long as I get a good mark right?":
            $ shouko_message = False;
            pass
    return

label Idontknow:
    Nine "Uhh okay? Why though?"
    menu:
        "I'm just a little indecisive":
            Nine "Right…"
            Nine "Decide fast though cause I’m sorta in high demand right now."
            Nine "REALLY"
            Nine "HIGH"
            Nine "DEMAND"
            "(Nine leaves the room)"                      # NINE LEAVES
            pass
        "You seem like kinda a shitty person...":
            call nine_be_angry
            pass
    return

label nine_be_angry:
    $ Nine_angry = True
    Nine "{cps=*3}What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fuckin-{/cps}"
    "(Nine leaves the room)"                              # NINE LEAVES
    return

label shouko_final_moments:
    Shouko "..."
    Shouko "Is he finally gone?"
    Shouko "Thank goodness..."

    menu:
        "What a relief":
            pass
        "Why are you still here?":
            Shouko "?!"
            Shouko "Am I not supposed to be?"
            Shouko "..."
            "(Shouko leaves the call)"                   # E N D --- SHOUKO LEAVES
            $ Shouko_angry = True
            return
            pass

    Shouko "I know right."
    # SHOUKO BLUSHES
    Shouko "Thank you for accepting my friend request"

    menu:
        "No worries!":
            pass
        "It was fun talking to you!":
            pass

                                                                 # SHOUKO BLUSHES

    Shouko "I just wanted to warn you about Nine."
    Shouko "Thanks for believing me."

    player "How did you know Nine cheated?"

    Shouko "Do you know Alistair from our class?"

    menu:
        "Alistair Maffot?":
            "Yes that’s right!"
            pass
        "I'm not too sure...":
            pass

    Shouko "Well, him and Nine-One are both repeating the subject this semester."
    Shouko "But Alistair is actually a really nice and hardworking person!"
    Shouko "Alistair only failed because Nine cheated!"

    menu:
        "I see...":
            pass
        "Thanks for the heads up!":
            pass
    centered "Outbreak room ends in 60 seconds."

    Shouko "It was nice talking to you!"
                                                                        # SHOUKO BLUSHES
    Shouko "Hopefully I’ll get to talk to you again! (> <)"

    menu:
        "Hope to talk again soon too!":
            pass
        "See you!":
            pass

    "(Shouko leaves the room)"                            # SHOUKO LEAVES
    return
