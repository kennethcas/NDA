# --- NDA SCRIPT ---
define s = Character("Sachi")
define v = Character("Vincent")
define q = Character("???")
define db = Character("Drunk Businessman")
define qb = Character("Sober Businessman")

define h = Character("Hostess")

define ab = Character("Awkward Businessman")
define sb = Character("Sleazy Businessman")
define dgb = Character("Dignified Businessman")

define g = Character("Gerard")
define r = Character("Richard")
define m = Character("Malcolm")

define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.7
define config.default_voice_volume = 07

$ N1_Wallet = False

$ what = False
$ why = False

$ alcohol_q = False
$ sex_q = False

$ db_picked = False
$ vincent_n2_intro_done = False

# ---GAME START---
label start:

    # scene black

    # music: tense, ominous
    play music profoundSadness loop fadein 1.0

    # DIALOGUE. ---
    menu:
        "SKIP INTRO, GO TO MINIGAME":
            stop music fadeout 1.0
            play music caravan loop fadein 1.0
            jump vincent_minigame_intro
        "PLAY GAME FROM BEGINNING":
            "THE GAME WILL START NOW."

    "OCTOBER 31, 1983 \nNEW YORK"
    q "..."
    q "...{w=1.0}Y-you..."
    q "{i}...{w=1.0}Is this not what you wanted?{/i}"
    q "{i}...You {color=#6b091b}killed{/color} her. And so many more."
    q "{i}You {color=#6b091b}asked{/color} for this, right?{/i}"
    q "I didn't mean...{p=1.0}now..."
    q "...{w=2.0}I have a daughter."
    q "{i}{color=#6b091b}She{/color} had a son.{/i}"
    # shake effect
    "{w=2.0}{nw}"
    q "{color=#6b091b}Sachi{/color}..."
    q "Take care of yourself, okay?"

    # ---

    jump intro_convo

label intro_convo:
    stop music fadeout 1.0
    play music susClub loop fadein 1.0
    scene bg lounge
    with fade
    # ambience sfx: bar
    # music: jazzy? lowkey?

    # DIALOGUE. ---
    "OCTOBER 21, 1983 \nNEW YORK"
    show richard fullbody
    with fade

    show richard icon at left onlayer mcsprite
    db "...Come on, kitty. Let's have a {i}good time,{/i} yeah?"
    hide richard icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    s "{i}{color=#6b091b}...I want to retch.{/color}"

    menu:
        "You don't even know my name.":
            hide sachi mask icon at left onlayer mcsprite

            show richard icon at left onlayer mcsprite
            db "Well, it's not like you're gonna tell me, right?"
            db "You all go by fake ones, anyway.{w=1.0} Not that I care."
            db "I'm not here to wine and dine you, doll."
            hide richard icon at left onlayer mcsprite

            jump intro_expos

        "Pay up first.":
            "{i}{color=#6b091b}I swat away his hand, which was inching dangerously
            close to my thigh.{/color}"
            s "Pay up in the front if you want a private room."
            hide sachi mask icon at left onlayer mcsprite

            show richard icon at left onlayer mcsprite
            db "Aw, come on baby. I just wanted to buy you a drink."
            hide richard icon at left onlayer mcsprite
            jump intro_expos

        "(Ignore him.)":
            show sachi mask icon at left onlayer mcsprite
            s "{i}(sigh...)"

            jump intro_expos

label intro_expos:
    hide richard fullbody
    hide richard fullbody drunk
    hide sachi mask icon at left onlayer mcsprite
    hide richard icon at left onlayer mcsprite
    with fade

    "A typical Friday night. The {i}Cabaret{/i} is busy as usual, full of
    drunk Wall Street dogs with coke addictions and housewives to cheat on."

    "Of course, the {i}Cabaret{/i} isn't really a Cabaret. {w=1.0}And the
    only performance us girls would be putting on is faking an orgasm."

    #black?

    "{color=#6b091b}Madame Han{/color} has always been discrete in her
    dealings. But I have my ways of figuring things out."

    "{i}{color=#6b091b}The Scarlet Cabaret{/i}{/color} capitalizes off Wall
    Street men with Orientalist fetishes, pent-up libido, and pocketfuls of
    dirty cash."

    "While the Madame herself is far away from her glory days, the talk of
    the gentleman's club locker rooms is that she has exquisite taste in her
    handpicked selection of young, beautiful women from across the Asian
    subcontinent."

    "And for a hefty sum, your pick of the lot can be yours for the night.
    Obedient and compliant to each and every one of your twisted, depraved
    fantasies."

    "...{i}I{/i} was born and raised in Queens. But as long as I can fake
    an accent and hit a sweet spot on the Madonna-Whore complex, I stay
    employed."

    #back to frontroom, map-style pick and choose who to talk to
    jump N1_Menu

label N1_Menu:
    # (theres a temporary menu for now)
    menu:
        "Drunk Businessman":
            if db_picked==False:
                jump CW2_N1
            else:
                jump N1_Menu

        "Sober Businessman":
            jump Vincent_N1

#if you choose CW#2:
label CW2_N1:
    $ db_picked == True
    show richard fullbody drunk
    with fade

    show richard icon drunk at left onlayer mcsprite
    db "...Can...{p=1.0}
    Can't find my..."
    #realization sfx(?)
    db "'Ey! You! You take my wallet?!" #change formatting
    hide richard icon drunk at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    "{i}I bat my eyes at him."
    s "Sorry?"
    hide sachi mask icon at left onlayer mcsprite

    show richard icon drunk at left onlayer mcsprite
    db "What? Y'dunno English or something?"
    hide richard icon drunk at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    "{i}I motion to the bouncer, who nods and swiftly takes care of him. I slip
    out of the scene and into a dark corner."

    hide richard fullbody drunk
    hide richard fullbody
    with dissolve

    "{i}Three hundred dollars in cash and a platinum AmEx. Not a bad haul if you
    ask me."

    "{i}I usually have to wait {i}after{/i} the fun behind closed doors starts.
    So being able to keep my dignity is definitely a plus."
    hide sachi mask icon at left onlayer mcsprite

    $ N1_Wallet = True
    jump N1_Menu

label Vincent_N1:
    show sachi mask icon at left onlayer mcsprite
    "{i}...{w=1.0}I feel like I'm being watched."

    "{i}It's not uncommon. Predators zone in before they kill."

    "{i}I look around in search for a perpetrator. And sure enough, I find him in
    seconds' time."

    show vincent fullbody masked
    with dissolve

    "{i}He looks...out of place. Far too put together for a joint like this."

    "{i}The men here are well off, that's for sure...but he seems refined in a way
    the others aren't."

    "{i}The other girls can tell too. I can see some of them eyeing him from afar."

    "{i}Have I seen his face somewhere?{p=1.0}
    It's hard to tell with the mask..."

    menu:
        "Keep Staring":
            "{i}I stare him straight in the eye. He isn't phased."

        "Look Away":
            "{i}There's something...strangely intense about the way he's staring."
            "{i}It isn't the same type of sleazy eyefuck you get from most guys
            here."
            "{i}He's...cold. Almost Machiavellian."
    "{i}He gets up and starts to make his way towards me."

    "{i}Upon closer inspection, he seems younger than most clientele, probably in
    his mid-twenties or so."
    menu:
        "Hey, handsome.":
            "{i}He doesn't reply."

        "Do you need something, sir?":
            "{i}He nods."
    "{i}The man leans in, his voice low."
    hide sachi mask icon at left onlayer mcsprite

    show vincent mask icon at left onlayer mcsprite
    qb "I need to talk to you. Come with me."
    hide vincent mask icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    s "You need to pay-{w=2.0}{nw}"
    hide sachi mask icon at left onlayer mcsprite

    show vincent mask icon at left onlayer mcsprite
    qb "That's taken care of."
    hide vincent mask icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    menu:
        "Go with him":
            hide sachi mask icon at left onlayer mcsprite
            jump chattalk
        "Object":
            s "I...will check with the front first."
            hide sachi mask icon at left onlayer mcsprite

            show vincent mask icon at left onlayer mcsprite
            qb "It's urgent. I don't have a lot of time."
            hide vincent mask icon at left onlayer mcsprite

            show sachi mask icon at left onlayer mcsprite
            s "I'm sorry, sir. {w=1.0}Protocol."
            "{i}He nods, frowning."
            hide sachi mask icon at left onlayer mcsprite

            show vincent mask icon at left onlayer mcsprite
            qb "...Fine. Make it quick."
            hide vincent mask icon at left onlayer mcsprite

            hide vincent fullbody masked
            with fade

            show sachi mask icon at left onlayer mcsprite
            "{i}I walk up to the hostess and point at him."
            s "...Did he ask for me?"
            hide sachi mask icon at left onlayer mcsprite

            #SHOW HOSTESS ICON !!!!!!!!!!!!
            h "H-huh? Oh, did he?"

            show sachi mask icon at left onlayer mcsprite
            s "...Can you check?"
            hide sachi mask icon at left onlayer mcsprite

            h "Sure. Hm...that's...{i}oh.{/i}"
            h "He's...a {i}special guest{/i}."

            show sachi mask icon at left onlayer mcsprite
            "{i}…Explains the mask."
            hide sachi mask icon at left onlayer mcsprite

            h "I would...do what he asks."

            jump vincent_minigame_intro

label vincent_minigame_intro:
    stop music fadeout 1.0
    play music caravan loop fadein 1.0
    
    "{i}I follow him into one of the backrooms."
    show bg private room
    show vincent fullbody masked
    with fade
    #scene backroom

    show sachi mask icon at left onlayer mcsprite
    s "You wanted to {color=#6b091b}ask me something?{/color}"
    hide sachi mask icon at left onlayer mcsprite

    show vincent mask icon at left onlayer mcsprite
    qb "…That’s correct."
    qb "Your real name…is {color=#6b091b}Sachi Kaur{/color}, is it not?"#(music pause, sfx surprised)
    hide vincent mask icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    "{i}...Uh-oh."
    hide sachi mask icon at left onlayer mcsprite

    stop music fadeout 1.0
    play music caravan loop fadein 1.0
    jump chattalk

label n1_part2:
    stop music fadeout 1.0
    play music susClub loop fadein 1.0
    show sachi mask icon at left onlayer mcsprite
    s "Hm. So..."
    hide sachi mask icon at left onlayer mcsprite

    if (v1_ev_4a==True):
        show sachi mask icon at left onlayer mcsprite
        s "Should I call you {i}Mr. Carmine{/i}? Or is that too informal…"
        hide sachi mask icon at left onlayer mcsprite

    elif (v1_ev_1==True and v1_ev_4a==False):
        show sachi mask icon at left onlayer mcsprite
        s "You knew my father while he used to work at-"
        hide sachi mask icon at left onlayer mcsprite

        show vincent mask icon at left onlayer mcsprite
        qb "…Carmine. That’s correct."
        hide vincent mask icon at left onlayer mcsprite

    show vincent mask icon at left onlayer mcsprite
    qb " …You can call me Vincent."
    hide vincent mask icon at left onlayer mcsprite

    if (v1_ev_4a==True):
        show sachi mask icon at left onlayer mcsprite
        s "But that’s-"
        hide sachi mask icon at left onlayer mcsprite

        show vincent mask icon at left onlayer mcsprite
        v "I’d prefer it if you {i}didn’t{/i} call me by my last name,
            actually. "
        hide vincent mask icon at left onlayer mcsprite

    elif (v1_ev_1==False and v1_ev_4a==False):
        show sachi mask icon at left onlayer mcsprite
        "{i}{color=#6b091b}Vincent?{/color} …Why does that sound so familiar?"
        hide sachi mask icon at left onlayer mcsprite

        show vincent mask icon at left onlayer mcsprite
        v "I knew your father while he used to work at Carmine. Before
            his passing."
        hide vincent mask icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        s "My-"
        hide sachi mask icon at left onlayer mcsprite

        "Vincent…{i}Carmine{/i}…"
        "…Oh my god."

        show sachi mask icon at left onlayer mcsprite
        s "You’re…the CEO’s son. I saw you on
        {i}{color=#6b091b}Time{/i}{/color} last month."
        hide sachi mask icon at left onlayer mcsprite

        show vincent mask icon at left onlayer mcsprite
        v "That’s correct."
        v "…I have reason to believe that he…{i}my father{/i}…is responsible for
         your father’s death."
        hide vincent mask icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        s "…The reports said he had a {i}stress-induced heart attack.{/i}"
        hide sachi mask icon at left onlayer mcsprite

        show vincent mask icon at left onlayer mcsprite
        v "Both you and me know that isn’t true."
        v "…Is that not what you’ve been investigating this whole time?"
        v "Everyone you’ve scammed, blackmailed, stole from…all of them had ties
         to your father somehow."
        v "And {i}coincidentally,{/i} those who treated your father the worst at his
        time in the company have received the worst…{i}punishments{/i} from you."
        v "I suspect you’ve been {i}interrogating{/i} them as well, just as
        you’ve tried to do with me."
        v "…Which is why I would like to join forces with you."
        v "I would like you to help me prove the involvement of my father in the
        murder of Rahul Kaur."
        v "Of course, your father is only one of many victims. But if I were to
        get {color=#6b091b}properly incriminating evidence{/color} for this
        incident specifically, I believe I could make a proper case against him."
        hide vincent mask icon at left onlayer mcsprite

        show sachi mask icon at left onlayer mcsprite
        menu:
            "But he's your father.":
                hide sachi mask icon at left onlayer mcsprite

                show vincent mask icon at left onlayer mcsprite
                v "..."
                v "…Only when its convenient."
                hide vincent mask icon at left onlayer mcsprite

                show sachi mask icon at left onlayer mcsprite
                "{i}So he has daddy issues. Good to know."
                hide sachi mask icon at left onlayer mcsprite

                show vincent mask icon at left onlayer mcsprite
                v "I don’t feel any familial connection to the man. He needs to
                be held accountable for what he’s done."
                hide vincent mask icon at left onlayer mcsprite

                show sachi mask icon at left onlayer mcsprite
                s "With him out of the way, {i}you{/i} would also get to be
                full-time CEO."
                s "But…yes. Accountability."
                hide sachi mask icon at left onlayer mcsprite

                show vincent mask icon at left onlayer mcsprite
                v "The company’s better in my hands than his."
                hide vincent mask icon at left onlayer mcsprite

            "You don't have another way?":
                hide sachi mask icon at left onlayer mcsprite

                show vincent mask icon at left onlayer mcsprite
                v "Men tend to be very malleable in…compromised states.
                As you’re well aware of, I’m sure."
                v "I suspect that you would be able to get the most out of his
                witnesses and accomplices."
                hide vincent mask icon at left onlayer mcsprite

        hide sachi mask icon at left onlayer mcsprite

        show vincent mask icon at left onlayer mcsprite
        v "You would be properly compensated, of course. I can provide you with
         whatever you’d like—better housing, finery, even a new job after this
         entire ordeal is over."
        hide vincent mask icon at left onlayer mcsprite

    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    jump vincent_intro_questions

label vincent_intro_questions:
    show sachi mask icon at left onlayer mcsprite
    if (what == False or why == False):
        menu:
            "What do I need to do?" if (what == False):
                hide sachi mask icon at left onlayer mcsprite

                show vincent mask icon at left onlayer mcsprite
                v "What you usually do."
                v "{color=#6b091b}Get the information you need from your clients{/color} and report
                back to me."
                v "Seeing how you dealt with me just now, that shouldn’t be too hard. "
                v " Don’t say anything too {color=#6b091b}suspicious{/color}, and use your
                {color=#6b091b}vices{/color} to your advantage."
                hide vincent mask icon at left onlayer mcsprite

                show sachi mask icon at left onlayer mcsprite
                s "{i}Vices?{/i}"
                hide sachi mask icon at left onlayer mcsprite

                show vincent mask icon at left onlayer mcsprite
                v "…{color=#6b091b}Alcohol{/color} and {color=#6b091b}sex{/color}."
                hide vincent mask icon at left onlayer mcsprite

                $ what = True
                jump what_menu

            "Why should I trust you?" if (why == False):
                hide sachi mask icon at left onlayer mcsprite

                show vincent mask icon at left onlayer mcsprite
                v "What ulterior motive could I have? If I was interested in
                your…{i}services{/i}, I would utilize them right now."
                v "I don’t have any reason to swindle you either. In fact, I
                could make any payment you wish for upfront if that eases your
                troubles."
                hide vincent mask icon at left onlayer mcsprite

                show sachi mask icon at left onlayer mcsprite
                menu:
                    "I wouldn't mind.":
                        hide sachi mask icon at left onlayer mcsprite

                        show vincent mask icon at left onlayer mcsprite
                        v "How much? Ten grand? Twenty?"
                        hide vincent mask icon at left onlayer mcsprite

                        show sachi mask icon at left onlayer mcsprite
                        s "Fifty?"
                        hide sachi mask icon at left onlayer mcsprite

                        show vincent mask icon at left onlayer mcsprite
                        v "You have a deal."
                        hide vincent mask icon at left onlayer mcsprite

                        "{i}No one in their right mind would object to that."

                    "I’m still not sold.":
                        hide sachi mask icon at left onlayer mcsprite

                        show vincent mask icon at left onlayer mcsprite
                        v "Hm. I understand."
                        hide vincent mask icon at left onlayer mcsprite

                "{i}Vincent hands me a piece of paper. An autopsy report, shredded into
                vertical strips of paper and gingerly re-taped together."

                show sachi mask icon at left onlayer mcsprite
                s "Cause of death…"
                hide sachi mask icon at left onlayer mcsprite

                show vincent mask icon at left onlayer mcsprite
                v "{color=#6b091b}Rahul Kaur was poisoned.{/color} My father paid for a
                false autopsy report."
                v "This is the real one."
                hide vincent mask icon at left onlayer mcsprite

                "{i}Vincent hands me another piece of paper."

                show vincent mask icon at left onlayer mcsprite
                v "And {i}here’s{/i} the NDA he signed to keep quiet about the whole
                ordeal."
                v "I have most hard pieces of evidence with me currently. All
                that’s left is the {color=#6b091b}witness testimonies{/color} of
                those involved."
                v "I trust that you want the man who killed your father behind
                bars, no?"
                hide vincent mask icon at left onlayer mcsprite

                "{i}Vincent hands me three other NDAs."

                show vincent mask icon at left onlayer mcsprite
                v "{color=#6b091b}Gerard Wade{/color} and {color=#6b091b}Richard
                 Bloomberg.{/color} Two current employees of Carmine who were
                 involved in the incident…"
                v "…And {color=#6b091b}Malcolm Hunt{/color}, the assistant
                pathologist who examined Rahul’s body."
                v "If you could get them to admit to what they saw, we could
                have a solid case that my father can’t pay his way out of. Not
                if I’m involved, that is."
                hide vincent mask icon at left onlayer mcsprite
                hide sachi mask icon at left onlayer mcsprite
                $ why = True
                jump vincent_intro_questions

    elif (what == True and why == True):
        hide sachi mask icon at left onlayer mcsprite
        hide vincent mask icon at left onlayer mcsprite

        jump n1_part2_2

label what_menu:
    if (alcohol_q == True and sex_q == True):
        jump vincent_intro_questions

    show sachi mask icon at left onlayer mcsprite
    menu:
        "...Alcohol?" if (alcohol_q == False):
            hide sachi mask icon at left onlayer mcsprite

            show vincent mask icon at left onlayer mcsprite
            v "Self explanatory. The more uninhibited they are, the easier it is."
            v "As long as you don’t get your client
            {color=#6b091b}too drunk{/color}, you can get a coherent answer out
            of them."
            hide vincent mask icon at left onlayer mcsprite

            $ alcohol_q = True
            jump what_menu

        "...Sex?" if (sex_q == False):
            hide sachi mask icon at left onlayer mcsprite

            show vincent mask icon at left onlayer mcsprite
            v "You usually avoid the act by getting your clients blackout drunk, no?"
            hide vincent mask icon at left onlayer mcsprite

            show sachi mask icon at left onlayer mcsprite
            s "…Maybe."
            hide sachi mask icon at left onlayer mcsprite

            show vincent mask icon at left onlayer mcsprite
            v "Impressive."
            v "Of course, I don’t want you to go through the ordeal of {i}actually{/i}
            sleeping with them. That’s a fate I wouldn’t wish upon my worst enemy. "
            v "…But you, above all people, know that men are simple creatures."
            v "As long as you continue to seduce your clients, they won’t become
            too suspicious."
            v "But laying it on too strong may not be the best thing to do,
            either…or they’ll get impatient."
            hide vincent mask icon at left onlayer mcsprite

            $ alcohol_q = True
            jump what_menu

label n1_part2_2:
    show sachi mask icon at left onlayer mcsprite
    s "Fine."
    s "…I’m in."
    hide sachi mask icon at left onlayer mcsprite

    show vincent mask icon at left onlayer mcsprite
    v "Perfect."
    hide vincent mask icon at left onlayer mcsprite

    "{i}Vincent shakes my hand."

    show vincent mask icon at left onlayer mcsprite
    v "I look forward to working with you, Miss Kaur-"
    hide vincent mask icon at left onlayer mcsprite

    show sachi mask icon at left onlayer mcsprite
    s "Sachi."
    s "You…asked me to call you Vincent, right? It’s only fair."
    hide sachi mask icon at left onlayer mcsprite

    "{i}He nods again."

    show vincent mask icon at left onlayer mcsprite
    v "…Sachi, then."
    hide vincent mask icon at left onlayer mcsprite

    jump client_select

label client_select:
    #THIS IS WHERE THE MAP WILL BE. CHOICES R VINCENT GERARD RICHARD MALCOLM
    # PLACEHOLDER MENU FOR NOW
    menu:
        "Vincent":
            "something goes here"
        "Gerard":
            "something goes here"
        "Richard":
            "something goes here"
        "Malcolm":
            "something goes here"

label vincent_n2_intro:
    return

label vincent_n2_questions:

label gerard_intro:
    jump chattalk

label richard_intro:
    jump chattalk

label malcolm_intro:
    jump chattalk

label gerard_post_minigame:

label richard_post_minigame:

label malcolm_post_minigame:

return
