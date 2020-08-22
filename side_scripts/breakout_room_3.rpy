label breakout_room_3:
    "You are the first to join, Jessica connects shortly after with camera and mic on."
    
    Jessica "Oh, it's just you."
    
    menu:
        "Hey! Hopefully the other guy joins soon.":
            call HopefullyOtherGuyJoins
            pass
        "Yeah, I guess. Do you have any ideas for the project?":
            call ProjectIdeas"
            pass
        
        if Jessica_angry
            call JessGone
        else 
            ...
            ...
            
    return
    
    label HopefullyOtherGuyJoins:
        Jessica “Yeah, I’ve got something for you guys when he joins.”
        "{i}Alistair joins muted and without his camera on, but he turns on his mic shortly after.{/i}"
        Alistair “Sorry I joined late, what's happening?”
        menu:
            "No worries, I think Jessica wants to tell us something.":
                call NoWorries
                pass
            "What took you so long? We were both waiting!"
                call Waiting
                pass
        return
    
    label NoWorries
        Jessica “You guys are gonna love this.”
        Alistair “I’m excited, let's hear it!”
        return
        
    label Waiting
        Alistair “Ahhh… I just had some issues. I’m really sorry.”
        Jessica “He already apologised, what do you want from him?”
        "..."
        Jessica “Anyways…”

        return

    label ProjectIdeas:
        Jessica “Project? Who cares about that, I’ve got better things to spend my time on.”
        "Alistair joins muted and without his camera on, but he turns on his mic shortly after."
        Alistair “Sorry I joined late, what's happening?”
        Jessica “Can you believe [player_name]? They want to talk about the project… how lame.”
        [player_name] "I-"
        Alistair “Ahh there’s nothing wrong with that! Maybe we should talk about it.”
        Jessica “You too?? ... I can’t believe you guys.”
        "Alistair and Jessica go back and forth for a minute."
        Jessica "Yikes. You guys suck, I’m out of here.”
        {i}Jessica mutes and turns off her camera.{/i}
        $ Jessica_angry = True
        menu:
            "Ah, I’m sorry... that was my fault.":
                Alistair “Don’t worry about it, she was definitely in the wrong. Let's move on!”
                pass
            "Let's continue without her, we don't need her."
                Alistair “Ah, that’s not nice... But you’re right, let's not waste time.”
                pass
        return
        
    label JessGone:
        Alistair “Actually, I’ve got something cool to show you.”
        {i}You hear some shuffling sounds.{/i}
        Alistair “Wanna know why my camera has been off the entire time?”
        menu:
            "Yeah, let’s see it!":
                pass
            "No offense man, I just want to talk about the project.":
                Alistair “Well... I would say it’s related.”
                pass
        You hear some sounds of metal clanking.
        {i}Alistair turns on his camera, revealing Alistair in his kitchen.{/i}
        Alistair “Yo. I’m making some pancakes.”
        Alistair “If you pick me for your team, I’ll give you some pointers…”
        Alistair “And maybe, just maybe… I’ll reveal my secret recipe.”
        menu:
            "Aren’t all pancakes the same? Waffles are better anyways. Also why are you cooking during class time?"
                call WhyCooking
                pass
            "Oooh... now THAT is something I'm interested in!"
                call Interested
                pass
        return
        
    label WhyCooking:
        Alistair “Ahh, come on man! You really don’t understand do you?”
        Alistair “Kinda a pity. Don’t worry about it.”
        "{i}Alistair seems disappointed.{/i}"
        Alistair “Guess I can’t blame you for wanting to stay on track. I guess we can talk about the project.”
        You “Let’s get back on topic then!”
        "{i}You and Alistair talk about the subject for the last few remaining minutes. {/i}"
        jump end
        
    label end:
        if num_team_members < 2:
        ...
        ...
        return

    label Interested:
        Alistair “Now that’s what I’m talking about”
        You and Alistair talk about pancakes for a minute.
        Alistair “Anyway, I’ve actually got something related to the class... I think it will help out big time.”
        Alistair “But! I can only show you if you work with me though.”
        menu:
            "Yeah, let’s team up!"
                if num_team_members < 2
                  call TeamUp
                  pass
                else
                    "You already have a full team"
            "Oh sorry! I’ve already found my other group members."
                call FoundMembers
                pass
            "Nah, I’m good."
                call ImGood
                pass
        return
        
    label ImGood:
        Alistair “Welp. I’ll see you in class I guess.”
        "{i}Alistair mutes and turns off video.{/i}"
        jump end
        return
        
    label FoundMembers:
        Alistair “Ah... you realise this is a room to find group members right?”
        player “Yikes, I missed that part of the instructions…”
        Alistair “Welp. I’ll see you in class I guess.”
        "{i}Alistair does not want to work with you.{/i}"
        $ Alistair_angry = true
        "{i}Alistair mutes and turns off video.{/i}"
        jump end
        return
        
    label TeamUp:
        "{i}Alistair joins your team{/i}"                        #     - TEAM MATE ACQUIRED - Alistair
        Alistair “Alright, give me a second.”
        Alistair sends a link.
        Alistair “I present… detailed notes for the whole class!”
        player “Woah.”
        Alistair “I like working with people who aren’t just work-oriented.”
        Alistair “You all seem fun… I’m looking forward to working together!”
        menu:
            "Me too!" 
            pass
            "Seems like it’s gonna be a great semester already!"
            pass
            
        Alistair “Woooo! We can make some pancakes together after quarantine too!”
        jump end 
        return
               
            
        
        
            
