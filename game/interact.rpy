#init python:
#    def hideIcons():
#        hide vincent mask icon at left onlayer mcsprite
#        hide sachi mask icon at left onlayer mcsprite

#SETTING SOME BOOLS AND VARIABLES---------------------------
#$ hideIcons:
    

#if hideIcons: #HIDES ALL PORTRAITS
 #   hide vincent mask icon at left onlayer mcsprite
  #  hide sachi mask icon at left onlayer mcsprite

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


#START VINCENT MINIGAME ------------------------------------
label vincent_minigame:
    scene bg private room
    show vincent fullbody

    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    #VARIABLE FOR CHECKING WHAT NAME TO PRINT ON SCREEN
    $ soberBusinessmanScreen = True

    $ renpy.show_screen("mapchat")
    $ renpy.pause ()
    $ drunk = pointsdrunk
    $ sus = pointssus

label points_check:
    if (turns <= 5 and drunk < 100 and sus < 100):
        #ADD OTHER MINIGAMES
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

    show vincent fullbody

    #$ hideIcons = True
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    if (talk_turns == 1):
        show sachi mask icon at left onlayer mcsprite
        """
        {i}Clients knowing personal information…is never a good thing.

        {i}Especially when its someone like {/i}him.{i} The last thing I
            need right now is someone more powerful than even the richest,
            sleaziest Wall Street bankers on my tail right now.

        {i}If I play my cards right—nudge them in the right direction while
            telling him what he wants to hear—I can make him fold easy.{/i}
        """

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

    hide sachi mask icon at left onlayer mcsprite

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

    jump points_check

label vincent_ev_2:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    $ v1_ev_2 = True;
    $ sus += 20
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
    jump points_check

label vincent_ev_3:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    $ v1_ev_3 = True;
    $ sus += 20
    show vincent mask icon at left onlayer mcsprite
    qb "I need your help."
    hide vincent mask icon at left onlayer mcsprite
    show sachi mask icon at left onlayer mcsprite
    s "My…{i}help{/i}?"

    hide sachi mask icon at left onlayer mcsprite
    jump points_check

label vincent_ev_4a:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    $ v1_ev_4a = True;
    $ sus += 20

    show vincent mask icon at left onlayer mcsprite
    qb "..."
    qb "...He used to work under me. To an extent."
    hide vincent mask icon at left onlayer mcsprite
    show sachi mask icon at left onlayer mcsprite
    s "…"
    "{i}So he used to work at Carmine. A white-collar investment firm that I’m all
    too familiar with.{/i}"
    "{i}No, scratch that…he’s a bigwig at Carmine.{/i}"

    hide sachi mask icon at left onlayer mcsprite
    jump points_check

label vincent_ev_4b:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    $ v1_ev_4b = True;
    $ sus += 20
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
    jump points_check

label vincent_ev_5a:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    $ v1_ev_5a = True;
    $ sus += 20

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
    jump points_check

label vincent_ev_5b:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    $ v1_ev_5b = True;
    $ sus += 20

    show vincent mask icon at left onlayer mcsprite
    qb "Believe me. If I wanted you behind bars, I could easily find a way."
    qb "…I think we could be useful to one another."

    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    jump points_check

label vincent_1_end:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    show vincent mask icon at left onlayer mcsprite
    qb "..."
    qb "...Revenge."
    jump points_check

# DRINK MECHANIC --------
label chatgift:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    $ turns += 1
    $ drink_turns += 1

    show sachi mask icon at left onlayer mcsprite

    if drink_turns == 1:
        "My secret weapon: alcohol. I hand him a glass of Whiskey on the rocks."
        hide sachi mask icon at left onlayer mcsprite
        show vincent mask icon at left onlayer mcsprite
        qb "…I prefer bourbon. But thank you."

    hide vincent mask icon at left onlayer mcsprite
    show sachi mask icon at left onlayer mcsprite
    "He takes a small sip and puts it on the table."
    $ drunk += 25

    hide sachi mask icon at left onlayer mcsprite
    hide vincent mask icon at left onlayer mcsprite
    $ canwarp = True

    jump points_check

# FLIRT MECHANIC ---------
label chatdate:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    $ turns += 1
    $ flirt_turns += 1

    if (flirt_turns <= 2):
        $ sus -= 20

    if (flirt_turns == 1):

        show sachi mask icon at left onlayer mcsprite
        s " Y’know, our customers aren’t usually too easy on the eyes."
        s "Men like you are hard to come by."
        "{i}I wink at him."
        hide sachi mask icon at left onlayer mcsprite
        show vincent mask icon at left onlayer mcsprite
        qb "..."
        hide vincent mask icon at left onlayer mcsprite
        show sachi mask icon at left onlayer mcsprite
        "{i}He must be shy…"
        $ sus -= 20

        hide sachi mask icon onlayer mcsprite

    if (flirt_turns >=2):
        show sachi mask icon at left onlayer mcsprite
        s "So…do you {i}just{/i} want to talk? "
        s "I mean, you have me all night. Might as well make the most of it."
        hide sachi mask icon at left onlayer mcsprite
        show vincent mask icon at left onlayer mcsprite
        qb "..."
        qb "Are you trying to seduce me?"
        qb "I don’t have any ulterior motives with you, Miss Kaur. Believe me."

    $ canwarp = True
    hide sachi mask icon at left onlayer mcsprite
    hide vincent mask icon at left onlayer mcsprite
    jump points_check

label drunk_full:
    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite

    "…He’s had around four glasses now. "
    "And yet…he seems as focused as ever. Strange."
    "He doesn’t look like {i}that{/i} much of a heavyweight."
    hide sachi mask icon at left onlayer mcsprite
    show vincent mask icon at left onlayer mcsprite
    qb "…You haven’t touched your glass."
    hide vincent mask icon at left onlayer mcsprite
    show sachi mask icon at left onlayer mcsprite
    s "Huh? Yes I have. You saw me."
    hide sachi mask icon at left onlayer mcsprite
    show vincent mask icon at left onlayer mcsprite
    "He shakes his head."
    qb "You’re pretending. Your glass hasn’t gone down one bit."
    hide vincent mask icon at left onlayer mcsprite
    "Yeah. Except {i}you’re{/i} supposed to be drunk enough not to notice."
    "I plaster on a smile and take a sip—a real one. It’s…bubbly and sweet?"
    show sachi mask icon at left onlayer mcsprite
    s "…This is coke."
    hide sachi mask icon at left onlayer mcsprite
    show vincent mask icon at left onlayer mcsprite
    qb "I’m glad you noticed. I replaced it before you came."
    show sachi mask icon at left onlayer mcsprite
    s "…"
    hide sachi mask icon at left onlayer mcsprite
    show vincent mask icon at left onlayer mcsprite
    qb "…I know your tricks, Miss Kaur."

    hide sachi mask icon at left onlayer mcsprite
    hide vincent mask icon at left onlayer mcsprite

    jump n1_part2

label sus_full:
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
    "…Thanks for telling me how to do my job."
    hide vincent mask icon at left onlayer mcsprite
    show sachi mask icon at left onlayer mcsprite
    "{i}He’s right, though. I should try not to be too obvious…{/i}"
    hide sachi mask icon at left onlayer mcsprite
    jump n1_part2
