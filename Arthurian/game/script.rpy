# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nine = Character("Nine", who_color = "#000000")

default inventory = []
default deckard = player("Deckard", "484-12-04")

# Status Variables

default primChar = "Deckard"
default yr = "484-12-04"
default loc = "Wildwood"

# Tracker Variables

default deckardCover = 0
default deckardChivalry = 0
default deckardVanity = 0
default deckardTrickery = 0
default deckardHonesty = 0

# Declare background

image parchment = "parchment.png"
image scroll = "scroll.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show screen asWeProceed
    
    #Intro Files
    $ hymnOfCaedmon = getPage("text/caedmonHymn.txt")
    $ ctesibiusMan = getPage("text/ctesibiusMan.txt")
    $ deckIntro1 = getPage("text/charIntro1.txt")
    $ deckIntro2 = getPage("text/charIntro2.txt")
    $ deckIntro3 = getPage("text/charIntro3.txt")
    $ deckIntro4 = getPage("text/charIntro4.txt")
    $ deckIntro5 = getPage("text/charIntro5.txt")
    $ deckIntro6 = getPage("text/charIntro6.txt")
    $ deckIntro7 = getPage("text/charIntro7.txt")
    $ deckIntro8 = getPage("text/charIntro8.txt")
    
    #Initialize
    scene parchment

    # Intro 
    "[hymnOfCaedmon]"
    "[ctesibiusMan]"    
    "[deckIntro1]"
    show screen sideScreen
    "[deckIntro2]"
    "[deckIntro3]"
    "[deckIntro4]"
    "[deckIntro5]"
    "[deckIntro6]"
    "[deckIntro7]"
    "[deckIntro8]"
    
    jump seq1   

    # This ends the game.

    label fin:
        return