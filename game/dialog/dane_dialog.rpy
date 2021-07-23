##########################################################################################
##########################################################################################
##### DANE ###################
label dane_dialog:
    stop music fadeout 2.0
    play music dane
    python:
        if who_list[0] == 3:
            renpy.jump(label='dane_castle')
    scene wall
    show tabled
    show dane behind tabled at truecenter:
        zoom .3
    if gamedata["dane_talked"]:
        "He sips his drink and nods at you."
        d "Always good to see you, [playername]."
        jump back
    jump dane_forward
label dane_castle:
    scene bg hallway
    show dane at truecenter:
        zoom 0.3
    if gamedata["dane_talked"]:
        d "Oh, I'd love to chat with you right now [playername], but I'm in the middle of royal business."
        d "Perhaps next time?"
        jump select_castle
label dane_forward:
    python:
        if gamedata["dane_talked"] == False:
            gamedata["c_dane"] += 1
            convo = "dane_" + str(gamedata["c_dane"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(d, "Error: End of dialog.")
                renpy.jump("back")
        else:
            renpy.jump("selection")

##########################################################################################
##########################################################################################
##### DANE & ELLIE ###################

label dane_ellie_dialog:
    scene wall
    show tabled
    show dane behind tabled at right
    show ellie behind tabled at left
    if gamedata["dane_ellie_talked"]:
        "He sips his drink and nods at you."
        d "Always good to see you, [playername]."
        jump selection
    python:
        if gamedata["dane_ellie_talked"] == False:
            gamedata["c_dane_ellie"] += 1
            convo = "dane_ellie_" + str(gamedata["c_dane_ellie"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(d, "Dane has nothing left to say.")
                renpy.jump("selection")
        else:
            renpy.jump("selection")


##########################################################################################
##########################################################################################
## DANE DIALOG ##

label dane_1:
    python:
        print("Dane 1 playing.")
    "Sitting at a table, you see a very muscular and tall man wearing the largest grin you've ever seen."
    q "Hello there!"
    "You look around, then point to yourself with a puzzled look on your face. He nods and beckons you forward."
    q "Come and have a seat! No need to be shy or confused."
    "Against your better judgment, you decide to take a seat in front of the jubilant knight."
    q "You know, I don't think I've ever seen you before. And I've seen most people in town, believe me."
    "He squints at you." 
    menu:
        q "Have we met before?"

        "No, I don't think so.":
            q "Well, that's alright. No place to meet strangers than a tavern!"
        "I think I would remember you...":
            q "I'm not quite sure what you mean by that, but that's alright."
    q "My name is Silas Dane. Most people around here know who I am, and now you do, too!"
    d "What brings you to the fine town of Santos today? Errands? Meeting a friend?"
    menu:
        "You think to yourself for a moment."

        "I don't rightly know, myself..":
            d "You.. don't know? Did you have too much to drink?"
    d "Well, that's troubling to hear. You look fairly sober to me, and you don't know why you're here?"
    d "It's not my business to barge into the lives of strangers anymore, but I would sure like to help you if you need it."
    d "Ah, but it's getting to be that time. I was actually hoping to meet someone here, myself, but it looks to me like they aren't coming."
    d "I hope you'll come and talk to me again sometime! Take care of yourself!"
    "He stands up and walks out of the tavern."
    jump dane_done

label dane_2:
    python:
        print("Dane 2 playing.")
    d "Hello again, [playername]!"
    d "Last we spoke, did I tell you what I do for a living?"
    d "I'm actually a royal bodyguard. Well, I'm not royalty myself, but I'm the bodyguard of someone who is."
    d "Maybe I'll bring her here sometime. She's a bit picky, but.. who knows?"
    d "Her name is Princess Elena Adelaide. You should talk with her if you see her around."
    d "Well, maybe not, she.. doesn't exactly get us common folk."
    d "You should come visit us at the castle, actually. It's not too far of a walk from here, just up the main streets a bit."
    d "It's busy sometimes and the common folk might struggle to get near it depending on what's going on..."
    d "But, it would be nice to see a friendly face over there if you get a chance."
    d "Regarding your situation... have you figured anything else out about why you're here?"
    menu:
        "You think to yourself for a moment."

        "Not exactly..":
            d "Well, it can't be helped. You've only been here for a short amount of time."
    d "Perhaps coming to the castle could help you find some answers. If nothing else, it's sure to provide a lovely walk this time of year."
    d "Anywho, I have to be going again. Have a good one, [playername]."
    jump dane_done

label dane_3:
    python:
        print("Dane 3 playing.")
        gamedata["d_lies"] = 0
    show dane at truecenter:
        zoom 0.3
    d "Oh, [playername]! I didn't expect you to take me up on my offer to see the castle."
    menu:
        d "It's good to see you. Have you visited the castle before?"

        "Nope!":
            d "Well, that's alright. There's a first time for everything!"
        "Well, actually, in my spare time, I'm a city guard myself.":
            d "It's not a great idea to lie to someone all the time, you know."
            python:
                gamedata["d_lies"] += 1

    d "I don't think I've told you yet, but I was actually Captain of the Guard here before I started my current job."
    d "It's the reason that King Castor already knew who I was, and found me to guard his daughter."
    python:
        if gamedata["d_lies"] == 0:
            renpy.jump(label='d3_cont')
    d "Which is, of course, the reason I know you're a dirty liar."
    d "I know every person in the royal guard in this city. Every single one."
label d3_cont:
    d "Anywho, the weather is nice today. Maybe you should consider visiting more often!"
    d "Have a good one, [playername]!"
    jump dane_done

label dane_4:
    show dane at truecenter:
        zoom 0.3
    python:
        print("Dane 4 playing.")
    d "[playername]! Welcome back, it's good to see you again."
    d "The castle gardens always look so lovely this time of year."
    d "I'd love to take a walk over there sometime, but I've actually got work to do."
    menu:
        d "By the way, I was thinking... do you have a place here in town?"

        "Well, not yet..":
            d "Well, you should consider getting a place if you're sticking around."
            d "I'm sure that room at the inn is fine and all, but you have to start thinking about your future."
        "I'm not from here.":
            d "Where are you from, then? Tor'Qua? Dunmerk?"
            "He squints a little."
            d "... Greenhold?"
            "He holds his squint for a moment then chuckles and returns to normal eyesight."
            d "Ha, who am I kidding. If you were from Greenhold, you wouldn't be alive!"
            d "But seriously, you should consider your future if you're going to stick around."
    d "You'd better take care of yourself. Maybe you could consider taking a up a job with the guard?"
    d "The royal guard could use someone like you. You know, um, someone who.."
    "He stammers awkwardly for a moment."
    d "Come to think of it, I don't really know that much about you. But hey, I'm sure you'll fit right in.."
    d "Anywho, I have to run some royal errands. Ellie needs a new shower curtain for a reason that has not been disclosed to me."
    d "See you later, [playername]!"
    jump dane_done

label dane_5:
    python:
        print("Dane 5 playing.")
    show ellie at left:
        zoom .35
        ypos 1.2
        xalign 0.15
    show westra at right:
        zoom 0.27
        ypos 1.05
        xalign .9 
    show dane at truecenter:
        xalign 0.5
        zoom 0.3
    d "[playername]! Hello, it's good to see you again."
    d "Hopefully by now you've met Ellie and Westra. Ellie is the princess I told you about. And Westra is..."
    "He twiddles his thumbs for a moment."
    d "..The castle gardens always look so lovely this time of year."
    w "Dane... as the court mage, it is my professional suggestion that you should finish that thought. Before I blast you into next week."
    d "Ah, uh.. Westra is.. a very talented mage! Yes, the court wizard. Ha. Of course."
    show dane at truecenter:
        linear 1 xalign 0.3
        zoom 0.3
    "He looks a bit nervous for some reason, and sidles slightly away from Westra."
    d "Anyway, turns out we've been selected by the King himself to go on some kind of journey."
    d "Something about looking around and helping to protect the realm. From cultists, most likely. The rascals!"
    "He chuckles and slaps his knee playfully."
    w "Dane, you need to take your job more seriously. This could be dangerous."
    e "Yes, Dane. Your tomfoolery needs to be curbed immediately. Daddy said so."
    d "He did not. He just told us we were going to Tele to talk to everyone's favorite cowboy."
    w "He is not going to like that you said that."
    "Westra scribbles something down on a notepad."
    d "Are you going to blackmail me with that later?"
    w "Depending on what happens, you may not see Dane for a while."
    e "Oh, no. There's no depending here. You really won't see Dane for a while. You won't be seeing much of us, either."
    d "Yes, regardless of my legal status we will certainly be out for a while. Probably about a week."
    d "We can regale you with our tales of valor when we return! Be prepared for epic tales!"
    show westra at right:
        zoom 0.27
        ypos 1.05
        linear .5 xalign .5 
    "Westra walks calmly over to Dane and slams her elbow into his gut."
    show dane at truecenter:
        linear .3 xalign 0.27
        zoom 0.3   
    d "Ow! What was that for?"
    w "We will see you shortly, [playername]. Try to read some books while we're gone."
    scene bg hallway with dissolve
    "The three of them walk away from you. Not too long after, you see a crowd of people disburse and you can hear Ellie shouting 'ROYALTY!' at the top of her lungs."
    python:
        gamedata["progress"] = "main_1"
    jump dane_done

label dane_done:
    python:
        gamedata["dane_talked"] = True
        g.save(gamedata)
        if who_list[0] == 3:
            renpy.jump(label="select_castle")
        elif who_list[0] == 1:
            renpy.jump(label="start_music")

##########################################################################################
##########################################################################################
## DANE + ELLIE DIALOG ##
label dane_ellie_1:
    python:
        print("Dane+Ellie 1 playing.")
    d "Hello there!"
    e "Yes.. hello, [playername]."
    d "We were just about to order our drinks. Care to join us?"
    e "Do we have to order peasant drinks? I'm not so sure about this.. bean juice."
    d "But you like tea, which is leaf juice."
    e "It's different! Tea is tea. Coffee is a dark abyss of bean juice."
    "Ellie grumbles at Dane, but realizes that she's staring at him and starts to blush and turn away."
    e "But, but, if you.. like it.. then it's okay, I guess.."
    d "Backing down so quickly? Does this mean you've succumbed to my bean juice powers?"
    "She crosses her arms."
    e "I've succumbed to your ability to waste our guest's time! How could you do this to your princess??"
    menu:
        d "Ah, you're right. Would you like to order something?"

        "Just some good old fashioned bean juice.":
            d "Yeah, that's the spirit. Cuppa, some coffee for our friend here!"
            n "Sure, sure."
            "You receive a piping hot cup of joe."
            python:
                gamedata["inventory"].append("Coffee")
        "Is the tea here any good?":
            e "I mean, I wouldn't call it excellent, but..."
            n "Here you are."
            "You are handed a cup of tea. It's unclear which tea it is."
            python:
                gamedata["inventory"].append("Tea")
        "Water is fine.":
            e "You're boring. You should order something else."
            n "Water for the.. boring one. Ha ha."
            "Cuppa hands you a cuppa water."
            python:
                gamedata["inventory"].append("Water")

    d "Well, we'll be here enjoying our drinks if you need anything."
    e "Dane, how much longer do we have to stay here?"
    d "We don't have to stay here too much longer, but I would like to enjoy my coffee.."
    "You leave them to their bickering."
    jump dane_ellie_done

label dane_ellie_2:
    python:
        print("Dane+Ellie 2 playing.")
    d "Hello again, [playername]!"
    e "Back again? You can actually stand being around Dane?"
    d "Now, now. This is what it's like having friends, Ellie."
    e "I wouldn't know. I was locked up in that castle for so long with hardly anyone competent to talk to."
    e "Not that my current company is much of an improvement."
    "She glares at Dane, but there's something in her eyes that doesn't indicate anger."
    d "What's that supposed to mean? You know I was captain of the guard.."
    e "Yes, yes, this again. We all know you were a Guard Captain. It's really not that prestigious or anything."
    d "Well, I certainly think it is. What do you think, [playername]?"
    menu:
        d "Well, I certainly think it is. What do you think, [playername]?"

        "Captain of the Guard? Pretty impressive.":
            d "Exactly. I worked for a long time to get to where I am."
            "Dane smiles to himself."
        "Eh, I've seen better...":
            e "Yes, that's what I'm saying. It's nothing impressive."
            "Her tone of voice seems to indicate that she feels otherwise, but you decide not to pursue it."
    d "Well, in any event, I would like a cup of coffee before going back out into the field."
    e "Yes, today we're looking for some cultists. They're supposed to be holed up in a cave outside of town, actually."
    d "You'd better stay safe, [playername]. You never know what's going on outside these walls."
    "He smiles at you as you walk back to your table."

    jump dane_ellie_done

label dane_ellie_done:
    python:
        gamedata["dane_ellie_talked"] = True

    jump selection