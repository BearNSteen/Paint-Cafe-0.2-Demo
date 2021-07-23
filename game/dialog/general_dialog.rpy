#####################################################
#
# Player goes on caravan to Meraxia
# They arrive in Kazzik
# Player cannot pay for their room so they go monster hunting
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#####################################################
#####################################################
### INTRO ###
label new:

    menu:
        "Play Intro":
            jump _intro
        "Skip Intro":
            jump _skip_intro

label _intro:
    "Your head hurts."
    "You feel almost like you were pulled through a very tight and small tube."
    "Could it have been just a bad dream?"
    scene bedroom with dissolve
    "You awaken to find yourself in some kind of bedroom. The room smells of pine and the air feels tingly."
    "You don't recognize your surroundings, though this isn't your first time in a tavern bedroom."
    "Shaking off your tiredness, you gather yourself and head downstairs."
    scene bg paint cafe with dissolve
    "You are surrounded by the smell of various foods, alcohols, and some unidentifiable stench. You think to plug your nose, but you adjust quickly."
    "Though this tavern seemed to be bustling when you were heading downstairs, you find that there is only one patron, and a nosy looking bartender."
    show cuppa at truecenter with dissolve
    "He smiles at you, though you can see confusion in his eyes."
    q "Hello there, traveler. I.. don't believe we've met before."
    q "Did you come from upstairs? I didn't see you come in..."
    menu:
        "Where am I?":
            q "You're in my tavern, and as such, I should really know who you are already."
        "I... had a room, so I must've been here before...":
            q "You had a room? What are you, some kind of squatter?"
    "He pauses and takes a good look at you."
    q "Come to think of it, those clothes aren't really from around here. It's been a while since I've had a patron wearing something like that."
    q "What's your name?"

    # character name is set here
    define pov = Character("[povname]")

    python:
        povname = renpy.input("What is your name?")
        playername = povname.strip()
        if not playername:
             playername = "Dan"
        gamedata["playername"] = playername

    q "Well... all I can really say is welcome, [playername]."
    n "My name is Cuppa. Thanks for choosing my establishment."
    n "Um... I won't ask you about the whole borrowing a room thing. You seem confused enough as it is, so go ahead and keep using it until you figure out what's going on."
    n "Oh, by the way. It looks like that man over there is eager to talk with you."
    "He points across the room. Someone is trying to flag you down."
    n "I'll be here if you want a drink."
    hide cuppa
    "You decide to wander over to the waving patron."
    stop music fadeout 2.0
    play music dane
    scene wall
    show tabled
    show rock behind tabled at truecenter:
        zoom .4
    menu:
        "Why were you waving me down?":
            q "Can't I just talk to a stranger? Have a seat."

    "You accept his suggestion and take a seat."
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

    python:
        player_char = rpg.Character(playername, 1, rpg.dane_tree)
        gamedata["party"].append(player_char)
        gamedata['characters'] = [
        g.Char("Rock", 11),
        ]
        gamedata["c_rock"] += 1

    jump continue

label _skip_intro:
    python:
        povname = renpy.input("What is your name?")
        playername = povname.strip()
        if not playername:
             playername = "Dan"
        gamedata["playername"] = playername
        player_char = rpg.Character(playername, 1, rpg.dane_tree)
        gamedata["party"].append(player_char)
        gamedata['characters'] = [
        g.Char("Rock", 11),
        ]
        gamedata["rock_talked"] = True
        g.save(gamedata)
        gamedata["c_rock"] += 1

    jump continue

##########################################################################################
##########################################################################################
##### CUPPA ###################
label hint_dialog:
    #play music [name]
    show cuppa at truecenter
    python:
        convo = "cuppa_" + str(gamedata["cuppa"])
        if renpy.has_label(convo) == True:
            renpy.jump(convo)
        else:
            renpy.say(n, "Error: End of dialog.")
            renpy.jump("selection")

##########################################################################################
##########################################################################################
## CUPPA HELP DIALOG ##
label cuppa_help1:
    n "Hey there. You look a little lost in thought."
    n "Let me see if I can help you out.."
    python:
        if gamedata["c_dane"] == 4 and gamedata["c_ellie"] == 4 and gamedata["c_westra"] == 3:
            renpy.say(n, "You know, I think you're doing okay. Go look at the castle, Dane was looking for you.")
        elif gamedata["c_dane"] == 4:
            if gamedata["c_ellie"] < 4:
                renpy.say(n, "Have you seen the princess around?")
                renpy.say(n, "She looked like she wanted someone to talk to.. as hard as that is to imagine.")
            if gamedata["c_westra"] < 3:
                renpy.say(n, "Have you seen the court mage around?")
                renpy.say(n, "She's always lost in a book, but something tells me she wants to talk... call it my intuition.")
        elif gamedata["c_ellie"] == 4:
            if gamedata["c_dane"] < 4:
                renpy.say(n, "Have you seen that guard around?")
                renpy.say(n, "He's good company. I think he was in the army, has lots of friends. Maybe you could be one of them?")
            if gamedata["c_westra"] < 3:
                renpy.say(n, "Have you seen the court mage around?")
                renpy.say(n, "She's always lost in a book, but something tells me she wants to talk... call it my intuition.")
        elif gamedata["c_westra"] == 3:
            if gamedata["c_dane"] < 4:
                renpy.say(n, "Have you seen that guard around?")
                renpy.say(n, "He's good company. I think he was in the army, has lots of friends. Maybe you could be one of them?")
            if gamedata["c_ellie"] < 4:
                renpy.say(n, "Have you seen the princess around?")
                renpy.say(n, "She looked like she wanted someone to talk to.. as hard as that is to imagine.")
    n "Hope that helps you. Have a good one."
    scene bg paint cafe
    jump back

###############################################################
############ MAIN STORY ACT 1 #################################

label main_1:
    show bg paint cafe with dissolve
    python:
        if demo == 1:
            renpy.jump("demo_end")
    "{i}Warning: This segment will take some time to complete. If you don't have time to read it all, quit now and read it later. If you don't, you may find yourself with a bad ending you didn't want; the bad ending will have a way to return to this conversation, however.{/i}"
    "Cuppa becons you over with a look of concern on his porcelain face. Rock sits opposite him at the counter, paused in thought."
    show cuppa at truecenter:
        xpos .7
    show rock at truecenter:
        zoom .4
        linear .5 xpos .3
    n "[playername]. We seem to have run into a bit of a problem."
    n "You see, your being here in one of my rooms unpaid and unaccounted for is actually a legal offense in this city."
    n "I would love to continue helping you, but unfortunately, the government here finds it to be akin to squatting in a government building."
    "He looks around cautiously as he talks about the Royal Guard."
    n "Frankly, it would've been nice to have Dane talk to the proper authority about this, but he happens to be away on some kind of holy quest or something."
    n "That being said, I really don't have a lot of options as to what to do with you two right now."
    "Rock sighs."
    r "Unfortunately, I have found myself in a predicament similar to yours, as you are well aware."
    n "Though that is the case, I do have a proposal for you."
    n "There is a caravan leaving here tonight with refugees and some good companions of mine."
    n "You are free to have a seat on the caravan, as it's certainly nowhere near capacity. It will take you to the next country down the way from here."
    "Rock shudders in your peripheral vision."
    r "I haven't heard very good things about Meraxia. Lots of deserts, lots of banditry... but, then again, I heard all of that from the guard in this city."
    r "The guards in this city also happen to be very racist and xenophobic. I don't think their word is worth trusting."
    n "So? How about it?"
label main1_options:
    menu:

        "Do I really have to?":
            n "Consider it this way. If you don't, the guards will come here in the morning and throw you in jail."
            n "In said jail, you will probably rot, be tortured, and have unspeakable wrongs committed against you."
            n "Do you really want that?"
            jump main1_options
        "But I'm a human!":
            n "Human or not, you aren't from here, clearly, and you're illegally living on my property."
            n "Again, I'd not have thrown you out, but the guards are going to be here tomorrow morning to collect you otherwise."
            jump main1_options
        "Fine, I understand.":
            n "Good. I think you're making the right choice."
            r "And remember, I'll be with you the whole way. I've still got business to take care of, and you're going to help me."
            jump main1_confirmed
        "I'm staying here. I don't care what the guard says.":
            n "That's... not wise. Are you sure you want to do that?"
    menu:
        "Yes. I'm absolutely sure.":
            "Cuppa sighs."
            n "You're your own worst enemy here, I'm telling you now. Suit yourself."
            "Rock shakes his head."
            r "I don't envy the life you're about to experience. You're going to wish you were out of it as soon as you're put in."
            r "You're sure I can't persuade you out of this?"
        "No, you're right. I'll go to Meraxia.":
            n "Good. I was scared for you, for a moment."
            r "I think you made the right choice. Besides, I still need you, remember? You can't help me out if you're in a cell. Or worse."
            jump main1_confirmed
    menu:
        "{i}Warning: This will lead to a bad ending if you decide to go to prison. You will be able to return to this point once the bad ending is over.{/i}"

        "You can't tell me what to do. I have a right to squat and I'm exercising it. [BAD ENDING]":
            r "Fine. Fine! Do what you want. I didn't need your help, anyway. I'll find someone else to help me."
            "You sit proudly as Rock leaves the tavern. Cuppa sighs and walks away."
            scene bedroom
            "You head upstairs to YOUR room and go to sleep."
            window hide
            show bedroom with sleepfade
            python:
                gamedata["progress"] = "bad_ending_1"
                gamedata["date"] += "69 lmao"
                g.save(gamedata)
            show bg paint cafe with dissolve
            jump begin
        "You know what, Rock? You're right. I'm making a huge mistake. [SUBVERT FATE]":
            r "Thank goodness. We'll be better off down south, believe me."
            jump main1_confirmed

label main1_confirmed:
    n "I'm sorry that I can't do more for you. Here, at least take this for the road."
    "Cuppa hands you some gold."
    n "Use it to pay for the inn where you're going. So you can have an actual room, you know."
    r "We'll be leaving tonight. I'll be waiting for you outside."
    n "Good luck, [playername]. It's a big world out there. I'm sure you'll figure out what you're doing here eventually."
    "Cuppa waves you off and leaves you standing at the counter to deal with another customer. Rock stands up and walks outside."
    python:
        # you still have the potential of getting the bad ending, if you decide not to move within a day
        gamedata["progress"] = "bad_ending_1"

label main1_menu:
    scene bg cafe
    menu:
        "What would you like to do? You are currently at the Cafe. Rock is waiting for you outside."

        "Travel to Meraxia.":
            jump main1_part2

        "Move.":
            "It would be best if you didn't go anywhere. The guards are already looking for you."
            jump main1_menu

        "Go to Sleep":
            "Are you sure you want to go to sleep? The guards will be looking for you in the morning..."
            menu:
                "Yes. [BAD ENDING]":
                    scene bedroom
                    "You head upstairs to your room and go to sleep."
                    window hide
                    show bedroom with sleepfade
                    python:
                        gamedata["date"] += "69 lmao"
                        g.save(gamedata)
                    show bg paint cafe with dissolve
                    jump begin
                "No. [SUBVERT FATE]":
                    jump main1_menu


        "Save & Quit":
            "Despite now not being the best time for a break, you decide to take one. Make sure you're back before tomorrow..."
            python:
                g.save(gamedata)
                renpy.quit()

label main1_part2:
    scene bg outside
    "You head outside. Rock is waiting next to a caravan."
    show rock at truecenter:
        zoom .4
    r "I'm glad to see you here. The road ahead might be a bumpy one, but it's good to have a familiar face along for the ride."
    "He shudders and makes an uncomfortable noise."
    r "I hate to think what might've happened if we waited even a moment longer here."
    "You follow him to the back of the caravan. A number of unfamiliar faces line the vehicle, but there's plenty of space for two more."
    r "Well? After you."
    scene caravan_dark with dissolve
    show rock at truecenter:
        zoom .4
    "Rock helps you up into the back. You trudge through a small crowd of travelers until you find a somewhat comfortable wooden seat to make your own."
    r "It might be a long ride, but at least it's a long ride with company."
    "Rock gives you a reassuring look, though he doesn't smile. He then turns to the side and strikes up a conversation with one of the various nomads."
    "Before long, an older fellow gets up on the front seat and grabs the reins."
    "With a few whips and a cacophonous barrage of questionable horse sounds, the caravan starts off."
    "Unfortunately, this is also the same time you realize that there is something wrong with one of the wheels. This ride will be bumpier than you may have originally suspected."
    jump main1_no_new_bg

label main1_caravan:
    scene caravan_dark with dissolve
label main1_no_new_bg:
    python:
        # no more bad ending hooray
        gamedata["progress"] = "main1_caravan"
    "You are riding in a caravan. You can choose to wait until tomorrow manually, or you can skip the ride."
    menu:
        "Time to enjoy some bumpy shuteye...":
            python:
                g.save(gamedata)
                renpy.quit()
        "Are we there yet? [Skip the ride.]":
            "You decide to sleep through the remainder of the caravan ride."
            scene caravan_light with sleepfade

label main1_part3:
    show rock at truecenter:
        zoom .4
    "Rock shakes you awake softly. You awaken to find the caravan stopped with most of the occupants already departed."
    r "We're here. Get up."
    "Rock stands up, though he has to crouch as the ceiling of the passenger area is low for him."
    "He starts walking out and you find it is in your best interest to follow him."
    scene kazzik with dissolve
    show rock at truecenter:
        zoom .4
    "You exit the vehicle and find yourself in a completely different land. You can see sand for miles off in several directions, but you do see a port and some water as well."
    r "Kazzik. A rare coastal town in a very large desert. Thankfully, the Adelaides' influence doesn't reach this far, but we still have to be careful."
    r "Let's find a tavern so we can establish a home base."
    "You walk with Rock through the bustling city. There are people of all shapes and sizes admiring goods from various stalls lining the street."
    "The wardrobes of each individual varies greatly, with some wearing lighter robes and others in full platemail, despite the burn from the desert sun."
    "A slight wind picks up and pushes some sand in your face. You try your best to swat it away."
    r "Not used to deserts, huh? Frankly, I'm not either... I'm from a mountainous region, myself, always surrounded by snow."
    r "From the looks of it, this seems like a very merchant-focused city. Quite a lot larger than Santos was, surprisingly considering that was the capital of the Resolve Territory."
    "Rock glances around. He notices something and beckons you to follow him, leading you to what looks like a somewhat upper class tavern."
    r "I know we should probably be saving our money and finding something dinkier, but I have an idea as to how we can finance our way into the upper class."
    "He opens the door and lets himself in, with you following closely behind."
    scene kazzik_cafe with dissolve
    show rock at truecenter:
        zoom .4
    "In a strong contrast to your previous lodgings, this tavern seems a great deal better kept than Cuppa's Cafe was."
    "There are also a larger amount of patrons here, and in larger groups. You spot a group of dwarves loudly banging their steins on a table. Next to them, a group of misplaced elves quietly reading what appear to be spellbooks."
    r "Looks like we're stepping up quite a bit. Hopefully the price tag isn't going to run us back out of town."
    "Rock approaches a woman who resembles a bartender you're fairly familiar with."
    show kazza at truecenter:
        xpos .7
    show rock at truecenter:
        zoom .4
        linear .5 xpos .3
    r "Hello, there. We would like to procure two rooms from you, if you don't mind."
    "The bartender looks back at him cheerily as she grabs two room keys off the back wall."
    k "Sure thing! Our rate is 5 silver a night, and we require you to pay for a week in advance."
    r "A week in advance? I mean.. we can do that, but do you mind me asking why you require such a thing?"
    k "It's really just because our rooms are in high demand. There are always people who will stay at least a week, and that ensures that we make the profits we're looking for here at the Golden Saloon."
    r "Golden Saloon, huh...? Come to think of it, I should've really read the sign before we came in here."
    "Rock pulls out 3 gold pieces and 5 silver pieces to pay the rent. He then turns to you."
    r "How about it? How much did the old man end up giving you?"
    "You pull out the money that Cuppa handed you. Turns out he actually gave you 20 gold."
    r "Wow, I'm surprised he was willing to give you so much. That should do you for a while... though I think we can get more."
    "You put 4 gold on the table. The bartender takes Rock's 5 silver and hands it to you, then takes the collective 7 gold. She puts the rooms keys on the table."
    k "Alrighty! You let me know if you need anything else. My name is Kazza. I'll always be down here if you need anything!"
    r "Thanks, Kazza. We will let you know."
    hide kazza
    show rock at truecenter:
        zoom .4
        linear .5 xpos .5
    "He swipes the room key and hands you yours."
    r "I'm going to go up to my room and drop off all of my cartography tools. You should go check out your room too, while you're at it."
    "He walks up the stairs and out of sight. You decide it's probably best to follow him and find your room."
    scene kazzik_bedroom with dissolve
    "You walk into your bedroom. It's much fancier than your previous place, and you aren't squatting in it to boot."
    "You would spend some time putting your stuff down, but you realize that you don't actually have any possessions, so there's nothing to unload."
    "Through the wall, you can hear Rock muttering to himself as he puts down his stuff."
    "{i}You will now have to move to your bedroom to save your progress, though the game will autosave at certain points.{/i}"
    python:
        gamedata["progress"] = "chapter_1"
    jump bedroom_menu_kazzik

label bad_ending_1:

label demo_end:
    "Thank you for playing the demo for Paint Cafe."
    "Development is ongoing, so check back for a new demo at some point in the future."
    "The game will now be reset. Thanks for stopping by!"
    python:
        g.delete_save()
        renpy.quit(relaunch=True, status=0)