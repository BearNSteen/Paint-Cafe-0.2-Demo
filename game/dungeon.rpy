label combat_process:
    show screen rpg_battle
    python:

        def flow_combat(enemies):
            turn_order = turns(enemies)
            renpy.say(None, "You are in combat.")
            result = take_turn(turn_order)
            if result == False:
                return False
            else:
                end_combat(enemies)

        def turns(enemies):
            in_combat = True
            battle_info["enemy"] = []
            party = gamedata["party"]
            battle_info["party_hp"] = []
            for n in party:
                battle_info["party_hp"].append(n.get_hp())
            for enemy in enemies:
                battle_info["enemy"].append(enemy)
            print(battle_info["enemy"])
            enemynum = battle_info["enemy"]
            battle_info["enemy_hp"] = []
            for n in battle_info["enemy"]:
                if n != None:
                    battle_info["enemy_hp"].append(n.get_hp())
                else:
                    battle_info["enemy_hp"].append(None)
            turn_order = rpg.turn_order(party, battle_info["enemy"])
            return turn_order

        def take_turn(turn_order):
            enemy = battle_info["enemy"]
            xp_copy = battle_info["enemy"]
            renpy.hide_screen("rpg_battle")
            renpy.show_screen("rpg_battle")
            renpy.show_screen("enemy_display")
            print(turn_order)
            while True:
                t_o = []
                for char in turn_order:
                    t_o.append(char)
                while len(t_o) > 0:
                    menu_state = 1
                    char = t_o[0]
                    name = char[0]
                    while menu_state == 1:
                        if char[2].get_alignment() == 1:
                            if gamedata["battle_mode"] == "manual":
                                renpy.say(None, "It is %s's turn." % (name))
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
                                                    renpy.say(None, "%s uses %s on %s!" % (name, attack.get_name(), target_name))
                                                    damage = rpg.compute_damage(char[2], attack, target)
                                                    renpy.say(None, "The attack does %s damage!" % (damage))
                                                    index = battle_info["enemy"].index(target)
                                                    battle_info["enemy_hp"][index] -= damage
                                                    if battle_info["enemy_hp"][index] < 0:
                                                        battle_info["enemy_hp"][index] = 0
                                                    if battle_info["enemy_hp"][index] == 0:
                                                        renpy.hide_screen("enemy_display")
                                                        renpy.hide_screen("rpg_battle")
                                                        renpy.show_screen("rpg_battle")
                                                        renpy.show_screen("enemy_display")
                                                        renpy.say(None, "%s falls!" % (target_name))
                                                        for entity in t_o:
                                                            if entity[2] == target:
                                                                t_o.remove(entity)
                                                        battle_info["enemy"][index] = None
                                                        # move all enemies to the front of the list
                                                        for x in range(1, 4, -1):
                                                            if battle_info["enemy"][x-1] == None and battle_info["enemy"][x] != None:
                                                                battle_info["enemy"][x-1] = battle_info["enemy"][x]
                                                                battle_info["enemy"][x] = None
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
                                    renpy.hide_screen("enemy_display")
                                    renpy.hide_screen("rpg_battle")
                                    renpy.say(None, "You turn around and leave the dungeon.")
                                    return False
                            else:
                                renpy.say(None, "It is %s's turn." % (name))
                                attack_list = []
                                attacks = char[2].get_attacks()
                                for attack in attacks:
                                    if attack != None:
                                        attack_list.append(attack)
                                attack_num = g.generate_number(0, len(attack_list)-1)
                                chosen = attack_list[attack_num]
                                if chosen == None:
                                    renpy.say(None, "%s steadies their breath." % (name))
                                    del t_o[0]
                                    menu_state=0
                                else:
                                    count = 0
                                    for e in battle_info["enemy"]:
                                        if e != None:
                                            count += 1
                                    chosen_name = attacks[attack_num].get_name()
                                    target_rand = None
                                    if count <= 1:
                                        for x in range(0, 4):
                                            if enemy[x] != None:
                                                target_rand = x
                                    else:
                                        target_rand = g.generate_number(0, count-1)
                                        while enemy[target_rand] == None:
                                            target_rand = g.generate_number(0, 3)
                                            print(target_rand)
                                    if target_rand == None:
                                        renpy.say(None, "You aren't sure what happened, but combat ends!")
                                        return True
                                    target_name = enemy[target_rand].get_name()
                                    target = enemy[target_rand]
                                    renpy.say(None, "%s uses %s on %s!" % (name, chosen_name, target_name))
                                    damage = rpg.compute_damage(char[2], chosen, target)
                                    renpy.say(None, "%s is hit for %s damage!" % (target_name, damage)) 
                                    battle_info["enemy_hp"][target_rand]  -= damage
                                    renpy.hide_screen("rpg_battle")
                                    renpy.show_screen("rpg_battle")
                                    index = battle_info["enemy"].index(target)
                                    if battle_info["enemy_hp"][target_rand] <= 0:
                                        battle_info["enemy_hp"][target_rand] = 0
                                        renpy.hide_screen("enemy_display")
                                        renpy.show_screen("enemy_display")
                                        renpy.say(None, "%s falls!" % (target_name))
                                        for entity in t_o:
                                            if entity[2] == target:
                                                t_o.remove(entity)
                                            battle_info["enemy"][index] = None
                                            # move all enemies to the front of the list
                                            for x in range(1, 4, -1):
                                                if battle_info["enemy"][x-1] == None and battle_info["enemy"][x] != None:
                                                    battle_info["enemy"][x-1] = battle_info["enemy"][x]
                                                    battle_info["enemy"][x] = None
                                            if battle_info["enemy"] == [None,None,None,None]:
                                                renpy.say(None, "Combat ends!")
                                                return True
                                    renpy.hide_screen("enemy_display")
                                    renpy.show_screen("enemy_display")
                                    del t_o[0]
                                    menu_state = 0
                        else:
                            renpy.say(None, "It is %s's turn." % (name))
                            attack_list = []
                            attacks = char[2].get_attacks()
                            for attack in attacks:
                                if attack != None:
                                    attack_list.append(attack)
                            attack_num = g.generate_number(0, len(attack_list)-1)
                            chosen = attack_list[attack_num]
                            if chosen == None:
                                renpy.say(None, "%s appears to just loaf around." % (name))
                                del t_o[0]
                                menu_state=0
                            else:
                                chosen_name = attacks[attack_num].get_name()
                                targets_left = 0
                                for value in battle_info["party_hp"]:
                                    if value != 0:
                                        targets_left += 1
                                x = 1
                                while x == 1:
                                    target_rand = g.generate_number(0, targets_left)
                                    try:
                                        if battle_info["party_hp"][target_rand] != 0:
                                            x = 0
                                    except IndexError:
                                        pass
                                target_name = party[target_rand].get_name()
                                target = party[target_rand]
                                renpy.say(None, "%s uses %s on %s!" % (name, chosen_name, target_name))
                                damage = rpg.compute_damage(char[2], chosen, target)
                                renpy.say(None, "%s is hit for %s damage!" % (target_name, damage))
                                battle_info["party_hp"][target_rand] -= damage
                                renpy.hide_screen("rpg_battle")
                                renpy.show_screen("rpg_battle")
                                if battle_info["party_hp"][target_rand] <= 0:
                                    battle_info["party_hp"][target_rand] = 0
                                    renpy.say(None, "%s retreats!" % (target_name))
                                    if party[target_rand] in t_o:
                                        t_o.remove(party[target_rand])
                                    for x in turn_order:
                                        if x[0] == target_name:
                                            turn_order.remove(x)
                                    continue_fight = 0
                                    for value in battle_info["party_hp"]:
                                        if value != 0 and value != None:
                                            continue_fight = 1
                                    if continue_fight == 0:
                                        renpy.say(None, "The party has retreated!")
                                        renpy.hide_screen("enemy_display")
                                        return False
                                del t_o[0]
                                menu_state = 0
                


        def end_combat(enemies):
            renpy.hide_screen("enemy_display")
            party = gamedata["party"]
            xp = 0
            for enemy in enemies:
                print(enemy)
                if enemy != None:
                    print(enemy.get_xp())
                    xp += enemy.get_xp()
            renpy.say(None, "Your party receives %s experience points." % (xp))
            for member in party:
                level_up = member.gain_xp(xp)
                if level_up == True:
                    renpy.say(None, "%s grew stronger!" % (member.get_name()))


#===================================================================#

# Beginning of action #

        in_dungeon = True
        party = gamedata["party"]
        while in_dungeon:
            if floor == len(dungeon)-1:
                renpy.say(None, "You reach the final floor of the dungeon.")
            encounters = dungeon[floor][0]
            for encounter in range(0, encounters):
                enemies = [None, None, None, None]
                if floor == len(dungeon)-1:
                    for e in range(0, dungeon[floor][1]):
                        num = g.generate_number(0, len(b_list)-1)
                        enemies[e] = b_list[num]  
                else:    
                    for e in range(0, dungeon[floor][1]):
                        num = g.generate_number(0, len(e_list)-1)
                        enemies[e] = e_list[num]
                success = flow_combat(enemies)
                if success == False:
                    renpy.say(None, "Your run has ended at floor " + str(floor+1) + ".")
                    renpy.hide_screen("rpg_battle")
                    renpy.jump(label='cave_menu')
                else:
                    #random event chance
                    renpy.say(None, "The party continues.")
            renpy.say(None, "Your party reaches the end of the floor.")
            if floor == len(dungeon)-1:
                renpy.say(None, "Your party has completed the dungeon!")
                # random party member says something
                # give rewards
                # add affection
                renpy.say(None, "The party leaves victorious and beaming.")
                renpy.hide_screen("rpg_battle")
                renpy.jump(label='cave_menu')
            floor += 1
            renpy.say(None, "You are now on floor " + str(floor+1) + ".")


