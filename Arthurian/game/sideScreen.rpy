screen sideScreen:
    window id "window":
        vbox:
            spacing 10
            
            text "[primChar]"
            text "[yr]"
            text "[loc]"

screen asWeProceed:
    modal True
    textbutton "Click to Proceed" xpos 500 ypos 650 action renpy.curry(renpy.end_interaction) (True)
