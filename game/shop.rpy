# shop! if you need multiple shops, you can either duplicate these labels or add a variable to determine which information is shown. be sure to do the same for mapshop in custom_screens.
label shop:
    scene bg shop
    $ renpy.show_screen("mapshop")
    $ renpy.pause ()

label shoptalk:
    $ renpy.hide_screen("mapshop")
    
    # by default this just recites one of 3 random dialogue snippets, but feel free to expand or replace with your own shopkeep's dialogue.
    
    $ rand = renpy.random.randint(1, 3)
    if (rand == 1):
        c "You'll make a bit more money if you're a little more charismatic."
    elif (rand == 2):
        c "We could use more help around the shop, I guess."
    else:
        c "Hey! Are you gonna buy something, or what?"
    jump shop
    
# workHP and workpay are set in the mapshop screen. if you want to have multiple jobs in one location, you should set them up there -- this label can be used for any/all.
label shopwork:
    if (HP >= workHP):
        $ HP -= workHP
        $ gold += workpay
    else:
        $ renpy.hide_screen("mapshop")
        "You don't have enough HP for that!"
    jump shop
    
# giftprice and curgift are set in the mapshop screen, and store the item you clicked on and its price.
label shopbuy:
    if (gold >= giftprice):
        $ gold -= giftprice
        $ globals()[curgift] += 1
    else:
        $ renpy.hide_screen("mapshop")
        "You can't afford that!"
    jump shop
