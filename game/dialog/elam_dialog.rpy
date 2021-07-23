#########################################################################################
##########################################################################################
##### ELAM  ###################
label elam_dialog:
    stop music fadeout 2.0
    play music dane
    scene wall
    show tabled
    show elam behind tabled at truecenter:
        zoom .3
    if gamedata["elam_talked"]:
        "He looks at you from the shadows."
        d "[playername]..."
        jump back
    jump elam_forward
label elam_forward:
    python:
        if gamedata["elam_talked"] == False:
            gamedata["c_elam"] += 1
            convo = "elam_" + str(gamedata["c_elam"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(None, "Error: End of dialog.")
                renpy.jump("back")
        else:
            renpy.jump("selection")

##########################################################################################
##########################################################################################
## ELAM DIALOG ##

label elam_1:
    python:
        print("elam 1 playing.")
    jump elam_done


label elam_done:
    python:
        gamedata["elam_talked"] = True
        g.save(gamedata)
        renpy.jump(label="start_music")