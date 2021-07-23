##########################################################################################
##########################################################################################
##### BOYD ###################
label boyd_dialog:
    stop music fadeout 2.0
    play music dane
    scene wall
    show tabled
    show boyd behind tabled at truecenter:
        zoom .3
    if gamedata["boyd_talked"]:
        "He takes a big swig of ale and nods."
        d "Aye, [playername]. Great to see ya."
        jump back
    jump boyd_forward
label boyd_forward:
    python:
        if gamedata["boyd_talked"] == False:
            gamedata["c_boyd"] += 1
            convo = "boyd_" + str(gamedata["c_boyd"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(None, "Error: End of dialog.")
                renpy.jump("back")
        else:
            renpy.jump("selection")

##########################################################################################
##########################################################################################
## BOYD DIALOG ##

label boyd_1:
    python:
        print("Boyd 1 playing.")
    jump boyd_done


label boyd_done:
    python:
        gamedata["boyd_talked"] = True
        g.save(gamedata)
        renpy.jump(label="start_music")