##########################################################################################
##########################################################################################
##### ELLIE ###################

label ellie_dialog:
    play music ellie
    python:
        if who_list[1] == 3:
            renpy.jump(label='ellie_castle')
    scene wall
    show tabled
    if gamedata["ellie_talked"]:
        if gamedata["c_ellie"] < 3:
            "She sips her drink and looks down at you."
            e "What do you want?"
        else:
            "She puts down her drink and looks at you inquisitively."
            e "[playername]. Do you need something from me?"
        jump selection
    if gamedata["ellie_mad"] > 0:
        python:
            gamedata["ellie_talked"] = True
        if gamedata["ellie_mad"] > 1:
            "She ignores you. She probably won't want to talk with you for [gamedata["ellie_mad"]] more days."
        else:
            e "So you've come crawling back to me, hmm?"
            e "Have you given your actions some thought? Perhaps you won't want to disrespect me as much in the future."
            e "I don't have to put up with you, but this time I'll let it slide."
            e "Now get out of my sight."
        python:
            gamedata["ellie_mad"] -= 1
        jump selection
    jump ellie_continue
label ellie_castle:
    scene bg hallway
    show ellie at truecenter
    if gamedata["ellie_talked"]:
        e "Oh, it's you. Look, I have some royal business that needs doing. Elsewhere."
        "She walks away from you."
        jump select_castle
label ellie_continue:
    python:
        if gamedata["ellie_talked"] == False:
            gamedata["c_ellie"] += 1
            convo = "ellie_" + str(gamedata["c_ellie"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(e, "Error: No Ellie dialog.")
                renpy.jump("selection")
        else:
            renpy.jump("selection")

##########################################################################################
##########################################################################################
## ELLIE DIALOG ##

label ellie_1:
    python:
        print("Ellie 1 playing.")
    show ellie behind tabled at truecenter:
        zoom .4
        ypos .7
    "A short irritated lady looks simultaneously confused and concerned as you approach."
    q "Oh, look. It's a peasant approaching my table, looking for friendship and companionship."
    q "Joyous day. I can finally experience what I've always dreamed of, real life and romance and destiny!"
    q "Get away from my table. You're dirtying it up with your presence."
    "You stare confused and are unsure of what to do."
    menu:
        q "What??"

        "I just wanted to --":
            q "You just wanted to get in my space."
        "My name is --":
            q "Is the name of a peasant important to me?"
    q "I'll have you know that you are speaking to royalty. I shouldn't even be in a place like this."
    q "My boneheaded bodyguard told me to come here and wait for him in a \"lovely, peaceful atmosphere\"."
    q "I can't fathom what in the world he could be talking about in regards to this.. hole."
    q "I feel as if I have already caught every known disease just sitting in this booth."
    q "But despite that, I would take that experience any day over having to listen to the likes of you."
    q "Now then, leave me alone to enjoy my tea. Far on the other side of the room, preferably."
    "She turns away from you. You consider taking more of a verbal beating, but decide to call it quits and return to your table."
    jump ellie_done

label ellie_2:
    show ellie behind tabled at truecenter:
        zoom .4
        ypos .7
    python:
        print("Ellie 2 playing.")
    q "You again. What do you want this time?"
    menu:
        "Waiting for Dane again?":
            q "How do you know who I'm waiting for, peasant?"
            q "That information is on a purely need-to-know basis, a basis which you are not privy to."

    "She tries to turn away from you again, but after seeing your unwavering resolve to stand in place, she takes another stab at turning you away."
    q "I, Princess Elena Adelaide, deserve better than your company."
    e "A princess should not be in the presence of commoners, unless they are in the employ of the royal guard."
    e "Clearly, you are not a member of the royal guard. The only thing you are clearly a part of is the lowest of low classes."
    "She looks down at you over her nose, which is very ineffective considering she is seated and is also shorter than you."
    e "Ugh... why aren't you leaving?"
    e "And where's Dane...? If he were here, I could just have him push you away into a gutter or something."
    e "But.. if you know who he is... chances are good that you're already friends with him..."
    "She sighs audibly and very aggressively, turning the heads of some of those in the tavern."
    e "Your presence irks me greatly. But I just have the worst feeling Dane is going to make me interact with you at some point anyway."
    e "Tell me your name, commoner. Quickly, before I change my mind."
label ellie_answer_1:
    menu:
        "My name is [playername].":
            e "[playername]? The names the common people give their children these days, I swear."
        "I am Silas Dane, Royal Bodyguard! Feel the might of my sword...":
            e "Is that supposed to be a joke?"
            e "I could see him saying that... but that is most assuredly not who you are. I would know my boneheaded guard anywhere."
            jump ellie_answer_1

    "You tell her very quickly that you aren't a peasant, and that you don't actually know why you're here."
    e "What? Not a peasant? With clothes like that? Surely you must be joking. Although..."
    "She eyes you up and down."
    e "... I don't think I've seen anyone wear clothes like that before. You must be from Dunmerk or something."
    e "I'm going to pretend you're some kind of Dunmerkian royal so I don't feel so disgusting talking to you."
    # insert door noise
    "The door to the tavern suddenly opens and in walks a familiar face."
    show ellie behind tabled at truecenter:
        ypos .7
        linear .5 xpos .3
        zoom .4
    show dane behind tabled at truecenter:
        zoom .3
        xpos 1.2
    show dane behind tabled at truecenter:
        zoom .3
        linear .5 xpos .7
    d "Ah, your highness! I told you waiting in here would be a good idea. How do you find the ---"
    "He pauses as he sees you sitting with the Princess. He puts his hand on his sword hilt momentarily, then removes it when he realizes who you are."
    d "[playername]! I did not expect to see you at the table with the Princess."
    "He squints as he looks at Ellie, realizing that she's talking to someone who isn't royalty."
    d "Okay, something's wrong here. Did you do something to the Princess?"
    e "No, Dane. Just because your incompetent self wasn't here protecting me doesn't mean I can't have conversations with the.. real people of Santos."
    "She starts to squint too as she looks at you. Perhaps she's trying not to see you in order to help pretend that you're royalty."
    menu:
        "[Start squinting at Dane and Ellie]":
            "Dane stops squinting to rub his eyes with his gauntlets. Ellie sighs."
        "[Wave at the two people squinting at you]":
            d "Oh, hello there, [playername]."
            "Dane waves back at you. Ellie puts her face in her hands and groans audibly."
    e "Dane, we need to stop fooling around. Why did you make me come here in the first place?"
    d "Oh, no reason, really. I just wanted you to experience something other than the castle for once. And look, you made a new friend!"
    show ellie behind tabled at truecenter:
        ypos .6 xpos .3
        zoom .4
    "Ellie stands up."
    e "Nonsense. I was making idle chatter because YOU decided to take your sweet time coming to get me. Let's get out of here."
    show ellie behind tabled at truecenter:
        zoom .4
        ypos .6
        linear .5 xpos -.5
    show dane behind tabled at truecenter:
        zoom .3
        linear .5 xpos .5
    
    "Ellie walks out of the establishment. You can see her out the window looking very impatient."
    hide ellie
    d "Well, I guess I'd better follow her. Hope you two were getting along! Ha ha..."
    "He laughs dryly. You get the feeling that she doesn't get along with a lot of people."
    d "Have a good one, [playername]."
    show dane behind tabled at truecenter:
        zoom .3
        linear .5 xpos 1.2
    "Dane stands up and follows Ellie out the door."

    jump ellie_done

label ellie_3:
    show ellie behind tabled at truecenter:
        ypos .7
        xpos .3
        zoom .4
    show westra behind tabled at truecenter:
        zoom .3
        xpos .7
    "You see Her Majesty sitting at a table with another familiar face."
    e "[playername]. You have come at an opportune time."
    e "You have the opportunity of a lifetime. The opportunity to stay here and talk to Westra while I sneak away."
    "You feel a strange aura in the air, and the princess is jolted with something."
    "She looked like she was going to leave, but now she looks rigid, as if something is holding her in place."
    e "Mmmmph...."
    w "Nice try. You should know better than to try running from me."
    w "Now, be a good girl and wait for Dane like you said you were going to."
    show westra behind tabled at truecenter:
        zoom .3
        linear .5 xpos 2.5
    show ellie behind tabled at truecenter:
        zoom .4
        ypos .7
        linear .5 xpos .5
    "The wizard stands up and walks away from the table, back to her usual spot at the bar."
    "Ellie's body becomes loose again, and she falls over in the booth."
    e "Ugh... always with the magic..."
    "She rights herself in her seat and grimaces as she rubs her neck."
    e "One of these days, I'll really show her, [playername]. She's not the only one who can use magic here..."
    menu:
        "Because I can use magic too!":
            e "No, not you. I'm talking about me."
        "Are you a magician?":
            e "What? No, magicians are the ones who do little inconsequential card tricks at an orphan's birthday party."

    e "You wouldn't know, but I'm training to be a mighty and powerful warlock."
    menu:
        "A warlock? Like summoning zombies and stuff?":
            "Ellie visibly gags when you finish your question."
    e "Don't.. please don't say the Z-word. I don't.. I don't do well with the Z-word.."
    menu:
        "Zombies?":
            "She retches towards her seat and resists the urge to dry heave."
            e "Stop right now!"
            "She throws a piece of bread at you in a frivolous attempt to stop your vocal rampage."
        "Sorry to offend you.":
            e "As long as you don't say it anymore, we will be fine."
    "She takes a deep breath."
    e "Anyways... let's... talk about literally anything else..."
    "She clearly doesn't enjoy the word zombie. You decide it would be better if you left it alone."
    e "My royal staff at the castle has been teaching me dark magic in the event that I need to defend myself."
    e "Of course, I have Dane to protect me, most of the time."
    "She makes an irritated face while glancing off to the side."
    e "But there might come a time where I'm faced with such horror that I have to do something myself."
    e "Such is the duty of a princess! And I will have none of your sympathy!"
    "She pauses for a moment, expecting you to offer some form of sympathy."
    menu:
        ".....":
            e "Hmph. The life of a princess is a daring and difficult one, I'm afraid."
        "It must be hard having to learn how to use magic.":
            e "I have no time to grovel about how difficult my life is."
    e "Besides, as long as Dane is here, I have nothing to worry about. He's the meatiest meat shield that my father could find."
    "She beams for a moment, then retracts, looking embarrassed and somewhat regretful."
    e "Erm... don't tell Dane I told you he was meaty. That.. could be portrayed incorrectly.."
    "She coughs."
    "You hear the door open and Dane waves at you and Ellie."
    e "Finally, my ride is here."
    e "... don't take that the wrong way either!"
    show ellie behind tabled at truecenter:
        zoom .3
        linear .5 xpos -.5
    "She gets up and walks out of the establishment."
    
    jump ellie_done


label ellie_4:
    # ELLIE 4 IS AFTER SHE RETURNS. DANE 4 HAS ELLIE/WESTRA IN IT.
label ellie_done:
    python:
        gamedata["ellie_talked"] = True

    jump start_music