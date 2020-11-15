image black = "#000000"

#image choice_background = Solid('#29F988', xsize=50, ysize=50)
image choice_empty = Transform("#000000", size=(18, 18))
image choice_used = Transform("#29F988", size=(30, 30))
image choice_background = Fixed(
    Solid('#29F988', xsize=2, xalign=.0),
    Solid('#29F988', xsize=2, xalign=1.0),
    Solid('#29F988', ysize=2, yalign=.0),
    Solid('#29F988', ysize=2, yalign=1.0))

image darka06:
    "#000000"
    alpha 0.87
image blue05:
    "#3CFDB8"
    alpha 0.5


transform MainMenuTransform:
    yalign 0.1 xalign 0.45
    linear 1.0 yalign 0.3
    repeat
