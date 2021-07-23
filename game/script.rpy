## TODO: Location sync
## TODO: If day advances, but character not spoken to, don't advance story (might already work)
## TODO: Location changing doesn't add characters to talk list.


label begin:
init python:
        import game as g
        import rpg
        # if something goes wrong, delete save at the start
        #g.delete_save()
        renpy.music.register_channel("ambience", mixer="sound", loop=True)
        debug = 0
        demo = 1
        gamedata = g.initialize()
        class Quit(Action):

            def __init__(self, confirm=True, msg=layout.QUIT):
                self.confirm = confirm
                self.msg = msg

            def __call__(self):
                if self.confirm:
                    renpy.loadsave.force_autosave()
                    layout.yesno_screen(self.msg, Quit(False))
                else:
                    # can autosave on quit: currently disabled
                    #g.on_quit(gamedata)
                    renpy.quit()
        config.rollback_enabled = False


define q = Character("???")
define d = Character("Dane")
define n = Character("Cuppa")
define k = Character("Kazza")
define e = Character("Ellie")
define w = Character("Westra")
define emb = Character("Ember")
define l = Character("Lana")
define r = Character("Rock")
define el = Character("Elam")
define h = Character("Hargen")
define b = Character("Boyd")
define gr = Character("Grapefart")
define we = Character("Weiss")
define m = Character("Mort")

define sleepfade = Fade(1.0, 2.0, 1.0, color="#000")

label main_menu:    # No main menu
    return          # get outta there, stop that
label start:

    python:
        _game_menu_screen = "preferences"
        flag = None                                     # Set placemarker flag to none
        #gamedata = g.initialize()                       # Put data[""] into gamedata object
        add_day = g.find_day(gamedata)                  # Determine if it is the same day as it was when last opened
        battle_info = g.init_battle()
        rock_talk = g.rock_talk(gamedata)
        try:
            if gamedata["playername"]:                  # If a name is already set
                playername = gamedata["playername"]     # then someone completed the tutorial
                flag = "continue"                       # and we should skip the tutorial and get to the selection menu.
        except KeyError:                    # (If there's no name)
            print("Name not found.")        # (Then they didn't do the tutorial yet)
    if flag == "continue":                              # If there is a name and a tutorial completed
        jump continue                                   # Continue the game
    else:
        jump new

label continue:

    python:
        #gamedata["chapter"] = 1
        #gamedata["c_lana"] = 0
        gamedata["c_mort"] = 0
        print("Days elapsed: " + str(gamedata["days"]))
        if add_day:
            # for debug
            #gamedata["progress"] = "main_1"
            print("It's a new day.")
            gamedata["dane_talked"] = False
            gamedata["ellie_talked"] = False
            gamedata["westra_talked"] = False
            gamedata["ember_talked"] = False
            if gamedata["days"] != 1:
                gamedata["rock_talked"] = False
            gamedata["elam_talked"] = False
            gamedata["hargen_talked"] = False
            gamedata["boyd_talked"] = False
            gamedata["cuppa_talked"] = False
            gamedata["grapefart_talked"] = False
            gamedata["weiss_talked"] = False
            gamedata["mort_talked"] = False
            gamedata["dane_ellie_talked"] = False
            patron_list = g.who_here(gamedata)
            who_list = g.check_who(patron_list)

            # determine where to place the player depending on gamedata progress
            part = gamedata["progress"]
            print(part)
            if part == "main_1":
                renpy.jump(label=part)
            if part == "bad_ending_1":
                renpy.jump(label=part)
            if part == "main1_caravan":
                renpy.jump(label="main1_part3")
            if part == "chapter_1":
                renpy.jump(label="bedroom_menu_kazzik")
        else:
            print("It's the same day.")
            patron_list = gamedata["in_cafe"]
            who_list = g.check_who(patron_list)
            dane_talked = gamedata["dane_talked"]

            # determine where to place the player depending on gamedata progress
            part = gamedata["progress"]
            print(part)
            if part == "bad_ending_1":
                renpy.jump(label="main1_menu")
            if part == "main1_caravan":
                renpy.jump(label="main1_caravan")
            if part == "chapter_1":
                renpy.jump(label="bedroom_menu_kazzik")

######################################################
################## PROLOGUE MENUS ####################

label start_music:
    stop music fadeout 2.0
    play music thecafe

label selection:
# selection is also the default for when player is in Cafe

    python:
        date = gamedata["date"]
        gamedata["location"] = "Cafe"
        g.save(gamedata)

    show bg paint cafe with dissolve
    play ambience rain
    jump back

label select_blacksmith:
    
    scene bg blacksmith
    jump back

label select_castle:
    
    scene bg castle
    play ambience outside

label back:

    python:
        renpy.restart_interaction
    #show screen rpg_overlay
    python:
        location = gamedata["location"]
        g.where_who(who_list, gamedata)
        if rock_talk == True and gamedata["rock_talked"] == False:
            renpy.jump("rock_talk")
        else:
            rock_go_ahead = False

    menu:
        "What would you like to do? You are currently at the [location]."

        "Talk to someone.":
            python:
                if gamedata["location"] == "Cafe":
                    renpy.jump(label='talk_to_cafe')
                if gamedata["location"] == "Blacksmith":
                    renpy.jump(label='talk_to_smith')
                if gamedata["location"] == "Castle":
                    renpy.jump(label='talk_to_castle')

        "Move.":
            call screen move_menu

        "Test" if debug == 1:
            jump debug

        "Go to Sleep":
            scene bedroom
            "You head upstairs to your room and go to sleep."
            window hide
            show bedroom with sleepfade
            python:
                gamedata["date"] += "69 lmao"
                g.save(gamedata)
            show bg paint cafe with dissolve
            python:
                renpy.jump(label="begin")

        "Save & Quit":
            python:
                g.save(gamedata)
                renpy.quit()
        
label debug:
    menu:
        "Debug options."

        "Fill Party":
            python:
                if len(gamedata["party"]) < 4:
                    renpy.say(r, "Dane joins your party.")
                    gamedata["party"].append(rpg.dane_char)
                else:
                    renpy.jump(label='debug')
                if len(gamedata["party"]) < 4:
                    renpy.say(r, "Ellie joins your party.")
                    gamedata["party"].append(rpg.ellie_char)
                else:
                    renpy.jump(label='debug')
                if len(gamedata["party"]) < 4:
                    renpy.say(r, "Westra joins your party.")
                    gamedata["party"].append(rpg.westra_char)
                else:
                    renpy.jump(label='debug')
                renpy.jump(label="selection")

        "Reset Party":
            python:
                player_char = rpg.Character(playername, 1, rpg.dane_tree)
                gamedata["party"] = []
                gamedata["party"].append(player_char)
            jump debug

        "Delete Save":
            menu:
                "Are you sure you want to delete your save data?"

                "Yes.":
                    n "Thanks for stopping by."
                    python:
                        g.delete_save()
                        renpy.quit(relaunch=True, status=0)

                "No.":
                    jump debug

        "View Inventory":
            jump inventory

        "Console Output Gamedata":
            "Current Days Elapsed: [gamedata[days]]"
            python:
                print("You are playing as " + gamedata["playername"])
                print("Dane:" + str(gamedata["c_dane"]))
                print("Ellie:" + str(gamedata["c_ellie"]))
                print("Westra:" + str(gamedata["c_westra"]))
                print("Ember:" + str(gamedata["c_ember"]))
                print("Rock:" + str(gamedata["c_rock"]))
                print(who_list)
            jump debug

        "Back":
            python:
                if gamedata["chapter"] == 0:
                    renpy.jump("back")
                if gamedata["chapter"] == 1:
                    renpy.jump("bedroom_menu_kazzik")

label inventory:
    menu:
        "In your current inventory, you have:"

        "Coffee" if "Coffee" in gamedata["inventory"]:
            "A steaming cup of coffee. From the first conversation with Dane and Ellie."
            jump inventory
        "Tea" if "Tea" in gamedata["inventory"]:
            "A steaming cup of tea. From the first conversation with Dane and Ellie."
            jump inventory
        "Water" if "Water" in gamedata["inventory"]:
            "A standard cup of water. From the first conversation with Dane and Ellie."
            jump inventory
        "Back":
            jump back

label move_menu:
    menu:
        "Where would you like to move to?"

        "Outside." if gamedata["days"] >= 3 and gamedata["location"]=="Cafe":
            jump outside_menu

        "Blacksmith." if gamedata["c_ember"] >= 2 and gamedata["location"]!="Blacksmith":
            scene bg blacksmith
            python:
                gamedata["location"]="Blacksmith"
                renpy.jump("back")

        "Castle." if gamedata["c_dane"] >= 2 and gamedata["location"]!="Castle":
            scene bg castle
            play ambience outside
            python:
                gamedata["location"]="Castle"
                renpy.jump("back")

        "Café." if gamedata["location"] != "Cafe":
            jump selection

        "Back":
            jump back

    label outside_menu:
    scene bg outside
    "It is cold and rainy outside. The streets are empty and nobody is seen wandering around."
    jump selection

label castle_button:
    scene bg castle
    stop music fadeout 2.0
    stop ambience fadeout 2.0
    play ambience outside
    python:
        gamedata["location"]="Castle"
        renpy.jump("back")

label cafe_button:
    stop music fadeout 2.0
    python:
        gamedata["location"]="Cafe"
        renpy.jump("start_music")


label smith_button:
    scene bg blacksmith
    stop music fadeout 2.0
    stop ambience fadeout 2.0
    python:
        gamedata["location"]="Blacksmith"
        renpy.jump("back")

label cave_button:
    scene bg cave
    stop ambience fadeout 2.0
    stop music fadeout 2.0
    play ambience drips
    python:
        gamedata["location"]="Cave"
        renpy.jump("cave_menu")

label cave_menu:
    python:
        goblin = rpg.Character("Heat Goblin", 2, rpg.heat_goblin)
        w_goblin = rpg.Character("Water Goblin", 2, rpg.wet_goblin)
        g_goblin = rpg.Character("Grass Goblin", 2, rpg.grass_goblin)
        b_goblin = rpg.Character("Boss Goblin", 2, rpg.big_goblin)
        cave = [(2, 1), (2, 1), (3, 2), (4, 3), (5, 4), (1, 1)]
        e_list = [goblin, w_goblin, g_goblin]
        b_list = [b_goblin]
        for x in range(0, len(battle_info["party_hp"])):
            battle_info["party_hp"][x] = gamedata["party"][x].get_hp()
    menu:
        "You are currently in the cave."

        "Start Run":
            python:
                floor = gamedata["cave_floor"]
                dungeon = cave
                gamedata["battle_mode"] = "automatic"
            play music cave
            jump combat_process

        "Proceed Carefully":
            python:
                floor = gamedata["cave_floor"]
                dungeon = cave
                gamedata["battle_mode"] = "manual"
            play music cave
            jump combat_process

        "Check Floor":
            python:
                renpy.say(None, "You are on floor " + str(gamedata["cave_floor"]+1) + ".")
            jump cave_menu

        "Return to Tavern":
            python:
                gamedata["location"]="Cafe"
            jump cafe_button

#####################################################################################
#### CHAPTER 1 MENUS ################################################################

label bedroom_menu_kazzik:

    scene kazzik_bedroom with dissolve
    menu:
        "What would you like to do?"

        "Go downstairs.":
            jump cafe_menu_kazzik

        "Test [DO NOT CLICK]" if debug == 1:
            jump debug

        "Go to Sleep":
            scene bedroom
            "You decide it's time to sleep."
            window hide
            python:
                gamedata["date"] += "69 lmao"
                g.save(gamedata)
            python:
                renpy.jump(label="begin")

        "Save & Quit":
            python:
                g.save(gamedata)
                renpy.quit()


label cafe_menu_kazzik:
    scene kazzik_cafe with dissolve
    python:
        location = gamedata["location"]
        g.where_who(who_list, gamedata)
        if rock_talk == True and gamedata["rock_talked"] == False:
            renpy.jump("rock_talk_ch1")
        else:
            rock_go_ahead = False
    menu:
        "What would you like to do?"

        "Talk to someone.":
            jump talkto_kazzik_cafe

        "Move.":
            call screen move_menu_kazzik

        "Go to Bedroom":
            jump bedroom_menu_kazzik