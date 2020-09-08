label b1_end:
    stop music fadeout 5.0
    scene transition
    centered "{i}The Outbreak room has ended."

    if not Josh_joined_team:
        menu:
            "Will you invite Josh to join your team?"
            "Yes":
                call add_Josh
                pass
            "No":
                pass

    if not Brigette_joined_team:
        menu:
            "Will you invite Brigette to join your team?"
            "Yes":
                call add_Brigette
                pass
            "No":
                pass

    return


label breakout_room_1:
    play music music_room_one fadein 3.0 loop
    scene blank
    show Josh_one at top_left_screen
    show Brigette_one at top_right_screen

    "You are last to join."
    "The two strangers are already talking."

    menu:
        "Hey! How are you guys doing?":
            call b1_howareyou
            pass
        "Ooh.. did I interrupt something?":
            call b1_interrupt
            pass

    show Brigette_one at top_right_screen
    player "Oh! Do you guys know each other?"
    Josh "Hmm… I dunno her."
    show Brigette_twob at top_right_screen
    Brigette "Hey!"
    Josh "Joking, joking! I’ve known Bri for like a year, I basically pestered her until she talked to me."
    show Brigette_threeb at top_right_screen
    Brigette "Yeah, you were annoying."
    show Josh_two at top_left_screen
    Josh "Yeah, yeah, I know. I’m just that annoying guy you know."
    Brigette "No you’re n-"

    menu:
        "You cut Brigette off to get back on topic.":
            jump b1_cutoff
            pass
        "You let Brigette continue.":
            jump b1_continue
            pass
    return

label b1_howareyou:
    Josh "Yo dude!"
    show Brigette_two at top_right_screen
    Brigette "..."

    Josh "I’m doing great, just a ‘lil bit behind on lectures but nothing a 2am sesh won’t fix."
    show Brigette_oneb at top_right_screen
    Brigette "..."
    return

label b1_interrupt:
    Josh "Yo dude!"
    show Brigette_two at top_right_screen
    Brigette "Mind your own business!"
    Josh "Sorry we just went off on a tangent, nothing to worry about!"
    return

label b1_continue:
    hide Josh_two
    show Josh_one at top_left_screen
    Brigette "No you’re not! There’s… more annoying guys out there. "
    Josh "Ooh. Like who?"
    show Brigette_oneb at top_right_screen
    Brigette "U-uh..."
    "{i}Brigette looks away to the side, blushing. Her voice softens."

    show Brigette_threeb at top_right_screen
    Brigette "Y-you won’t know them."

    show Josh_two at top_left_screen
    Josh "Good. I was gonna fight them haha."
    scene blank
    show Brigette_threeb at top_right_screen
    show Josh_one at top_left_screen
    Josh "Hey [player_name], you still here?"

    menu:
        "Remain silent.":
            Josh "Welp, looks like they’re not there. Maybe connection problems."
            show Brigette_oneb at top_right_screen
            Brigette "Yeah, I guess so."
            Josh "Oh well. Bri, guess it’s back to storytime."
            "{i}They continue talking for a minute."
            "..."
            player "So..."
            pass
        "Yeah! I just didn’t want to interrupt you guys.":
            show Brigette_two at top_right_screen
            Josh "Nah no worries! Just wanted to check if you were still there."
            Brigette "{size=-15}It was better when it was just me and Josh..{/size}"
            Josh "Wait did you say something Brigette?"
            show Brigette_threeb at top_right_screen
            Brigette "Nothing at all!"
            pass

    menu:
        "How did you guys meet?":
            call b1_howtheymet
            pass
        "Excuse me, what did you say?":
            Brigette "No nothing at all haha."
            Josh "?"
            call b1_tellus
            pass
        "Cute teddy bear in the background Brigette!":
            call b1_teddybear
            pass

    return

label b1_teddybear:
    $ Brigette_mentioned_teddy = True
    show Brigette_three at top_right_screen
    Brigette "..."
    hide Brigette_three
    show Brigette_threeb at top_right_screen
    Brigette "Thanks..."
    show Josh_two at top_left_screen
    Josh "I actually gave her that teddy bear!"
    scene blank
    show Brigette_oneb at top_right_screen
    show Josh_one at top_left_screen
    Brigette "Yeah... It's really special to me."
    call b1_tellus
    return

label b1_howtheymet:
    Josh "Oh we actually met a year back!"
    show Brigette_oneb at top_right_screen
    Brigette "Exactly 13 months and 27 days…"
    Josh "Woah..."
    show Josh_two at top_left_screen
    Josh "You have really good memory!"
    Brigette "Thanks..."
    scene blank
    show Brigette_oneb at top_right_screen
    show Josh_one at top_left_screen
    Josh "We were in the same group for a project team and well..."
    Josh "For some reason we lost communication with our other group members after the first meeting…"
    scene blank
    show Josh_one at top_left_screen
    show Brigette_threeb at top_right_screen
    Brigette "Yeah….. Not sure how that happened... Hahaha"
    Josh "They seemed like cool people though."
    Brigette "No, I don’t think so."
    show Brigette_two at top_right_screen
    Brigette "That girl was raising some serious red flags."
    Brigette "“Did you see how she always sat way too close to you?”"
    Josh "Really? Damn I didn't notice..."
    show Brigette_twob at top_right_screen
    Brigette "You never do..."
    Josh "?"
    Josh "..."
    call b1_tellus
    return

label b1_tellus:
    Josh "Oh well, what about you? Tell us a bit about yourself!"
    show Brigette_one at top_right_screen
    menu:
        "I like music!":
            Josh "Oh nice!! Music is my passion!!"
            show Brigette_two at top_right_screen
            Brigette "You’re not just saying that are you? Just to please him?"
            Josh "Hey! That’s not nice."
            show Brigette_twob at top_right_screen
            Brigette "Hmph."
            call b1_end                           # END ABRUPT
            pass
        "I enjoy science!":
            Josh "Oh! Bri really enjoys science!"
            Josh "She’s super good at it too! Won multiple prizes!!"
            show Brigette_one at top_right_screen
            Brigette "..."
            Josh "It's true!!"
            call b1_end                          #     EN D LOL

            pass
        "I don't want to talk about anyting...":
            Josh "Okay..."
            Brigette "Killjoy much..."
            Josh "Hey that's rude!"
            Brigette "They had it coming!"
            call b1_end                                 # END ABRUPT LOL
    return

label b1_cutoff:
    player "Ah, look at the time! We should get back on task."
    scene blank
    show Josh_one at top_left_screen
    show Brigette_two at top_right_screen

    Josh "Yeah man, all good."
    Brigette "... okay."

    Josh "It sure is cold in here. I’m gonna go turn on the heater real quick."
    show Josh_room at top_left_screen
    "{i}Josh disappears from the camera view. His mic is left unmuted."
    Brigette "Don’t cut people off next time."
    Brigette "{size=-12}Jerk.{/size}"

    scene blank
    show Josh_room at middle
    "{i}Brigette has left the outbreak room."
    "..."

    $ Brigette_angry = True

    show Josh_one at middle
    Josh "And... I’m back!"

    menu:
        "Looks like it's just us two now.":
            call b1_justtwo
            pass
        "Cool guitar you got there!":
            Josh "Thanks, it's cool isn't it?"
            call b1_coolguitar
            pass
    return

label b1_justtwo:
    Josh "Yeah, Bri’s been busy lately… I hope she’s okay."
    menu:
        "So... what are you majoring in?":
            Josh "I’m in second year Arts, majoring in Creative Writing! Took me a whole year to decide though."
            player "That’s crazy cool!"
            Josh "Thanks man! Bri’s major is hella cool though, wish she was here to tell you more about it."
            Josh "She’s going into forensics… man Crim is real interesting."
            Josh "Though... I wonder where she went..."
            menu:
                "I think it was my fault.":
                    Josh "Nah, she's just like that. No hard feelings."
                    call b1_worktogether
                    pass
                "Yeah, I’m not sure either...":
                    call b1_worktogether
                    pass
        "How’s quarantine?":
            Josh "It’s been chill! I’ve just been playing on my guitar lately… honestly been practising like mad."
            call b1_coolguitar

    return

label b1_coolguitar:
    player "What type of guitar is that?"
    Josh "It's an electric guitar, it was my dad's."
    Josh "It was his favourite guitar, he handed it down to me before he passed."
    menu:
        "Ah... I’m sorry for your loss dude.":
            call b1_sorryloss
        "Uhh, you selling it? I think it’s just what I need.":
            scene blank
            show Josh_three at middle
            Josh "That’s real fucked up man."
            $ Josh_angry = True
            scene blank
            "{i}Josh has left the outbreak room."
            call b1_end                                                 #END

    return

label b1_sorryloss:
    Josh "It’s okay man... it’s not your fault."
    Josh "Do you play guitar too?"
    menu:
        "Nah, I’ve never played before.":
            Josh "Oh I see!"
            pass
        "Yeah I do, let's play together sometime!":
            Josh "It’s a date then!"
            pass
    Josh "Oh, It looks like the outbreak room is ending! It was nice chatting with you."
    player "Let's chat again sometime!"
    call b1_end                                         #END
    return

label b1_worktogether:
    Josh "..."
    Josh "So, do you wanna work together?"
    menu:
        "Of course!":
            Josh "Sweet, I’ll message you!"                            # ADD JOSH   -- END
            call add_Josh
            call b1_end
            pass
        "Sorry, I’m working with someone else.":
            Josh "Nah all good man. Good luck on the project!"                    # END
            call b1_end
            pass

    return
