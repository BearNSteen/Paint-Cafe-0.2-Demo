label talk_to_cafe:

    menu:
        "You look around at who is visiting. (Current Day: [date])"

        "???" if who_list[6] == 1 and gamedata["c_rock"] < 1:
            hide screen rpg_overlay
            jump rock_dialog

        "Rock" if who_list[6] == 1 and gamedata["c_rock"] >= 1:
            hide screen rpg_overlay
            jump rock_dialog

        "???" if who_list[0] == 1 and gamedata["c_dane"] < 1:
            hide screen rpg_overlay
            jump dane_dialog

        "Dane" if who_list[0] == 1 and gamedata["c_dane"] >= 1 and gamedata["dane_talked"] == False:
            hide screen rpg_overlay
            jump dane_dialog

        "???" if who_list[1] == 1 and gamedata["c_ellie"] < 1:
            hide screen rpg_overlay
            jump ellie_dialog

        "Ellie" if who_list[1] == 1 and gamedata["c_ellie"] >= 1 and gamedata["ellie_talked"] == False:
            hide screen rpg_overlay
            jump ellie_dialog

            # currently not in use
        "Dane and Ellie" if who_list[4] == 1:
            hide screen rpg_overlay
            jump dane_ellie_dialog

        "???" if who_list[2] == 1 and gamedata["c_westra"] < 1:
            hide screen rpg_overlay
            jump westra_dialog

        "Westra" if who_list[2] == 1 and gamedata["c_westra"] >= 1 and gamedata["westra_talked"] == False:
            hide screen rpg_overlay
            jump westra_dialog

        "???" if who_list[3] == 1 and gamedata["c_ember"] < 1:
            hide screen rpg_overlay
            jump ember_dialog

        "Ember" if who_list[3] == 1 and gamedata["c_ember"] >= 1 and gamedata["ember_talked"] == False:
            hide screen rpg_overlay
            jump ember_dialog

        "Lost?" if who_list[5] == 1:
            hide screen rpg_overlay
            jump hint_dialog


        "Back":
            jump back


###########################

label talk_to_smith:

    menu:
        "You look around at who is visiting. (Current Day: [date])"

        "Dane" if who_list[0] == 2:
            jump dane_dialog

        "Ember" if who_list[3] == 2:
            jump ember_dialog

        "Back":
            jump back

###########################

label talk_to_castle:

    menu:
        "You look around at who is visiting. (Current Day: [date])"

        "Dane" if who_list[0] == 3:
            jump dane_dialog

        "Ellie" if who_list[1] == 3 and gamedata["return"] == 0:
            jump ellie_dialog

        "Westra" if who_list[2] == 3 and gamedata["return"] == 0:
            jump westra_dialog

        "Back":
            jump back

###########################

label talkto_kazzik_cafe:

    menu:
        "You look around at who is visiting. (Current Day: [date])"

        "Rock" if who_list[6] == 1 and gamedata["c_rock"] >= 1:
            hide screen rpg_overlay
            jump rock_dialog_ch1

        "Dane" if who_list[0] == 4 and gamedata["c_dane"] >= 1 and gamedata["dane_talked"] == False:
            hide screen rpg_overlay
            jump dane_dialog

        "Ellie" if who_list[1] == 4 and gamedata["c_ellie"] >= 1 and gamedata["ellie_talked"] == False:
            hide screen rpg_overlay
            jump ellie_dialog

        "Westra" if who_list[2] == 4 and gamedata["c_westra"] >= 1 and gamedata["westra_talked"] == False:
            hide screen rpg_overlay
            jump westra_dialog

        "???" if who_list[7] == 1 and gamedata["c_mort"] < 1:
            hide screen rpg_overlay
            jump mort_dialog

        "Mort" if who_list[7] == 1 and gamedata["c_mort"] >= 1 and gamedata["mort_talked"] == False:
            hide screen rpg_overlay
            jump mort_dialog

        "???" if who_list[8] == 1 and gamedata["c_lana"] < 1:
            hide screen rpg_overlay
            jump lana_dialog

        "Lana" if who_list[8] == 1 and gamedata["c_lana"] >= 1 and gamedata["lana_talked"] == False:
            hide screen rpg_overlay
            jump lana_dialog

        "???" if who_list[9] == 1 and gamedata["c_weiss"] < 1:
            hide screen rpg_overlay
            jump weiss_dialog

        "Weiss" if who_list[9] == 1 and gamedata["c_weiss"] >= 1 and gamedata["weiss_talked"] == False:
            hide screen rpg_overlay
            jump weiss_dialog

        "???" if who_list[10] == 1 and gamedata["c_elam"] < 1:
            hide screen rpg_overlay
            jump elam_dialog

        "Elam" if who_list[10] == 1 and gamedata["c_elam"] >= 1 and gamedata["elam_talked"] == False:
            hide screen rpg_overlay
            jump elam_dialog

        "???" if who_list[3] == 1 and gamedata["c_ember"] < 1:
            hide screen rpg_overlay
            jump ember_dialog

        "Ember" if who_list[3] == 1 and gamedata["c_ember"] >= 1 and gamedata["ember_talked"] == False:
            hide screen rpg_overlay
            jump ember_dialog

        "Lost?" if who_list[5] == 1:
            hide screen rpg_overlay
            jump hint_dialog


        "Back":
            jump cafe_menu_kazzik