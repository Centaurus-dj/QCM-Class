screen DelayedText(text, xalign=0.5, yalign=0.5):
    text text:
        xalign xalign
        yalign yalign
        size 50

    timer 3.0 action [Hide("DelayedText", Fade(0.3, 0.3, 0.3)), Return()]




### Main Menu
screen main_menu():
    style_prefix "MainMenu"
    default opt_string = "  Options"
    default start_string = "  Start"
    default quit_string = "  Quit"
    frame:
        background None
        xalign 0.5
        yalign 0.1

        vbox:
            label ug.title at MainMenuTransform text_size 80

    frame:
        background None
        yalign 0.9
        xalign 0.5

        hbox:
            spacing 30

            textbutton _(start_string):
                text_style "MainMenu_text"
                hovered SetScreenVariable("start_string", "| Start")
                unhovered SetScreenVariable("start_string", "  Start")
                action Start()
            textbutton _(quit_string):
                text_style "MainMenu_text"
                hovered SetScreenVariable("quit_string", "| Quit")
                unhovered SetScreenVariable("quit_string", "  Quit")
                action Quit()



### Setup Screen
screen Setup():
    frame:
        background "blue05"

        vbox:
            xalign 0.4
            yalign 0.02
            label ug.title text_style "GameTitle"

        vbox:
            button:
                hbox:
                    text _("1 joueur")
                    null width 20
                    if player_nbr == 0 or player_nbr == 2:
                        hbox:
                            xmaximum 30
                            ymaximum 30

                            add "choice_background"
                    else:
                        hbox:
                            xmaximum 30
                            ymaximum 30

                            add "choice_used"
                if player_nbr == 1:
                    action SetVariable("player_nbr", 0)
                else:
                    action SetVariable("player_nbr", 1)

            button:
                hbox:
                    text _("2 joueurs")
                    null width 20
                    if player_nbr == 0 or player_nbr == 1:
                        hbox:
                            xmaximum 30
                            ymaximum 30

                            add "choice_background"
                    else:
                        hbox:
                            xmaximum 30
                            ymaximum 30

                            add "choice_used"
                if player_nbr == 2:
                    action SetVariable("player_nbr", 0)
                else:
                    action SetVariable("player_nbr", 2)


        vbox:
            spacing 30
            xalign 0.2
            yalign 0.56
            text "Catégories"

            vpgrid:
                cols 2
                rows 2
                spacing 10

                button:
                    hbox:
                        text _("Culture Générale"):
                            if not cg_chosen and cat_nbr == 2:
                                style "Unclickable"
                        null width 20
                        hbox:
                            xmaximum 30
                            ymaximum 30
                            if not cg_chosen:
                                add "choice_background"
                            else:
                                add "choice_used"
                    if not cg_chosen and cat_nbr < 2:
                        action [ToggleVariable("cg_chosen"), SetVariable("cat_nbr", cat_nbr+ 1)]
                    elif cg_chosen and cat_nbr < 2:
                        action [ToggleVariable("cg_chosen"), SetVariable("cat_nbr", cat_nbr-1)]
                    elif cg_chosen and cat_nbr == 2:
                        action [ToggleVariable("cg_chosen"), SetVariable("cat_nbr", cat_nbr-1)]

                    if cg_chosen and not prog_chosen and not mang_chosen and not mus_chosen or not cg_chosen and not prog_chosen and not mang_chosen and not mus_chosen:
                        tooltip "Des questions sur la culture générale"
                    elif cg_chosen and prog_chosen or not cg_chosen and prog_chosen:
                        tooltip "Des questions sur la culture générale et la programmation"
                    elif cg_chosen and mang_chosen or not cg_chosen and mang_chosen:
                        tooltip "Des questions sur la culture générale et les mangas"
                    elif cg_chosen and mus_chosen or not cg_chosen and mus_chosen:
                        tooltip "Des questions sur la culture générale et la musique"
                    else:
                        tooltip "Error, please report to Unknown Games"


                button:
                    hbox:
                        text _("Musique"):
                            if not mus_chosen and cat_nbr == 2:
                                style "Unclickable"
                        null width 20
                        hbox:
                            xmaximum 30
                            ymaximum 30
                            if not mus_chosen:
                                add "choice_background"
                            else:
                                add "choice_used"
                    if not mus_chosen and cat_nbr < 2:
                        action [ToggleVariable("mus_chosen"), SetVariable("cat_nbr", cat_nbr+1)]
                    elif mus_chosen and cat_nbr < 2:
                        action [ToggleVariable("mus_chosen"), SetVariable("cat_nbr", cat_nbr-1)]
                    elif mus_chosen and cat_nbr == 2:
                        action [ToggleVariable("mus_chosen"), SetVariable("cat_nbr", cat_nbr-1)]

                    if mus_chosen and not mang_chosen and not prog_chosen and not cg_chosen or not mus_chosen and not mang_chosen and not prog_chosen and not cg_chosen:
                        tooltip "Des questions sur la musique"
                    elif mus_chosen and mang_chosen or not mus_chosen and mang_chosen:
                        tooltip "Des questions sur la musique et les mangas"
                    elif mus_chosen and prog_chosen or not mus_chosen and prog_chosen:
                        tooltip "Des questions sur la musique et la programmation"
                    elif mus_chosen and cg_chosen or not mus_chosen and cg_chosen:
                        tooltip "Des questions sur la musique et la culture générale"
                    else:
                        tooltip "error, please report at Unknown Games"

                button:
                    hbox:
                        text _("Mangas"):
                            if not mang_chosen and cat_nbr == 2:
                                style "Unclickable"
                        null width 20
                        hbox:
                            xmaximum 30
                            ymaximum 30
                            if not mang_chosen:
                                add "choice_background"
                            else:
                                add "choice_used"
                    if not mang_chosen and cat_nbr < 2:
                        action [ToggleVariable("mang_chosen"), SetVariable("cat_nbr", cat_nbr+1)]
                    elif mang_chosen and cat_nbr < 2:
                        action [ToggleVariable("mang_chosen"), SetVariable("cat_nbr", cat_nbr-1)]
                    elif mang_chosen and cat_nbr == 2:
                        action [ToggleVariable("mang_chosen"), SetVariable("cat_nbr", cat_nbr-1)]

                    if mang_chosen and not prog_chosen and not cg_chosen and not mus_chosen or not mang_chosen and not prog_chosen and not cg_chosen and not mus_chosen:
                        tooltip "Des questions sur les mangas"
                    elif mang_chosen and prog_chosen or not mang_chosen and prog_chosen:
                        tooltip "Des questions sur les mangas et la programmation"
                    elif mang_chosen and cg_chosen or not mang_chosen and cg_chosen:
                        tooltip "Des questions sur les mangas et la culture générale"
                    elif mang_chosen and mus_chosen or not mang_chosen and mus_chosen:
                        tooltip "Des questions sur les mangas et les musiques"
                    else:
                        tooltip "error, please report to Unknown Games"

                button:
                    hbox:
                        text _("Programmation"):
                            if not prog_chosen and cat_nbr == 2:
                                style "Unclickable"

                        null width 20
                        hbox:
                            xmaximum 30
                            ymaximum 30
                            if not prog_chosen:
                                add "choice_background"
                            else:
                                add "choice_used"
                    if not prog_chosen and cat_nbr < 2:
                        action [ToggleVariable("prog_chosen"), SetVariable("cat_nbr", cat_nbr+1)]
                    elif prog_chosen and cat_nbr < 2:
                        action [ToggleVariable("prog_chosen"), SetVariable("cat_nbr", cat_nbr-1)]
                    elif prog_chosen and cat_nbr == 2:
                        action [ToggleVariable("prog_chosen"), SetVariable("cat_nbr", cat_nbr-1)]

                    if prog_chosen and not mang_chosen and not mus_chosen and not cg_chosen or not prog_chosen and not mang_chosen and not mus_chosen and not cg_chosen:
                        tooltip "Des questions sur la programmation"
                    elif prog_chosen and mang_chosen or not prog_chosen and mang_chosen:
                        tooltip "Des questions sur la programmation et les mangas"
                    elif prog_chosen and mus_chosen or not prog_chosen and mus_chosen:
                        tooltip "Des questions sur la programmation et la musique"
                    elif prog_chosen and cg_chosen or not prog_chosen and cg_chosen:
                        tooltip "Des questions sur la programmation et la culture générale"
                    else:
                        tooltip "Error, please report to Unknown Games"

        vbox:
            xalign 0.97
            yalign 0.13
            if cat_nbr <= 1:
                text _("Vous avez choisi [cat_nbr!q] catégorie")
            else:
                text _("Vous avez choisi [cat_nbr!q] catégories")


        vbox:
            xalign 0.85
            yalign 0.85

            textbutton _("Commencer"):
                text_size 40
                if cat_nbr <= 2 and cat_nbr > 0:
                    action Return()

    $ tooltip = GetTooltip()

    if tooltip:
        frame:
            background "darka06"
            pos renpy.get_mouse_pos()

            vbox:
                xmaximum 400

                text "[tooltip!q]"


screen QnA(quest, *answers):
    default x = 0
    default store = None
    default store2 = None
    default store3 = None
    default store4 = None
    default f_scores = players[f_name][0]
    if player_nbr == 2:
        default s_scores = players[s_name][0]
    default mult_choice = False
    default true_answers = 0
    ### Solution of an issue with the buttons | I know it's not optimised
    default b1 = False
    default b2 = False
    default b3 = False
    default b4 = False

    python:
        if x != 1:
            ans = list(answers)
            print(ans)
            a = renpy.random.randint(0, len(ans)-1)
            print(ans)
            b = renpy.random.randint(0, len(ans)-1)
            while b == a:
                b = renpy.random.randint(0, len(ans)-1)
            print(ans)
            c = renpy.random.randint(0, len(ans)-1)
            while c == b or c == a:
                c = renpy.random.randint(0, len(ans)-1)
            if len(answers) == 4:
                d = renpy.random.randint(0, len(ans)-1)
                while d == c or d == b or d == a:
                    d = renpy.random.randint(0, len(ans)-1)
            x = 1

        if x != 1:
            for answer in answers:
                if true_answers > 1:
                    if answer[0]:
                        true_answers += 1
                        mult_choice = True
                else:
                    if answer[0]:
                        true_answers += 1

            x = 1


    frame:
        background "darka06"
        xalign 0.0
        yalign 0.15

        vbox:
            text _("[f_name!q]: [f_scores!q] points")
            if player_nbr == 2:
                text _("[s_name!q]: [s_scores!q] points")

            if config.developer == True:
                text _("[true_answers!q], [mult_choice!q]")
                hbox:
                    text _(str(answers[a][0]))
                    text _(str(answers[b][0]))
                    text _(str(answers[c][0]))
                    if len(answers) > 3:
                        text _(str(answers[d][0]))
                text _("[store!q], [store2!q], [store3!q], [store4!q]")
                text _("[temp!q]")
            null height 20
            hbox:
                if b1 or b2 or b3 or b4:
                    text _("Vous avez sélectionné: ")
                    if b1:
                        if not len(answers[a][1]) >= 80:
                            text _(answers[a][1])
                        else:
                            text _("la réponse à gauche")
                    elif b2:
                        if not len(answers[b][1]) >= 80:
                            text _(answers[b][1])
                        else:
                            text _("la réponse au milieu")
                    elif b3:
                        if not len(answers[c][1]) >= 80:
                            text _(answers[c][1])
                        else:
                            text _("la réponse à droite")
                    elif b4:
                        if not len(answers[d][1]) >= 80:
                            text _(answers[d][1])
                        else:
                            text _("la réponse tout à droite")
                else:
                    text _("Vous n'avez sélectionné aucune réponse")


    frame:
        background None
        xalign 0.45
        yalign 0.38

        text _("[quest]")

    frame:
        background None
        xalign 0.45
        yalign 0.7

        hbox:
            style_prefix "radio"
            spacing 10

            hbox:
                xmaximum 200
                button:
                    text _(answers[a][1])
                    selected True
                    if mult_choice:
                        action [SetScreenVariable("b1", True), SetScreenVariable("b2", False), SetScreenVariable("b3", False), SetScreenVariable("b4", False), SetScreenVariable("store", answers[a][0])]
                    else:
                        action [SetScreenVariable("b1", True), SetScreenVariable("b2", False), SetScreenVariable("b3", False), SetScreenVariable("b4", False), SetScreenVariable("store", answers[a][0])]

            hbox:
                xmaximum 200
                button:
                    text _(answers[b][1])
                    selected True
                    if mult_choice:
                        if store == None:
                            action [SetScreenVariable("b1", False), SetScreenVariable("b2", True), SetScreenVariable("b3", False), SetScreenVariable("b4", False), SetScreenVariable("store", answers[b][0])]
                        else:
                            action [SetScreenVariable("b1", False), SetScreenVariable("b2", True), SetScreenVariable("b3", False), SetScreenVariable("b4", False), SetScreenVariable("store2", answers[b][0])]
                    else:
                        action [SetScreenVariable("b1", False), SetScreenVariable("b2", True), SetScreenVariable("b3", False), SetScreenVariable("b4", False), SetScreenVariable("store", answers[b][0])]

            hbox:
                xmaximum 200
                button:
                    text _(answers[c][1])
                    selected True
                    if mult_choice:
                        if store == None:
                            action [SetScreenVariable("b1", False), SetScreenVariable("b2", False), SetScreenVariable("b3", True), SetScreenVariable("b4", False), SetScreenVariable("store", answers[c][0])]
                        else:
                            action [SetScreenVariable("b1", False), SetScreenVariable("b2", False), SetScreenVariable("b3", True), SetScreenVariable("b4", False), SetScreenVariable("store3", answers[c][0])]
                    else:
                        action [SetScreenVariable("b1", False), SetScreenVariable("b2", False), SetScreenVariable("b3", True), SetScreenVariable("b4", False), SetScreenVariable("store", answers[c][0])]

            if len(answers) > 3:
                hbox:
                    xmaximum 200
                    button:
                        text _(answers[d][1])
                        selected True
                        if mult_choice:
                            if store == None:
                                action [SetScreenVariable("b1", False), SetScreenVariable("b2", False), SetScreenVariable("b3", False), SetScreenVariable("b4", True), SetScreenVariable("store", answers[d][0])]
                            else:
                                action [SetScreenVariable("b1", False), SetScreenVariable("b2", False), SetScreenVariable("b3", False), SetScreenVariable("b4", True), SetScreenVariable("store", answers[d][0])]
                        else:
                            action [SetScreenVariable("b1", False), SetScreenVariable("b2", False), SetScreenVariable("b3", False), SetScreenVariable("b4", True), SetScreenVariable("store", answers[d][0])]
    frame:
        background None
        xalign 0.9
        yalign 0.9

        textbutton _("Suivant"):
            if store or store2 or store3 or store4:
                action [SetVariable("temp", True), Return()]
            else:
                action [SetVariable("temp", False), Return()]




screen PlayerSay(player_name):
    frame:
        background "black"
        xalign  0.5
        yalign 0.45

        text _("[player_name], c'est à vous de jouer !")

    timer 2.5 action Return()

screen Scores(*players_stats):
    frame:
        background "blue05"
        xalign 0.47
        yalign 0.24

        vbox:
            xalign 0.47
            yalign 0.24
            spacing 20
            xminimum 0.5
            yminimum 0.2

            hbox:
                spacing 25

                text _("[f_name]: ")
                text _("[players_stats[0][0]] bonnes réponses")
                text _("[players_stats[0][1]] mauvaises réponses")

            if len(players_stats) == 2:
                hbox:
                    spacing 25

                    text _("[s_name]: ")
                    text _("[players_stats[1][0]] bonnes réponses")
                    text _("[players_stats[1][1]] mauvaises réponses")

    python:
        if player_nbr == 2:
            comp = ug.ComparePlayers(players)

    frame:
        background None
        xalign 0.45
        yalign 0.6

        if player_nbr == 2:
            if comp is list():
                text _("[f_name] et [s_name] sont à égalité"):
                    size 50
            else:
                text _("[comp] est vainqueur"):
                    size 50

    frame:
        background None
        xalign 0.45
        yalign 0.8


        textbutton _("Menu Principal"):
            text_size 35
            action MainMenu()


### Styles
style MainMenu_text:
    color "#bce"
    size 35

style GameTitle:
    color "#5AFCF5"
    size 60

style Unclickable:
    color gui.insensitive_color
