# each location is designed to hold one love interest, so "park" and "parkA" should be duplicated or edited to fit your own needs.
# hi hihihi
label vincentMinigame:
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
    $ turns += 1
    $ talkTurns += 1

<<<<<<< HEAD
    show side mc at midleft onlayer mcsprite
=======
        show side mc at left onlayer mcsprite
>>>>>>> 77db540c9f448f6631f4e672e6392a45693316a7

        if (turns == 1):
            "Clients knowing personal information…is never a good thing."

            "Especially when its someone like {i}him.{/i} The last thing I
                need right now is someone more powerful than even the richest,
                sleaziest Wall Street bankers on my tail right now."

            "If I play my cards right—nudge them in the right direction while
                telling him what he wants to hear—I can make him fold easy."
            qb "Your real name…is Sachi Kaur, is it not?"

            menu:
                "Yes.":

                    qb "good answer"

                "You have the wrong girl.":
                    qb "bad answer"
                "Why?"
                    qb ""
        elif (talkTurns == 2):
            menu:
                "What do you want from me?":
                    qb "good answer"

                "How do you know who I am?":
                    qb "bad answer"

        elif (talkTurns == 3):
            menu:
                "How do you know my father?":

                    qb "good answer"

                "Why me?":
                    qb "bad answer"
                "What kind of help do you need?":
        elif (talkTurns == 4):
            menu:
                "You have no proof.":

                    qb "good answer"

                "Why me?":
                    qb "bad answer"
                "What kind of help do you need?":

        else:
            jump n1_part2

        hide side mc onlayer mcsprite

label vincentEvidence1:
label vincentEvidence2:
label vincentEvidence3:
label vincentEvidence4A:
label vincentEvidence4B:
label vincentEvidence5A:
label vincentEnd:


label chatgift:
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    if (HP >= 10):
        $ HP -= 10

        show side mc at midleft onlayer mcsprite
        s "T1"
        s "T2"
        "We drink."
        $ drunk += 10
        # 'loveup' is a small animation that shows the player theyve made a good choice.
        show loveup

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
