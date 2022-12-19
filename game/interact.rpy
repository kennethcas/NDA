#init python:
#    def hideIcons():
#        hide vincent mask icon at left onlayer mcsprite
#        hide sachi mask icon at left onlayer mcsprite

#SETTING SOME BOOLS AND VARIABLES---------------------------
#$ hideIcons:


#if hideIcons: #HIDES ALL PORTRAITS
 #   hide vincent mask icon at left onlayer mcsprite
  #  hide sachi mask icon at left onlayer mcsprite
$ client = 0
$ just_talked = False
$ showSachiMask = False
if showSachiMask:
    hide vincent mask icon at left onlayer mcsprite
    show sachi mask icon at left onlayer mcsprite
    $ hideIcons == False
else:
    hide sachi mask icon at left onlayer mcsprite

$ showVincentMask = False
if showVincentMask:
    hide sachi mask icon at left onlayer mcsprite
    show vincent mask icon at left onlayer mcsprite
    $ hideIcons == False
else:
    hide vincent mask icon at left onlayer mcsprite


#START MINIGAME ------------------------------------
label vincent_minigame:
    scene bg private room
    show vincent fullbody masked

    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    #VARIABLE FOR CHECKING WHAT NAME TO PRINT ON SCREEN
    $ name = "SOBER BUSINESSMAN"
    $ client = 1

    $ renpy.show_screen("mapchat")
    $ renpy.pause ()
    $ drunk = pointsdrunk
    $ sus = pointssus

#SET DRUNK/SUS TO 0 BEFORE MINIGAMES START

label gerard_minigame:
    scene bg private room
    #show GERARD FULLBODY SPRITE

    #hide GERARD icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    #VARIABLE FOR CHECKING WHAT NAME TO PRINT ON SCREEN
    $ name = "GERARD WADE"
    $ client = 2

    $ renpy.show_screen("mapchat")
    $ renpy.pause ()
    $ drunk = pointsdrunk
    $ sus = pointssus

label richard_minigame:
    scene bg private room
    #show RICHARD FULLBODY SPRITE

    #hide RICHARD icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    #VARIABLE FOR CHECKING WHAT NAME TO PRINT ON SCREEN
    $ name = "RICHARD BLOOMBERG"
    $ client = 3

    $ renpy.show_screen("mapchat")
    $ renpy.pause ()
    $ drunk = pointsdrunk
    $ sus = pointssus

label malcolm_minigame:
    scene bg private room
    #show MALCOLM FULLBODY SPRITE

    #hide MALCOLM icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    #VARIABLE FOR CHECKING WHAT NAME TO PRINT ON SCREEN
    $ soberBusinessmanScreen = False
    $ name = "MALCOLM HUNT"
    $ client = 4

    $ renpy.show_screen("mapchat")
    $ renpy.pause ()
    $ drunk = pointsdrunk
    $ sus = pointssus

label vincent_points_check:
    $ just_talked = False
    if (turns <= 5 and drunk < 80 and sus < 60):
        jump vincent_minigame
    elif (drunk >= 80):
        jump drunk_full
    elif (sus >= 60):
        jump sus_full
    elif (turns > 5):
        jump n1_part2

label gerard_points_check:
    $ just_talked = False
    if (turns <= 5 and drunk < 80 and sus < 60):
        jump gerard_minigame
    elif (drunk >= 80):
        jump drunk_full
    elif (sus >= 60):
        jump sus_full
    elif (turns > 5):
        jump n1_part2

label chattalk:
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    $ turns += 1
    $ talk_turns += 1
    $ just_talked = True

    if (drunk <= 20):
        $ sus += 20
    elif (drunk > 20 and <= 40):
        $ sus += 15
    elif (drunk > 40 and <= 80):
        $ sus += 10
    else:
        $ sus += 5
    if (client == 1):
        show vincent fullbody masked
        stop music fadeout 1.0
        play music caravan loop fadein 1.0

        hide vincent mask icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite

        if (talk_turns == 1):
            show sachi mask icon at left onlayer mcsprite

            "Clients knowing personal information…is never a good thing."

            "Especially when its someone like {i}him.{/i} The last thing I
                need right now is someone more powerful than even the richest,
                sleaziest Wall Street bankers on my tail right now."

            "If I play my cards right—nudge them in the right direction while
                telling him what he wants to hear—I can make him fold easy."

            hide sachi mask icon at left onlayer mcsprite

            show vincent mask icon at left onlayer mcsprite
            qb "Your real name…is Sachi Kaur, is it not?"
            hide vincent mask icon at left onlayer mcsprite

            show sachi mask icon at left onlayer mcsprite
            menu:
                "Yes.":
                    jump vincent_ev_1
                "You have the wrong girl.":
                    jump vincent_ev_2
                "Why?":
                    jump vincent_ev_3

        elif (talk_turns == 2):
            show sachi mask icon at left onlayer mcsprite
            menu:
                "What do you want from me?":
                    if (v1_ev_1 == True):
                        jump vincent_ev_3
                    if (v1_ev_2 == True):
                        jump vincent_ev_3
                    if (v1_ev_3 == True):
                        jump vincent_ev_1

                "How do you know who I am?":
                    if (v1_ev_1 == True):
                        jump vincent_ev_2
                    if (v1_ev_2 == True):
                        jump vincent_ev_1
                    if (v1_ev_3 == True):
                        jump vincent_ev_1

        elif (talk_turns == 3):
            show sachi mask icon at left onlayer mcsprite
            menu:
                "How do you know my father?" if v1_ev_1 == True:
                    jump vincent_ev_4a

                "Why me?" if v1_ev_2 == True:
                    jump vincent_ev_5a

                "What kind of {i}help{/i} do you need?" if v1_ev_3 == True:
                    jump vincent_1_end

        elif (talk_turns == 4):
            show sachi mask icon at left onlayer mcsprite
            menu:
                "How long have you been working at Carmine?" if v1_ev_4a == True:
                    jump vincent_ev_4b

                "You have no proof." if v1_ev_5a == True:
                    jump vincent_ev_5b

                "What kind of {i}help{/i} do you need?":
                    jump vincent_1_end

        elif (talk_turns == 5):
            show sachi mask icon at left onlayer mcsprite
            menu:
                "How long have you been working at Carmine?" if v1_ev_4a == True:
                    jump vincent_ev_4b

                "You have no proof." if v1_ev_5a == True:
                    jump vincent_ev_5b

                "What kind of {i}help{/i} do you need?":
                    jump vincent_1_end

        hide sachi mask icon at left onlayer mcsprite
    if (client == 2):
                #show gerard fullbody
                stop music fadeout 1.0
                play music caravan loop fadein 1.0

                if (talk_turns == 1):
                    show sachi mask icon at left onlayer mcsprite
                    menu:
                        "How’s work?":
                            jump gerard_ev_1
                        "How long have you worked at Carmine?":
                            jump gerard_ev_2
                        "You seem like a bigshot.":
                            jump gerard_ev_3

                elif (talk_turns == 2):
                    show sachi mask icon at left onlayer mcsprite
                    menu:
                        "How long have you worked at Carmine?" if (g_ev_2 == False or g_ev_3 == True):
                            if (g_ev_3 == True):
                                jump gerard_ev_3b
                            elif (g_ev_3 == False and g_ev_2 == True):
                                jump gerard_ev_2
                        "Why don't you like work?" if (g_ev_1 == True):
                            jump gerard_ev_4
                        "Who's Gwen?":
                            jump gerard_ev_5



                elif (talk_turns >= 3):
                    show sachi mask icon at left onlayer mcsprite
                    menu:
                        "Who's Gwen?" if g_ev_5 == False:
                            jump gerard_ev_5

                        "(Ask about Gwen.)" if g_ev_5 == True:
                            jump gerard_ev_6

                        "(Ask about dirty money.)" if g_ev_4 == True:
                            jump gerard_ev_7

                        "Why don't you like work?" if (g_ev_4 == False and g_ev_1 == True):
                            jump gerard_ev_4
                hide sachi mask icon at left onlayer mcsprite

    if (client == 3):
        "."
    if (client == 4):
        "."


label vincent_ev_1:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ v1_ev_1 = True;

    show sachi mask icon at left onlayer mcsprite
    s "…How did you know my name?"
    hide sachi mask icon at left onlayer mcsprite

    show vincent mask icon at left onlayer mcsprite
    qb "I’ve been looking for you. You’re {color=#6b091b}Rahul Kaur{/color}’s daughter."
    qb "…I wonder what he’d think now of your…er…profession. And {color=#6b091b}exploits{/color}, for that matter…"
    hide vincent mask icon at left onlayer mcsprite
    show sachi mask icon at left onlayer mcsprite
    s "…Well isn’t {i}he{/i} a delight."
    hide sachi mask icon at left onlayer mcsprite

    jump vincent_points_check

label vincent_ev_2:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ v1_ev_2 = True;
    #$ sus += 20
    if (talk_turns <= 1):
        "{i}He shakes his head."

    show vincent mask icon at left onlayer mcsprite
    qb "…I’ve been hearing lots of back alley talk about mysterious maxed out
        credit cards, incriminating pictures mailed to wives and kids..."
    qb "...thousands of dollars of jewelry mysteriously going missing…"

    hide vincent mask icon at left onlayer mcsprite
    show sachi mask icon at left onlayer mcsprite
    s "I’m surprised someone of your…{i}esteemed status{/i} keeps up with
        {i}back-alley talk{/i}."

    hide sachi mask icon at left onlayer mcsprite
    show vincent mask icon at left onlayer mcsprite

    qb "My…{i}esteemed status{/i}?"

    hide vincent mask icon at left onlayer mcsprite
    show sachi mask icon at left onlayer mcsprite

    s "…Your mask."
    s "The only clients who wear masks are people in the public eye. For
        uh…pretty obvious reasons. Not getting caught by the press and all…"

    hide sachi mask icon at left onlayer mcsprite
    show vincent mask icon at left onlayer mcsprite

    qb "…Well, I have my sources."

    hide vincent mask icon at left onlayer mcsprite
    jump vincent_points_check

label vincent_ev_3:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    $ v1_ev_3 = True;
    #$ sus += 20

    show vincent mask icon at left onlayer mcsprite
    qb "I need your help."

    hide vincent mask icon at left onlayer mcsprite
    show sachi mask icon at left onlayer mcsprite

    s "My…{i}help{/i}?"

    hide sachi mask icon at left onlayer mcsprite
    jump vincent_points_check

label vincent_ev_4a:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    $ v1_ev_4a = True;
    #$ sus += 20

    show vincent mask icon at left onlayer mcsprite
    qb "..."
    qb "...He used to work under me. To an extent."
    hide vincent mask icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    s "…"
    "{i}So he used to work at Carmine. A white-collar investment firm that I’m all
    too familiar with."
    "{i}No, scratch that…he’s a bigwig at Carmine."
    hide sachi mask icon at left onlayer mcsprite

    jump vincent_points_check

label vincent_ev_4b:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    $ v1_ev_4b = True;
    #$ sus += 20

    show vincent mask icon at left onlayer mcsprite
    qb "…Around {color=#6b091b}five years{/color} now."
    hide vincent mask icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    "{i}Five years? That’s way too soon for such a big promotion…"
    s "You’re…Antony Carmine’s son."
    hide sachi mask icon at left onlayer mcsprite

    show vincent mask icon at left onlayer mcsprite
    qb "…"

    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    jump vincent_points_check

label vincent_ev_5a:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    $ v1_ev_5a = True;
    #$ sus += 20

    show vincent mask icon at left onlayer mcsprite
    qb "Those who have been scammed, blackmailed, and otherwise victimized
        in some shape and form all had one thing in common."
    qb "…They visited The Scarlet Cabaret on a
        {color=#6b091b}Friday night{/color} after {color=#6b091b}June 1985{/color}."
    qb "Currently, there are {color=#6b091b}ten women{/color} who work on
        Fridays. Each of you wear a different {color=#6b091b}animal
        mask{/color}, correct?"
    qb "Coincidentally, my…{i}sources{/i} began to report seeing a
        {color=#6b091b}girl with a cat mask{/color} around that time."
    hide vincent mask icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    s "..."
    hide sachi mask icon at left onlayer mcsprite

    jump vincent_points_check

label vincent_ev_5b:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    $ v1_ev_5b = True;
    #$ sus += 20

    show vincent mask icon at left onlayer mcsprite
    qb "Believe me. If I wanted you behind bars, I could easily find a way."
    qb "…I think we could be useful to one another."
    hide vincent mask icon at left onlayer mcsprite

    jump vincent_points_check

label vincent_1_end:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    $ v1_end = True;

    show vincent mask icon at left onlayer mcsprite
    qb "..."
    qb "...Revenge."
    hide vincent mask icon at left onlayer mcsprite

    jump vincent_points_check

label gerard_ev_1:
    #hide gerard icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ g_ev_1 = True;

    #show gerard icon at left onlayer mcsprite
    g "Work?"
    g "Don’t people come here to get {i}away{/i} from work?"
    g " …I don’t want to think about it."
    #hide gerard icon at left onlayer mcsprite

    "...Yikes."

    jump gerard_points_check

label gerard_ev_2:
    #hide gerard icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ g_ev_2 = True;

    #show gerard icon at left onlayer mcsprite
    g "Car-"
    g "Wait. How…do you know where I work?"
    #hide gerard icon at left onlayer mcsprite

    "...{i}Shit.{/i}"

    show sachi mask icon at left onlayer mcsprite
    s "Oh! You, just, uh…seem like the type."
    hide sachi mask icon at left onlayer mcsprite

    #show gerard icon at left onlayer mcsprite
    g "…Sure."
    g "But uh…I haven’t been there too long. Around four years now."
    g " I used to intern there."
    #hide gerard icon at left onlayer mcsprite

    "…So he was a newbie back then."

    jump gerard_points_check

label gerard_ev_3:
    #hide gerard icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ g_ev_3 = True;

    #show gerard icon at left onlayer mcsprite
    g "..."
    g "What makes you say that?"
    #hide gerard icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    s "Oh…y’know. You seem like the Wall Street type."
    hide sachi mask icon at left onlayer mcsprite

    #show gerard icon at left onlayer mcsprite
    g "...I work at Carmine, I guess. If that’s what you mean."
    g "Not that it really makes a difference."
    #hide gerard icon at left onlayer mcsprite

    jump gerard_points_check

label gerard_ev_3b:

    #hide gerard icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ g_ev_3b = True;

    #show gerard icon at left onlayer mcsprite
    g " But uh…I haven’t been there too long. Around four years now."
    g "I used to intern there."
    #hide gerard icon at left onlayer mcsprite

    "…So he was a newbie back then."

    jump gerard_points_check


label gerard_ev_4:
    #hide gerard icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ g_ev_4 = True;

    #show gerard icon at left onlayer mcsprite
    g "There’s nothing to like. All I’m doing is helping rich people get richer, and killing myself in the process."
    #hide gerard icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    s " …What about the money?"
    hide sachi mask icon at left onlayer mcsprite

    #show gerard icon at left onlayer mcsprite
    g "‘Money’ my ass. I’ve been a runt this whole damn time."
    g " I hardly even get half of what my supervisors get. And even less now that the market’s gone haywire."
    g "..."
    g "...All of the money’s dirty, anyway."
    #hide gerard icon at left onlayer mcsprite

    jump gerard_points_check

label gerard_ev_5:

label gerard_ev_6:

label gerard_ev_7:

# DRINK MECHANIC --------
label chatgift:
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    $ turns += 1
    $ drink_turns += 1
    $ drunk += 20
    if (client == 1):
        hide vincent mask icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite
        if drink_turns == 1:
            show sachi mask icon at left onlayer mcsprite
            "My secret weapon: alcohol. I hand him a glass of Whiskey on the rocks."
            hide sachi mask icon at left onlayer mcsprite

            show vincent mask icon at left onlayer mcsprite
            qb "…I prefer bourbon. But thank you."
            hide vincent mask icon at left onlayer mcsprite

        "He takes a small sip and puts it on the table."

        hide sachi mask icon at left onlayer mcsprite
        hide vincent mask icon at left onlayer mcsprite
        $ canwarp = True

        jump vincent_points_check
    if (client == 2):
        #hide gerard icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite
        if drink_turns == 1:
            show sachi mask icon at left onlayer mcsprite
            "Do you want something to drink?"
            hide sachi mask icon at left onlayer mcsprite

            #show gerard icon at left onlayer mcsprite
            g "Uh…sure. A beer is fine."
            #hide gerard icon at left onlayer mcsprite

            "I hand him the bottle. He opens it and takes a large sip."

        "He takes a large sip of his beer."

        hide sachi mask icon at left onlayer mcsprite
        hide vincent mask icon at left onlayer mcsprite
        $ canwarp = True
    if (client == 3):
        "."
    if (client == 4):
        "."




# FLIRT MECHANIC ---------
label chatdate:
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    $ turns += 1
    $ flirt_turns += 1
    if (flirt_turns <= 2):
        $ sus -= 20
    if (client == 1):
        hide vincent mask icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite
        if (flirt_turns == 1):
            show sachi mask icon at left onlayer mcsprite
            s "Y’know, our customers aren’t usually too easy on the eyes."
            s "Men like you are hard to come by."
            "I wink at him."
            hide sachi mask icon at left onlayer mcsprite

            show vincent mask icon at left onlayer mcsprite
            qb "..."
            hide vincent mask icon at left onlayer mcsprite

            show sachi mask icon at left onlayer mcsprite
            "He must be shy…"
            hide sachi mask icon onlayer mcsprite

        if (flirt_turns >=2):
            show sachi mask icon at left onlayer mcsprite
            s "So…do you {i}just{/i} want to talk?"
            s "I mean, you have me all night. Might as well make the most of it."
            hide sachi mask icon at left onlayer mcsprite

            show vincent mask icon at left onlayer mcsprite
            qb "..."
            qb "Are you trying to seduce me?"
            qb "I don’t have any ulterior motives with you, Miss Kaur. Believe me."
            hide vincent mask icon at left onlayer mcsprite

        $ canwarp = True
        hide sachi mask icon at left onlayer mcsprite
        hide vincent mask icon at left onlayer mcsprite
        jump vincent_points_check

    if (client == 2):
        #hide gerard icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite
        if (flirt_turns == 1):
            show sachi mask icon at left onlayer mcsprite
            s "I’m surprised you haven’t made a move on me yet."
            hide sachi mask icon at left onlayer mcsprite

            g "…Should I?"

            "I wink at him."

            show sachi mask icon at left onlayer mcsprite
            "Only if you want to."
            hide sachi mask icon onlayer mcsprite

        if (flirt_turns >=2):
            show sachi mask icon at left onlayer mcsprite
            s "You know…you seem really sweet."
            s "…I kinda like you."
            hide sachi mask icon at left onlayer mcsprite

            "I rest my hand on his thigh. His face is flushed."
        $ canwarp = True
        hide sachi mask icon at left onlayer mcsprite
        jump gerard_points_check
    if (client == 3):
        "."
    if (client == 4):
        "."


label drunk_full:
    if (client == 1):
        hide vincent mask icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        "{i}…He’s had around four glasses now. "
        "{i}And yet…he seems as focused as ever. Strange."
        "{i}He doesn’t look like {/i}that{i} much of a heavyweight."
        hide sachi mask icon at left onlayer mcsprite

        show vincent mask icon at left onlayer mcsprite
        qb "…You haven’t touched your glass."
        hide vincent mask icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        s "Huh? Yes I have. You saw me."
        hide sachi mask icon at left onlayer mcsprite

        "{i}He shakes his head."
        show vincent mask icon at left onlayer mcsprite
        qb "You’re pretending. Your glass hasn’t gone down one bit."
        hide vincent mask icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        "{i}Yeah. Except {/i}you’re{i} supposed to be drunk enough not to notice."
        "{i}I plaster on a smile and take a sip—a real one. It’s…bubbly and sweet?"
        s "…This is coke."
        hide sachi mask icon at left onlayer mcsprite

        show vincent mask icon at left onlayer mcsprite
        qb "I’m glad you noticed. I replaced it before you came."
        hide vincent mask icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        s "…"
        hide sachi mask icon at left onlayer mcsprite

        show vincent mask icon at left onlayer mcsprite
        qb "…I know your tricks, Miss Kaur."
        hide vincent mask icon at left onlayer mcsprite

        jump n1_part2
    if (client == 2):
        #hide gerard icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite

        #show gerard icon at left onlayer mcsprite
        g "…"
        #hide gerard icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        s "..."
        hide sachi mask icon at left onlayer mcsprite

        #show gerard icon at left onlayer mcsprite
        g "…"
        g "...{i}snore{/i}..."
        #hide gerard icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        s "Did he…pass out? That’s no good…"
        s "I still had a lot I needed to {color=#6b091b}ask him{/color}..."
        hide sachi mask icon at left onlayer mcsprite

        jump client_select

    if (client == 3):
        "."
    if (client == 4):
        "."



label sus_full:
    if (client == 1):
        hide vincent mask icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite

        show vincent mask icon at left onlayer mcsprite
        qb "…You seem to have a lot of questions."
        qb "Do you not trust me?"
        hide vincent mask icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        s "I-"
        hide sachi mask icon at left onlayer mcsprite

        show vincent mask icon at left onlayer mcsprite
        qb "You shouldn’t. You have no reason to."
        qb "But if I was expecting, er…favors from you, I would grow impatient by now."
        hide vincent mask icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        "…Thanks for telling me how to do my job."
        "He’s right, though. I should try not to be too obvious…"
        hide sachi mask icon at left onlayer mcsprite
        jump n1_part2
    if (client == 2):
        #hide gerard icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite

        #show gerard icon at left onlayer mcsprite
        g " …Aren’t we supposed to hook up? What is this, a job interview?"
        g "This isn’t what I paid for."
        #hide gerard icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        s "Sorry. I guess…I got too curious."
        hide sachi mask icon at left onlayer mcsprite

        " …Shit. I probably should’ve been a little more {color=#6b091b}subtle{/color}."
        jump client_select
    if (client == 3):
        "."
    if (client == 4):
        "."
