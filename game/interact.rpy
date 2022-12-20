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
    show gerard fullbody

    hide gerard icon at left onlayer mcsprite
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
    show richard fullbody
    #show RICHARD FULLBODY SPRITE

    hide richard icon at left onlayer mcsprite
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
    show malcolm fullbody

    hide malcolm icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    #VARIABLE FOR CHECKING WHAT NAME TO PRINT ON SCREEN
    $ soberBusinessmanScreen = False
    $ name = "MALCOLM HUNT"
    $ client = 4

    $ renpy.show_screen("mapchat")
    $ renpy.pause ()
    $ drunk = pointsdrunk
    $ sus = pointssus

#POINTS CHECK FOR EACH CLIENT-----------------------------
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
        jump gerard_post_minigame

label richard_points_check:
    $ just_talked = False
    if (turns <= 5 and drunk < 80 and sus < 60):
        jump richard_minigame
    elif (drunk >= 80):
        jump drunk_full
    elif (sus >= 60):
        jump sus_full
    elif (turns > 5):
        jump richard_post_minigame

label malcolm_points_check:
    $ just_talked = False
    if (turns <= 5 and drunk < 80 and sus < 60):
        jump malcolm_minigame
    elif (drunk >= 80):
        jump drunk_full
    elif (sus >= 60):
        jump sus_full
    elif (turns > 5):
        jump malcolm_post_minigame
#POINTS CHECK FOR EACH CLIENT END--------------------

#TALK MECHANIC---------------------------------------
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

    if (client == 1): #TALK WITH VINCENT-----------------------------------------------------
        show vincent fullbody masked

        hide vincent mask icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite

        if (talk_turns == 1):
            

            "{i}Clients knowing personal information…is never a good thing."

            "{i}Especially when its someone like {/i}him.{i} The last thing I
                need right now is someone more powerful than even the richest,
                sleaziest Wall Street bankers on my tail right now."

            "{i}If I play my cards right—nudge them in the right direction while
                telling him what he wants to hear—I can make him fold easy."
            hide sachi mask icon at left onlayer mcsprite

            show vincent mask icon at left onlayer mcsprite
            qb "Your real name…is Sachi Kaur, is it not?"
            hide vincent mask icon at left onlayer mcsprite

            show sachi mask icon at left onlayer mcsprite
            menu:
                "Yes.":
                    hide sachi mask icon at left onlayer mcsprite
                    jump vincent_ev_1
                "You have the wrong girl.":
                    hide sachi mask icon at left onlayer mcsprite
                    jump vincent_ev_2
                "Why?":
                    hide sachi mask icon at left onlayer mcsprite
                    jump vincent_ev_3

        elif (talk_turns == 2):
            show sachi mask icon at left onlayer mcsprite
            menu:
                "What do you want from me?":
                    hide sachi mask icon at left onlayer mcsprite
                    if (v1_ev_1 == True):
                        jump vincent_ev_3
                    if (v1_ev_2 == True):
                        jump vincent_ev_3
                    if (v1_ev_3 == True):
                        jump vincent_ev_1

                "How do you know who I am?":
                    hide sachi mask icon at left onlayer mcsprite
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
                    hide sachi mask icon at left onlayer mcsprite
                    jump vincent_ev_4a

                "Why me?" if v1_ev_2 == True:
                    hide sachi mask icon at left onlayer mcsprite
                    jump vincent_ev_5a

                "What kind of {i}help{/i} do you need?" if v1_ev_3 == True:
                    hide sachi mask icon at left onlayer mcsprite
                    jump vincent_1_end

        elif (talk_turns == 4):
            show sachi mask icon at left onlayer mcsprite
            menu:
                "How long have you been working at Carmine?" if v1_ev_4a == True:
                    hide sachi mask icon at left onlayer mcsprite
                    jump vincent_ev_4b

                "You have no proof." if v1_ev_5a == True:
                    hide sachi mask icon at left onlayer mcsprite
                    jump vincent_ev_5b

                "What kind of {i}help{/i} do you need?":
                    hide sachi mask icon at left onlayer mcsprite
                    jump vincent_1_end

        elif (talk_turns == 5):
            show sachi mask icon at left onlayer mcsprite
            menu:
                "How long have you been working at Carmine?" if v1_ev_4a == True:
                    hide sachi mask icon at left onlayer mcsprite
                    jump vincent_ev_4b

                "You have no proof." if v1_ev_5a == True:
                    hide sachi mask icon at left onlayer mcsprite
                    jump vincent_ev_5b

                "What kind of {i}help{/i} do you need?":
                    hide sachi mask icon at left onlayer mcsprite
                    jump vincent_1_end

        hide sachi mask icon at left onlayer mcsprite

    if (client == 2): #TALK WITH GERARD----------------------------------------------------------
        show gerard fullbody
        if (talk_turns == 1):
            
            "{i}{color=#6b091b}Gerard Wade{/color} is an employee in the lower ranks. From what Vincent said, he was {color=#6b091b}involved{/color} in the incident."
            "{i}I should figure out what he meant by that. I shouldn’t be too obvious from the get-go, though, or he’ll get too suspicious of my intentions."
            "{i}…{color=#6b091b}Sweet-talk{/color} and {color=#6b091b}booze{/color} might help him loosen up too. But I shouldn’t overdo either…"
            show sachi mask icon at left onlayer mcsprite
            menu:
                "How’s work?":
                    hide sachi mask icon at left onlayer mcsprite
                    jump gerard_ev_1

                "How long have you worked at Carmine?":
                    hide sachi mask icon at left onlayer mcsprite
                    jump gerard_ev_2

                "You seem like a bigshot.":
                    hide sachi mask icon at left onlayer mcsprite
                    jump gerard_ev_3

        elif (talk_turns == 2):
            show sachi mask icon at left onlayer mcsprite
            menu:
                "How long have you worked at Carmine?" if (g_ev_2 == False or g_ev_3 == True):
                    hide sachi mask icon at left onlayer mcsprite
                    if (g_ev_3 == True):
                        jump gerard_ev_3b
                    elif (g_ev_3 == False and g_ev_2 == True):
                        jump gerard_ev_2

                "Why don't you like work?" if (g_ev_1 == True):
                    hide sachi mask icon at left onlayer mcsprite
                    jump gerard_ev_4

                "Who's Gwen?":
                    hide sachi mask icon at left onlayer mcsprite
                    jump gerard_ev_5

        elif (talk_turns >= 3):
            show sachi mask icon at left onlayer mcsprite
            menu:
                "Who's Gwen?" if g_ev_5 == False and knows_gwen == True:
                    hide sachi mask icon at left onlayer mcsprite
                    jump gerard_ev_5

                "(Ask about Gwen.)" if g_ev_5 == True:
                    hide sachi mask icon at left onlayer mcsprite
                    jump gerard_ev_6

                "(Ask about dirty money.)" if g_ev_4 == True:
                    hide sachi mask icon at left onlayer mcsprite
                    jump gerard_ev_7

                "Why don't you like work?" if (g_ev_4 == False and g_ev_1 == True):
                    hide sachi mask icon at left onlayer mcsprite
                    jump gerard_ev_4

        hide sachi mask icon at left onlayer mcsprite

    if (client == 3): #TALK WITH RICHARD---------------------------
        show richard fullbody
        hide richard icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite

        if (talk_turns == 1):
            """
            {i}{color=#6b091b}Richard Bloomberg{/color} is an employee in the higher ranks. From what Vincent said, he was involved in the incident.

            {i}I should figure out what he meant by that. I shouldn’t be too obvious from the get-go, though, or he’ll get too suspicious of my intentions.

            {i}…{color=#6b091b}sweet-talk{color} and {color=#6b091b}booze{/color} might help him loosen up too. But I shouldn’t overdo either…
            """
            show sachi mask icon at left onlayer mcsprite

            menu:
                "You’re a Wall-Street hotshot, huh?":
                    hide sachi mask icon at left onlayer mcsprite
                    jump richard_ev_1

                "You like your job?":
                    hide sachi mask icon at left onlayer mcsprite
                    jump richard_ev_2

        elif (talk_turns >= 2):
            show sachi mask icon at left onlayer mcsprite
            menu:
                "(Ask about work.)" if (r_ev_2 == True):
                    hide sachi mask icon at left onlayer mcsprite
                    jump richard_ev_2a

                "(Ask about 'the whole deal.')" if (r_ev_1 == True and r_ev_3 ==False):
                    hide sachi mask icon at left onlayer mcsprite
                    jump richard_ev_3

                "The ‘nasty stuff?’" if (r_ev_2c == True and r_ev_4 == False):
                    hide sachi mask icon at left onlayer mcsprite
                    jump richard_ev_4

    if (client == 4): #TALK WITH MALCOLM--------------------------------
        hide malcolm icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite

        if (talk_turns == 1):
            
            """
            {i}So {color=#6b091b}Malcolm Hunt{/color} is an assistant in forensics. From what Vincent said,
            he helped with {/i}Baba's{i} autopsy. The {color=#6b091b}real one.{/color}

            {i}I should find out more about what {color=#6b091b}really happened{/color}. I shouldn't be too obvious
            from the get-go, though. Or he'll get too suspicious of my intentions.

            {i}…{color=#6b091b}sweet-talk{color} and {color=#6b091b}booze{/color} might help him loosen up too. But I shouldn’t overdo either…
            """
            show sachi mask icon at left onlayer mcsprite
            menu:
                "You don't seem like the Wall Street type.":
                    hide sachi mask icon at left onlayer mcsprite
                    jump malcolm_ev_1

        elif (talk_turns ==2):
            ""
        elif (talk_turns >=3):
            ""


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
    hide gerard icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ g_ev_2 = True;

    show gerard icon at left onlayer mcsprite
    g "Car-"
    g "Wait. How…do you know where I work?"
    hide gerard icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    "...{i}Shit.{/i}"
    s "Oh! You, just, uh…seem like the type."
    hide sachi mask icon at left onlayer mcsprite

    show gerard icon at left onlayer mcsprite
    g "…Sure."
    g "But uh…I haven’t been there too long. Around four years now."
    g "I used to intern there."
    hide gerard icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    "{i}…So he was a newbie back then."
    hide sachi mask icon at left onlayer mcsprite

    jump gerard_points_check

label gerard_ev_3:
    hide gerard icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ g_ev_3 = True;

    show gerard icon at left onlayer mcsprite
    g "..."
    g "What makes you say that?"
    hide gerard icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    s "Oh…y’know. You seem like the Wall Street type."
    hide sachi mask icon at left onlayer mcsprite

    show gerard icon at left onlayer mcsprite
    g "...I work at Carmine, I guess. If that’s what you mean."
    g "Not that it really makes a difference."
    hide gerard icon at left onlayer mcsprite

    jump gerard_points_check

label gerard_ev_3b:
    hide gerard icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ g_ev_3b = True;

    show gerard icon at left onlayer mcsprite
    g " But uh…I haven’t been there too long. Around four years now."
    g "I used to intern there."
    hide gerard icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    "{i}…So he was a newbie back then."
    hide sachi mask icon at left onlayer mcsprite

    jump gerard_points_check

label gerard_ev_4:
    hide gerard icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ g_ev_4 = True;

    show gerard icon at left onlayer mcsprite
    g "There’s nothing to like. All I’m doing is helping rich people get richer, and killing myself in the process."
    hide gerard icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    s " …What about the money?"
    hide sachi mask icon at left onlayer mcsprite

    show gerard icon at left onlayer mcsprite
    g "‘Money’ my ass. I’ve been a runt this whole damn time."
    g " I hardly even get half of what my supervisors get. And even less now that the market’s gone haywire."
    g "..."
    g "...All of the money’s dirty, anyway."
    hide gerard icon at left onlayer mcsprite

    jump gerard_points_check

label gerard_ev_5:
    hide gerard icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ g_ev_5 = True;

    show gerard icon at left onlayer mcsprite
    g "…"
    g "…Are you supposed to ask so many questions?"
    hide gerard icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    s "I mean, you asked to call me Gwen. It's not too much of a stretch to ask-"
    hide sachi mask icon at left onlayer mcsprite

    show gerard icon at left onlayer mcsprite
    g "She’s just… someone."
    hide gerard icon at left onlayer mcsprite

    if (drunk < 20):
        "{i}He probably won't tell me anything else {color=#6b091b}sober.{/color}"

    jump gerard_points_check

label gerard_ev_6:
    hide gerard icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ g_ev_6 = 1;

    show sachi mask icon at left onlayer mcsprite
    s "Is Gwen someone…special?"
    hide sachi mask icon at left onlayer mcsprite

    show gerard icon at left onlayer mcsprite
    g "Was. And…I guess."
    hide gerard icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    s "{i}…Was?{/i}"
    hide sachi mask icon at left onlayer mcsprite

    if (drunk < 20):
        show gerard icon at left onlayer mcsprite
        g "..."
        hide gerard icon at left onlayer mcsprite

        "{i}He probably won't tell me anything else {color=#6b091b}sober.{/color}"

    elif (drunk == 20):
        show gerard icon at left onlayer mcsprite
        g "She was a journalist. We were friends from college."
        g "She…was super into crime stuff, I guess. Like conspiracy theories and all that."
        g "And it kinda…got to her."
        g "…"
        hide gerard icon at left onlayer mcsprite

        "{i}He probably won't tell me anything else until he {color=#6b091b}drinks a bit more.{/color}"
        $ g_ev_6 = 2;

    elif (drunk >= 40):
        show gerard icon at left onlayer mcsprite
        g "There’s…a conspiracy about Antony Carmine, y’know?"
        g "He was part of a {color=#6b091b}trafficking ring{/color} before he got big. Went by a different name ‘n all."
        g "…What was it? I know she told-oh. Yeah."
        g "{color=#6b091b}Alonzo Romano.{/color}"
        g "…Anyways. Gwen got really into this shit. When I got my internship, she was seriously stoked. Asked me to tell her everything I could."
        g "I…found out a lot of things I wouldn’t wanna know."
        hide gerard icon at left onlayer mcsprite

        $ g_ev_6 = 3;

    jump gerard_points_check

label gerard_ev_7:
    hide gerard icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ g_ev_7 = True;

    show gerard icon at left onlayer mcsprite
    g "Y’know. Shady people."
    g "…{i}Really{/i} shady people."
    hide gerard icon at left onlayer mcsprite

    if (drunk < 20):
        show gerard icon at left onlayer mcsprite
        g "..."
        hide gerard icon at left onlayer mcsprite

        "{i}He probably won't tell me anything else {color=#6b091b}sober.{/color}"

    elif (drunk == 20):
        show gerard icon at left onlayer mcsprite
        g "Drugs, murder…"
        g "…Trafficking."
        hide gerard icon at left onlayer mcsprite

        "{i}He stops."
        $ g_ev_7b = True

    jump gerard_points_check

label richard_ev_1:
    $ r_ev_1 = True;
    hide sachi icon at left onlayer mcsprite

    show richard icon at left onlayer mcsprite
    r """
    Damn right I am.

    You into that, baby?
    """
    hide richard icon at left onlayer mcsprite

    show sachi icon at left onlayer mcsprite
    "{i}...Major ew."
    s "What kinda...{i}big Wall Street stuff{/i} do you do, mister?"
    hide sachi icon at left onlayer mcsprite

    show richard icon at left onlayer mcsprite
    r "Haha. I guess I boss people around, schmooze up with black suits... y'know. The whole deal."
    hide richard icon at left onlayer mcsprite

    jump richard_points_check


label richard_ev_2:
    $ r_ev_2 = True

    hide sachi icon at left onlayer mcsprite

    show richard icon at left onlayer mcsprite
    r "What’s not to like? I get paid major buck. That’s what matters."
    r "As long as I’m making over six figures, I don’t give a damn ‘bout the actual work involved."
    hide richard icon at left onlayer mcsprite

    jump richard_points_check


label richard_ev_2a:
    $ r_ev_2a = 1

    hide sachi icon at left onlayer mcsprite

    show richard icon at left onlayer mcsprite
    r "As long as I’m making over six figures, I don’t give a damn ‘bout the actual work involved."
    hide richard icon at left onlayer mcsprite

    if $drunk <=20:
        show richard icon at left onlayer mcsprite
        r "‘That all, sweetheart?"
        hide richard icon at left onlayer mcsprite

        "…He needs more {color=#6b091b}booze{/color} in him before he’ll blab."

    if $drunk ==20:
        $ r_ev_2a = 2
        show richard icon at left onlayer mcsprite
        r "It…can get a bit dirty though, sometimes."
        hide richard icon at left onlayer mcsprite

        show sachi icon at left onlayer mcsprite
        s "{i}Dirty?{/i}"
        hide sachi icon at left onlayer mcsprite

        show richard icon at left onlayer mcsprite
        r "…It’s better not to think about it."
        hide richard icon at left onlayer mcsprite

        "He might need a little more {color=#6b091b}booze{/color} in him to {i}really{/i} open up.."

    if $drunk == 40:
        $ r_ev_2a = 3
        show richard icon at left onlayer mcsprite
        r "Sometimes…our clients get into bad business, and we have to cover up the tracks."
        r "Luckily, I’ve only ever had to do cleanup. I feel a bit bad for the runts who {i}actually{/i} had to do the nasty stuff."
        r "...Just kidding. No I don't"
        hide richard icon at left onlayer mcsprite

    jump richard_points_check

label richard_ev_3:
    $ r_ev_3 = True

    show richard icon at left onlayer mcsprite
    r "…More than you could ever think up in your {i}pretty little head{/i}. That’s for sure."
    r "As long as I’m making over six figures, I don’t give a damn ‘bout the actual work involved."
    hide richard icon at left onlayer mcsprite

jump richard_points_check

label richard_ev_4:
    $ r_ev_4 = True

    show richard icon at left onlayer mcsprite
    r " …Oooh, baby. I would need you to sign a form if I told you."
    hide richard icon at left onlayer mcsprite

jump richard_points_check

label malcolm_ev_1:
    $ m_ev_1 = True

    show malcolm icon at left onlayer mcsprite
    m "I'm not."
    m "I... work for the NYPD, actually."
    hide malcolm icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    s "So you-"
    hide sachi mask icon at left onlayer mcsprite

    show malcolm icon at left onlayer mcsprite
    m "Haha, don’t worry. I’m not reporting the Cabaret. I’m here on my own terms."
    m "The feds are in kahoots with most of the guys that come here, anyways. So I doubt it makes a difference."
    m "…Anyway. I work in forensics, for what its worth. I’m not a cop or anything."
    hide malcolm icon at left onlayer mcsprite

# DRINK MECHANIC --------
label chatgift:
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    $ turns += 1
    $ drink_turns += 1
    $ drunk += 20

    play sound pourDrink

    if (client == 1): #DRINK WITH VINCENT
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

    if (client == 2): #DRINK WITH GERARD
        hide gerard icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite

        if (drink_turns == 1):
            show sachi mask icon at left onlayer mcsprite
            "Do you want something to drink?"
            hide sachi mask icon at left onlayer mcsprite

            show gerard icon at left onlayer mcsprite
            g "Uh…sure. A beer is fine."
            hide gerard icon at left onlayer mcsprite

            "{i}I hand him the bottle. He opens it and takes a large sip."

        "{i}He takes a large sip of his beer."

        hide sachi mask icon at left onlayer mcsprite
        hide vincent mask icon at left onlayer mcsprite

        $ canwarp = True
        jump gerard_points_check

    if (client == 3): #DRINK WITH RICHARD
        hide richard icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite

        if (drink_turns == 1):
            show richard icon at left onlayer mcsprite
            r "…Can I have a beer, sweetheart?"
            hide richard icon at left onlayer mcsprite

            show sachi mask icon at left onlayer mcsprite
            "{i}I hand him a bottle, and he takes a large swig."
            hide sachi mask icon at left onlayer mcsprite

        "{i}He takes a large sip of his beer."

        hide sachi mask icon at left onlayer mcsprite
        hide vincent mask icon at left onlayer mcsprite

        $ canwarp = True
        jump richard_points_check

    if (client == 4): #DRINK WITH MALCOLM
        hide sachi mask icon at left onlayer mcsprite
        hide malcolm icon at left onlayer mcsprite

        if (drink_turns == 1):
            show sachi mask icon at left onlayer mcsprite
            s "Would you like a drink?"
            hide sachi mask icon at left onlayer mcsprite

            show malcolm icon at left onlayer mcsprite
            m "Oh! Sure. A glass of rum on the rocks sounds good."
            m "Cheers."
            hide malcolm icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        "{i}I gesture to his glass. It's empty."
        s "Would you like some more?"
        hide sachi mask icon at left onlayer mcsprite

        show malcolm icon at left onlayer mcsprite
        m "Of course."
        hide malcolm icon at left onlayer mcsprite

        hide sachi mask icon at left onlayer mcsprite
        hide vincent mask icon at left onlayer mcsprite

        $ canwarp = True
        jump malcolm_points_check

# FLIRT MECHANIC ---------
label chatdate:
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    $ turns += 1
    $ flirt_turns += 1


    if (flirt_turns <= 2):
        $ sus -= 20


    if (client == 1):#FLIRT WITH VINCENT
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

    if (client == 2): #FLIRT WITH GERARD
        hide gerard icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite
        if (flirt_turns == 1):
            show sachi mask icon at left onlayer mcsprite
            s "I’m surprised you haven’t made a move on me yet."
            hide sachi mask icon at left onlayer mcsprite

            show gerard icon at left onlayer mcsprite
            g "…Should I?"
            hide gerard icon at left onlayer mcsprite

            show sachi mask icon at left onlayer mcsprite
            "{i}I wink at him."
            s "Only if you want to."
            hide sachi mask icon onlayer mcsprite

        if (flirt_turns >=2):
            show sachi mask icon at left onlayer mcsprite
            s "You know…you seem really sweet."
            s "…I kinda like you."
            "{i}I rest my hand on his thigh. His face is flushed."
            hide sachi mask icon at left onlayer mcsprite

        $ canwarp = True
        jump gerard_points_check

    if (client == 3): #FLIRT WITH RICHARD
        hide richard icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite

        if (flirt_turns == 1):
            show sachi mask icon at left onlayer mcsprite
            s "So…what do you wanna do tonight?"
            hide sachi mask icon at left onlayer mcsprite

            show richard icon at left onlayer mcsprite
            r "A better question, sweetheart, is what I {i}don’t{/i} wanna do."
            hide richard icon at left onlayer mcsprite

        if (flirt_turns >=2):
            show sachi mask icon at left onlayer mcsprite
            s "Y’know…you look so sexy right now. "
            hide sachi mask icon at left onlayer mcsprite

            show richard icon at left onlayer mcsprite
            r "I could say the same thing about you, darling."
            hide richard icon at left onlayer mcsprite


        hide sachi mask icon at left onlayer mcsprite
        $ canwarp = True

        jump richard_points_check

    if (client == 4): #FLIRT WITH  MALCOLM
        hide malcolm icon at left onlayer mcsprite
        hide sachi icon at left onlayer mcsprite
        if (flirt_turns == 1):
            show sachi mask icon at left onlayer mcsprite
            s "Y'know... I think you're pretty cute."
            hide sachi mask icon at left onlayer mcsprite

            show malcolm icon at left onlayer mcsprite
            "{i}He blushes."
            m "Oh...thank you. The feeling's mutual."
            hide malcolm icon at left onlayer mcsprite

        if (flirt_turns >= 2):
            s "Let me know when you wanna cut to the chase."
            s "No need to {i}hold back{/i}, 'kay?"

            show malcolm icon at left onlayer mcsprite
            m "...Noted. Though... I don't mind just talking to you."
            m "I didn't pay in full, after all. You don't...er, owe any sexual favors to me, you know?"
            hide malcolm icon at left onlayer mcsprite

        hide sachi mask icon at left onlayer mcsprite
        hide malcolm icon at left onlayer mcsprite

        $ canwarp = True

        jump malcolm_points_check

#FULLY DRUNKK--------------------------------------------------------------
label drunk_full:
    if (client == 1): #VINCENT FULLY DRUNK
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


    if (client == 2): #GERARD FULLY DRUNK
        hide gerard icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite

        show gerard icon at left onlayer mcsprite
        g "…"
        hide gerard icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        s "..."
        hide sachi mask icon at left onlayer mcsprite

        show gerard icon at left onlayer mcsprite
        g "…"
        g "...{i}(snore){/i}..."
        hide gerard icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        "{i}Did he…pass out? That’s no good…"
        "{i}I still had a lot I needed to {color=#6b091b}ask him{/color}..."
        hide sachi mask icon at left onlayer mcsprite

        stop music fadeout 1.0
        play music susClub loop fadein 1.0

        jump client_select

    if (client == 3): #RICHARD FULLY DRUNK
        hide sachi mask icon at left onlayer mcsprite

        show richard icon at left onlayer mcsprite
        r "So…are we ever…gonna…"
        r "…We…"
        r "…Hm…"
        hide richard icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        "{i}He’s too {color=#6b091b}drunk{/color} to make sense right now. That’s a shame…"
        "{i}I still had a lot I needed to {color=#6b091b}ask him.{/color}"
        hide sachi mask icon at left onlayer mcsprite

        jump client_select

    if (client == 4):
        hide sachi mask icon at left onlayer mcsprite

        show malcolm icon at left onlayer mcsprite
        m "I…need…"
        m "Bathroom…where’s the nearest-"
        hide malcolm icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        s "Nearest right."
        "{i}He dashes out of the room at lightning speed. I hear retching a few minutes later."
        "{i}He shouldn’t have {color=#6b091b}drank so much…{/color}"
        hide sachi mask icon at left onlayer mcsprite

        jump client_select


#FULLY SUSPICIOUS------------------------------------------------------------------------------
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
        "{i}…Thanks for telling me how to do my job."
        "{i}He’s right, though. I should try not to be too obvious…"
        hide sachi mask icon at left onlayer mcsprite

        stop music fadeout 1.0
        play music susClub loop fadein 1.0
        jump n1_part2

    if (client == 2):
        hide gerard icon at left onlayer mcsprite
        hide sachi mask icon at left onlayer mcsprite

        show gerard icon at left onlayer mcsprite
        g " …Aren’t we supposed to hook up? What is this, a job interview?"
        g "This isn’t what I paid for."
        hide gerard icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        s "Sorry. I guess…I got too curious."


        "{i}…Shit. I probably should’ve been a little more {color=#6b091b}subtle{/color}."
        hide sachi mask icon at left onlayer mcsprite

        stop music fadeout 1.0
        play music susClub loop fadein 1.0
        jump client_select

    if (client == 3):
        hide sachi mask icon at left onlayer mcsprite

        show richard icon at left onlayer mcsprite
        r "So…are we ever gonna get to the fun part, are are you just gonna keep blabbing? ‘Cuz I’m getting a bit impatient here."
        hide richard icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        s "…Damn. Guess I should’ve been a bit more {color=#6b091b}subtle.{/color}"
        hide sachi mask icon at left onlayer mcsprite

        stop music fadeout 1.0
        play music susClub loop fadein 1.0
        jump client_select

    if (client == 4):
        hide sachi mask icon at left onlayer mcsprite

        show malcolm icon at left onlayer mcsprite
        m " …"
        m "I…don’t feel comfortable sharing confidential information with you. Sorry."
        hide malcolm icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        s "…Damn. I should’ve been more subtle."
        hide sachi mask icon at left onlayer mcsprite

        stop music fadeout 1.0
        play music susClub loop fadein 1.0
        jump client_select
