# each location is designed to hold one love interest, so "park" and "parkA" should be duplicated or edited to fit your own needs.

label park:
    scene bg park
    show casey

    # this checks if youre at the end of the game (by default set to day 31), and sends you to the ending with the specified character.
    if (day > lastDay):
        $ renpy.hide_screen("townmap")
        "End game with Casey?"
        menu:
            "Yes":
                jump endA
            "No":
                jump map

    call relAcheck from _call_relAcheck
    jump parkA


# this is separate from park so that the relationship upgrade scene doesnt replay when it shouldnt.
label parkA:
    scene bg park
    show casey

    # reset date tallies to default in case we end up going on one
    $ mood = 0
    $ talkcount = talkcountmax
    $ giftcount = giftcountmax
    $ photocount = photocountmax

    # these calculations determine the date variables. curbar uses the relationship status to determine progress to next date, assuming it takes 100 points to reach each stage.
    $ curdate = "Casey"
    $ currel = Arel

    if (currel == "Stranger"):
        $ curnext = pointsfriend
        $ curbar = min(Alove, pointsfriend)
    if (currel == "Friend"):
        $ curnext = pointslove - pointsfriend
        $ curbar = min(Alove - pointsfriend, pointslove - pointsfriend)
    if (currel == "Lover"):
        $ curnext = pointssoul - pointslove
        $ curbar = min(Alove - pointslove, pointssoul - pointslove)
    if (currel == "Soulmate"):
        $ curnext = 100
        $ curbar = 100

    $ renpy.show_screen("mapchat")
    $ renpy.pause ()


# a simple little label that will handle the relationship upgrades when youre close enough. each LI should have their own version of this label.
label relAcheck:
    $ canwarp = False
    $ renpy.hide_screen("townmap")
    if (Alove >= pointsfriend) and (Arel == "Stranger"):
        $ Arel = "Friend"

        # put your own dialogue here

        "You are now 'Friends' with Casey. You can now give her gifts."

    if (Alove >= pointslove) and (Arel == "Friend"):
        $ Arel = "Lover"

        # put your own dialogue here

        "You are now dating Casey! You can now go on dates."

    if (Alove >= pointssoul) and (Arel == "Lover"):
        $ Arel = "Soulmate"

        # put your own dialogue here

        "You and Casey are now soulmates. Stick around until day 31 to get a special ending with her!"

    $ canwarp = True
    return


# if you have multiple love interests you can add an "if (curdate == ??)" to this label too, but if you have a lot of potential dialogue itll likely be more efficient to put each character in a new label and use this to jump to the right one.
label chattalk:
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    if (HP >= 10):
        $ HP -= 10

        show side mc at midleft onlayer mcsprite

        if (Trust == 0):
            s "T1"
            s "T2"

            menu:
                "DIALOGUE CHOICE 1":

                    # 'loveup' is a small animation that shows the player theyve made a good choice.
                    $ Trust += 1
                    show loveup

                    c "good answer"

                "DIALOGUE CHOICE 1":
                    c "bad answer"
        elif (Trust == 1):
            menu:
                "DIALOGUE CHOICE 1":

                    c "good answer"
                    $ Trust += 1
                    show loveup

                "DIALOGUE CHOICE 1":
                    c "bad answer"
        elif (Trust == 2):
            menu:
                "DIALOGUE CHOICE 1":

                    c "good answer"
                    $ Trust += 1
                    show loveup

                "DIALOGUE CHOICE 1":
                    c "bad answer"
        else:
            jump n1_part2

        hide side mc onlayer mcsprite


    else:
        "You don't have enough HP for that!"
    $ canwarp = True
    jump parkA


label chatgift:
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    if (HP >= 10):
        $ HP -= 10

        show side mc at midleft onlayer mcsprite
        s "T1"
        s "T2"
        "We drink."
        $ Alove += 10

        hide side mc onlayer mcsprite


    else:
        "You don't have enough HP for that!"
    $ canwarp = True
    jump parkA



label chatdate:
    $ renpy.hide_screen("mapchat")
    if (currel == "Stranger") or (currel == "Friend"):

        if (curdate == "Casey"):
            c "Um... Sorry, I don't think today is a good day."
            jump parkA

    else:
        if (HP >= 50):
            $ HP -= 50

            if (curdate == "Casey"):
                c "H-Huh? You really want to? Great! Let's head out, then."
                jump dateA

        else:
            "You don't have enough HP for that!"
            jump parkA