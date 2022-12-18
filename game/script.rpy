# --- NDA SCRIPT ---
define s = Character("Sachi")
define v = Character("Vincent")
define q = Character("???")
define db = Character("Drunk Businessman")
define qb = Character("Sober Businessman")
define h = Character("Hostess")

define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.7
define config.default_voice_volume = 07

$ N1_Wallet = False

# ---GAME START---
label start:

    # scene black

    # music: tense, ominous
    play music profoundSadness loop fadein 1.0

    # DIALOGUE. ---
    menu:
        "SKIP INTRO, GO TO MINIGAME":
            jump vincent_minigame
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
    s "{color=#6b091b}...I want to retch.{/color}"

    menu:
        "You don't even know my name.":
            hide sachi mask icon at left onlayer mcsprite
            show richard icon at left onlayer mcsprite
            db "Well, it's not like you're gonna tell me, right?"
            db "You all go by fake ones, anyway.{w=1.0} Not that I care or
            anything."
            db "I'm not here to wine and dine you, doll."
            hide richard icon at left onlayer mcsprite
            jump intro_expos

        "Pay up first.":
            hide sachi mask icon at left onlayer mcsprite
            "{color=#6b091b}I swat away his hand, which was inching dangerously
            close to my thigh.{/color}"
            show sachi mask icon at left onlayer mcsprite
            s "Pay up in the front if you want a private room."
            hide sachi mask icon at left onlayer mcsprite
            show richard icon at left onlayer mcsprite
            db "Aw, come on baby. I just wanted to buy you a drink."
            jump intro_expos

        "(Ignore him.)":
            show sachi mask icon at left onlayer mcsprite
            s "(sigh...)"

            jump intro_expos

label intro_expos:
    hide richard fullbody 
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
            jump CW2_N1
        "Sober Businessman":
            jump Vincent_N1

#if you choose CW#2:
label CW2_N1:
    show richard fullbody
    with fade
    show richard icon at left onlayer mcsprite
    db "...Can...{p=1.0}
    Can't find my..."
    #realization sfx(?)
    db "'Ey! You! You take my wallet?!" #change formatting

    hide richard icon at left onlayer mcsprite
    "I bat my eyes at him."
    show sachi mask icon at left onlayer mcsprite
    s "Sorry?"
    hide sachi mask icon at left onlayer mcsprite
    show richard icon at left onlayer mcsprite
    db "What? Y'dunno English or something?"
    hide richard mask icon at left onlayer mcsprite
    show sachi mask icon at left onlayer mcsprite
    "{i}I motion to the bouncer, who nods and swiftly takes care of him. I slip
    out of the scene and into a dark corner."
    hide richard fullbody
    with dissolve
    "{i}Three hundred dollars in cash and a platinum AmEx. Not a bad haul if you
    ask me."

    "{i}I usually have to wait {i}after{/i} the fun behind closed doors starts.
    So being able to keep my dignity is definitely a plus."
    hide sachi mask icon at left onlayer mcsprite
    hide richard icon at left onlayer mcsprite

    $ N1_Wallet = True
    jump N1_Menu

label Vincent_N1:
    show sachi mask icon at left onlayer mcsprite
    "{i}...{w=1.0}I feel like I'm being watched."

    "{i}It's not uncommon. Predators zone in before they kill."

    "{i}I look around in search for a perpetrator. And sure enough, I find him in
    seconds' time."
    show vincent fullbody
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
            hide vincent fullbody
            with fade
            show sachi mask icon at left onlayer mcsprite
            "{i}I walk up to the hostess and point at him."
            s "...Did he ask for me?"
            #SHOW HOSTESS ICON !!!!!!!!!!!!
            h "H-huh? Oh, did he?"
            s "...Can you check?"
            h "Sure. Hm...that's...{i}oh.{/i}"
            h "He's...a {i}special guest{/i}."
            "…Explains the mask."
            h "I would...do what he asks."
            jump vincent_minigame_intro

label vincent_minigame_intro:
    "I follow him into one of the backrooms."
    show bg private room
    with fade
    #scene backroom
    show vincent fullbody
    show sachi mask icon at left onlayer mcsprite
    s "You wanted to {color=#6b091b}ask me something?{/color}"
    hide sachi mask icon at left onlayer mcsprite
    show vincent mask icon at left onlayer mcsprite
    qb "…That’s correct."
    qb "Your real name…is {color=#6b091b}Sachi Kaur{/color}, is it not?"
    #(music pause, sfx surprised)
    hide vincent mask icon at left onlayer mcsprite
    show sachi mask icon at left onlayer mcsprite
    "{i}...Uh-oh."
    hide sachi mask icon at left onlayer mcsprite
    jump chattalk

label n1_part2:
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
    hide sachi mask icon at left onlayer mcsprite

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
        show sachi mask icon at left onlayer mcsprite
        "…Oh my god."

    hide vincent mask icon at left onlayer mcsprite
    hide sachi mask icon at left onlayer mcsprite
    jump n2_intro

label n2_intro:
    "testing testing"
    return
label gerard_intro:
    jump chattalk
label richard_intro:
    jump chattalk
label malcolm_intro:
    jump chattalk

label n3_intro_and_selection:
    #FINISH
    return

label n4_intro:
    #FINISH
    return

label minigame2:
    jump chattalk

label unsuccessful2A:
    return
label unsuccessful2B:
    return

label ending1:
    return
label ending2:
    return
label ending3:
    return

label minigame3:
    jump chattalk

label successful3A:
    #FINISH
    return
label unsuccessful3B:
    #FINISH
    return
