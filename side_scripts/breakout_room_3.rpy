label breakout_room_3:
    "You are the first to join, Jessica connects shortly after with camera and mic on."

    Jessica "Oh, it's just you."

    menu:
        "Hey! Hopefully the other guy joins soon.":
            call b3_HopefullyOtherGuyJoins
            pass
        "Yeah, I guess. Do you have any ideas for the project?":
            call b3_ProjectIdeas
            pass

    if Jessica_angry:
        call b3_JessGone
    else:
        call b3_JessStay

    return

label b3_HopefullyOtherGuyJoins:
        Jessica "Yeah, I’ve got something for you guys when he joins."  
        "{i}Alistair joins muted and without his camera on, but he turns on his mic shortly after.{/i}" 
        Alistair "Sorry I joined late, what's happening?"
        menu:
            "No worries, I think Jessica wants to tell us something.":
                call b3_NoWorries
                pass
            "What took you so long? We were both waiting!":
                call b3_Waiting
                pass
        return

label b3_NoWorries:
        Jessica "You guys are gonna love this."
        Alistair "I’m excited, let's hear it!"
        return

label b3_Waiting:
        Alistair "Ahhh… I just had some issues. I’m really sorry."
        # Show Jessica_unhappy at top_left
        Jessica "He already apologised, what do you want from him?"                                                                                 # Jessica uncomfortable (change expression?)
        "..." 
        # Show Jessica_default at top_left                                                                                                                              # return to Jessica default expression
        Jessica "Anyways…"
        return

label b3_ProjectIdeas:
        Jessica "Project? Who cares about that, I’ve got better things to spend my time on."
        "Alistair joins muted and without his camera on, but he turns on his mic shortly after."
        Alistair "Sorry I joined late, what's happening?"
        Jessica "Can you believe [player_name]? They want to talk about the project… how lame."
        player "I-"
        Alistair "Ahh there’s nothing wrong with that! Maybe we should talk about it."
        # Show  Jessica_unhappy at top_left                                                                                                       #Jessica unhappy (change expression?)
        Jessica "You too?? ... I can’t believe you guys."
        "Alistair and Jessica go back and forth for a minute."
        Jessica "Yikes. You guys suck, I’m out of here."
        "{i}Jessica mutes and turns off her camera.{/i}"  
        # Show  Alistair_default at middle                                                                                                           #Jessica turns off camera
        $ Jessica_angry = True
        menu:
            "Ah, I’m sorry... that was my fault.":
                Alistair "Don’t worry about it, she was definitely in the wrong. Let's move on!"
                pass
            "Let's continue without her, we don't need her.":
                Alistair "Ah, that’s not nice... But you’re right, let's not waste time."
                pass
        return

label b3_JessGone:
        Alistair "Actually, I’ve got something cool to show you."
        "{i}You hear some shuffling sounds.{/i}"
        Alistair "Wanna know why my camera has been off the entire time?"
        menu:
            "Yeah, let’s see it!":
                pass
            "No offense man, I just want to talk about the project.":
                Alistair "Well... I would say it’s related."
                pass
        "You hear some sounds of metal clanking."
        "{i}Alistair turns on his camera, revealing Alistair in his kitchen.{/i}"
        # Show  Alistair_default at top_right                                                                                                          #Alistair turns on camera (are we making his pancake flip?)
        Alistair "Yo. I’m making some pancakes."
        Alistair "If you pick me for your team, I’ll give you some pointers…"
        Alistair "And maybe, just maybe… I’ll reveal my secret recipe."
        menu:
            "Aren’t all pancakes the same? Waffles are better anyways. Also why are you cooking during class time?":
                call b3_WhyCooking
                pass
            "Oooh... now THAT is something I'm interested in!":
                call b3_Interested
                pass
        return

label b3_WhyCooking:
        Alistair "Ahh, come on man! You really don’t understand do you?"
        Alistair "Kinda a pity. Don’t worry about it."
        "{i}Alistair seems disappointed.{/i}"
        # Show  Alistair_unhappy                                                                                                                    # Alistair unhapppy 
        Alistair "Guess I can’t blame you for wanting to stay on track. I guess we can talk about the project."
        player "Let’s get back on topic then!"
        "{i}You and Alistair talk about the subject for the last few remaining minutes. {/i}"
        jump b3_end

label b3_end:
      if (num_team_members < 2):
          if not Alistair_joined_team:
              menu:
                  "Will you invite Alistair to join your team?"
                  "Yes":
                      call add_Alistair
                  "No":
                      pass
      if (num_team_members < 2):
          if not Jessica_joined_team:
              menu:
                  "Will you invite Jessica to join your team?"
                  "Yes":
                        call add_Jessica
                  "No":
                      pass
      return

label b3_Interested:
        Alistair "Now that’s what I’m talking about"
        "You and Alistair talk about pancakes for a minute."
        Alistair "Anyway, I’ve actually got something related to the class... I think it will help out big time."
        Alistair "But! I can only show you if you work with me though."
        menu:
            "Yeah, let’s team up!":
                if num_team_members < 2:
                  call b3_TeamUp
                  pass
                else:
                    "You already have a full team"
            "Oh sorry! I’ve already found my other group members.":
                call b3_FoundMembers
                pass
            "Nah, I’m good.":
                call b3_ImGood
                pass
        return

label b3_ImGood:
        Alistair "Welp. I’ll see you in class I guess."
        "{i}Alistair mutes and turns off video.{/i}"                                                                                          #ALISTAIR TURN OFF VIDEO
        jump b3_end
        return

label b3_FoundMembers:
        Alistair "Ah... you realise this is a room to find group members right?"
        player "Yikes, I missed that part of the instructions…"
        Alistair "Welp. I’ll see you in class I guess."
        # Show Alistair_unhappy at top_right                                                                                        #ALISTAIR UNHAPPY (change picture?)
        "{i}Alistair does not want to work with you.{/i}"
        $ Alistair_angry = true
        "{i}Alistair mutes and turns off video.{/i}"                                                                                                     # ALISTAIR TURN OFF VIDEO ??
        jump b3_end
        return

label b3_TeamUp:
        call add_Alistair                                                               
        Alistair "Alright, give me a second."
        "{i}Alistair sends a link.{/i}"
        Alistair "I present… detailed notes for the whole class!"
        player "Woah."
        Alistair "I like working with people who aren’t just work-oriented."
        Alistair "You all seem fun… I’m looking forward to working together!"
        menu:
            "Me too!":
                pass
            "Seems like it’s gonna be a great semester already!":
                pass
        Alistair "Woooo! We can make some pancakes together after quarantine too!"
        jump b3_end
        return

label b3_JessStay:
        Jessica "I actually just got my third UMLL yesterday! Not trying to flex, just wanted you guys to know!"
        Jessica "Oh! Also, have you guys heard of the new party happening next week? Secret Mondays?"
        Alistair "Hey, that sounds lit! You guys wanna all go together?"
        menu:
            "Yeah!! I’m so down!":
                pass
            "Hm, I’ll have to see if I’m free...":
                pass
        Jessica "Sick! I can actually give you guys a discount, just jump on this link."
        "{i}Jessica sends a link in chat.{/i}"
        Alistair "Is there a dress code or something? I haven’t been before if I’m being honest"
        Jessica "Just come in casual, don’t stress."
        Jessica "… Actually, you might want to bring a mask too."
        menu:
            "A mask?":
                call b3_Mask
            "Shouldn’t we get back on topic?":
                call b3_BackOnTopic
        return

label b3_BackOnTopic:
        Jessica "Really…? You're just gonna to interrupt me with your boring project?"                             
        Jessica "Yikes, I’m outta here."         
        # Show Jessica_unhappy at top_left                                                                      #JESSICA UNHAPPY (CHANGE PICTURE?)
        "Jessica mutes and turns off camera."
        "{i}Jessica doesn’t want to work with you{/i}" 
        $ Jessica_angry = True
        Alistair "Woah. Explosive."
        call b3_JessGone
        return

label b3_Mask:
        Jessica "Yeah! I actually make them myself, let me show you some of my designs."
        Jessica "If there’s any you like, check out my website! I’ll hook you guys up with a discount too."
        "{i}Jessica disappears but quickly returns to her seat, now wearing a mask.{/i}"                           
        # Show Jessica_3 at top_left                                                                                     # JESSICA NEEDS A MASK HERE  
        Jessica "Check it out."
        Alistair "Damn, that's pretty cool!"
        Jessica "Right?? Look at this one too!"  
        "{i}Jessica swaps out her mask to another design.{/i}"
        # Show Jessica_4 at top_left                                                                                     #CHANGE MASK FOR JESSICA                          
        Jessica "I’ll link you guys my {i}stangram{/i}, I’ve got more there"
        menu:
            "Damn, that's really cool!":
                Jessica "Thanks!!"
                "{i}You talk with Jessica and Alistair for a minute, you guys seem to really get along{/i}"
                jump b3_end
                pass
            "Hm, that top stitching isn’t very neat... but not bad for a beginner.":
                call b3_InsultJessica
                pass
        return

label b3_InsultJessica:
        Jessica "… Seriously? That’s all you have to say? What an asshole."            
        # Show Jessica_unhappy at top_left                                                                        # Change expression for Jessica (unhappy)
        "{i}Jessica leaves the outbreak room.{/i}"
        # Show Alistair_1 at middle
        $ Jessica_angry = True
        Alistair "Hey man. That wasn’t nice."
        "..."
        # Show Alistair_unhappy at middle                                                                         # Change expression for Alistair
        Alistair "I don’t appreciate that."   
        $ Alistair_angry = True    
        "{i}Alistair leaves the outbreak room{/i}"
        "{i}You think about your actions.{/i}"
        "{i}You regret your actions.{/i}"
        show blue_screen
        jump b3_end
        return



#PICTURES NEEDED
#Jessica:
#       Jessica_default
#       Jessica_unhappy
#       Jessica_mask1
#       Jessica_mask2
#Alistair:
#       Alistair_default (flipping pancake so 2/3 pictures??)
#       Alistair_unhappy
