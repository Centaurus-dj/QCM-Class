label start:
    window hide
    call startscreen from _call_startscreen
    show black with fade
    scene black
    call screen Setup
    if player_nbr >= 1:
        python:
            f_name = renpy.input("Le pseudo du joueur 1:")
            f_name = f_name.strip()

            ug.AddPlayer(f_name, players)
            if cg_chosen and not mus_chosen and not mang_chosen and not prog_chosen:
                ug.CreateOneCategoryPlayerQuestions(f_name, questions, questionary["Culture Generale"])
            elif not cg_chosen and mus_chosen and not mang_chosen and not prog_chosen:
                ug.CreateOneCategoryPlayerQuestions(f_name, questions, questionary["Musique"])
            elif not cg_chosen and not mus_chosen and mang_chosen and not prog_chosen:
                ug.CreateOneCategoryPlayerQuestions(f_name, questions, questionary["Mangas"])
            elif not cg_chosen and not mus_chosen and not mang_chosen and prog_chosen:
                ug.CreateOneCategoryPlayerQuestions(f_name, questions, questionary["Programmation"])
            else:
                if cg_chosen and mus_chosen and not mang_chosen and not prog_chosen:
                    ug.CreateTwoCategoriesPlayerQuestions(f_name, questions, questionary["Culture Generale"], questionary["Musique"])
                elif cg_chosen and not mus_chosen and mang_chosen and not prog_chosen:
                    ug.CreateTwoCategoriesPlayerQuestions(f_name, questions, questionary["Culture Generale"], questionary["Mangas"])
                elif cg_chosen and not mus_chosen and not mang_chosen and prog_chosen:
                    ug.CreateTwoCategoriesPlayerQuestions(f_name, questions, questionary["Culture Generale"], questionary["Programmation"])
                elif not cg_chosen and mus_chosen and mang_chosen and not prog_chosen:
                    ug.CreateTwoCategoriesPlayerQuestions(f_name, questions, questionary["Musique"], questionary["Mangas"])
                elif not cg_chosen and mus_chosen and not mang_chosen and prog_chosen:
                    ug.CreateTwoCategoriesPlayerQuestions(f_name, questions, questionary["Musique"], questionary["Programmation"])
                elif not cg_chosen and not mus_chosen and mang_chosen and prog_chosen:
                    ug.CreateTwoCategoriesPlayerQuestions(f_name, questions, questionary["Mangas"], questionary["Programmation"])

    if player_nbr == 2:
        python:
            s_name = renpy.input("Le pseudo du joueur 2:")
            s_name = s_name.strip()

            ug.AddPlayer(s_name, players)
    python:

        if player_nbr == 1:
            for setting in questions[f_name]:
                renpy.call_screen("QnA", setting[0], setting[1], setting[2], setting[3])
                if temp is True:
                    players[f_name][0] += 1
                else:
                    players[f_name][1] += 1
            renpy.call_screen("Scores", players[f_name])

        else:
            x = 0
            while x < len(questions[f_name]):
                renpy.call_screen("PlayerSay", f_name)
                for setting in questions[f_name]:
                    renpy.call_screen("QnA", setting[0], setting[1], setting[2], setting[3])
                    if temp is True:
                        players[f_name][0] += 1
                    else:
                        players[f_name][1] += 1
                    break
                questions[f_name].pop(0)
                renpy.call_screen("PlayerSay", s_name)
                for setting in questions[f_name]:
                    renpy.call_screen("QnA", setting[0], setting[1], setting[2], setting[3])
                    if _return:
                        players[s_name][0] += 1
                    else:
                        players[s_name][1] += 1
                    break
                questions[f_name].pop(0)
                x += 2

            renpy.call_screen("Scores", players[f_name], players[s_name])


label after_setup:
    if persistent.first_play:
        c "C'est votre première partie."
        $ persistent.first_play = False
    else:
        python:

            persistent.count_play += 1
            renpy.save_persistent()
        if persistent.count_play == 2:
            c "C'est votre [persistent.count_play]nde partie."
        else:
            c "C'est votre [persistent.count_play]ième partie."
