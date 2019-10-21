# TO-DO:
## Transition scenes
## Different backgrounds for settings
## Better variable tracking

label seq1:

    #Sequence One Files
    $ chapOne1Zero = getPage("text/Sequence01/chap1.1.0.txt")
    $ chapOne1One = getPage("text/Sequence01/chap1.1.1.txt")
    $ ChapOne1Two = getPage("text/Sequence01/chap1.1.2.txt")
    $ ChapOne1Three = getPage("text/Sequence01/chap1.1.3.txt")
    $ ChapOne1Four = getPage("text/Sequence01/chap1.1.4.txt")
    $ ChapOne1Five = getPage("text/Sequence01/chap1.1.5.txt")
    $ ChapOne1Six = getPage("text/Sequence01/chap1.1.6.txt")
    $ ChapOne1Seven = getPage("text/Sequence01/chap1.1.7.txt")
    $ ChapOne1Eight = getPage("text/Sequence01/chap1.1.8.txt")
    $ ChapOne1Nine = getPage("text/Sequence01/chap1.1.9.txt")
    $ ChapOne1Ten = getPage("text/Sequence01/chap1.1.10.txt")

    $ chapOne2One = getPage("text/Sequence01/chap1.2.1.txt")
    $ chapOne2Two = getPage("text/Sequence01/chap1.2.2.txt")
    $ chapOne2Three = getPage("text/Sequence01/chap1.2.3.txt")
    $ chapOne2Four = getPage("text/Sequence01/chap1.2.4.txt")
    $ chapOne2Five = getPage("text/Sequence01/chap1.2.5.txt")

    $ vision1 = getPage("text/Visionsof497/Vision497.1.txt")

    $ zenoAndRomulus = getPage("text/Sequence01/ZenoAndRomulus1.txt")
    $ tristanAndMordred = getPage("text/Sequence01/TristanAndMordred1.txt")
    $ raechelleAndLucan = getPage("text/Sequence01/RaechelleAndLucan1.txt")
    $ wlencingAndFrederic = getPage("text/Sequence01/WlencingAndFrederic1.txt")
    $ clovisAndRagnachar = getPage("text/Sequence01/ClovisAndRagnachar1.txt")   

    scene scroll

    $ yr = "484-12-05"
    $ loc = "Wlencing's Dungeon"

    "[chapOne1Zero]"

    hide screen asWeProceed
    
    menu:
        "A Mounted Noble of King Lucius Artorius Castus Pendragon's Round Table.":
            jump soldierBoy

        "Deckard, one of the Welsh whom your brother was hunting down in the Wildwood.":
            jump welshMan

    label soldierBoy:

        $ deckardCover = 0
        show screen asWeProceed

        "[chapOne1One]"
        "[ChapOne1Two]"
        "[ChapOne1Three]"
        $ loc = "Wildwood"
        "[ChapOne1Four]"
        "[ChapOne1Five]"   

        "[vision1]"
        
        "[ChapOne1Six]"
        $ loc = "The Channel"
        "[ChapOne1Seven]"
        "[ChapOne1Eight]"

        hide screen asWeProceed

        menu:
            "No, I'll take care of him.":
                jump deckVDruid1

            "I cannot stop you.":
                jump intermediarySeqOne

    label welshMan:

        $ deckardCover = 1
        show screen asWeProceed

        "[chapOne2One]"
        "[chapOne2Two]"
        "[chapOne2Three]"
        $ loc = "Wildwood"
        "[chapOne2Four]"
        "[chapOne2Five]"

        "[vision1]"
        
        jump intermediarySeqOne

    label deckVDruid1:

        $ deckardDruid = "DeckFight"
        show screen asWeProceed
        "[ChapOne1Nine]"
        $ loc = "Coast of Gaul"
        "[ChapOne1Ten]"
        jump intermediarySeqOne


    label intermediarySeqOne:

        $ primChar = "Zeno the Isaurian"
        $ yr = "484-12-06"
        $ loc = "Constantinople"
        "[zenoAndRomulus]"
        $ primChar = "Tristan"
        $ loc = "Camelot"
        "[tristanAndMordred]"
        $ primChar = "Raechelle"
        "[raechelleAndLucan]"
        $ primChar = "Wlencing"
        $ loc = "South Saxon Hold"
        "[wlencingAndFrederic]"
        $ primChar = "King Clovis"
        $ loc = "Tournai"
        "[clovisAndRagnachar]"

        jump seq2