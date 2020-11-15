
### Persistent variables
init 999:
    $ persistent.first_play = True
    $ persistent.count_play = 1

### Static variables
define c = Character("Centaurus", color="#f93")

### Dynamic variables
init 5 python:
    cg_chosen = False
    mang_chosen = False
    mus_chosen = False
    prog_chosen = False
    cat_nbr = 0
    player_nbr = 0
    f_name = ""
    s_name = ""
    players = {}
    questions = {}
    temp = None

init 4:
    default mus_chosen = mus_chosen

### Creator-defined variables under "ug" tag
init 99999 python in ug:
    title = "Quizzio"
