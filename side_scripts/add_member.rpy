label add_Josh:
    if num_team_members >= 2:
        "Your team is already full"
        return
    if Josh_angry:
        "You pissed off Josh, looks like he doesn't want to join your team..."
        return

    "{i}Josh joined your team."
    $ Josh_joined_team = True
    $ num_team_members += 1
    return

label add_Brigette:
    if num_team_members >= 2:
        "Your team is already full"
        return
    if Brigette_angry:
        "You pissed off Brigette, looks like she doesn't want to join your team..."
        return

    "{i}Brigette joined your team."
    $ Brigette_joined_team = True
    $ num_team_members += 1
    return

label add_Nine:
    if num_team_members >= 2:
        "Your team is already full"
        return
    if Nine_angry:
        "You pissed off Nine, looks like he doesn't want to join your team..."
        return

    "{i}Nine joined your team."
    $ Nine_joined_team = True
    $ num_team_members += 1
    return

label add_Shouko:
    if num_team_members >= 2:
        "Your team is already full"
        return
    if Shouko_angry:
        "You pissed off Shouko, looks like she doesn't want to join your team..."
        return

    "{i}Shouko joined your team."
    $ Shouko_joined_team = True
    $ num_team_members += 1
    return

label add_Jessica:
    if num_team_members >= 2:
        "Your team is already full"
        return
    if Jessica_angry:
        Jessica "You seriously think I would even consider working with you??"
        return

    "{i}Jessica joined your team."
    $ Jessica_joined_team = True
    $ num_team_members += 1
    return

label add_Alistair:
    if num_team_members >= 2:
        "Your team is already full"
        return
    if Alistair_angry:
        Alistair "Not after what you've said."
        return

    "{i}Alistair joined your team."
    $ Alistair_joined_team = True
    $ num_team_members += 1
    return
