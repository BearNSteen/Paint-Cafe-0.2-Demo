##########################################################################################
##########################################################################################
##### LANA ###################
label lana_dialog:
    stop music fadeout 2.0
    play music dane
    scene wall
    show tabled
    show lana behind tabled at truecenter:
        zoom .3
    if gamedata["lana_talked"]:
        "She sips her water and nods at you."
        l "[playername] has come to visit me. Thank you for the visit."
        jump back
    jump lana_forward
label lana_forward:
    python:
        if gamedata["lana_talked"] == False:
            gamedata["c_lana"] += 1
            convo = "lana_" + str(gamedata["c_lana"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(None, "Error: End of dialog.")
                renpy.jump("back")
        else:
            renpy.jump("selection")

##########################################################################################
##########################################################################################
## LANA DIALOG ##

label lana_1:
    python:
        print("Lana 1 playing.")
    jump lana_done


label lana_done:
    python:
        gamedata["lana_talked"] = True
        g.save(gamedata)
        renpy.jump(label="start_music")