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
    centered "Your score was good - but you could have done better
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
    $ player_score = "High on Drugs"
    return

label outcome_Shouko_and_Jessica:
    $ player_score = "High on Drugs"
    return

label outcome_Shouko_and_Nine:
    $ player_score = "High on Drugs"
    return
