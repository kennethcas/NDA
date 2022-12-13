label vincent_minigame:
    scene bg private room
    show casey
    $ renpy.show_screen("mapchat")
    $ renpy.pause ()
    $ drunk = pointsdrunk
    $ sus = pointssus

label points_check:
    if (turns <= 5 and drunk < 100 and sus < 100):
        #add other minigames
        jump vincent_minigame
    elif (drunk >= 100):
        jump drunk_full
    elif (sus >= 100):
        jump sus_full
    elif (turns > 5):
        jump n1_part2

label chattalk:
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    $ turns += 1
    $ talk_turns += 1

    show side mc at left onlayer mcsprite

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
            "Why?":
                qb "."
    elif (talk_turns == 2):
        menu:
            "What do you want from me?":
                qb "good answer"

            "How do you know who I am?":
                qb "bad answer"

    elif (talk_turns == 3):
        menu:
            "How do you know my father?":

                qb "good answer"

            "Why me?":
                qb "bad answer"
            "What kind of help do you need?":
                ""
    elif (talk_turns == 4):
        menu:
            "You have no proof.":
                qb "good answer"

            "Why me?":
                qb "bad answer"
            "What kind of help do you need?":
                "."

    else:
        jump points_check

        hide side mc onlayer mcsprite

label vincentEvidence1:
    $ v1_ev_1 = True;
    jump points_check
label vincentEvidence2:
    $ v1_ev_2 = True;
    jump points_check

label vincentEvidence3:
    $ v1_ev_3 = True;
    jump points_check

label vincentEvidence4A:
    $ v1_ev_4a = True;
    jump points_check

label vincentEvidence4B:
    $ v1_ev_4b = True;
    jump points_check

label vincentEvidence5A:
    $ v1_ev_5a = True;
    jump points_check

label vincentEnd:
    $ v1_ev_5b = True;
    jump points_check

label chatgift:
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    $ turns += 1
    $ drink_turns += 1

    show side mc at left onlayer mcsprite
    s "T1"
    s "T2"
    "We drink."

    $ drunk += 25
    hide side mc onlayer mcsprite
    $ canwarp = True

    jump points_check



label chatdate:
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    $ turns += 1
    $ flirt_turns += 1

    if (flirt_turns < 2):
        show side mc at left onlayer mcsprite
        s "T1"
        s "T2"
        "We drink."
        $ sus -= 2
        hide side mc onlayer mcsprite
    if (flirt_turns > 2):
        "."
        "."

    $ canwarp = True

    jump points_check

label drunk_full:
    s "please work please please please"
    jump vincent_minigame

label sus_full:
    return
