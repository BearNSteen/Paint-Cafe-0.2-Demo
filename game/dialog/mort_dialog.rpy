##########################################################################################
##########################################################################################
##### MORT ###################
label mort_dialog:
    stop music fadeout 2.0
    play music dane
    show mort at truecenter
    if gamedata["mort_talked"]:
        "He looks blankly back at you."
        m "Do you need something, pal?"
        jump back
    jump mort_forward
label mort_forward:
    python:
        if gamedata["mort_talked"] == False:
            gamedata["c_mort"] += 1
            convo = "mort_" + str(gamedata["c_mort"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(None, "Error: End of dialog.")
                renpy.jump("cafe_menu_kazzik")
        else:
            renpy.jump("cafe_menu_kazzik")

##########################################################################################
##########################################################################################
## MORT DIALOG ##

label mort_1:
    python:
        print("Mort 1 playing.")
    "Mort sees you and squawks violently."
    jump mort_done


label mort_done:
    python:
        gamedata["mort_talked"] = True
        g.save(gamedata)
        renpy.jump(label="cafe_menu_kazzik")