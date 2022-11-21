# Define your characters here.
init:
    $ pName = "Alexis"
    
    define c = Character("Casey")
    define m = Character("[pName]")
    

    
    ## you can use this custom layer and position to show mc's image on top of all text as well as during choices, or just ignore it and use a normal side image.
    #   show side mc onlayer mcsprite at midleft
    #   hide side mc onlayer mcsprite

label start:
    $ renpy.show_screen("nameinput")
    
label intro:
    # this populates the mini-gallery feature with images, if you don't intend to use it, just set "usegallery" to False.
    $ usegallery = True
    call makegal from _call_makegal
    
    
    ## Place your own intro here and delete the 'pause'!
    pause
    
    
    # if you dont want the player to have a quick-button that takes them home or to the main map from wherever they are, set this to False instead.
    # if you do want that, leave it -- but make sure to toggle it off/on before and after cutscenes so the player cant accidentally teleport out of dialogue.
    $ canwarp = True
    
    # leave these!
    $ renpy.show_screen("statusbar")
    jump map
