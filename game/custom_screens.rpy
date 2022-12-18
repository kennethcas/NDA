#  LITTLE WINDOW IN THE TOP RIGHT THAT SHOWS YOUR HP, MONEY, DAY ETC
screen statusbar:
    zorder 1
    add "UI/UI mirror base.png" xpos 958 ypos 8

    text "Day:" xpos 994 ypos 80 color "#000000" bold True size 20
    text "[day]" xpos 1055 ypos 80 color "#000000" bold True size 20
    text "HP:" xpos 1000 ypos 103 color "#000000" bold True size 20
    text "[HP]" xpos 1050 ypos 103 color "#000000" bold True size 20
    text "$" xpos 1010 ypos 126 color "#000000" bold True size 20
    text "[gold]" xpos 1030 ypos 126 color "#000000" bold True size 20

    # these buttons open a custom menu and renpys preferences, respectively
    imagebutton auto "UI/UI mirror stats %s.png" action [Show("statsmenu"), Hide("statusbar")] xpos 1014 ypos 171
    imagebutton auto "UI/UI mirror gear %s.png" action ShowMenu("preferences") xpos 1048 ypos 32

    # this button takes the user back to their room, provided theyre not in a cutscene.
    if (canwarp == True):
        imagebutton auto "UI/UI mirror sleep %s.png" action Jump("bedroom") xpos 1002 ypos 32
    else:
        add "UI/UI mirror sleep idle.png" xpos 1002 ypos 32

    # this button takes the user right back to the main map, provided theyre not in a cutscene.
    if (canwarp == True):
        imagebutton auto "UI/UI mirror face %s.png" action Jump("map") xpos 1094 ypos 8


# this is a custom menu that shows your inventory, stats, and relationship points with the datable characters
screen statsmenu:
    # this background covers the entire screen, so you cant accidentally click somewhere and put a map on top of your menu
    add "UI/UI menu base.png" xpos 0 ypos 0

    # since the status bar is covered, we put that information back in
    text "Day:" xpos 994 ypos 80 color "#000000" bold True size 20
    text "[day]" xpos 1055 ypos 80 color "#000000" bold True size 20
    text "HP:" xpos 1000 ypos 103 color "#000000" bold True size 20
    text "[HP]" xpos 1050 ypos 103 color "#000000" bold True size 20
    text "$" xpos 1010 ypos 126 color "#000000" bold True size 20
    text "[gold]" xpos 1030 ypos 126 color "#000000" bold True size 20

    # write in your stats in the STATS section
    text "Charm:" xpos 686 ypos 80 color "#000000" bold True size 18
    text "[charm]" xpos 770 ypos 80 color "#000000" bold True size 18
    text "Intell:" xpos 695 ypos 110 color "#000000" bold True size 18
    text "[intel]" xpos 770 ypos 110 color "#000000" bold True size 18
    text "Creative:" xpos 665 ypos 140 color "#000000" bold True size 18
    text "[create]" xpos 770 ypos 140 color "#000000" bold True size 18

    # items!
    add "UI/UI menu cookie.png" xpos 123 ypos 80
    add "UI/UI menu label.png" xpos 130 ypos 175
    text "[cookies]" xpos 160 ypos 180 color "#000000" bold True size 16

    add "UI/UI menu game.png" xpos 123 ypos 240
    add "UI/UI menu label.png" xpos 130 ypos 335
    text "[games]" xpos 160 ypos 340 color "#000000" bold True size 16

    add "UI/UI menu bouquet.png" xpos 123 ypos 400
    add "UI/UI menu label.png" xpos 130 ypos 495
    text "[bouquets]" xpos 160 ypos 500 color "#000000" bold True size 16

    add "UI/UI menu bear.png" xpos 123 ypos 560
    add "UI/UI menu label.png" xpos 130 ypos 655
    text "[teddies]" xpos 160 ypos 660 color "#000000" bold True size 16

    # relationship section. shows a separate image obscuring face of date you havent met yet.
    if (Alove > 0):
        add "UI/UI menu date.png" xpos 825 ypos 290
    else:
        add "UI/UI menu date locked.png" xpos 825 ypos 290
    if (pointsonly == False):
        add "UI/UI menu label.png" xpos 860 ypos 431
        text "[Arel]" xpos 865 ypos 438 color "#000000" bold True size 12
    else:
        text "[Alove]" xpos 880 ypos 440 color "#000000" bold True size 16


    # this back button hides the menu
    imagebutton auto "UI/UI button back %s.png" action [Show("statusbar"), Hide("statsmenu")] xpos 8 ypos 615


#  MAP FOR NAVIGATING TO VARIOUS LOCATIONS
screen townmap:
    modal True
    # this tag ensures that only one map location can be seen at a time
    tag map

    # these are the buttons leading to the locations. the %s in the filename auto replaces with idle and hover. the Jump action will take you to the label indicated.
    imagebutton auto "UI/UI map home %s.png" action Jump("bedroom") xpos 235 ypos 165
    imagebutton auto "UI/UI map shop %s.png" action Jump("shop") xpos 490 ypos 65
    imagebutton auto "UI/UI map park %s.png" action Jump("park") xpos 635 ypos 325


#  LOCATION WHERE YOU CAN INTERACT WITH A DATE
screen mapchat:
    modal True
    # this tag ensures that only one map location can be seen at a time
    tag map


    #DISPLAYS NAME
    if soberBusinessmanScreen == True:
        text "SOBER BUSINESSMAN" xpos 70 ypos 35 color "#ffffff" bold True size 24 outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
    else:
        text "Firstname Lastname" xpos 70 ypos 35 color "#ffffff" bold True size 24 outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    # DRUNK SUS BARS -----------
    bar value drunk range pointsdrunk xpos 70 ypos 80 xsize 250 ysize 30
    bar value sus range pointssus xpos 70 ypos 120 xsize 250 ysize 30

    add "UI/DrunkBarIcon.png" xpos 7 ypos 45
    add "UI/SusBarIcon.png" xpos 7 ypos 80
    # text currel xpos 212 ypos 166 color "#ffffff" outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]

    # these buttons allow you to interact with your date
    imagebutton auto "UI/UI button talk %s.png" action Jump("chattalk") xpos 60 ypos 175
    imagebutton auto "UI/UI button gift %s.png" action Jump("chatgift") xpos 60 ypos 300
    imagebutton auto "UI/UI button date %s.png" action Jump("chatdate") xpos 60 ypos 425

    # this is a back button that will return to the previous location
    #imagebutton auto "UI/UI button back %s.png" action Jump("map") xpos 18 ypos 615


#  THE ACTUAL DATE SCREEN
screen date:
    modal True
    # this tag ensures that only one map location can be seen at a time
    tag map

    # this bar shows the date Mood, which needs to reach 5 in order to finish the date
    text "Mood" xpos 242 ypos 45 color "#ffffff" bold True size 20 outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
    bar value mood range maxmood xpos 190 ypos 70 xsize 177 ysize 24

    # the main actions of the date
    imagebutton auto "UI/UI button date talk %s.png" action Jump("datetalk") xpos 60 ypos 120
    imagebutton auto "UI/UI button date gift %s.png" action Show("giftdate") xpos 60 ypos 220
    imagebutton auto "UI/UI button date photo %s.png" action Jump("datephoto") xpos 60 ypos 320

    # kissing will end the date, but you can only do it if the mood is full
    if (mood == maxmood):
        imagebutton auto "UI/UI button date kiss %s.png" action Jump("datekiss") xpos 60 ypos 420
    else:
        add "UI/UI button date kiss locked.png" xpos 60 ypos 420

    # this back button takes you to a label that automates exiting the date, so you return to the screen you came from
    imagebutton auto "UI/UI button back %s.png" action Jump("dateexit") xpos 18 ypos 615


#  GIFT WINDOW FOR DATES
screen giftdate:
    modal True
    # so that you cant exit the room and keep the gift window up
    tag map

    # the background of the gift window
    add "UI/UI gift base.png" xpos 890 ypos 275

    # labels for the available items
    add "UI/UI gift label.png" xpos 918 ypos 347
    text "[cookies]" xpos 935 ypos 350 color "#000000" bold True size 10
    add "UI/UI gift label.png" xpos 1009 ypos 347
    text "[games]" xpos 1026 ypos 350 color "#000000" bold True size 10
    add "UI/UI gift label.png" xpos 918 ypos 445
    text "[bouquets]" xpos 935 ypos 448 color "#000000" bold True size 10
    add "UI/UI gift label.png" xpos 1008 ypos 445
    text "[teddies]" xpos 1026 ypos 448 color "#000000" bold True size 10

    # shows a button for each gift, or a greyed out image if none are available
    if (cookies > 0):
        imagebutton auto "UI/UI gift cookie %s.png" action [SetVariable("curgift", "cookies"), Jump("dategift")] xpos 908 ypos 283
    else:
        add "UI/UI gift cookie locked.png" xpos 908 ypos 283
    if (games > 0):
        imagebutton auto "UI/UI gift game %s.png" action [SetVariable("curgift", "games"), Jump("dategift")] xpos 999 ypos 283
    else:
        add "UI/UI gift game locked.png" xpos 999 ypos 283
    if (bouquets > 0):
        imagebutton auto "UI/UI gift bouquet %s.png" action [SetVariable("curgift", "bouquets"), Jump("dategift")] xpos 908 ypos 378
    else:
        add "UI/UI gift bouquet locked.png" xpos 908 ypos 378
    if (teddies > 0):
        imagebutton auto "UI/UI gift bear %s.png" action [SetVariable("curgift", "teddies"), Jump("dategift")] xpos 999 ypos 378
    else:
        add "UI/UI gift bear locked.png" xpos 999 ypos 378

    # back button closes the gift window
    imagebutton auto "UI/UI button back %s.png" action Show("date") xpos 18 ypos 615


#  GIFT WINDOW FOR NORMAL INTERACTIONS
screen chatgift:
    modal True
    # so that you cant exit the room and keep the gift window up
    tag map

    # the background of the gift window
    add "UI/UI gift base.png" xpos 890 ypos 275

    # labels for the available items
    add "UI/UI gift label.png" xpos 918 ypos 347
    text "[cookies]" xpos 935 ypos 350 color "#000000" bold True size 10
    add "UI/UI gift label.png" xpos 1009 ypos 347
    text "[games]" xpos 1026 ypos 350 color "#000000" bold True size 10
    add "UI/UI gift label.png" xpos 918 ypos 445
    text "[bouquets]" xpos 935 ypos 448 color "#000000" bold True size 10
    add "UI/UI gift label.png" xpos 1008 ypos 445
    text "[teddies]" xpos 1026 ypos 448 color "#000000" bold True size 10

    # shows a button for each gift, or a greyed out image if none are available
    if (cookies > 0):
        imagebutton auto "UI/UI gift cookie %s.png" action [SetVariable("curgift", "cookies"), Jump("chatgift")] xpos 908 ypos 283
    else:
        add "UI/UI gift cookie locked.png" xpos 908 ypos 283
    if (games > 0):
        imagebutton auto "UI/UI gift game %s.png" action [SetVariable("curgift", "games"), Jump("chatgift")] xpos 999 ypos 283
    else:
        add "UI/UI gift game locked.png" xpos 999 ypos 283
    if (bouquets > 0):
        imagebutton auto "UI/UI gift bouquet %s.png" action [SetVariable("curgift", "bouquets"), Jump("chatgift")] xpos 908 ypos 378
    else:
        add "UI/UI gift bouquet locked.png" xpos 908 ypos 378
    if (teddies > 0):
        imagebutton auto "UI/UI gift bear %s.png" action [SetVariable("curgift", "teddies"), Jump("chatgift")] xpos 999 ypos 378
    else:
        add "UI/UI gift bear locked.png" xpos 999 ypos 378

    # back button closes the gift window
    imagebutton auto "UI/UI button back %s.png" action Show("mapchat") xpos 18 ypos 615


#  MAP LOCATION (BUY ITEMS OR WORK FOR MONEY)
screen mapshop:
    modal True
    # this tag ensures that only one map location can be seen at a time
    tag map

    # these buttons allow you to talk to the shopkeep and work, which trades HP for money. work sets the HP cost and pay into variables to be used in shopwork.
    imagebutton auto "UI/UI button talk %s.png" action Jump("shoptalk") xpos 485 ypos 100
    imagebutton auto "UI/UI button work %s.png" action [SetVariable("workHP", 20), SetVariable("workpay", 15 + charm), Jump("shopwork")] xpos 485 ypos 218

    # these buttons are for the purchasable items. they set the "curgift" and price variables that will be used in shopbuy.
    imagebutton auto "UI/UI shop game %s.png" action [SetVariable("curgift", "games"), SetVariable("giftprice", 20), Jump("shopbuy")] xpos 918 ypos 295
    imagebutton auto "UI/UI shop bouquet %s.png" action [SetVariable("curgift", "bouquets"), SetVariable("giftprice", 15), Jump("shopbuy")] xpos 918 ypos 475
    imagebutton auto "UI/UI shop bear %s.png" action [SetVariable("curgift", "teddies"), SetVariable("giftprice", 10), Jump("shopbuy")] xpos 918 ypos 610

    # this is a back button that will return to the previous location
    imagebutton auto "UI/UI button back %s.png" action Jump("map") xpos 15 ypos 15


#  HOME LOCATION (RESTORES HP AND TRAINS SKILLS)
screen maphome:
    modal True
    # this tag ensures that only one map location can be seen at a time
    tag map

    # this is the bed, which jumps to a label that will restore HP and progress to the next day.
    imagebutton auto "UI/UI home bed %s.png" action Jump("bedsleep") xpos 15 ypos 355

    # this button jumps to a label that will lower HP and raise a skill; a training function. the default one also gives an item.
    imagebutton auto "UI/UI home study %s.png" action Jump("bedstudy") xpos 870 ypos 340

    # this is a back button that will return to the previous location
    imagebutton auto "UI/UI button back %s.png" action Jump("map") xpos 15 ypos 15


    if (usegallery == True):
        # this image is the background for the mini-gallery, which displays photos taken on dates. none of this will show if usegallery is False
        add "UI/UI home photos base.png" xpos 481 ypos 71

        add cork.make_button("A", "UI/UI home photos 1 idle.png", "UI/UI home photos 1 locked.png", "UI/UI home photos 1 hover.png", None, None, xpos=515, ypos=95)
        add cork.make_button("B", "UI/UI home photos 1 idle.png", "UI/UI home photos 1 locked.png", "UI/UI home photos 1 hover.png", None, None, xpos=585, ypos=95)
        add cork.make_button("C", "UI/UI home photos 1 idle.png", "UI/UI home photos 1 locked.png", "UI/UI home photos 1 hover.png", None, None, xpos=655, ypos=95)
        add cork.make_button("D", "UI/UI home photos 1 idle.png", "UI/UI home photos 1 locked.png", "UI/UI home photos 1 hover.png", None, None, xpos=725, ypos=95)
        add cork.make_button("E", "UI/UI home photos 1 idle.png", "UI/UI home photos 1 locked.png", "UI/UI home photos 1 hover.png", None, None, xpos=515, ypos=175)
        add cork.make_button("F", "UI/UI home photos 1 idle.png", "UI/UI home photos 1 locked.png", "UI/UI home photos 1 hover.png", None, None, xpos=585, ypos=175)
        add cork.make_button("G", "UI/UI home photos 1 idle.png", "UI/UI home photos 1 locked.png", "UI/UI home photos 1 hover.png", None, None, xpos=655, ypos=175)
        add cork.make_button("H", "UI/UI home photos 1 idle.png", "UI/UI home photos 1 locked.png", "UI/UI home photos 1 hover.png", None, None, xpos=725, ypos=175)

        # these 'pins' are just single dots representing how many gallery photos you havent unlocked yet. this can be removed if desired
        if (d8total > 0):
            add "UI/UI home photos pin.png" xpos 787 ypos 263
        if (d8total > 1):
            add "UI/UI home photos pin.png" xpos 779 ypos 263
        if (d8total > 2):
            add "UI/UI home photos pin.png" xpos 771 ypos 263
        if (d8total > 3):
            add "UI/UI home photos pin.png" xpos 763 ypos 263
        if (d8total > 4):
            add "UI/UI home photos pin.png" xpos 787 ypos 256
        if (d8total > 5):
            add "UI/UI home photos pin.png" xpos 779 ypos 256
        if (d8total > 6):
            add "UI/UI home photos pin.png" xpos 771 ypos 256
        if (d8total > 7):
            add "UI/UI home photos pin.png" xpos 763 ypos 256
