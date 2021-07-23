##########################################################################################
##########################################################################################
##### WESTRA ###################

label westra_dialog:
    play music westra
    scene wall
    show tabled
    show westra behind tabled at truecenter:
        zoom 0.3
    if gamedata["westra_talked"]:
        if gamedata["c_westra"] < 5:
            "She looks at you coldly."
            w "What?"
        else:
            w "Hello, [playername]."
        jump selection
    python:
        if gamedata["westra_talked"] == False:
            gamedata["c_westra"] += 1
            convo = "westra_" + str(gamedata["c_westra"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(w, "Error: No dialog.")
                renpy.jump("selection")
        else:
            renpy.jump("selection")

##########################################################################################
##########################################################################################
## WESTRA DIALOG ##
label westra_1:
    python:
        print("Westra 1 playing.")
    "You decide to approach a lady at the bar."
    menu:
        "She sits atop a barstool reading a book. She doesn't notice you."

        "Excuse me.":
            q "Yes, excuse you."
        "Enjoying your book?":
            q "Enjoying pestering people who are trying to enjoy their book?"
    q "I just want my peace and quiet. Please leave me alone."
    "She goes back to reading her book. Perhaps now isn't the best time."
    jump westra_done

label westra_2:
    python:
        print("Westra 2 playing.")
    "You decide to approach the wizard again."
    menu:
        "The scholarly woman is still reading her book."

        "What are you reading?":
            q "None of your business."
        "Can I buy you a drink?":
            q "No."
        "...":
           "She still doesn't notice you standing there."

    "She continues reading her book without acknowledging you further."
    menu:

            "Why won't you talk to me?":
                q "Because I'm busy studying my spellbook. This is important royal work. Leave me alone."
            "Fine. I'll leave then.":
                q "Good. These spells won't study themselves."

    "You leave her to study her spells."

    jump westra_done

label westra_3:
    python:
        print("Westra 3 playing.")
    "Despite your previous attempts, you decide this might be the right time to approach the wizard."
    "She puts down her book and sighs."
    q "You again. Don't you have better things to do than pester me?"
    "She sighs, and for once she actually puts her book down and looks directly at you."
    q "You are going to waste my time again with more of your 'conversation skills', are you?"
    menu:
        q "What is it that you want from me?"

        "Just looking to be friendly.":
            q "I don't need friends, I need time to study my spells.."
            "She grimaces, but then sighs and looks down."
            q "Forgive me. I can't be turning down allies at a time like this."
        "I want to look in your spellbook.":
            q "There's nothing for you to see in my spellbook. Unless..."
            q "Do you want to be a mage, perhaps?"
            q "Maybe there is merit to our alliance, yet."
    q "My name is Westra. I am court mage to his royal highness King Adelaide."
    w "And your name is.. [playername]?"
    "She smirks."
    w "Of course you are. Dane wouldn't shut up about meeting a new friend in the tavern."
    w "My apologies for being curt. You wouldn't believe the kinds of people who bother you here."
    w "Well, actually, you might know exactly what I mean. If you don't yet, I'm sure you will if you hang around here too long."
    w "I'm going to head back to the castle. Maybe I'll see you over there sometime?"
    w "Maybe we can discuss the finer intricacies of magic sometime.."
    "She raises her eyebrows briefly and walks out of the establishment."
    jump westra_done

label westra_done:
    python:
        gamedata["westra_talked"] = True

    jump start_music