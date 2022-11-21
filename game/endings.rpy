# this label will check your relationship with the character attached to it, and then play one of three endings. adjust the logic however you like.
label endA:
    $ canwarp = False
    
    ## add any dialogue that should be seen regardless of your relationship with the character
    
    if (Arel == "Stranger"):
        
        ## add your "bad ending" dialogue here
        
        scene white with dissolve
        
        "You got Casey's Bad Ending! Maybe you should have gotten a little bit closer."
        "That's all for now. Have fun making games!"
        
    elif (Arel != "Soulmate"):
        
        ## add your "neutral ending" dialogue here
        
        scene white with dissolve
        
        "You got Casey's Neutral Ending! Good going! But you can do a little better than that."
        "That's all for now. Have fun making games!"
        
    else:
        
        ## add your "good ending" dialogue here
        
        scene white with dissolve
        
        "You got Casey's Good Ending! Congrats!"
        "That's all for now. Have fun making games!"

    $ MainMenu(confirm=False)()
    
label badend:
    $ canwarp = False
    $ renpy.hide_screen("maphome")
    scene white with dissolve
    
    "You sleep away the days, and slowly the game fades to a close."
    "You got the worst ending! Great going!"
    "That's all for now. Have fun making games!"
    $ MainMenu(confirm=False)()
