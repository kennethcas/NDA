# if you have multiple love interests then dateA can be either duplicated or have conditionals added, but you must have only one each of the other labels.
    
label dateA:
    scene bg room
    show casey
    $ renpy.show_screen("date")
    $ renpy.pause ()
    
    
label datetalk:
    $ renpy.hide_screen("date")
    
    if (curdate == "Casey"):
        if (talkcount > 0):
            $ talkcount -= 1
            $ rand = renpy.random.randint(1, 3)
            
            if (rand == 1):
                c "It's such a nice day today. The sun is so bright. Good day to stay inside instead!"
            elif (rand == 2):
                c "I've got some movies we can watch, if you're interested. Let's see... Batman Begins... The Notebook... Ten Things I Hate About You...."
            else:
                c "Do you like my outfit? I know I didn't change clothes. That's not important right now."
            $ mood += 1
            
        else:
            c "Hey, I'm getting kind of bored. Can we do something else?"
        jump dateA
        
        
label dategift:
    $ renpy.hide_screen("giftdate")
    
    if (giftcount > 0):
        $ globals()[curgift] -= 1
        $ mood += 1
        $ giftcount -= 1
        
        if (curdate == "Casey"):
            c "Oh! Thank you, [pName], this is great!"
            jump dateA
            
    else:
        if (curdate == "Casey"):
            c "Hey, I'm getting kind of bored. Can we do something else?"
            jump dateA
            
            
label datephoto:
    $ renpy.hide_screen("date")
    
    if (photocount > 0):
        $ photocount -= 1
        $ mood += 1
        show whiteflash
        
        if (curdate == "Casey"):
            c "Hee hee. This'll make a great memory, don't you think?"
            jump dateA
            
    else:
        if (curdate == "Casey"):
            c "Hey, I'm getting kind of bored. Can we do something else?"
            jump dateA
            
            
label datekiss:
    $ renpy.hide_screen("date")
    
    if (curdate == "Casey"):
        show whiteflash
        "*MWAH!*"
        $ Alove += 60
        if (Ad8 == False):
            $ Ad8 = True
            $ d8total -= 1
        c "I had a great time today... Thank you for inviting me out."
        c "We should do this again sometime!"
        show loveupbig
        "Date Success! Relationship up."
        jump parkA
        
        
label dateexit:
    $ renpy.hide_screen("date")
        
    if (curdate == "Casey"):
        c "Oh, are you going? I guess we can try again another time."
        jump parkA
