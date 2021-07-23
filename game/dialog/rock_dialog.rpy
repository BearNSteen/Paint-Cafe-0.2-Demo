##########################################################################################
##########################################################################################
##### ROCK ###################
label rock_dialog:
    python:
        in_party_rock = False
        for member in gamedata["party"]:
            name = member.get_name()
            if name == "Rock":
                in_party_rock = True
    stop music fadeout 2.0
    play music dane
    scene wall
    show tabled
    show rock behind tabled at truecenter:
        zoom .4
    python:
        if gamedata["c_rock"] == 0:
            gamedata["c_rock"] += 1
            renpy.jump(label='rock_1')
    "He puts his tools down and nods at you."
    menu:
        r "Can I help you, [playername]?"

        "You wanted to talk to me?" if gamedata["rock_talked"]==False and rock_go_ahead == True:
            python:
                convo = "rock_" + str(gamedata["c_rock"]+1)
                if renpy.has_label(convo) == True:
                    gamedata["c_rock"] += 1
                    renpy.jump(convo)
                else:
                    renpy.say(r, "Not really. Sorry. I'll be here if you need anything else.")
                    renpy.jump("start_music")

        "Can I ask you about something?":
            r "Sure. Ask away."
            jump rock_asks

        "Come with me. (DO NOT CLICK)" if in_party_rock == False:
            python:
                if len(gamedata["party"]) < 4:
                    renpy.say(r, "Sure, let's be sneaky about it though.")
                    gamedata["party"].append(rpg.rock_char)
                else:
                    renpy.say(r, "Sorry, looks like your party is full.")
                renpy.jump(label="selection")

        "No, just stopping by.":
            jump back_rock

label back_rock:
    r "Alright, take care. I'll be here if you need me."
    jump start_music

label rock_done:
    python:
        gamedata["rock_talked"] = True
        g.save(gamedata)
        renpy.jump(label="start_music")

##########################################################################################
##########################################################################################

label rock_asks:
    python:
        ceres_question = 0
    menu:

        "Do you know Dane?" if gamedata["c_dane"] > 0:
            r "Dane, huh...?"
            if gamedata["c_dane"] < 4:
                r "Yeah, he used to be the Captain of the Resolve Guard."
                r "You know, the guards posted all around the city?"
                r "Gods, I hate the guards in this city. They're really racist, and they all wear sunglasses."
                r "Anyway, he used to lead those guys. Now he's the bodyguard to Princess Adelaide."
                r "He's really well known in this town since he was basically the leader of the police."
                r "They don't really have police where I'm from, so it's a weird new thing to me."
                r "I don't think he's untrustworthy, but I wouldn't get too close to him..."
                r "Chances are, if his underlings are racist, he's got it worse than them."
                r "Anything else?"
                jump rock_asks
            else:
                r "I don't know anything worth telling you at this particular moment."
                jump rock_asks

        "Do you know Ellie?" if gamedata["c_ellie"] > 0:
            r "Princess Adelaide..."
            if gamedata["c_ellie"] < 3:
                r "Did you know she used to be afraid of the undead? Like, really afraid?"
                r "I don't know about now, but something apparently happened to her that scarred her forever."
                r "... What, me? How do I feel about the undead?"
                r "I'm... not exactly the best person to ask. And besides, weren't you asking about Ellie?"
                r "The rumors that I'm hearing a lot are as follows:"
                r "Ellie has an unimaginably large crush on her bodyguard, and has for many years."
                r "This is something I overheard some guards gossiping about, so it could be false, you never know."
                r "Actually.. besides the whole undead thing, that's about as far as the rumor mill spins on her."
                r "Her dad is Castor Adelaide, which I believe I've told you before."
                r "Her mom is.. ugh.. Ceres Adelaide. Who I don't believe I mentioned, and there's a reason for that."
                r "Please, please, please do not ask me about Ceres Adelaide."
                python:
                    ceres_question = 1
                r "That's all I know for now. If something else comes up I'll let you know."
                r "Anything else?"
                jump rock_asks
            else:
                r "No, nothing comes to mind."
                jump rock_asks

        "Do you know Westra?" if gamedata["c_westra"] > 3:
            r "That court mage..."
            if gamedata["c_westra"] < 5:
                r "She's an elusive one, for sure."
                r "The only times I've heard her name come up are guards sobbing about how scary she was."
                r "Something tells me that she isn't really scary, though. I think she might just be stern."
                r "She really reminds me of someone I used to travel with... she seems to put her face in her palm very frequently."
                r "Maybe she's just that disappointed in everyone around her. I mean, she has to put up with the Adelaide family all the time..."
                r "I'll let you know if I hear anything else."
                r "Any other questions?"
                jump rock_asks

        "Do you know Ember?" if gamedata["c_ember"] > 0:
            r "The blacksmith?"
            r "No, sorry. I don't really know anything about her."
            jump rock_asks

        "Do you know... Ceres Adelaide?" if ceres_question == 1:
            r "Ugh, you have got to be kidding me."
            r "She's an irritable ruler who might as well not even be on her throne."
            r "What makes it worse, is that me speaking that phrase makes me feel hunted."
            r "It's like she has eyes everywhere.. and the eyes don't work for Santos. They work for something else..."
            r "Something dark is going on here. Usually, I'm all for dark stuff, but not this time."
            r "Count me out."
            jump rock_asks

        "Back":
            jump back_rock        



##########################################################################################
##########################################################################################

label rock_talk:
    show rock at truecenter:
        zoom .4
    python:
        if gamedata["c_rock"] == 10000:
            renpy.say(None, "A red man sitting at a table looks at you inquisitively from across the room.")
            renpy.say(q, "Hey... you look lost, pal. Why don't you come and have a seat?")
            renpy.say(None, "To talk to someone, click the talk to button, and then select your desired conversation partner.")
            renpy.say(None, "In this instance, the name will be \"???\" because you haven't met them yet. Good luck!")
        elif gamedata["c_rock"] == 1:
            renpy.say(r, "Hey, [playername]. I've got something I want to talk to you about. Mind coming over here?")
        else:
            renpy.say(r, "Hey, [playername]. I've got something I want to talk to you about. Mind coming over here?")
        rock_talk = False
        rock_go_ahead = True
    scene bg paint cafe
    jump back

##########################################################################################
##########################################################################################

label rock_1:
    "You look around the Cafe and see a mysterious looking red man busy at work on a large piece of parchment."
    "You decide to approach him."
    menu:
        "Mind if I sit here?":
            q "Sure, if you'd like."
        "What are you working on?":
            q "Why don't you have a seat and take a look?"

    "You accept the stranger's suggestion and take a seat."
    "Spread across the table is a large, mostly blank piece of paper, though some work has been done in the area closest to the man."
    q "Admiring my work?"
    "He chuckles softly to himself."
    q "There's not much to admire, unfortunately. But I'm not exactly the most talented cartographer yet."
    "You look at the paper again. Upon closer examination, it does appear that what was already drawn was, in fact, landmarks and landmasses."
    "However, it really only looks like a town and maybe some of the surrounding landmarks so far."
    menu:
        "Are you sure you're a mapmaker?":
            q "Well, don't we have the utmost confidence in our favorite neighborhood artist."
        "Where's the rest of the map?":
            q "Relax, give me some time. I just got here."
    q "Rest assured, the map is incomplete because I'm not a local. I'm more of an.. outlander."
    "He rustles around in his pack, and hands you what looks to be a smaller and more confidently made version of the large map."
    q "Here, consider this an investment in our future partnership. It's a map of the city."
    q "Santos isn't the largest of cities, but for this region, it seems to be the capital."
    menu:
        "... Santos?":
            q "What, you didn't even know what city you were in?"
        "... The capital?":
            q "What you didn't even know what kind of city you were in?"
    q "Santos is the capital of the Adelaide Empire. Ruled by Castor and Ceres Adelaide, high king and queen of the Resolve."
    q "At least, that's what information I've gleaned from the people around here. Again, I'm not a local."
    q "Oh, by the way, my name is Rock. It's good to meet you..."
    menu:
        "[playername].":
            r "[playername]. The pleasure is all mine."
    r "Listen. Neither of us seem to be from around here, so let's stay in touch."
    r "I'll be living here in the Inn from now on if I'm not traveling, so make sure you check in with me from time to time."
    r "If you need anything else, I'll be working on my map."
    r "Have a good one."
    python:
        gamedata["rock_talked"] = True
        g.save(gamedata)
        renpy.jump(label="continue")

#############################################

label rock_2:

    r "Have you tried wandering around with that map that I gave you? It's not much, but it should get you places you might want to go."
    r "Last time we talked, I told you this was the Adelaide Kingdom."
    r "This town isn't particularly friendly to non-humans, which makes it somewhat annoying for me to walk around outside."
    r "That being said, I was something of a charlatan where I'm from, and I'm used to sneaking about, even with my giant tail."
    "He sighs and scribbles something on his map."
    r "From my understanding, we're currently on a continent called \"T'Lass\". This region is called Adelaide, named after the ruler."
    r "Unfortunately, it doesn't look like there's any way to get back to where I'm from from this place."
    "He coughs. His eyes show a distinct sadness."
    r "Hey, listen.."
    r "If you run into anyone who looks like me, long tail, red skin, similar facial features.. let me know immediately."
    r "Until then, I can't really get out of this town, let alone this kingdom, and I'm stuck in this tavern."
    r "I will try to help you in any way that I can. Hopefully we can get out of this strange situation we find ourselves in."
    r "I'll be here if you need anything."
    jump rock_done


##############################################################
# CHAPTER 1 ##################################################

label rock_dialog_ch1:
    python:
        in_party_rock = False
        for member in gamedata["party"]:
            name = member.get_name()
            if name == "Rock":
                in_party_rock = True
    stop music fadeout 2.0
    play music dane
    #scene wall
    #show tabled
    show rock at truecenter:
        zoom .4
    "He puts his tools down and nods at you."
    menu:
        r "Can I help you, [playername]?"

        "You wanted to talk to me?" if gamedata["rock_talked"]==False and rock_go_ahead == True:
            python:
                convo = "rock_" + str(gamedata["c_rock"]+1)
                if renpy.has_label(convo) == True:
                    gamedata["c_rock"] += 1
                    renpy.jump(convo)
                else:
                    renpy.say(r, "Not really. Sorry. I'll be here if you need anything else.")
                    renpy.jump("cafe_menu_kazzik")

        "Can I ask you about something?":
            r "Sure. Ask away."
            jump rock_asks_ch1

        "Come with me. (DO NOT CLICK)" if in_party_rock == False:
            python:
                if len(gamedata["party"]) < 4:
                    renpy.say(r, "Sure, let's be sneaky about it though.")
                    gamedata["party"].append(rpg.rock_char)
                else:
                    renpy.say(r, "Sorry, looks like your party is full.")
                renpy.jump(label="cafe_menu_kazzik")

        "No, just stopping by.":
            jump back_rock_ch1

label back_rock_ch1:
    r "Alright, take care. I'll be here if you need me."
    jump cafe_menu_kazzik

label rock_done_ch1:
    python:
        gamedata["rock_talked"] = True
        g.save(gamedata)
        renpy.jump(label="cafe_menu_kazzik")

label rock_asks_ch1:
    python:
        ceres_question = 0
    menu:

        "Do you know Dane?" if gamedata["c_dane"] > 0:
            r "Dane, huh...?"
            if gamedata["c_dane"] < 4:
                r "Yeah, he used to be the Captain of the Resolve Guard."
                r "You know, the guards posted all around the city?"
                r "Gods, I hate the guards in this city. They're really racist, and they all wear sunglasses."
                r "Anyway, he used to lead those guys. Now he's the bodyguard to Princess Adelaide."
                r "He's really well known in this town since he was basically the leader of the police."
                r "They don't really have police where I'm from, so it's a weird new thing to me."
                r "I don't think he's untrustworthy, but I wouldn't get too close to him..."
                r "Chances are, if his underlings are racist, he's got it worse than them."
                r "Anything else?"
                jump rock_asks_ch1
            else:
                r "I don't know anything worth telling you at this particular moment."
                jump rock_asks_ch1

        "Do you know Ellie?" if gamedata["c_ellie"] > 0:
            r "Princess Adelaide..."
            if gamedata["c_ellie"] < 3:
                r "Did you know she used to be afraid of the undead? Like, really afraid?"
                r "I don't know about now, but something apparently happened to her that scarred her forever."
                r "... What, me? How do I feel about the undead?"
                r "I'm... not exactly the best person to ask. And besides, weren't you asking about Ellie?"
                r "The rumors that I'm hearing a lot are as follows:"
                r "Ellie has an unimaginably large crush on her bodyguard, and has for many years."
                r "This is something I overheard some guards gossiping about, so it could be false, you never know."
                r "Actually.. besides the whole undead thing, that's about as far as the rumor mill spins on her."
                r "Her dad is Castor Adelaide, which I believe I've told you before."
                r "Her mom is.. ugh.. Ceres Adelaide. Who I don't believe I mentioned, and there's a reason for that."
                r "Please, please, please do not ask me about Ceres Adelaide."
                python:
                    ceres_question = 1
                r "That's all I know for now. If something else comes up I'll let you know."
                r "Anything else?"
                jump rock_asks_ch1
            else:
                r "No, nothing comes to mind."
                jump rock_asks_ch1

        "Do you know Westra?" if gamedata["c_westra"] > 3:
            r "That court mage..."
            if gamedata["c_westra"] < 5:
                r "She's an elusive one, for sure."
                r "The only times I've heard her name come up are guards sobbing about how scary she was."
                r "Something tells me that she isn't really scary, though. I think she might just be stern."
                r "She really reminds me of someone I used to travel with... she seems to put her face in her palm very frequently."
                r "Maybe she's just that disappointed in everyone around her. I mean, she has to put up with the Adelaide family all the time..."
                r "I'll let you know if I hear anything else."
                r "Any other questions?"
                jump rock_asks_ch1

        "Do you know Ember?" if gamedata["c_ember"] > 0:
            r "The blacksmith?"
            r "No, sorry. I don't really know anything about her."
            jump rock_asks_ch1

        "Do you know... Ceres Adelaide?" if ceres_question == 1:
            r "Ugh, you have got to be kidding me."
            r "She's an irritable ruler who might as well not even be on her throne."
            r "What makes it worse, is that me speaking that phrase makes me feel hunted."
            r "It's like she has eyes everywhere.. and the eyes don't work for Santos. They work for something else..."
            r "Something dark is going on here. Usually, I'm all for dark stuff, but not this time."
            r "Count me out."
            jump rock_asks_ch1

        "Back":
            jump back_rock_ch1   

##########################################################################################
##########################################################################################

label rock_talk_ch1:
    show rock at truecenter:
        zoom .4
    python:
        if gamedata["c_rock"] == 1:
            renpy.say(r, "Hey, [playername]. I've got something I want to talk to you about. Mind coming over here?")
        else:
            renpy.say(r, "Hey, [playername]. I've got something I want to talk to you about. Mind coming over here?")
        rock_talk = False
        rock_go_ahead = True
    jump cafe_menu_kazzik

##########################################################################################
##########################################################################################


#############
# DIALOG ####

label rock_3:

    r ""
    jump rock_done