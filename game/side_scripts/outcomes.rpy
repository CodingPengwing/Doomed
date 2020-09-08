label end_game:

    if num_team_members < 2:
        jump outcome_not_enough_members


    # All Josh
    if Josh_joined_team and Brigette_joined_team:
        jump outcome_Josh_and_Brigette

    if Josh_joined_team and Shouko_joined_team:
        jump outcome_Josh_and_Shouko

    if Josh_joined_team and Nine_joined_team:
        jump outcome_Josh_and_Nine

    if Josh_joined_team and Alistair_joined_team:
        jump outcome_Josh_and_Alistair

    if Josh_joined_team and Jessica_joined_team:
        jump outcome_Josh_and_Jessica


    # All Brigette, except with Josh
    if Brigette_joined_team and Shouko_joined_team:
        jump outcome_Brigette_and_Shouko

    if Brigette_joined_team and Nine_joined_team:
        jump outcome_Brigette_and_Nine

    if Brigette_joined_team and Alistair_joined_team:
        jump outcome_Brigette_and_Alistair

    if Brigette_joined_team and Jessica_joined_team:
        jump outcome_Brigette_and_Jessica


    # All Shouko, except with Josh or Brigette
    if Shouko_joined_team and Nine_joined_team:
        jump outcome_Shouko_and_Nine

    if Shouko_joined_team and Alistair_joined_team:
        jump outcome_Shouko_and_Alistair

    if Shouko_joined_team and Jessica_joined_team:
        jump outcome_Shouko_and_Jessica


    # All Nine, except with Josh, Brigette or Shouko
    if Nine_joined_team and Alistair_joined_team:
        jump outcome_Nine_and_Alistair

    if Nine_joined_team and Jessica_joined_team:
        jump outcome_Nine_and_Jessica


    # Alistair, with only Jessica
    if Alistair_joined_team and Jessica_joined_team:
        jump outcome_Alistair_and_Jessica

    return

label outcome_not_enough_members:
    centered "{b}{size=40}Score: 23\%{/size}{/b} \n
    Your score was... really bad - You failed, and quite miserably too."
    centered "You ended up having [num_team_members] members on your team. Let's just say the following 3 months consisted of many long sleepless nights."
    centered "If only you had 2 good teammates, how good would that have been? \n
    If not for your final score, then at least for the sake of your now very saggy eye bags. \n
    You had one job..."
    centered "You wish you had the confidence and charm of a Nigerian Prince to approach people and convince them to work with you."
    centered "Think about it, if you were to do it again, what could you have done better?"
    return


label outcome_Alistair_and_Jessica:
    centered "{b}{size=40}Score: 70{/size}{/b} \n
    Your score was good - but you feel like you could have done better."
    centered "Alistair ended up becoming your best friend and Jessica invited you to a lot of parties. \n Unfortunately, you start to become addicted to pancakes and also get drawn into the party life. You eventually lose grip of university and decide to become a dessert chef. \n
    But if you could do it again... who knows, maybe you could've gotten 100."
    centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"

    return


label outcome_Brigette_and_Alistair:
    if Brigette_mentioned_teddy and Alistair_mentioned_recipe:
        centered "{b}{size=40}Score: 100{/size}{/b} \n
        You got the best score! - however the group environment could have been better."
        centered "Strangely, you got a good score. While the group didn't get along well, things just seemed to fall into place."
        centered "You get a strong sense of deja vu, maybe it's something to do with that dream you had."
        centered "You didn't make any friends, but at least you got a great score."

    else:
        centered "{b}{size=40}Score: 76{/size}{/b} \n
        You did quite well - however the group could have gotten along better."
        centered "Alistair and Brigette lacked common interests and things to talk about, but pulled through with a decent score."
        centered "You saw it coming while you were working on the project, though there wasn't anything you could have done about it."
        if Alistair_mentioned_recipe:
            centered "You think back and remember you had a dream about pancakes on the day you met Alistair, cooking pancakes ... how strange!"
            centered "He didn't have a teddy though ... did Brigette have one?"
            centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"


    return

label outcome_Brigette_and_Jessica:
    if Brigette_mentioned_teddy and Jessica_mentioned_teddy:
        centered "{b}{size=40}Score: 90{/size}{/b} \n
        You did really well - you chose a great combo!"
        centered "Brigette and Jessica both became extremely close friends for life after bonding over having the same teddy bear."
        centered "You also become good friends with them, partying and hanging out with them all the time."
        centered "However, sometimes you wonder if they were too similar, and if you could have achieved more with a variety in team members."
        centered "Ultimately, you finished with a great score and some good friends, which is what matters."
        centered "You still feel like you could have done better though ... and you still wonder what that dream you had on the first day was"

    else:
        centered "{b}{size=40}Score: 67{/size}{/b} \n
        You didn't do great ... but you passed! - the group dynamic was alright."
        centered "While everyone contributed, it just seemed a little awkward between Brigette and Jessica."
        centered "You feel like they could have gotten along well, but something was just missing."
        centered "If only you had gotten to know them more before deciding to work with them..."
        centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"
    return

label outcome_Brigette_and_Nine:
    centered "{b}{size=40}Score: 0{/size}{/b} \n
    Your score was really good but... you were caught cheating - this was the worst group you've been in ever."
    centered "Brigette and Nine fought all the time and you weren't able to coordinate anything."
    centered "In the end, Nine submitted the work ... but he was caught cheating."
    centered "You feel like it's impossible to work with Nine."
    centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"
    return

label outcome_Brigette_and_Shouko:
    if Brigette_mentioned_teddy and Shouko_mentioned_teddy:
        centered "{b}{size=40}Score: 80{/size}{/b} \n
        You did really well - the group environment was great!"
        centered "Brigette and Shouko bonded over their teddies and became close friends."
        centered "You feel like you worked well together, but sometimes things felt too repetitive."
        centered "Perhaps you needed more variety in your group, since Brigette and Shouko brought too similar thoughts to the table."
        centered "Despite a great score, you still feel like you could have done better ... and you wonder what that dream you had on the first day was"

    else:
        centered "{b}{size=40}Score: 55{/size}{/b} \n
        You didnt do great - Shouko and Brigette did not get along at all."
        centered "Shouko was easily offended by Brigette, despite her having good intentions, and miscommunication was rampant."
        centered "You feel the only thing that held you back was their differing personalities."
        centered "You also noticed they both had a teddy bear in their video. How interesting."
        centered "Maybe there was a way for things to have been better."
        centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"

    return

label outcome_Josh_and_Alistair:
    centered "{b}{size=40}Score: 76{/size}{/b} \n
    You did great - everyone worked well together!"
    centered "Your group got along with each other very well, leading to a great group-work experience."
    centered "You become close friends but only for the semester, quickly drifting apart as there was little common interests."
    centered "You feel the group was definitely solid, but something was definitely missing, something Josh and Alistair didnt have..."
    centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"

    return
label outcome_Josh_and_Brigette:
    if Brigette_mentioned_teddy and Josh_mentioned_guitar:
        centered "{b}{size=40}Score: 80{/size}{/b} \n
        You did really well - the group environment was alright, but sometimes a bit awkward for you."
        centered "You become quite close to both of them, enjoying their company."
        centered "You felt like something was blooming between the two ... but you're not sure."
        centered "You think they would make a good couple."
        centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"

    else:
        centered "{b}{size=40}Score: 77{/size}{/b} \n
        You did quite well - you felt like you were third wheeling at times ... despite them claiming to not be dating."
        centered "You dont become very close to either of them, and go your seperate ways"
        centered "They seem like a couple so much that it's strange they aren't already dating"
        centered "You feel happy ..."
        centered "for Josh and Bridgette but feel lonely yourself"
        centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"
    return
label outcome_Josh_and_Jessica:
    if Jessica_mentioned_teddy and Josh_mentioned_guitar:
        centered "{b}{size=40}Score: 80{/size}{/b} \n
        You did very well - the group environment was ok."
        centered "Although initially it seemed like you were bound for a bad score..."
        centered "You somehow pull through, and you all become good friends."
        centered "It was almost as if Jessica's teddy helped out."
        centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"
    else:
        centered "{b}{size=40}Score: 62{/size}{/b} \n
        You did ok - the group environemnt was mild at best."
        centered "You already felt initally that this wasnt going to work out, but it definitely could have been worse."
        centered "You guys hardly stayed in contact, you just felt that no one had anything in common."
        centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"
    return
label outcome_Josh_and_Nine:
    centered "{b}{size=40}Score: 0{/size}{/b} \n
    Your score was really good but... you were caught cheating - the group was a disaster!"
    centered "No one got along with each other at all. You do the project yourself, only to have Nine submit his own work."
    centered "Nine tells Josh you were the reason they failed and Josh now hates you."
    centered "Turns out Nine really is just all talk and is just a cheater."
    centered "This was awful. If only you could rewind time..."
    centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"
    return
label outcome_Josh_and_Shouko:
    if Shouko_mentioned_teddy and Josh_mentioned_guitar:
         centered "{b}{size=40}Score: 80{/size}{/b} \n
         You did very well - there was a really good group environment."
         centered "You become quite close with both Josh and Shouko, and Josh even teaches both of you to play guitar!"
         centered "The group work was very efficient, almost as if Shouko's teddy was helping out too."
         centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"
    else:
        centered "{b}{size=40}Score: 73{/size}{/b} \n
        You did well - everyone had a good time."
        centered "You three become friends but nothing special happens."
        centered "You feel like there was something missing. Perhaps the dream has something to do with it..."
        centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"
    return
label outcome_Nine_and_Alistair:
    centered "{b}{size=40}Score: 56{/size}{/b} \n
    Your score wasn't incredible, but at least you passed - your group did not get along well."
    centered "Nine was extremely insistent on cheating, but Alistair eventually convinced him not to. You all do the projects together, despite Nine complaining the entire time."
    centered "You merely stay tutorial friends with Alistair, and you don't really interact with Nine at all after the project is submitted."
    centered "There must have been a way to do better ... and you wonder what that dream you had on the first day was about"
    return
label outcome_Nine_and_Jessica:
    centered "{b}{size=40}Score: 0{/size}{/b} \n
    Your score was really good but... you were caught cheating - the group also struggled to do work together."
    centered "You become extremely close with Nine and Jessica. Both you and Nine become addicted to partying along with Jessica. \n
    You drop out of University to party and live off Nine's huge allowance. You really enjoy your life... but you've lost yourself."
    centered "You wonder what your life would have been like if you had passed this class..."
    centered "but that dream you had on the first day still haunts you"
    return
label outcome_Shouko_and_Alistair:
    if Shouko_mentioned_teddy and Alistair_mentioned_recipe:
        centered "{b}{size=40}Score: 100{/size}{/b} \n
        You got full marks ... and even set a record - Shouko and Alistair loved working with you."
        centered "You feel a sense of deja vu. This group project reminds you of that dream you had, with the teddybear and pancake."
        centered "The group members become lifelong friends, and you push each other to pursure their dreams."
        centered "You feel incredibly happy."
    else:
        centered "{b}{size=40}Score: 80{/size}{/b} \n
        You did very well  - your group enjoyed working together."
        centered "Alistair did a lot of the work and even taught both you and Shouko a few tricks. You remain friends with them, but only temporarily. \n
        While you scored well, you just feel like you missed something important ... You wonder why Alistair never had his camera on."
        centered "You feel still like you could have done better ... and you wonder what that dream you had on the first day was"
    return
label outcome_Shouko_and_Jessica:
    if Shouko_mentioned_teddy and Jessica_mentioned_teddy:
        centered "{b}{size=40}Score: 90{/size}{/b} \n
        You topped the class ... and set a personal record - everyone had a great time working together."
        centered "You become best friends with Shouko and Jessica.\n
        Shouko becomes less shy after partying with Jessica, and Jessica learns to be more empathetic from Shouko."
        centered "They are definitely an unconventional duo. You're glad you chose them to be in your team."
        centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"
    else:
        centered "{b}{size=40}Score: 75{/size}{/b} \n
        Your score was good - but you feel like you could have done better."
        centered "Shouko messaged you occasionally and Jessica invited you to a lot of parties, but you never became close with either of them. \n
        You eventually lose contact with both Shouko and Jessica."
        centered "Perhaps there was a way to make this unconventional pair work."
        centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"
    return
label outcome_Shouko_and_Nine:
    centered "{b}{size=40}Score: 0{/size}{/b} \n
    Your score was really good but... you were caught cheating - Nine is irritated and Shouko is very upset."
    centered "Nine ended up blaming you and Shouko for cheating, and Shouko now has trust issues. \n
    Shouko stayed silent throughout the whole project, almost as silent as her teddy."
    centered"Unfortunately, you recieve an 'at risk' email, and must speak university representatives. You eventually lose grip of university and leave."
    centered "You now also have trust issues."
    centered "If only there was a way to rewind time and do this all over again..."
    centered "You feel like you could have done better ... and you wonder what that dream you had on the first day was"
    return
