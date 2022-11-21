init python:
    # this function very simply takes the value passed to it and stores it in the real name variable. its called by the name input button
    def name_func(newstring):
        store.pName = newstring

init:
    # this variable is exactly what its name suggests; the number of stat points you have left to distribute. used here in the name input screen and nowhere else
    default pointsleft = 15
    
screen nameinput():
    modal True
    add "UI/UI name base.png" xpos 0 ypos 0
    
    add "UI/UI name stats base.png" xpos 205 ypos 245
    add "UI/UI name label.png" xpos 355 ypos 175
    
    # this button shows a default name on screen, that when the cursor hovers over it allows you to delete and replace it with a new one. it has a maximum of 9 characters
    button:
        id "input_1"
        xpos 370
        ypos 185
        xysize (210,25)
        action NullAction()
        add Input(hover_color="#000000",size=28, color="#888888", default=pName, changed=name_func, length=9, button=renpy.get_widget("nameinput","input_1")) yalign 0.4
    
        
    text "Stats:" xpos 350 ypos 265 color "#000000" bold False size 30
    
    #  the following three chunks of code allow you to assign stat points to 3 different stats, showing you how many you have so far
    add "UI/UI name stats label.png" xpos 410 ypos 330
    text "Charm" xpos 320 ypos 330 color "#000000" bold True size 20
    text "[charm]" xpos 420 ypos 331 color "#000000" bold False size 20
    if (charm > 0):
        imagebutton auto "UI/UI name stats minus %s.png" action [SetVariable("charm", max(charm-1, 0)), SetVariable("pointsleft", min(pointsleft+1, 15))] xpos 457 ypos 336
    else:
        add "UI/UI name stats minus hover.png" xpos 457 ypos 336
    if (pointsleft > 0):
        imagebutton auto "UI/UI name stats plus %s.png" action [SetVariable("charm", min(charm+1, 15)), SetVariable("pointsleft", max(pointsleft-1, 0))] xpos 480 ypos 336
    else:
        add "UI/UI name stats plus hover.png" xpos 480 ypos 336
    
    add "UI/UI name stats label.png" xpos 410 ypos 390
    text "Intelligence" xpos 260 ypos 390 color "#000000" bold True size 20
    text "[intel]" xpos 420 ypos 391 color "#000000" bold False size 20
    if (intel > 0):
        imagebutton auto "UI/UI name stats minus %s.png" action [SetVariable("intel", max(intel-1, 0)), SetVariable("pointsleft", min(pointsleft+1, 15))] xpos 457 ypos 396
    else:
        add "UI/UI name stats minus hover.png" xpos 457 ypos 396
    if (pointsleft > 0):
        imagebutton auto "UI/UI name stats plus %s.png" action [SetVariable("intel", min(intel+1, 15)), SetVariable("pointsleft", max(pointsleft-1, 0))] xpos 480 ypos 396
    else:
        add "UI/UI name stats plus hover.png" xpos 480 ypos 396
    
    add "UI/UI name stats label.png" xpos 410 ypos 450
    text "Creativity" xpos 280 ypos 450 color "#000000" bold True size 20
    text "[create]" xpos 420 ypos 451 color "#000000" bold False size 20
    if (create > 0):
        imagebutton auto "UI/UI name stats minus %s.png" action [SetVariable("create", max(create-1, 0)), SetVariable("pointsleft", min(pointsleft+1, 15))] xpos 457 ypos 456
    else:
        add "UI/UI name stats minus hover.png" xpos 457 ypos 456
    if (pointsleft > 0):
        imagebutton auto "UI/UI name stats plus %s.png" action [SetVariable("create", min(create+1, 15)), SetVariable("pointsleft", max(pointsleft-1, 0))] xpos 480 ypos 456
    else:
        add "UI/UI name stats plus hover.png" xpos 480 ypos 456
    
        
    # this field shows you how many points you have left to spend
    add "UI/UI name stats total.png" xpos 295 ypos 510
    text "Points remaining" xpos 360 ypos 515 color "#000000" bold False size 18
    text "[pointsleft]" xpos 310 ypos 514 color "#000000" bold False size 20
    
    
    # this button closes the screen and goes to the games intro (information is already saved)
    imagebutton auto "UI/UI name submit %s.png" action [Hide("nameinput"), Jump("intro")] xpos 285 ypos 595
