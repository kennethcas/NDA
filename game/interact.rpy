label vincent_minigame:
    scene bg private room
    show vincent fullbody
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

    show sachi mask at left onlayer mcsprite

    if (talk_turns == 1):
        "Clients knowing personal information…is never a good thing."

        "Especially when its someone like {i}him.{/i} The last thing I
            need right now is someone more powerful than even the richest,
            sleaziest Wall Street bankers on my tail right now."

        "If I play my cards right—nudge them in the right direction while
            telling him what he wants to hear—I can make him fold easy."
        hide sachi mask at left onlayer mcsprite
        show vincent mask at left onlayer mcsprite
        qb "Your real name…is Sachi Kaur, is it not?"
        hide vincent mask at left onlayer mcsprite
        show sachi mask at left onlayer mcsprite

        menu:
            "Yes.":
                jump vincent_ev_1
            "You have the wrong girl.":
                jump vincent_ev_2
            "Why?":
                jump vincent_ev_3

    elif (talk_turns == 2):
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
        menu:
            "How do you know my father?" if v1_ev_1 == True:
                jump vincent_ev_4a

            "Why me?" if v1_ev_2 == True:
                jump vincent_ev_5a

            "What kind of {i}help{/i} do you need?" if v1_ev_3 == True:
                jump vincent_1_end

    elif (talk_turns == 4):
        menu:
            "How long have you been working at Carmine?" if v1_ev_4a == True:
                jump vincent_ev_4b

            "You have no proof." if v1_ev_5a == True:
                jump vincent_ev_5b

            "What kind of {i}help{/i} do you need?":
                jump vincent_1_end

    hide side mc onlayer mcsprite

label vincent_ev_1:

    $ v1_ev_1 = True;

    s "…How did you know?"
    qb "I’ve been looking for you. You’re {color=#6b091b}Rahul Kaur{/color}’s daughter."
    #surprise sfx
    qb "…I wonder what he’d think now of your…er…profession. And {color=#6b091b}exploits{/color}, for that matter…"
    s "…Well isn’t {i}he{/i} a delight."

    jump points_check

label vincent_ev_2:
    $ v1_ev_2 = True;
    $ sus += 20
    if (talk_turns <= 1):
        "He shakes his head."
    qb "…I’ve been hearing lots of back alley talk about mysterious maxed out
        credit cards, incriminating pictures mailed to wives and kids, thousands of
        dollars of jewelry mysteriously going missing…"
    s "I’m surprised someone of your…{i}esteemed status{/i} keeps up with
        {i}back-alley talk{/i}."
    qb "My…{i}esteemed status{/i}?"
    s "…Your mask."
    s "The only clients who wear masks are people in the public eye. For
        uh…pretty obvious reasons. Not getting caught by the press and all…"
    qb "…Well, I have my sources."

    jump points_check

label vincent_ev_3:

    $ v1_ev_3 = True;
    $ sus += 20

    qb "I need your help."
    s "My…{i}help{/i}?"

    jump points_check

label vincent_ev_4a:
    $ v1_ev_4a = True;
    $ sus += 20

    qb "..."
    qb "...He used to work under me. To an extent."
    s "…"
    "So he used to work at Carmine. A white-collar investment firm that I’m all
    too familiar with."
    "No, scratch that…he’s a bigwig at Carmine."


    jump points_check

label vincent_ev_4b:
    $ v1_ev_4b = True;
    $ sus += 20

    qb "…Around {color=#6b091b}five years{/color} now."
    "{i}Five years?{/i} That’s way too soon for such a big promotion…"
    s "You’re…Antony Carmine’s son."
    qb "…"

    jump points_check

label vincent_ev_5a:
    $ v1_ev_5a = True;
    $ sus += 20

    qb "Those who have been scammed, blackmailed, and otherwise victimized
        in some shape and form all had one thing in common."
    qb "…They visited The Scarlet Cabaret on a
        {color=#6b091b}Friday night{/color} after {color=#6b091b}June 1985{/color}."
    qb "Currently, there are {color=#6b091b}ten women{/color} who work on
        Fridays. Each of you wear a different {color=#6b091b}animal
        mask{/color}, correct?"
    qb "Coincidentally, my…{i}sources{/i} began to report seeing a
        {color=#6b091b}girl with a cat mask{/color} around that time."
    "..."

    jump points_check

label vincent_ev_5b:
    $ v1_ev_5b = True;
    $ sus += 20

    qb "Believe me. If I wanted you behind bars, I could easily find a way."
    qb "…I think we could be useful to one another."

    jump points_check

label vincent_1_end:
    qb "..."
    qb "...Revenge."

# DRINK MECHANIC --------
label chatgift:
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    $ turns += 1
    $ drink_turns += 1

    show side mc at left onlayer mcsprite

    if drink_turns == 1:
        "My secret weapon: alcohol. I hand him a glass of Whiskey on the rocks."
        qb "…I prefer bourbon. But thank you."

    "He takes a small sip and puts it on the table."
    $ drunk += 25

    hide side mc onlayer mcsprite
    $ canwarp = True

    jump points_check

# FLIRT MECHANIC ---------

label chatdate:
    $ renpy.hide_screen("mapchat")
    $ canwarp = False
    $ turns += 1
    $ flirt_turns += 1

    if (flirt_turns <= 2):
        $ sus -= 20

    if (flirt_turns == 1):
        show side mc at left onlayer mcsprite

        s " Y’know, our customers aren’t usually too easy on the eyes."
        s "Men like you are hard to come by."
        "I wink at him."
        qb "..."
        "He must be shy…"
        $ sus -= 20

        hide side mc onlayer mcsprite

    if (flirt_turns >=2):
        s "So…do you {i}just{/i} want to talk? "
        s "I mean, you have me all night. Might as well make the most of it."
        qb "..."
        qb "Are you trying to seduce me?"
        qb "I don’t have any ulterior motives with you, Miss Kaur. Believe me."

    $ canwarp = True

    jump points_check

label drunk_full:

    show side mc at left onlayer mcsprite

    "…He’s had around four glasses now. "
    "And yet…he seems as focused as ever. Strange."
    "He doesn’t look like {i}that{/i} much of a heavyweight."
    qb "…You haven’t touched your glass."
    s "Huh? Yes I have. You saw me."
    "He shakes his head."
    qb "You’re pretending. Your glass hasn’t gone down one bit. "
    "Yeah. Except {i}you’re{/i} supposed to be drunk enough not to notice."
    "I plaster on a smile and take a sip—a real one. It’s…bubbly and sweet?"
    s "…This is coke."
    qb "I’m glad you noticed. I replaced it before you came."
    s "…"
    qb "…I know your tricks, Miss Kaur."

    hide side mc onlayer mcsprite

    jump n1_part2

label sus_full:
    qb "…You seem to have a lot of questions."
    qb "Do you not trust me?"
    s "I-"
    qb "You shouldn’t. You have no reason to."
    qb "But if I was expecting, er…favors from you, I would grow impatient by now."
    "…Thanks for telling me how to do my job."
    "He’s right, though. I should try not to be too obvious…"
    jump n1_part2
