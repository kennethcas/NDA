# a very simple label. this is just the main map. if you need multiple locations to travel between, you should add a label for each and copy + edit the townmap screen in custom_screens.
label map:
    scene bg map
    $ renpy.show_screen("townmap")
    $ renpy.pause ()
    
    
# this section contains the bedroom and all activities you can do in it
label bedroom:
    scene bg home
    $ renpy.show_screen("maphome")
    $ renpy.pause ()
    
    
label bedsleep:
    $ renpy.hide_screen("maphome")
    
    # if the player tries to sleep at the end of the game (default set to day 31), you can have them redirected to a bad ending.
    if (day > lastDay):
        "Sleeping now will end the game with no romance. Do you wish to do so?"
        menu:
            "Yes":
                jump badend
            "No":
                jump bedroom
                
    $ HP = maxHP
    $ day += 1
    
    show whiteflash
    "Day [day]."
    jump bedroom
    
    
# this label covers a stat  training option, currently allowing the player to make cookies to raise their charm. can be repurposed into studying, or any other stat training idea you have.
label bedstudy:
    if (HP >= 20):
        $ HP -= 20
        
        if (charm <= maxcharm - 5):
            $ charm += 5
        elif (charm < maxcharm):
            $ charm = maxcharm
        $ cookies += 1
        
    else:
        $ renpy.hide_screen("maphome")
        "You don't have enough HP for that!"
    jump bedroom
