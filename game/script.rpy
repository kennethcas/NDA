# --- NDA SCRIPT ---
#THIS IS A TESTING LINE
define s = Character("Sachi")
define v = Character("Vincent")
define c = Character("Vincent")
define q = Character("???")
define db = Character("Drunk Businessman")
define qb = Character("Sober Businessman")
define h = Character("Hostess")

$ N1_Wallet = False

# ---GAME START---
# testt

label start:

    # scene black

    # music: tense, ominous

    # DIALOGUE. ---

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
    # scene scarletCaberetFront
    # with fade # change transition?

    # ambience sfx: bar
    # music: jazzy? lowkey?

    # DIALOGUE. ---
    "OCTOBER 21, 1983 \nNEW YORK"

    db "...Come on, kitty. Let's have a {i}good time,{/i} yeah?"
    s "{color=#6b091b}...I want to retch.{/color}"

    menu:
        "You don't even know my name.":
            db "Well, it's not like you're gonna tell me, right?"
            db "You all go by fake ones, anyway.{w=1.0} Not that I care or
            anything."
            db "I'm not here to wine and dine you, doll."
            jump intro_expos

        "Pay up first.":
            "{color=#6b091b}I swat away his hand, which was inching dangerously
            close to my thigh.{/color}"
            s "Pay up in the front if you want a private room."
            db "Aw, come on baby. I just wanted to buy you a drink."
            jump intro_expos

        "(Ignore him.)":
            s "(sigh...)"
            jump intro_expos

label intro_expos:

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
    db "...Can...{p=1.0}
    Can't find my..."
    #realization sfx(?)
    db "'Ey! You! You take my wallet?!" #change formatting

    "I bat my eyes at him."

    s "Sorry?"
    db "What? Y'dunno English or something?"

    "I motion to the bouncer, who nods and swiftly takes care of him. I slip
    out of the scene and into a dark corner."

    "Three hundred dollars in cash and a platinum AmEx. Not a bad haul if you
    ask me."

    "I usually have to wait {i}after{/i} the fun behind closed doors starts.
    So being able to keep my dignity is definitely a plus."

    $ N1_Wallet = True
    jump N1_Menu

label Vincent_N1:
    "...{w=1.0}I feel like I'm being watched."

    "It's not uncommon. Predators zone in before they kill."

    "I look around in search for a perpetrator. And sure enough, I find him in
    seconds' time."

    "He looks...out of place. Far too put together for a joint like this."

    "The men here are well off, that's for sure...but he seems refined in a way
    the others aren't."

    "The other girls can tell too. I can see some of them eyeing him from afar."

    "Have I seen his face somewhere?{p=1.0}
    It's hard to tell with the mask..."

    menu:
        "Keep Staring":
            "I stare him straight in the eye. He isn't phased."

        "Look Away":
            "There's something...strangely intense about the way he's staring."
            "It isn't the same type of sleazy eyefuck you get from most guys
            here."
            "He's...cold. Almost Machiavellian."
    "He gets up and starts to make his way towards me."

    "Upon closer inspection, he seems younger than most clientele, probably in
    his mid-twenties or so."
    menu:
        "Hey, handsome.":
            "He doesn't reply."

        "Do you need something, sir?":
            "He nods."
    "The man leans in, his voice low."
    qb "I need to talk to you. Come with me."
    s "You need to pay-{w=2.0}{nw}"
    qb "That's taken care of."
    menu:
        "Go with him":
            jump n1_transition
        "Object":
            s "I...will check with the front first."
            qb "It's urgent. I don't have a lot of time."
            s "I'm sorry, sir. {w=1.0}Protocol."
            "He nods, frowning."
            qb "...Fine. Make it quick."
            "I walk up to the hostess and point at him."
            s "...Did he ask for me?"
            h "H-huh? Oh, did he?"
            s "...Can you check?"
            h "Sure. Hm...that's...{i}oh.{/i}"
            h "He's...a {i}special guest{/i}."
            "…Explains the mask."
            h "I would...do what he asks."
            jump n1_transition

label n1_transition:
    #black
    "I follow him into one of the backrooms."
    jump park

label n1_part2:
    jump map

label client1minigame:
    jump park
label client2minigame:
    jump park
label client3minigame:
    jump park

label n3_intro_and_selection:
    #FINISH
    return

label n4_intro:
    #FINISH
    return

label minigame2:
    jump park

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
    jump park

label successful3A:
    #FINISH
    return
label unsuccessful3B:
    #FINISH
    return
