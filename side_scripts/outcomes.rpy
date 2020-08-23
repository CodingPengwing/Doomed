label end_game:

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


label outcome_Alistair_and_Jessica:
    centered "{b}{size=40}Score: 70{/size}{/b} \n
    Your score was good - but you feel like you could have done better."
    centered "Alistair ended up becoming your best friend and Jessica invited you to a lot of parties. \n Unfortunately, you start to become addicted to pancakes and also get drawn into the party life. You eventually lose grip of university and decide to be a dessert chef. \n
    But if you could do it again... who knows, maybe you could've gotten 100."
    return


label outcome_Brigette_and_Alistair:
    $ player_score = "High Distinction"
    return

label outcome_Brigette_and_Jessica:
    $ player_score = "High Distinction"
    return

label outcome_Brigette_and_Nine:
    $ player_score = "High Distinction"
    return

label outcome_Brigette_and_Shouko:
    if Brigette_mentioned_teddy and Shouko_mentioned_teddy
        centered "{b}{size=40}Score: 80{/size}{/b} \n
        You did really well - the group environment great"
        centered "Brigette and Shouko bonded over their teddies and became close friends"
        centered "You feel like you worked well together, but sometimes things felt too repetitive"
        centered "You feel that you needed more variety in your group, that Brigette and Shouko bought similar thoughts to the table"
        centered "Despite a great score, you feel you could have done better"
    else 
        centered "{b}{size=40}Score: 55{/size}{/b} \n
        You didnt do great - Shouko and Brigette did not get along at all"
        centered "Shouko was easily offended by Brigette despite her having good intensions and miscommunication was rampant"
        centered "You feel the only thing that held you back was their personalities not aligning"
        centered "You also noticed they both had a teddy bear in their video"
    return

label outcome_Josh_and_Alistair:
    centered "{b}{size=40}Score: 76{/size}{/b} \n
    You did great - everyone worked well together"
    centered "Your group got along with eachother very well, leading to a great time together"
    centered "You become close friends but only for the semester, quickly drifting apart as there was little common interests"
    centered "You feel the group was definitely solid, but something was definitely missing, something Josh and Alistair didnt have..."
    return

label outcome_Josh_and_Brigette:
    if Brigette_mentioned_teddy and Josh_mentioned_guitar
        centered "{b}{size=40}Score: 80{/size}{/b} \n
        You did really well - the group environment was really good but sometimes a bit awkward for you"
        centered "You become quite close to both of them, enjoying their company"
        centered "You felt like something was blooming between the two ... but you're not sure."
        centered "You think they would make a good couple"
    else
        centered "{b}{size=40}Score: 77{/size}{/b} \n
        You did quite well - you felt like you were third wheeling at times ... despite them not dating"
        centered "You dont become very close to either of them, and go your seperate ways"
        centered "They seem like a couple so much that it's strange they aren't already dating"
        centered "You feel happy ..."
        centered "for Josh and Bridgette but feel lonely yourself"
    return

label outcome_Josh_and_Jessica:
    if Jessica_mentioned_teddy and Josh_mentioned_guitar
        centered "{b}{size=40}Score: 80{/size}{/b} \n
        You did very well - the group environment was ok"
        centered "Although initially it seemed like you were bound for a bad score..."
        centered "You somehow pull through, and all become good friends"
        centered "It was almost as if Jessica's teddy helped out"
    else 
        centered "{b}{size=40}Score: 62{/size}{/b} \n
        You did ok - the group environemnt was mild at best"
        centered "You already felt initally that this wasnt going to work out, but it definitely could have been worse"
        centered "You guys hardly stayed in contact, you just felt that no one had anything in common"
    return

label outcome_Josh_and_Nine:
    centered "{b}{size=40}Score: 0{/size}{/b} \n
    Your score was really good but... you were caught cheating - the group was a disaster"
    centered "No one got along with eachother well, you do the project yourself only to have Nine submit his own work"
    centered "Nine tells Josh you were the reason they failed and Josh now hates you"
    centered "Turns out Nine really is just all talk and is just a cheater"
    centered "You are unhappy"
    return

label outcome_Josh_and_Shouko:
    if Shouko_mentioned_teddy and Josh_mentioned_guitar
         centered "{b}{size=40}Score: 80{/size}{/b} \n
         You did very well - there was a really good group environment"
         centered "You become quite close with both Josh and Shouko, and Josh even teaches both of you to play guitar!"
         centered "The group work was very efficient, almost felt as if Shouko's teddy was helping out too"
    else
        centered "{b}{size=40}Score: 73{/size}{/b} \n
        You did well - everyone had a good time"
        centered "You three become friends but nothing special happens"
        centered "You feel like there was something missing"
    return


label outcome_Nine_and_Alistair:
    centered "{b}{size=40}Score: 56{/size}{/b} \n
    Your score wasn't incredible but at least you passed - your group did not get along well"
    centered "Nine was extremely insistent on cheating but Alistair convinced him not to. You did the projects without Nine making it difficult"
    centered "You merely stay tutorial friends with Alistair and dont really interact with Nine at all"
    return

label outcome_Nine_and_Jessica:
    centered "{b}{size=40}Score: 0{/size}{/b} \n
    Your score was really good but... you were caught cheating - the group also struggled to do work together"
    centered "You become extremely close with Nine and Jessica. Both you and Nine become addicted to partying along with Jessica. \n
    You drop out of University to party and live off Nine. You really enjoy your life"
    return


label outcome_Shouko_and_Alistair:
    if Shouko_mentioned_teddy and Alistair_mentioned_recipe
        centered "{b}{size=40}Score: 100{/size}{/b} \n
        You got full marks ... and even set a record - Shouko and Alistair loved working with you"
        centered "You feel a sense of deja vu, and it reminds you of that dream you had, with the teddybear and pancake"
        centered "The group becomes lifelong friends, and you push each other to pursure their dreams"
        centered "You feel incredibly happy"
    else
        centered "{b}{size=40}Score: 80{/size}{/b} \n
        You did very well  - enjoyed working together"
        centered "Alistair did a lot of the work and even taught both you and Shouko a few tricks. You remain friends with them but only temporarily. \n
        While you scored well, you just feel like you missed something important ... also I wonder why Alistair didn't have his camera on"
    return

label outcome_Shouko_and_Jessica:
    if Shouko_mentioned_teddy and Jessica_mentioned_teddy
        centered "{b}{size=40}Score: 90{/size}{/b} \n
        You topped the class ... and set a personal record - everyone had a great time"
        centered "You become best friends with Shouko and Jessica.\n
        Shouko becomes less shy after partying with Jessica- Jessica learns to be more empathetic from Shouko"
    else
        centered "{b}{size=40}Score: 75{/size}{/b} \n
        Your score was good - but you feel like you could have done better."
        centered "Shouko ended up becoming good friends with you and Jessica invited you to a lot of parties but you never became close. \n  
        You eventually lose contact with both Shouko and Jessica"
    return

label outcome_Shouko_and_Nine:
    centered "{b}{size=40}Score: 0{/size}{/b} \n
    Your score was really good but... you were caught cheating - Nine is irritated and Shouko is very unhappy"
    centered "Nine ended up blaming you and Shouko for cheating, and Shouko now has trust issues. \n 
    Shouko stayed very silent throughout the whole project, almost as silent as her teddy"
    Unfortunately, you recieve an 'at risk' email, and must speak university representatives. You eventually lose grip of university and leave."
    centered "You now also have trust issues"
    return
