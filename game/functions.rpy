init python in ug:
    ### Imports
    import random as r

    def ToggleIntVariable(variable, int_var, value):
        """
            variable: Boolean Variable
            int_var: Int Variable
            value: Value to add/substract
        """
        if type(variable) is bool:
            if variable:
                int_var += value
            elif not variable:
                int_var -= value
            else:
                renpy.notify("An error occured, contact Unknown Games")
        else:
            renpy.notify("The variable you've given isn't a boolean var, please check your input.")

    #### Functions
    def AddPlayer(player, dict):
        dict[player] = [0, 0, False]

    def CreateOneCategoryPlayerQuestions(player, dict, category):
        x = 0
        c = category.copy()
        if not player in dict:
            dict[player] = []
            while x < len(c):
                y = r.randint(0, len(c)-1)
                dict[player].append(c[y])
                c.pop(y)
                x += 1

    def CreateTwoCategoriesPlayerQuestions(player, dict, category_one, category_two):
        x = 0
        c = category_one.copy()
        c2 = category_two.copy()
        if not player in dict:
            dict[player] = []
            if len(c) == 40 and len(c2) == 40:
                print("One")
            elif len(c) == 40 and len(c2) != 40 or len(c) != 40 and len(c2) == 40:
                if len(c) == 40:
                    while x < len(c)/2:
                        y = r.randint(0, len(c))
                        dict[player].append(c[y])
                        c.pop(y)
                        x += 1
                    x = 0
                    while x < 20:
                        y = r.randint(0, len(c2))
                        dict[player].append(c2[y])
                        c2.pop(y)
                        x += 1
                else:
                    while x < len(c2)/2:
                        y = r.randint(0, len(c2)-1)
                        dict[player].append(c2[y])
                        c2.pop(y)
                        x += 1
                    x = 0
                    while x < 20:
                        y = r.randint(0, len(c)-1)
                        dict[player].append(c[y])
                        c.pop(y)
                        x += 1

    def SetPlayerGoodPoint(player, value, dict):
        if player in dict:
            dict[player][0] = value

    def SetPlayerBadPoint(player, value, dict):
        if player in dict:
            dict[player][1] = value

    def PrintPlayers(dict):
        for player, scores in dict.items():
            print(player, ":", scores)

    def PrintPlayerScores(player, dict):
        for player_name, scores in dict.items():
            if player_name == player and player in dict:
                print(player_name, "has", dict[player][0], "good answers")
                print(player_name, "has", dict[player][1], "bad answers")

    def ComparePlayers(dict):
        x = 0
        l = []
        winner = None
        for player, scores in dict.items():
            if not "best" in locals():
                best = scores[0]
                winner = player
                l.append(player)
            else:
                if scores[0] > best:
                    best = scores[0]
                    winner = player
                elif scores[0] == best:
                    l.append(player)
        if "l" in locals() and len(l) != 1:
            while x+1 <= len(l):
                if x+2 != len(l) and x+1 != len(l):
                    print(l[x], end=",")
                elif x+1 == len(l):
                    print(l[x], end=" ")
                else:
                    print(l[x], end=" et ")
                x += 1
            return best
        else:
            return winner

    def DisplayAnswers(set):
        set.pop(0)
        for answer in set:
            renpy.say("Dev", answer)

    def NoneFunction(*args, **kwargs):
        pass
