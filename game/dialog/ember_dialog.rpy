##########################################################################################
##########################################################################################
##### EMBER ###################

label ember_dialog:
    play music dane
    scene wall
    show tabled
    show ember behind tabled at truecenter
    if gamedata["ember_talked"]:
        if gamedata["c_ember"] < 5:
            "She turns to you and waves widely."
            emb "Hiiiiiiii [playername]!!!"
        else:
            emb "Good to see you, [playername]."
            "She smiles at you."
        jump selection
    python:
        if gamedata["ember_talked"] == False:
            gamedata["c_ember"] += 1
            convo = "ember_" + str(gamedata["c_ember"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(emb, "Error: No Ember dialog.")
                renpy.jump("selection")
        else:
            renpy.jump("selection")


##########################################################################################
##########################################################################################
## EMBER DIALOG ##
label ember_1:
    python:
        print("Ember 1 playing.")
    "You see a red-headed lady at the bar."
    menu:
        "Atop her barstool, she spins around and shouts boisterously and unintelligibly at the other patrons."

        "Um.. hello there.":
            emb "Hiiiiii!"
        "Having fun?":
            emb "Yesssssssss!"
    emb "I'm Ember!! Whooooo are you?"
    menu:
        "Despite asking you this, she continues spinning uncontrollably."

        "I'm [playername]. Who are you?":
            emb "Hiiiiii [playername]!"
        "Could you stop spinning please?":
            emb "Noooooope! I'll never stop!"

    "She stands up proudly on her seat, holding her questionably marked bottle."
    emb "You need to try some of this stuff they're serving here!"
    "She hiccups audibly and falls down into her seat. She seems to have been quieted down by gravity."
    emb "We shoulddd talk sometimee. T-talk more. Drink, MORE! We shouldd.. d-drink sometime.."
    "She falls asleep in her chair."
    "Perhaps you should leave her be."
    jump ember_done

label ember_2:
    python:
        print("Ember 2 playing.")
    "The boisterous woman is back at the bar again."
    menu:
        emb "Hiiiii [playername]!"

        "Hello again, Ember.":
            emb "You said hi to me, yaaaaay."
        "Can I.. buy you a drink?":
            emb "I already have a drink, but okay!"
        "...":
           "Hiiiiii quiet person!!"

    "She spins around in her chair. It's clear that she's excited to see you."
    menu:

        "What brings you here?":
            emb "Drinking! Drinking drinking and more drinking! BARTENDER!!"
        "Uh.. nice weather we're having.":
            emb "I wouldn't know, I've been inside for hours!! Speaking of which..."

    "She slams on the table."
    n "I told you that you're being cut off. Please stop asking for more drinks."
    emb "Uuuuuugh. You're no funnnnnn! You should be more fun! And you should drink!!"
    "Cuppa walks away sighing."
    n "Good luck with this one, [playername]. She's a slippery one."
    emb "And your jokes suck!!"
    "She sits back in her chair and continues drinking her questionable liquid."
    emb "I'll buy you something next time! We can drink together!!"
    "She turns away from you and starts shouting for the bartender again."

    jump ember_done

label ember_done:
    python:
        gamedata["ember_talked"] = True

    jump selection
