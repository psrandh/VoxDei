label seq2:
    $ chapTwo1One = getPage("text/Sequence02/chap2.1.1.txt")
    $ chapTwo1Two = getPage("text/Sequence02/chap2.1.2.txt")
    $ chapTwo1Three = getPage("text/Sequence02/chap2.1.3.txt")

    $ leodegranceCapture = getPage("text/Sequence02/LeodegranceCapture.txt")

    $ primChar = "Deckard"
    $ yr = "484-12-07"

    if (deckardCover == 0) and (deckardChivalry == 1):
        jump routeOne

    label routeOne:
        "[chapTwo1One]"
        "[chapTwo1Two]"
        "[chapTwo1Three]"

    label intermediarySeqTwo:
        "[leodegranceCapture]"

    jump fin