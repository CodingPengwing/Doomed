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
    $ player_score = "High Distinction"
    return


label outcome_Josh_and_Alistair:
    $ player_score = "High Distinction"
    return

label outcome_Josh_and_Brigette:
    $ player_score = "High Distinction"
    return

label outcome_Josh_and_Jessica:
    $ player_score = "High Distinction"
    return

label outcome_Josh_and_Nine:
    $ player_score = "High on Drugs"
    return

label outcome_Josh_and_Shouko:
    $ player_score = "High on Drugs"
    return


label outcome_Nine_and_Alistair:
    $ player_score = "High on Drugs"
    return

label outcome_Nine_and_Jessica:
    $ player_score = "High on Drugs"
    return


label outcome_Shouko_and_Alistair:
    if Shouko_mentioned_teddy and Alistair_mentioned_recipe
        centered "{b}{size=40}Score: 100{/size}{/b} \n
        You got full marks ... and even set a record - Shouko and Alistair loved working with you"
        centred "You feel a sense of deja vu, and it reminds you of that dream you had, with the teddybear and pancake"
        centred "The group becomes lifelong friends, and you push each other to pursure their dreams"
        centred "You feel incredibly happy"
    else
        centered "{b}{size=40}Score: 80{/size}{/b} \n"
    return

label outcome_Shouko_and_Jessica:
    if Shouko_mentioned_teddy and Jessica_mentioned_mask
        centered "{b}{size=40}Score: 90{/size}{/b} \n
        You topped the class ... and set a personal record - everyone had a great time"
        centred "You become best friends with Shouko and Jessica.\n
        Shouko becomes less shy after partying with Jessica- Jessica learns to be more empathetic from Shouko"
    else
        centered "{b}{size=40}Score: 75{/size}{/b} \n
        Your score was good - but you feel like you could have done better."
        centered "Shouko ended up becoming good friends with you and Jessica invited you to a lot of parties but you never became close. \n  
        You eventually lose contact with both Shouko and Jessica"
    return

label outcome_Shouko_and_Nine:
    centered "{b}{size=40}Score: 0{/size}{/b} \n
    Your score was really good - but... you were caught cheating"
    centered "Nine ended up blaming you and Shouko for cheating, and Shouko now has trust issues. \n 
    Unfortunately, you recieve an \'at risk\' email, and must speak university representatives. You eventually lose grip of university and leave. \n
    You now also have trust issues"
    return
