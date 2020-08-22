label breakout_room_1:

    scene blank

    show Josh_1 at top_left_screen

    show Brigette_1 at top_right_screen

    Josh "Hi I'm Josh"
    Brigette "Hi I'm Bri"

    hide Josh_1
    hide Brigette_1


#     "this in text box, but no speaker"
#
#     centered "text in the middle of screen"
#
#     player "the player says this"
#
#     $ num_team_members
#
#     "this will display the [playerNa] and the [num_team_members]"
#
#     menu:
#         "Option 1":
#             call action1
#             pass
#
#         "Option 2":
#             jump action2
#
#     if not Josh_angry:
#         call action1
#
#     return
#
# label action1:
#     Josh "Hello"
#     $ Josh_angry = True
#     return
#
# label action2:
#     Brigette "Hi"
#     return
