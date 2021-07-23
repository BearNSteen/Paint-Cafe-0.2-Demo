import datetime
import pickle
import random as r
import os
import time


class Char:

    def __init__(self, name, probability):
        self._name = name
        self._number = probability
        self._day = 1
        self._dialog = []

    def get_probability(self):
        return self._number

    def get_name(self):
        return self._name


def initialize():
    try:
        with open('savefile.txt', 'rb') as f:
            data = pickle.load(f)
            print("Data loaded.")
            print(data["playername"])
            return data
    except IOError:
        # in regards to dictionary storage:
        # c_name refers to how many unique days the player has interacted with a character
        # aff_name refers to the affection a character has for the player
        data = {"date": datetime.date.today().strftime("%m/%d/%Y"),
                "days": 0, "return": 0,
                "c_dane": 0, "aff_dane": 0, "dane_talked": 0,
                "c_ellie": 0, "aff_ellie": 0, "ellie_mad": 0, "ellie_talked": 0,
                "c_westra": 0, "aff_westra": 0, "westra_talked": 0,
                "c_ember": 0, "aff_ember": 0, "ember_talked": 0,
                "c_dane_ellie": 0,
                "c_rock": 0, "aff_rock": 0, "rock_talked": 0,
                "c_elam": 0, "aff_elam": 0, "elam_talked": 0,
                "c_hargen": 0, "aff_hargen": 0,
                "c_boyd": 0, "aff_boyd": 0,
                "c_cuppa": 0, "aff_cuppa": 0,
                "c_grapefart": 0, "aff_grapefart": 0,
                "c_weiss": 0, "aff_weiss": 0,
                "c_mort": 0, "aff_mort": 0,
                "c_lana": 0, "aff_lana": 0,
                "inventory": [],
                "party": [],
                "cave_floor": 0,
                "battle_mode": "automatic",
                "progress": "selection", "chapter": 0
                }
        return data

def init_battle():
    battle_info = {"enemy": [], "enemy_hp": [], "party_hp": []}
    return battle_info

def find_day(data):
    current_day = datetime.date.today().strftime("%m/%d/%Y")
    print("The current day is: " + str(current_day))
    day = data["date"]
    if day == current_day and data['days'] != 0:
        add_day = False
        return add_day
    else:
        add_day = True
        data["days"] += 1
        data["date"] = current_day
        return add_day


def who_here(data):
    """
    determines who is in the cafe today by rolling random integers
    :param data: The gamedata file.
    :return:
    """
    patrons = data['characters']
    if data["days"] == 2 and data["c_dane"] <= 5 or data["days"] >= 10:
        patrons.append(Char("Dane", 11))
    if data["days"] == 4 and data["c_dane"] > 1 and data["c_dane"] <= 5 or data["days"] >= 10:
        patrons.append(Char("Ellie", 11))
    if data["days"] == 2 and data["c_dane"] <= 5 or data["days"] >= 10:
        patrons.append(Char("Westra", 11))
    if data["chapter"] >= 1:
        patrons.append(Char("Mort", 6))
    if data["chapter"] >= 1:
        patrons.append(Char("Lana", 6))
    if data["chapter"] >= 1 and data["days"] > 8:
        patrons.append(Char("Hargen", 6))
    if data["chapter"] >= 1 and data["days"] > 11:
        patrons.append(Char("Elam", 6))
    if data["days"] == 14:
        patrons.append(Char("Boyd", 9))
    if data["days"] == 18:
        patrons.append(Char("Ember", 7))
    if data["days"] == 18:
        patrons.append(Char("Cuppa", 2))
    if data["days"] == 18:
        patrons.append(Char("Grapefart", 3))
    if data["days"] == 18:
        patrons.append(Char("Weiss", 4))

    in_cafe = []
    print(patrons)
    for indiv in patrons:
        prob = r.randint(0, 11)
        prob_pat = indiv.get_probability()
        if prob <= prob_pat:
            in_cafe.append(indiv.get_name())
            print(str(indiv.get_name()) + " is here today.")
        else:
            print(str(indiv.get_name()) + " is not here today.")
    # Timing for leaving event must sync up! Remove them if you
    # haven't watched all 3 of their stories yet.
    # In their place, add Cuppa, who will redirect them to the other 2.
    if "Dane" in in_cafe:
        if data["c_dane"] == 4:
            if data["c_ellie"] < 3 or data["c_westra"] < 3:
                in_cafe.remove("Dane")
                in_cafe.append("Cuppa")
                data["cuppa"] = "help1"
    if "Ellie" in in_cafe:
        if data["c_ellie"] == 3:
            if data["c_dane"] < 4 or data["c_westra"] < 3:
                in_cafe.remove("Ellie")
                in_cafe.append("Cuppa")
                data["cuppa"] = "help1"
    if "Westra" in in_cafe:
        if data["c_westra"] == 3:
            if data["c_dane"] < 4 or data["c_ellie"] < 3:
                in_cafe.remove("Westra")
                in_cafe.append("Cuppa")
                data["cuppa"] = "help1"
    # CODE FOR DANE + ELLIE (currently omitted)
    #if "Dane" in in_cafe and "Ellie" in in_cafe and True == False:
    #    if data["c_ellie"] in range(2,5):
    #        in_cafe.remove("Dane")
    #        in_cafe.remove("Ellie")
    #        in_cafe.append("Dane + Ellie")
    #    else:
    #        in_cafe.remove("Dane")
    print(in_cafe)
    data['in_cafe'] = in_cafe
    return in_cafe


def check_who(patron_list):
    # who_list corresponds to:
    # 0) Dane
    # 1) Ellie
    # 2) Westra
    # 3) Ember
    # 4) Dane + Ellie
    # 5) Cuppa
    # 6) Rock
    who_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if "Rock" in patron_list:
        who_list[6] = 1
    if "Dane" in patron_list:
        who_list[0] = 1
    else:
        who_list[0] = 0
    if "Ellie" in patron_list:
        who_list[1] = 1
    else:
        who_list[1] = 0
    if "Westra" in patron_list:
        who_list[2] = 1
    else:
        who_list[2] = 0
    if "Ember" in patron_list:
        who_list[3] = 1
    else:
        who_list[3] = 0
    if "Dane + Ellie" in patron_list:
        who_list[0] = 0
        who_list[1] = 0
        who_list[4] = 1
    if "Cuppa" in patron_list:
        who_list[5] = 1
    else:
        who_list[5] = 0
    if "Mort" in patron_list:
        who_list[7] = 1
    else:
        who_list[7] = 0
    if "Lana" in patron_list:
        who_list[8] = 1
    else:
        who_list[8] = 0
    if "Weiss" in patron_list:
        who_list[9] = 1
    else:
        who_list[9] = 0
    if "Elam" in patron_list:
        who_list[10] = 1
    else:
        who_list[10] = 0
    if "Boyd" in patron_list:
        who_list[11] = 1
    else:
        who_list[11] = 0
    return who_list

def where_who(who_list, data):
    if who_list[0] == 1:
        if data["c_dane"] >= 2:
            who_list[0] = 3
    if who_list[1] == 1:
        if data["c_ellie"] >= 3:
            if data["return"] == 0 and data["c_dane"] > 5:
                who_list[1] = 3
            else:
                who_list[1] = 0
    if who_list[2] == 1:
        if data["c_westra"] >= 3:
            if data["return"] == 0 and data["c_dane"] > 5:    
                who_list[2] = 3
            else:
                who_list[2] = 0

def rock_talk(gamedata):
    if gamedata["c_rock"] < 2:
        return True
    elif gamedata["c_dane"] == 5:
        if gamedata["c_rock"] <= 2:
            return True
    # Other instances where Rock needs to talk to you
    else:
        return False


def generate_number(num1, num2):
    num = r.randint(num1, num2)
    return num


def save(data):
    print("Saving...")
    with open('savefile.txt', 'wb') as save:
        pickle.dump(data, save)
    print("Save Completed.")


def delete_save():
    print("Thanks for stopping by.")
    print("Deleting..")
    try:
        os.remove("savefile.txt")
        print("Deleted.")
    except WindowsError:
        print("File does not exist. Cannot delete.")

def flow_combat(enemies):
    turns(enemies)
    renpy.say(None, "You are in combat.")
    result = take_turn()
    if result == False:
        return False
    else:
        end_combat(enemies)


def turns(enemies):
    in_combat = True
    party = gamedata["party"]
    battle_info["party_hp"] = []
    for n in party:
        battle_info["party_hp"].append(n.get_hp())
    battle_info["enemy"] = enemies
    enemynum = battle_info["enemy"]
    battle_info["enemy_hp"] = []
    for n in battle_info["enemy"]:
        if n != None:
            battle_info["enemy_hp"].append(n.get_hp())
        else:
            battle_info["enemy_hp"].append(None)
    turn_order = rpg.turn_order(party, battle_info["enemy"])
    

def take_turn():
    t_o = []
    for char in turn_order:
        t_o.append(char)
    while len(t_o) > 0:
        menu_state = 1
        char = t_o[0]
        name = char[0]
        while menu_state == 1:
            if char[2].get_alignment() == 1:
                if gamedata["battle_mode"] == "Manual":
                    renpy.say(None, "It is [name]'s turn.")
                    renpy.say(None, "What would you like to do?", interact=False)
                    choice = renpy.display_menu([("Attack", "attack"), ("Run","run")])
                    if choice == "attack":
                        menu_state = 2
                        while menu_state == 2:
                            pre_list = char[2].get_attacks()
                            atk_list = []
                            for attack in pre_list:
                                if attack != None:
                                    atk_list.append((attack.get_name(), attack))
                            atk_list.append(("Back", "back"))
                            attack = renpy.display_menu(atk_list)
                            if attack != "back":
                                menu_state = 3
                                while menu_state == 3:
                                    renpy.say(None, "Choose a target.", interact=False)
                                    enemy_list = []
                                    for n in range(len(battle_info["enemy"])):
                                        if battle_info["enemy"][n] != None:
                                            enemy_list.append((battle_info["enemy"][n].get_name(), battle_info["enemy"][n]))
                                    enemy_list.append(("Back", "back"))
                                    target = renpy.display_menu(enemy_list)
                                    if target != "back":
                                        menu_state = 1
                                        target_name = target.get_name()
                                        renpy.say(None, "[name] attacks!")
                                        renpy.say(None, "[target_name] is hit!")
                                        damage = rpg.compute_damage(char[2], attack, target)
                                        renpy.say(None, "The attack does [damage] damage!")
                                        index = battle_info["enemy"].index(target)
                                        battle_info["enemy_hp"][index] -= damage
                                        if battle_info["enemy_hp"][index] < 0:
                                            battle_info["enemy_hp"][index] = 0
                                        if battle_info["enemy_hp"][index] == 0:
                                            renpy.show_screen("rpg_battle")
                                            renpy.say(None, "[target_name] falls!")
                                            for entity in t_o:
                                                if entity[2] == target:
                                                    t_o.remove(entity)
                                            battle_info["enemy"][index] = None
                                            if battle_info["enemy"] == [None,None,None,None]:
                                                renpy.say(None, "Combat ends!")
                                                return True
                                        menu_state = 0
                                        del t_o[0]
                                        print(t_o)
                                    else:
                                        menu_state = 2
                            else:
                                menu_state = 1

                    else:
                        renpy.say(None, "You turn around and leave the dungeon.")
                        return False
            else:
                renpy.say(None, "It is [name]'s turn.")
                attack_list = []
                attacks = char[2].get_attacks()
                for attack in attacks:
                    if attack != None:
                        attack_list.append(attack)
                attack_num = g.generate_number(0, len(attack_list)-1)
                chosen = attack_list[attack_num]
                if chosen == None:
                    renpy.say(None, "[name] appears to just loaf around.")
                    del t_o[0]
                    menu_state=0
                else:
                    chosen_name = attacks[attack_num].get_name()
                    target_rand = g.generate_number(0, len(party)-1)
                    target_name = party[target_rand].get_name()
                    target = party[target_rand]
                    renpy.say(None, "They use [chosen_name]!")
                    damage = rpg.compute_damage(char[2], chosen, target)
                    renpy.say(None, "[target_name] is hit!")
                    renpy.say(None, "The attack does [damage] damage!")
                    battle_info["party_hp"][target_rand] -= damage
                    renpy.show_screen("rpg_battle")
                    del t_o[0]
                    menu_state = 0
    renpy.jump(label="take_turn")


def end_combat():
    xp = 0
    for enemy in enemynum:
        if enemy != None:
            xp += enemy.get_xp()
    for member in party:
        member.gain_xp(xp)
    renpy.hide_screen("rpg_overlay")
    renpy.hide_screen("rpg_battle")
    renpy.say(None, "Your party receives [xp] experience points.")