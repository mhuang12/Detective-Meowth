# The script of the game goes in this file. let the spaghettification commence

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define meowth = Character("Detective Meowth", image="meowth")
define meowth2 = Character("Detective Meowth", image="meowth2") # meowth's evil twin! >:)
define brewster = Character("Coffee Machine")
define shy = Character("Shy Guy")
define kirby = Character("Kirby")
define ditto = Character("Jerry")
define annie = Character("Annie")
define fakeannie = Character("\"Annie\"")
define moe = Character("Moe")
define rocky = Character("Bartender", image="rocky")
define phoneguy = Character("VOICE")

define shy_u = Character("Masked Hoodie")
define annie_u = Character("Anemone Hair")
define kirby_u = Character("Bouncy Boyo?")

default shy1 = False
default kirby1 = False
default annie1 = False

default shy2 = False
default kirby2 = False
default annie2 = False

# CLUE TRACKING FLAGS
default cf_1stain = False
default cf_1brewster = False
default cf_2photo = False
default cf_3headphones = False
default cf_3computer = False

# INTERROGATION LOOP: check if meowth said his first line yet
default int1 = False
default inv1 = False
default int2 = False
default inv2 = False

# GAME STATE TRACKER
# 0 - bar
# 1 - flashback
# 2 - investigation
default location = 1

# IMAGE DEFINITIONS

image static = "static.png"
image brewster = "brewster_machine.png"

image meowth = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth.png",
    "not _last_say_who=='meowth'", "meowth_dark.png"
)
image meowth happy = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_happy.png",
    "not _last_say_who=='meowth'", "meowth_happy_dark.png"
)
image meowth mad = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_mad.png",
    "not _last_say_who=='meowth'", "meowth_mad_dark.png"
)
image meowth inquisitive = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_inquisitive.png",
    "not _last_say_who=='meowth'", "meowth_inquisitive_dark.png"
)
image meowth silly = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_silly.png",
    "not _last_say_who=='meowth'", "meowth_silly_dark.png"
)
image meowth confused = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_confused.png",
    "not _last_say_who=='meowth'", "meowth_confused_dark.png"
)
image meowth sad = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_cry.png",
    "not _last_say_who=='meowth'", "meowth_cry_dark.png"
)
image side meowth sidepfp = "meowth_grayside.png"
image side meowth sidepfp_inquisitive = "meowth_grayside_inquisitive.png"
image side meowth sidepfp_confused = "meowth_grayside_confused.png"
image side meowth sidepfp_mad = "meowth_grayside_mad.png"
image side meowth2 sidepfp = "meowth_side.png"
image side meowth2 sidepfp_mad = "meowth_side_mad.png"
image side meowth2 sidepfp_sad = "meowth_side_cry.png"

image rocky = ConditionSwitch(
    "_last_say_who=='rocky'", "rocky.png",
    "not _last_say_who=='rocky'", "rocky_dark.png"
)
image rocky face= ConditionSwitch(
    "_last_say_who=='rocky'", "rocky_eyebrow.png",
    "not _last_say_who=='rocky'", "rocky_eyebrow_dark.png"
)
image side rocky sidepfp = "rocky_side.png"
image side rocky sidepfp_face = "rocky_side_eyebrow.png"

image shy = ConditionSwitch(
    "_last_say_who=='shy' or _last_say_who=='shy_u'", "shy.png",
    "not (_last_say_who=='shy' or _last_say_who=='shy_u')", "shy_dark.png"
)
image shy mad = ConditionSwitch(
    "_last_say_who=='shy' or _last_say_who=='shy_u'", "shy_mad.png",
    "not (_last_say_who=='shy' or _last_say_who=='shy_u')", "shy_mad_dark.png"
)

image shy shy = ConditionSwitch(
    "_last_say_who=='shy' or _last_say_who=='shy_u'", "shy_shy.png",
    "not (_last_say_who=='shy' or _last_say_who=='shy_u')", "shy_shy_dark.png"
)

image kirby = ConditionSwitch(
    "_last_say_who=='kirby' or _last_say_who=='kirby_u'", "kirby.png",
    "not (_last_say_who=='kirby' or _last_say_who=='kirby_u')","kirby_dark.png"
)
image kirby confused = ConditionSwitch(
    "_last_say_who=='kirby' or _last_say_who=='kirby_u'", "kirby_confused.png",
    "not (_last_say_who=='kirby' or _last_say_who=='kirby_u')","kirby_confused_dark.png"
)
image kirby happy = ConditionSwitch(
    "_last_say_who=='kirby' or _last_say_who=='kirby_u'", "kirby_happy.png",
    "not (_last_say_who=='kirby' or _last_say_who=='kirby_u')","kirby_happy_dark.png"
)

image annie = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe' or _last_say_who=='annie_u'", "annie.png",
    "not (_last_say_who=='annie' or _last_say_who=='moe' or _last_say_who=='annie_u')", "annie_dark.png"
)
image annie shy = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe' or _last_say_who=='annie_u'", "annie_shy.png",
    "not (_last_say_who=='annie' or _last_say_who=='moe' or _last_say_who=='annie_u')", "annie_shy_dark.png"
)
image annie sad = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe' or _last_say_who=='annie_u'", "annie_sad.png",
    "not (_last_say_who=='annie' or _last_say_who=='moe' or _last_say_who=='annie_u')", "annie_sad_dark.png"
)

# Annie with moe
image moe = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", "moe.png",
    "not (_last_say_who=='annie' or _last_say_who=='moe')", "moe_dark.png"
)
image moe mad = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", "moe_mad.png",
    "not (_last_say_who=='annie' or _last_say_who=='moe')", "moe_mad_dark.png"
)
image moe mad_nottalking = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", "moe_mad_nottalking.png",
    "not (_last_say_who=='annie' or _last_say_who=='moe')", "moe_mad_nottalking_dark.png"
)
image moe sad = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", "moe_sad.png",
    "not (_last_say_who=='annie' or _last_say_who=='moe')", "moe_sad_dark.png"
)
image moe shy = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", "moe_shy.png",
    "not (_last_say_who=='annie' or _last_say_who=='moe')", "moe_shy_dark.png"
)
image moe speak = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", "moe_speak.png",
    "not (_last_say_who=='annie' or _last_say_who=='moe')", "moe_speak_dark.png"
)
image moe speak_sad = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", "moe_speak_sad.png",
    "not (_last_say_who=='annie' or _last_say_who=='moe')", "moe_speak_sad_dark.png"
)
image moe speak_shy = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", "moe_speak_shy.png",
    "not (_last_say_who=='annie' or _last_say_who=='moe')", "moe_speak_shy_dark.png"
)

# fun little jump when they talk
transform talk_jump:
    ease .06 yoffset 15
    ease .06 yoffset -15
    ease .05 yoffset 7
    ease .05 yoffset -7
    ease .01 yoffset 0

# noir grayscale
transform gray:
    matrixcolor SaturationMatrix(0)

# preserving bgm after loading in from save
label after_load:
    if location == 0:
        play music "Cool Vibes.mp3" loop fadein 1.0 volume 2
    elif location == 1:
        play music "Hard Boiled.mp3" loop fadein 1.0
    else:
        play music "464923__plasterbrain__jazz-loop-rusted-maid.flac" loop fadein 1.0 volume 0.35
    return


# The game starts here.
# INTRO
label start:

    $ location = 0
    play music "Cool Vibes.mp3" loop fadein 1.0 volume 2
    play audio "main-door-opening-closing-38280.mp3" volume 1.5
    play audio "doorbell.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene milkbar with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    pause 4
    show meowth at left, talk_jump with dissolve
    meowth "The usual, please."

    show rocky at right, talk_jump
    rocky "The usual? Who're you?"
    meowth "Your finest Moomoo Milk, on the rocks."
    show rocky face at right, talk_jump
    rocky "..."
    rocky "Who do you think you are?"
    meowth "Who, me?"
    show rocky at right
    rocky "Who else?"
    show meowth happy at left, talk_jump
    meowth "Why, I'm glad you asked! Ahem..."
    meowth "Prepare for justice, I'm on the case!"
    meowth "On the double - I'll always give chase!"
    meowth "To protect the world from unsolved mystery!"
    meowth "To be the best gumshoe in all of history!"
    meowth "To follow all trails and find all clues!"
    meowth "To get super famous once I'm on the news!"
    meowth "Meowth solves crimes and denies all lies!"
    meowth "Surrender now, if ya got no alibi!"
    meowth "MEOWTH! THAT'S RIGHT!"
    rocky "Nope, doesn't ring a bell."
    show meowth at left
    meowth "..."
    meowth "Awright. News takes time to travel, I get it."
    meowth "My exploits - {w=0.1}I mean, my heroic deeds will be known all across the world soon enough."
    rocky "Sure."
    meowth "What, ya don't believe me?"
    meowth "Fine. For you, my friend, I'll tell you about my most thrilling adventure yet."
    meowth "Something that would make that yellow idiot turn his spiky tail and run. "
    show meowth happy at left, talk_jump
    meowth "This is stuff the press won't tell ya."
    rocky "I think I see another customer-"
    meowth "Listen closely to this shocking tale of deceit, love, and one noble cat's pursuit of the truth above all else!"
    rocky "No, really, that's quite alright-"
    meowth "It all started yesterday..."

    jump acti


# ACT I
label acti:

    $ location = 1
    play music "Hard Boiled.mp3" loop fadein 1.0
    scene apartment with fade

    show meowth at center, gray, talk_jump
    meowth "{i}I was going through my normal morning routine...{/i}"
    meowth "{i}Filing my claws, straightening my tie, drinking my coffee and eating cherry pie, when I received a call...{/i}"
    "*telephone rings*"
    show meowth inquisitive at center, gray, talk_jump
    meowth "Meowth Detective Agency, how may I help you?"
    phoneguy "Oh god, please help us! There's been a-"
    meowth "Brrzt - please wait while I transfer you over to the number one detective in the city!"
    meowth "..."
    meowth "Yello, detective Meowth speakin'. How can I help ya?"
    phoneguy "It's awful, there's blood everywhere and-"
    phoneguy "Wait... Meowth? I thought this was Detective Pika-"
    show meowth mad at center, gray, talk_jump
    meowth "Zip it, pal! Tell me about the case."
    meowth "Ol' Meowth will have it solved before you can say \"Meowth, that's right!\""
    phoneguy "Whatever! Just get over here quick!"
    meowth "{i}And so I went. Armed with nothing but my wits, my pen, and my dapper looks, off to solve the mystery of a lifetime...{/i}"
    rocky "Oh boy..."

    scene cafe with dissolve
    show shy at left with dissolve
    show kirby at center with dissolve
    show annie at right with dissolve

    meowth sidepfp "Awright, Detective Meowth on the scene. What's all the ruckus?"
    shy_u "Who're you?"
    meowth "Why, me? I'm glad you asked...  Ahem! To-"
    annie_u "No... Brewster... he was so young..."
    kirby_u "Poyo..."
    shy "Take a look behind the counter."
    meowth "{i}And so I did. What I saw behind the counter was... the lifeless body of Brewster, the brand new coffee machi - I mean, barista at their office lobby's coffee shop.{/i}"
    meowth "{i}It was a grim sight...{/i}"
    
    # reality interject
    show static
    pause 0.33
    hide static

    show brewster at truecenter with dissolve
    rocky sidepfp "A Brewster? I have one of those right here."
    meowth2 sidepfp "No, no, it most definitely was not a coffee machine! It was actually Brewster!"
    meowth2 "Ahem... where was I? Oh, right..."
    hide brewster with dissolve

    # noir returns
    show static
    pause 0.33
    hide static

    meowth sidepfp "Hmm... a troubling case indeed..."
    shy_u "So? Can you help us?"
    meowth "Can I help you? I'll take the case - and I'll crack it wide open!"

    stop music fadeout 1.0
    play music "464923__plasterbrain__jazz-loop-rusted-maid.flac" loop fadein 1.0 volume 0.35
    $ location = 2

    
    
# INVESTIGATION PRELIM
label investigate_1i: #interview
    if not int1:
        meowth sidepfp_inquisitive "{i}I should see what these guys know before I take a look around.{/i}"
        $ int1 = True
    else:
        show meowth at left, gray
        meowth "{i}Let's talk to the remaining guys.{/i}"
    menu:
        "Masked Hoodie":
            scene cafe
            show shy at right
            show meowth inquisitive at left, gray, talk_jump
            $ shy1 = True
            meowth "First things first. What's your name, and what do you do here?"
            shy "Uhh, I'm Shy Guy. I work in marketing."
            show meowth at left, gray
            meowth "Tough luck, huh?"
            shy "Tell me about it."
            show meowth inquisitive at left, gray, talk_jump
            meowth "Alright, Mr. Guy. I'm gonna need to know where you were last night."
            shy "Last night? Well... I stayed late to finish up work."
            shy "I'm the only one our crazy boss hired for marketing, so I have to do everything myself."
            show meowth confused at left, gray, talk_jump
            meowth "Stayed late, huh? Interesting. And just who is this boss of yours?"
            shy "Well, the thing is, he hardly comes into work. In fact, the last time I saw him was when I got hired."
            show meowth at left, gray
            meowth "You should consider a career change, pal."
            shy "Yeah..."
            jump investigate_1i_check
            
        "Bubbly Bubblegum?":
            scene cafe
            show kirby at right
            show meowth inquisitive at left, gray, talk_jump
            $ kirby1 = True
            meowth "What's up with you, beach ball?"
            show kirby happy at right, talk_jump
            kirby "Poyo!"
            show meowth at left, gray
            meowth "Well, it's a pleasure to meet you too, Kirby."
            meowth "You're the intern, huh? Lemme guess. Unpaid?"
            show kirby at right
            kirby "Poyo..."
            show meowth inquisitive at left, gray, talk_jump
            meowth "Figures. Now, what was a lil guy like you doin' last night?"
            kirby "Poyo!"
            show meowth confused at left, gray, talk_jump
            meowth "You... went back to your home planet after work? Using a star?"
            kirby "Poyo!"
            show meowth at left, gray
            meowth "You commute from Planet Popstar? Sure, kid. I'll take it you saw nothin', then."
            jump investigate_1i_check

        "Anemone Hair":
            scene cafe
            show annie at right
            show meowth inquisitive at left, gray, talk_jump
            $ annie1 = True
            meowth "Alright, ma'am. What's your name, and what do you do here?"
            annie "I'm Annie. I do IT."
            show meowth happy at left, gray, talk_jump
            meowth "Woah, we got a smart guy over here, huh? Wanna tell me where you were last night?"
            annie "I went straight home. The less time I have to spend in this office the better."
            show meowth inquisitive at left, gray, talk_jump
            meowth "And you didn't see anything?"
            annie "Nope."
            show meowth at left, gray
            meowth "Great."
            annie "Yeah."
            meowth "Uh-huh."
            jump investigate_1i_check


label investigate_1i_check:
    if shy1 and kirby1 and annie1:
        jump investigate_1
    else:
        jump investigate_1i

label investigate_1:

    scene cafe # game background
    if not inv1:
        meowth sidepfp "{i}I should have a look around and see what clues I can find.{/i}"
        $ inv1 = True
    call screen investigate_game_1 # clues as imagebutton overlay
    
    # starts game screen, pauses VN
    # each clue is a button to be pressed
    # each clue jumps to its own scene with explanation
    # after explanation ends, go back to investigation
    # once player clicks leave button, meowth checks relevant clues
    # if yes, he asks the player if player wants to leave
    # if player does not want to leave or if not all relevant clues found, return to jump back to this label


# CLUES - format: xy where x is the room number and y is the clue number
# Rooms: 1 - cafe
#        2 - office
#        3 - server room
# check_game_x: see if player obtained all relevant clues in this room: ask to leave if Y, go back to investigation if N

label clue1table:
    scene cafe
    show clue_1table_closeup at truecenter with dissolve
    meowth sidepfp "{i}An ordinary table.{/i}"
    show clue_1table_closeup with dissolve
    jump investigate_1

label clue1stain:
    scene cafe
    show clue_1stain_closeup at truecenter with dissolve
    meowth sidepfp "{i}An ordinary ta- wait a minute. What's that on the side?{/i}" # Meowth explanation of clue
    meowth "{i}...A stain? It couldn't be...{/i}"
    $ cf_1stain = True # Clue flag setting
    hide clue_1stain_closeup with dissolve
    jump investigate_1 # Jump to relevant clue collection check for this room

label clue1brewster:
    scene cafe
    show clue_1brewster_closeup at truecenter with dissolve
    meowth sidepfp "{i}Poor birdie... all he ever wanted was to make delicious coffee and they got 'im...{/i}"
    meowth "{i}It's enough to bring a cat to tears... I'll remember ya, pal...{/i}"
    meowth "{i}Hmm... I don't see any obvious causes of death. No sharp objects were used. His head is covered in blood... could it be...?{/i}"
    $ cf_1brewster = True
    hide clue_1brewster_closeup with dissolve
    jump investigate_1

label clue1coffee:
    scene cafe
    show clue_1coffee_closeup at truecenter with dissolve
    meowth sidepfp "{i}Looks delicious... but I gotta focus!{/i}"
    hide clue_1coffee_closeup with dissolve
    jump investigate_1

label clue1painting: #MISSING IMAGE!!!!!!!!!!!!
    scene cafe
    meowth sidepfp "{i}Real fancy place they got here. Feels pretentious.{/i}"
    jump investigate_1

label clue1ditto:
    scene cafe
    show clue_1ditto_closeup at truecenter with dissolve
    meowth sidepfp "{i}What is this guy doing here? Go figure, they shill for DittoCoin...{/i}"
    hide clue_1ditto_closeup with dissolve
    jump investigate_1

label check_game_1: # Clue collection check for room 1, after player clicks leave button
    if cf_1stain and cf_1brewster: # Check all flags have been collected
        meowth sidepfp "{i}Alright, I think I got everything I needed from here. Is it time to leave?{/i}" # Ask player to leave
        menu:
            "Leave":
                jump investigate_1e # Move on
            "Look for more clues":
                meowth "Let's look again... a little curiosity never killed the cat."
                jump investigate_1 # Investigation loop

    else:
        meowth sidepfp_inquisitive "{i}I can't quite put my paw on it, but I feel like I'm missing something...{/i}"
        jump investigate_1


label investigate_1e:
    stop music fadeout 1.0
    play music "Hard Boiled.mp3" loop fadein 1.0
    $ location = 1

    scene cafe
    show shy at right, talk_jump
    show meowth at left, gray
    shy "That's it? You're not gonna do an autopsy or anything?"
    shy "Did you even figure it out yet?"
    show meowth mad at left, gray, talk_jump
    meowth "Cool it, Mr. Guy. There's only so much I can do without my equipment."
    meowth "This was pretty short notice, so I had to reschedule all my other cases - I'm busy, ya know."
    show annie at center
    annie "I knew we should've just called the cops instead. How did this... quack even get here?"
    meowth "Woah, don't call the heat. Just let me work my magic."
    shy "This guy..."
    meowth "Why don'tcha show me your office, tough guy?"
    shy "Go on ahead without me. Annie and Kirby can show you."
    meowth "{i}At that time, I was so naive. I had no clue what I was gettin' myself into.{/i}"
    meowth"{i}The game...{w=0.2} had only just begun.{/i}"

    # reality interject
    show static
    pause 0.33
    hide static

    rocky sidepfp "Alright, hold on just a second."
    meowth2 sidepfp_mad "What?! Can'tcha save the questions 'til the end?"
    rocky sidepfp_face "Who would ever hire a two-bit \"detective\" like you for a \"murder\" - if there even was one?"
    meowth2 "Watch it, pebble. Some may call me a stray, but I prefer the term...{w=0.2} \"free agent.\""
    meowth2 "A private eye like me sees what everyone else can't - the cold, hard truth."
    rocky "Really? Why in the world didn't those office workers just... call the police?"
    meowth2 "The fuzz kill the vibe! They're not gonna get anything done!"
    meowth2 sidepfp_sad "Besides, all those Growlithe and Arcanine give me the creeps... I mean, I'm not scared! Nope, not me!"
    rocky "Sure..."
    meowth2 sidepfp "Anyways - where was I? Oh, right..."
    meowth2 "Off I went to investigate the workplace of these adorable but suspicious gaggle of workers..."
    meowth2 "Everyone keeps their claws out... I have to keep mine sharp."
    rocky sidepfp "Whatever that means."

    # noir returns
    show static
    pause 0.33
    hide static

label actii:

    scene office with dissolve
    show kirby at right with dissolve
    show meowth inquisitive at left, talk_jump, gray with dissolve

    meowth "So... what do you do here, exactly?"
    kirby "Poyo."
    meowth "DittoCoin? Sounds like a scam."

    show moe shy at center, talk_jump
    annie "Hey, can you guys keep it down? I'm trying to get some work done."
    show meowth confused at left, gray, talk_jump
    meowth "Annie? Weren't you just -"
    show moe
    annie "Shhh."
    meowth "Tough crowd, huh."
    kirby "Poyo?"
    meowth "Yeah, I was wonderin' where Mr. Guy ran off to..."
    show shy at right, talk_jump
    shy "I'm right here."
    show meowth happy at left, talk_jump, gray
    meowth "Woah! Caught up quick, huh?"
    shy "What are you doing here?"
    show meowth at left, gray
    meowth "Well, didn't I just tell ya? I'm here to investigate your office."
    meowth "Jeez, what is with everyone forgettin' things today?"
    shy "Well, go ahead and look around. Nothing is off limits for our detective, uh... friend."

    play music "464923__plasterbrain__jazz-loop-rusted-maid.flac" loop fadein 1.0 volume 0.35
    $ location = 2

label investigate_2:
    
    scene office
    if not inv2:
        meowth sidepfp "{i}Let's have a looksie, then.{/i}"
        $ inv2 = True
    call screen investigate_game_2

label clue_2drawer:
    show clue_2drawer_closeup at truecenter with dissolve
    meowth sidepfp_confused "{i}I see a crumpled up love-letter to... Brewster?!{/i}"
    meowth "{i}It reads...{/i}"
    meowth "\"Dear Brewster,"
    meowth "I have been working in this office with you for quite a long time and I have always admired your bushy mustache."
    meowth "I love nothing more than getting drinks with you."
    meowth "NO NO NO THEY CAN'T SEE THIS"
    meowth "HE CAN NEVER SEE THIS"
    meowth "NEVER NEVER NEVER!!!\""
    meowth sidepfp "{i}...Interesting.{/i}"
    hide clue_2drawer_closeup at truecenter with dissolve
    jump reading_trigger

label clue_2photo:
    show clue_2photo_closeup at truecenter with dissolve
    $ cf_2photo = True
    meowth sidepfp "{i}A picture with a bunch of DittoCoin employees...{/i}"
    meowth "{i}But the frame is cracked. Hmm...{/i}"
    meowth sidepfp_inquisitive "{i}Who's this blue Ditto fella?{/i}"
    meowth "{i}I haven't seen him around town. No one must've introduced 'em to me.{/i}"
    hide clue_2photo_closeup at truecenter with dissolve
    jump investigate_2

label clue_2burger:
    show clue_2burger_closeup at truecenter with dissolve
    meowth sidepfp "{i}Gross... and he ate the wrapper too.{/i}"
    "(The letters NNIE are visible on the wrapper)"
    hide clue_2burger_closeup at truecenter with dissolve
    jump investigate_2

label clue_2pencil:
    show clue_2pencil_closeup at truecenter with dissolve
    meowth sidepfp "{i}It's a number 4 pencil.{/i}"
    hide clue_2pencil_closeup at truecenter with dissolve
    jump investigate_2

label clue_2computer:
    show clue_2computer_closeup at truecenter with dissolve
    meowth sidepfp_mad "{i}I see some game about monkeys popping balloons on the monitor... these employees sure are working hard.{/i}"
    hide clue_2pencil_closeup at truecenter with dissolve
    jump investigate_2

label clue_2ditto:
    show clue_2ditto_closeup at truecenter with dissolve
    meowth sidepfp_mad "Hey! How'd you get out of my satchel?! You might tamper with evidence."
    hide clue_2ditto_closeup at truecenter with dissolve
    jump investigate_2


label check_game_2: # Clue collection check for room 1, after player clicks leave button
    if cf_2photo: # Check all flags have been collected
        meowth sidepfp "{i}Alright, I think I got everything I needed from here. Is it time to leave?{/i}" # Ask player to leave
        menu:
            "Leave":
                jump investigate_2i # Move on
            "Look for more clues":
                meowth "Let's look again... a little curiosity never killed the cat."
                jump investigate_2 # Investigation loop

    else:
        meowth sidepfp_inquisitive "{i}I can't quite put my paw on it, but I feel like I'm missing something...{/i}"
        jump investigate_2

label reading_trigger:
    scene office
    show shy at right
    show meowth at left, gray
            
    meowth "Alright, Mr. Guy. Care to explain this love letter?"
    show shy angry at right, talk_jump
    shy "Hey! You can't just go snooping through someone's desk!"
    show meowth angry at left, talk_jump, gray
    meowth "Are you kiddin'? You just said nothing is off limits."
    shy "No, I did not! I told you to follow Kirby!" 
    meowth "That was before, bub."
    shy "No! That was the last thing I said to you!" 
    meowth "No it wasn't."
    shy "Yes it was!" 
    meowth "No, I don't think it was."
    shy "Yes it was!" 
    meowth "No, I really don't think-"
    shy "Yes it was!"
    show meowth inquisitive at left, talk_jump, gray
    meowth "Alright! Fine. But that doesn't explain this note."
    meowth "You wrote in big letters that Brewster can never know about your secret."
    meowth "Dubious, is it not?"
    show shy shy at right, talk_jump
    shy "What is that??"
    meowth "Playing dumb won't get you out of this one, sport."
    shy "Um, I mean... That was just me writing to myself, I swear! It don't mean nothing."
    meowth "Double negative, huh?"
    shy "No!! It does not mean no- I mean, anything!"
    meowth "Look, I get it. Love is fickle... "
    show meowth sad at left, talk_jump, gray
    meowth "If anyone knows anything about unrequited love, it's me."
    meowth "Oh, my sweet Meowzie... I miss you..."
    shy "Honestly... I just couldn't bring myself to throw it away. I should probably do that."
    show meowth inquisitive at left, talk_jump, gray
    meowth "Hold it! Do you know who that blue guy is?"
    show shy at right
    shy "You can ask Kirby..."
    hide shy
    "He runs away to dispose of his embarassing note."
    jump investigate_2


label investigate_2i:
    if not int2:
        meowth "{i}I should see what these fellas know.{/i}"
        $ int2 = True
    else:
        show meowth at left, gray
        meowth "{i}Let's talk to the remaining guys.{/i}"
    menu:
        "Kirby":
            scene office
            show kirby at right
            show meowth happy at left, gray, talk_jump
            $ kirby2 = True
            
            meowth "How's it hangin', my spherical friend?"
            show kirby happy at right, talk_jump
            kirby "Poyo!"
            meowth "Glad to hear it!"
            show meowth inquisitive at left, gray, talk_jump
            meowth "Hey, Kirbs. I saw this blue guy in one of those group photos, but I haven't seen 'em around."
            meowth "Do ya know anything about this?"
            show kirby at right
            kirby "Poyo!"
            meowth "I see. He's da boss, the real Giovanni of the operation, huh?"
            kirby "Poyo!"
            meowth "So... where is this boss 'a yours?"
            kirby "Poyo!"
            show meowth confused at left, gray, talk_jump
            meowth "He just sends Teams messages with ominous requests and rants about... cryptocurrency?"
            meowth "What a real pain in the neck, huh?"
            kirby "Poyo!"
            show meowth at left, gray
            meowth "Alright, guess that rules him out as quick as I suspected him."
            kirby "Poyo!"
            meowth "So... uhh... I'm outta leads."
            meowth "..."
            show meowth inquisitive at left, gray, talk_jump
            meowth "Did you do it?"
            show kirby confused at right, talk_jump
            kirby "Poyo." 
            show meowth mad at left, gray, talk_jump
            meowth "Rats! You were supposed ta confess! This was gonna be my big break!"
            show kirby happy at right, talk_jump
            kirby "Poyo!"
            show meowth at left, gray
            meowth "Yeah, yeah, I'll keep lookin'."
            jump investigate_2i_check
        "Shy Guy":
            scene office
            show shy at right
            show meowth at left, gray
            $ shy2 = True

            shy "So did you find anything buddy?"
            meowth "Apart from that letter, not much."
            shy "What letter?"
            meowth "The one we just - never mind, forget it."
            shy "Hey... ya know, I really don't trust that Annie."
            show meowth inquisitive at left, gray, talk_jump
            meowth "Why's that?"
            shy "She's just... weird. It's almost like she talks to herself."
            meowth "Does she now?"
            shy "I wouldn't trust her if I was you."
            jump investigate_2i_check
        "Annie":
            scene office
            show meowth at left, gray, talk_jump
            show moe at right
            $ annie2 = True

            meowth "Heya, Annie. Who do you think did it?"
            annie "Did what? Oh, you mean the murder?"
            show moe shy at right, talk_jump
            annie "Uhh..."
            meowth "..."
            annie "Hmm..."
            annie "..."
            annie "What do you think?"
            show meowth confused at left, gray, talk_jump
            meowth "Huh? Me, well I-"
            show moe speak at right, talk_jump
            moe "I THINK IT WAS YOU!!!"
            show moe at right
            meowth "Whazzat? Who said that?!"
            show moe speak at right
            moe "That's me!!! The fish!!! I'm right here!!!"
            show moe shy at right, talk_jump
            annie "Sorry, that's Moe. He's always with me."
            show moe mad at right, talk_jump
            moe "That's right!!! And I don't trust you!!! Not one bit!!!"
            show moe mad_nottalking at right
            show meowth mad at left, gray, talk_jump
            meowth "You think I'm fishy? That's real funny comin' from you."
            show moe mad at right
            moe "WATCH IT!!!"
            show moe mad_nottalking at right
            meowth "You've got an attitude. You were reeeeal quiet downstairs, though."
            show moe speak at right
            moe "Downstairs?"
            show moe at right
            show meowth at left, gray
            meowth "Yeah, when I got here."
            show moe mad at right, talk_jump
            moe "What are you talkin' about, you crazy cat?"
            show moe at right
            annie "Shut it, Moe."
            annie "I don't remember being downstairs."
            show meowth confused at left, gray, talk_jump
            meowth "Huh?"
            annie "In fact, I never really leave this office. It's just so cozy here, you know?"
            hide annie with dissolve
            meowth "{i}So these people have memory loss - AND they willingly stay at this nightmare workplace?{/i}"
            meowth "{i}These guys are nuts...{/i}"
            jump investigate_2i_check

label investigate_2i_check:
    if shy2 and kirby2 and annie2:
        jump end_investigate_2
    else:
        jump investigate_2i

label end_investigate_2:
    $ location = 1
    stop music fadeout 1.0
    play music "Hard Boiled.mp3" loop fadein 1.0

    scene office
    show meowth happy at left, gray, talk_jump

    meowth "Alright, I'm startin' to see the bigger picture here."
    show shy at right
    shy "Are you really?"
    meowth "..."
    show meowth sad at left, gray
    meowth "Not at all." 
    show kirby at center
    kirby "Poyo..."
    meowth "You're right, buddy."
    show moe at right, talk_jump
    annie "Hey. Meowth."
    annie "I got an idea. Follow me."
    hide moe with dissolve
    show meowth inquisitive at left, gray, talk_jump
    meowth "Huh? You got an idea? Maybe you should leave it to the pro -"
    meowth "..."
    show meowth mad at left, gray
    meowth "Hey! Wait up!"
    hide meowth with dissolve

    # reality interject
    show static
    pause 0.33
    hide static

    rocky sidepfp_face "Okay, stop. What's even going on anymore?"
    meowth2 sidepfp_mad "Again?! Can you just let me tell my thrilling story?"
    rocky sidepfp "First off, \"thrilling\" is stretching it."
    rocky "Secondly, you're right - this definitely is some fantastical story."
    rocky "I mean, come on - getting through the day? Being energetic? Having drinks? This is obviously about a -"
    meowth2 "Pipe down, Rocky! It's just getting good!"
    rocky sidepfp_face "This is ridiculous! You're trying so hard to make it sound cool, but I know -"
    meowth2 sidepfp "And so, Detective Meowth presses on, even though the case seems hopeless..."
    meowth2 "As a true detective, you must fight on even with your back against the wall"
    meowth2 "Meowth knows this, of course, and he intends to get to the bottom of this mystery!"
    rocky sidepfp "God..."
    meowth2 "Let's get back to it..."

    # noir returns
    show static
    pause 0.33
    hide static
    
label actiii:
    scene server_room with dissolve
    show moe at right with dissolve
    show meowth inquisitive at left, gray with dissolve
    meowth "Woah, what is all this?"
    annie "This is the server room. It's where the servers and stuff are."
    meowth "And stuff?"
    show moe shy at right
    annie "To be honest, I barely know what's going on in here either."
    meowth "Wait, isn't this your job?"
    annie "What, you've never lied on a resume before?"
    show moe speak at right
    moe "True!"
    show moe at right
    annie "You do not pay rent."
    moe "..."
    show meowth at left, gray
    meowth "Hey, I get it. Ya gotta do what ya gotta do."
    show meowth inquisitive at left, gray, talk_jump
    meowth "Wait, didn't you say you never leave the office?"
    show moe shy at right
    annie "I just stay on this floor, I mean. Why go home if I just have to come back in the morning anyways?"
    show meowth confused at left, gray
    meowth "I never thought of it like that..."
    show moe at right
    annie "That's beside the point."
    annie "I have an idea. Something you should've thought of right away."
    meowth "Huh? Me? I assure you, a professional like me would know what to check first."
    annie "Oh yeah? Well, clearly that's not true. There's something really obvious that can help us -"
    annie "Something we can find in this very room. "
    meowth "Uhh..."
    annie "..."
    meowth "..."
    annie "It's the security -"
    show meowth happy at left, gray, talk_jump
    meowth "THE CAMERAS!!! I KNEW IT ALL ALONG!!!"

    stop music fadeout 1.0
    play music "464923__plasterbrain__jazz-loop-rusted-maid.flac" loop fadein 1.0 volume 0.35
    $ location = 2


label investigate_3:
    scene server_room
    call screen investigate_game_3

label clue_3headphones:
    show clue_3headphones_closeup at truecenter with dissolve
    meowth sidepfp "Huh, I thought she never comes down here... but these are definitely hers."
    meowth "Does this work?"
    $ cf_3headphones = True
    hide clue_3headphones_closeup at truecenter with dissolve
    jump investigate_3

label clue_3wires:
    show clue_3wires_closeup at truecenter with dissolve
    meowth sidepfp "I guess they plan on doing some maintenance."
    hide clue_3headphones_closeup at truecenter with dissolve
    jump investigate_3

label clue_3graphics:
    show clue_3graphics_closeup at truecenter with dissolve
    meowth sidepfp "This looks important... I'm just gonna put this down now."
    hide clue_3graphics_closeup at truecenter with dissolve
    jump investigate_3

label clue_3computer:
    show clue_3computer_closeup at truecenter with dissolve
    $ cf_3computer = True
    meowth sidepfp "This is where the security footage is stored. Let's take a look at the camera outside the cafe." 
    meowth "I'll just go ahead and skim through from closing time yesterday to opening time today..."
    meowth "..."
    show meowth at left, gray with dissolve
    meowth -sidepfp "On the screen, I see..."
    show annie at right with dissolve
    meowth "No way... is that..."
    annie "Huh??? KIRBY???"
    meowth "I see Kirby entering the cafe at 8 AM... and he leaves at 8:05 AM. That was this morning! But... he looks a bit weird..."
    hide clue_3computer at truecenter with dissolve
    jump investigate_3

label clue_3ditto:
    show clue_3ditto_closeup at truecenter with dissolve
    meowth sidepfp "Ok, I'm starting to see a pattern here..."
    hide clue_3ditto_closeup at truecenter with dissolve
    jump investigate_3

label check_game_3:
    if cf_3headphones and cf_3computer: # Check all flags have been collected
            meowth sidepfp "{i}Alright, I think I got everything I needed from here. Is it time to leave?{/i}" # Ask player to leave
            menu:
                "Leave":
                    jump investigate_3i # Move on
                "Look for more clues":
                    meowth "Let's look again... a little curiosity never killed the cat."
                    jump investigate_3 # Investigation loop

    else:
        meowth sidepfp_inquisitive "{i}I can't quite put my paw on it, but I feel like I'm missing something...{/i}"
        jump investigate_3

label investigate_3i:
    meowth "{i}Gotta choose who to interrogate very carefully...{/i}"
    menu:
        "Annie and Moe":
            show meowth at left, gray
            show moe at right
            annie "What do you think?"
            meowth "That definitely looks like the Kirby I know."
            annie "You've known him for, like, 15 minutes."
            show meowth sad at left, gray, talk_jump
            meowth "It feels like a lifelong friend stabbed you in the back..."
            meowth "{i}sniff{/i}... oh, the heartache... I can't bear it..."
            show moe speak at right, talk_jump
            moe "He'll pay for what he's done!!!"
            show moe at right
            annie "Yeah. Brewster was expensive, you know."
            show meowth at left, gray
            meowth "Hmm..."
            jump climax

label climax:

    stop music fadeout 1.0
    play music "Hard Boiled.mp3" loop fadein 1.0
    $ location = 1
    scene office with dissolve

    show meowth happy at left, gray with dissolve
    show moe at right with dissolve
    show kirby at center with dissolve
    show shy at right with dissolve

    meowth "Listen up, fellas! I know exactly who killed Brewster."
    show moe speak at right, talk_jump zorder 1
    moe "Obviously! We saw it already!"
    show moe at right
    annie "Just say it!"
    show kirby confused at center
    kirby "Poyo?"
    show kirby at center
    show shy at right zorder 1
    shy "Huh? Hold on, slow down a second! You actually figured it out??"
    meowth "Told ya to be patient and let me work my magic."
    meowth "Of course, this was a tough case."
    meowth "The toughest I've ever seen. But it was no match for my superior detective skills."
    meowth "Yes, indeed. It was only through my incredible ability that I was able to piece together the truth."
    show shy at right zorder 0
    show moe speak at right
    moe "Come on already!! Spit it out!"
    show moe at right
    meowth "The killer is..."

    menu:
        "Shy Guy":
            meowth "It's... SHY GUY!"
            show shy mad at right, talk_jump zorder 1
            shy "What?! No way!"
            meowth "That's right! You thought you were in the clear, bub."
            meowth "But I know you were the closest to Brewster!"
            show shy mad at right zorder 0
            show moe shy at right, talk_jump
            annie "Wait, what?! But the camera-"
            meowth "Forget about the camera!"
            meowth "This is damning evidence!"
            show shy shy at right zorder 1
            shy "B-but... I really loved him..."
            show shy shy at right zorder 0
            show moe mad at right
            moe "Are you crazy?! The camera is the damning evidence!"
            show moe mad_nottalking at right
            kirby "Poyo!"
            show meowth confused at left, gray, talk_jump
            meowth "If you really loved him, then..."
            jump bad_ending
        "Kirby":
            meowth "It's... KIRBY!"
            show kirby confused at center, talk_jump
            kirby "Poyo?!"
            meowth "Care to explain what you were doing here between 8:00 and 8:05 AM this morning?"
            kirby "Poyo..."
            show meowth confused at left, gray, talk_jump
            meowth "You weren't here yet?"
            show meowth at left, gray
            meowth "Heh, a likely story..."
            show moe at right
            annie "Sorry, Kirby. We saw everything!"
            show moe talk at right, talk_jump
            moe "You might be cute, but you're not cuter than me! I mean, uh, you monster!"
            moe "What's wrong with you?!"
            show moe at right
            kirby "P-poyo! Poyo!"
            show meowth confused at left, gray, talk_jump
            meowth "You're really innocent?"
            meowth "Hmm..."
            jump bad_ending
        "Annie":
            meowth "It's... ANNIE!"
            show moe sad at right, talk_jump
            annie "M-me? Wait!"
            show moe mad at right, talk_jump
            moe "Woah! No way! I was with her the whole time! I'm an airtight alibi!"
            show moe sad at right
            meowth "Oh yeah? And how am I supposed to trust you, lil' guppy?"
            show moe mad at right
            moe "Well - "
            show meo sad at right
            meowth "Deny it all you want - I know the truth."
            annie "B-but... I never leave the office! Right, guys?"
            show shy at right zorder 1
            shy "Now that you mention it..."
            kirby "Poyo!"
            show meowth confused at left, gray
            meowth "Huh? Wait, hold on..."
            jump bad_ending
        "Moe":
            meowth "It's... MOE!"
            show moe speak_shy at right
            moe "Whuh? Are you kidding?"
            show moe shy at right
            meowth "Absolutely not! I'm 100\% certain that you are the killer!"
            show shy at right zorder 1
            shy "..."
            kirby "..."
            show shy at right zorder 0
            show moe shy at right
            annie "..."
            show meowth confused at left, gray
            meowth "...What?"
            show moe speak_shy at right
            moe "Look at me. Do you really think I coulda done it?"
            show moe shy at right
            meowth "Uhh... Well, um..."
            jump bad_ending
        "None of the above":
            jump good_ending

label good_ending:
    meowth "The real killer... is none of you."
    show shy at right zorder 1
    shy "What?!"
    show shy at right zorder 0
    show moe at right
    annie "Huh?"
    show kirby confused at center, talk_jump
    kirby "Poyo?"
    meowth "But at the same time... the killer is all of you."
    show moe mad at right, talk_jump
    moe "You're not making any sense!!"
    show moe mad_nottalking at right
    show shy at right zorder 1
    shy "Explain yourself!"
    meowth "Instead of telling, allow me to show you."
    meowth "Ahem. I know you're there."
    meowth "Whoever you are... step forward. The jig is up, pal!"
    fakeannie "Hmph."
    show shy at right zorder 0
    annie "What?! Who is that?!"
    show moe mad at right
    moe "Hey! Why are there two of you?!"
    show moe mad_nottalking at right
    kirby "Poyo?!"
    show shy at right zorder 1
    shy "What's going on? Meowth, explain!"
    meowth "Why don't you explain yourself... Jerry?!"
    ditto "...not bad. I'm impressed."
    shy "Boss?! Where did you-"
    show kirby happy at center
    kirby "Poyo!"
    show shy at right zorder 0
    show moe at right
    annie "Wait, were you - "
    ditto "Looks like you might be worth your salt, Detective."
    meowth "Aww, really?"
    meowth "I mean - flattery will get you nowhere! Now, spill the beans."
    ditto "Well... you've figured me out."
    ditto "That's right - it was me. I killed Brewster."
    meowth "You slammed him against the table, which explains the stain... and you got in there by disgusing as Kirby!"
    show kirby confused at center
    kirby "Poyo?!"
    show kirby at center
    annie "Oh..."
    meowth "And you disguised as Shy Guy and Annie to try to throw me off... but you forgot two crucial things."
    meowth "One: You didn't recognize Shy Guy's love letter... because you didn't know about it either!"
    meowth "Two: Annie hates leaving the office... so she wouldn't be in the cafe investigating the body!"
    meowth "Am I right?"
    ditto "You're quite sharp, detective."
    show shy at right zorder 1
    shy "But... but why? Why go this far?"
    ditto "I didn't think I'd be revealing it this early, but... I might as well. "
    ditto "We're in the red. It's bad. We won't be in business for much longer."
    show shy at right zorder 0
    show moe shy at right
    annie "WHAT?"
    show shy at right zorder 1
    shy "You're telling me our irrelevant meme cryptocurrency isn't sustainable?"
    shy "How could this be happening?"
    ditto "I've been noticing some hostility between you guys recently."
    ditto "So, I wanted to do... I guess you could call it a team-building exercise. "
    show shy mad at right
    shy "Team-building?! Taking away our coffee was supposed to be team-building?!"
    ditto "Well, yeah. I wanted you guys to work together to figure it out."
    ditto "You know, strengthen your bonds. Make friends along the way."
    ditto "But, nope. Instead, you panicked and called some random detective who started snooping around! Like, come on!"
    ditto "The more I think about it, the more I realize you guys don't really care about this work!"
    ditto "So you needed a wake-up call to take this stuff seriously!"
    $ preferences.text_cps = (preferences.text_cps * 2)
    ditto "You see, crypto is the best and only way forward. We are on the verge of a global financial crisis and once that happens, everyone is going to flock to crypto.{nw}"
    ditto "Two things will happen when the global economy collapses a) HODLErs will become absurdly wealthy beyond anyone's wildest imagination and {nw}"
    ditto "b) cryptocurrency will start to become the new gold standard. 10 years from now, fiat won't even be a thing. {nw}"
    ditto "This is hard for a lot of technically inert people to fathom but either way, it's happening.{nw}"
    ditto "A lot of people have difficultly fathoming that knowledge will be swallowed in pill form by 2025 {nw}"
    ditto "( see Nicholas Negropante Ted Talk, you will literally be able to swallow a pill to learn calculus a decade from now ) {nw}"
    ditto "but it doesn't mean it's not happening. A lot of people can't fathom that, even today, you can literally hack your own DNA and code life forms{nw}"
    ditto "( like a T-Rex ) to scale using DNA Reprogramming ( Google it ). My buddy Austin Heinz had a company in SV called Cambrian Genomics( although everyone knows that's a load of bs ){nw}"
    ditto "where they were literally printing hackable DNA with 3D printers. The future is bright or bleak, depending on how you look at it.{nw}"
    ditto "It will be very easy to get phased out if you don't keep up with the times. {nw}"
    ditto "Ignorance will not be bliss is this particular situation. Sorry for the rant but it bothers me that people are still wondering how to transfer their money around {nw}"
    ditto "when you have this beautiful system in play called cryptocurrency that will do everything you're looking for."
    $ preferences.text_cps = (preferences.text_cps / 2)
    show shy mad at right zorder 0
    show moe shy at right
    annie "You can't be serious..."
    show shy mad at right zorder 1
    shy "Yeah, I quit."
    ditto "Good! I was gonna fire you anyway!"
    kirby "Poyo!"
    ditto "What'd you say?!"
    show shy mad at right zorder 0
    show moe at right
    annie "What a weirdo."
    ditto "You're weird! You have a fish in your hair! What's up with that?!"
    show moe speak at right
    moe "You got a problem with that?! Put em up, Jerry-boy!"
    show moe at right
    meowth "So, about my fees..."
    meowth "I'm gonna have to factor in the initial hiring fee, my rate per minute, room checking fee, clue finding fee, Meowth fee..."
    ditto "Get outta here!"
    meowth "{i}And so, I saved the day yet again. With the truth dragged out into the light, peace could return to the city...{/i}"
    meowth "{i}This was only the beginning of my rise to glory.{/i}"

    scene milkbar with dissolve
    show rocky at right with dissolve
    show meowth happy at left, talk_jump with dissolve
    stop music fadeout 1.0
    play music "Cool Vibes.mp3" loop fadein 1.0 volume 2
    $ location = 0

    meowth "And then, they all thanked me for being such a hero!"
    meowth "Everyone started clapping, even all the bystanders!"
    meowth "The President himself showed up shortly after to give me a handshake, and he announced that I'd be lead investigator on the force!"
    meowth "But I turned him down..."
    meowth "I'm a lone panther, roaming the streets of this city..."
    meowth "Then, he gave a bajillion pokedollars, and everyone was askin' for my autograph, and-"
    rocky "Funny, I didn't hear anything about a hero detective."
    meowth "Well, like I said, news takes time to travel - "
    show rocky face at right, talk_jump
    rocky "Oh yeah? I'm sure you investigating who broke a coffee machine is extremely news-worthy."
    show meowth at left
    meowth "Ah..."
    rocky "That was some story you came up with on the fly."
    rocky "I'm almost impressed. But it needs some work - it's too obvious what it was about!"
    meowth "W-well..."
    rocky "I mean, someone broke the coffee machine, right?"
    rocky "And you saw the stain on the table - which was obviously a coffee stain, not a bloodstain."
    rocky "Then you made up the whole thing with Annie not leaving her office, and Shy Guy being in love with Brewster - and the Kirby on the cameras was a red herring."
    rocky "And the mastermind was the head of the company, who happens to be a Ditto."
    rocky "But he showed up at the very end to reveal everything. Ya know what that sounds like?"
    rocky "What happened in reality was that you went around hardly investigating anything."
    rocky "Then the boss showed up and admitted that it was him, and nobody knew it because he just hadn't told them yet."
    rocky "The case was closed on its own, and you weren't even needed."
    rocky "I do admit you had some creative clues in there - like the alleged memory loss which was explained by Jerry posing as the workers."
    rocky "But his motive could've used some work, and -"
    show meowth happy at left, gray, talk_jump

    # noir returns
    show static
    pause 0.33
    hide static

    meowth "I dunno what you're talkin about, buster... It all happened the way I said it..."

    # reality interject
    show static
    pause 0.33
    hide static

    show meowth happy at left
    show rocky at right
    rocky "..."
    rocky "Sure... yeah, ya know what, I believe you."
    rocky "Nice job, Detective Meowth."
    meowth "You're a good fella, Rocky... The best..."
    meowth "Heh, those crazy guys were arguin' with their boss."
    meowth "I knew all along that work environment was a nightmare."
    meowth "Yeah... that was {i}some{/i} drama alright. "
    show meowth happy at left, talk_jump
    meowth "Guess you could even call it something like... real Nintendo drama."
    show rocky face at right
    rocky "..."
    show rocky at right
    rocky "I take it back."
    rocky "Get out."

    return #FIN

label bad_ending:
    fakeannie "Ahem... If you'd excuse me."
    show meowth confused at left, gray, talk_jump
    meowth "Whazzat?"
    show moe shy at right, talk_jump
    annie "Wh-what?! Is that me?"
    ditto "It seems like this is going nowhere."
    show shy at right zorder 1
    shy "Wh- boss?!"
    show kirby confused at center
    kirby "Poyo?!"
    show shy at right zorder 0
    show moe speak at right, talk_jump
    moe "Mr. Jerry? Where were you?!"
    show moe at right
    ditto "I was here all along."
    ditto "I must say... I'm disappointed, \"detective\"."
    ditto "Even with your tall tales, I thought you had what it takes to get to the bottom of this."
    ditto "Alas, it seems my hopes were misguided."
    ditto "Well, then. A good day to you, sir."
    show meowth sad at left, gray, talk_jump
    meowth "W-wait... hold on... that's not what happened!"
    meowth "I, uh, was joking! I know what actually went down here!"
    meowth "Give me another chance!"
    meowth "Uhh..."
    meowth "..."

    scene milkbar with dissolve
    show rocky at right with dissolve
    show meowth at left, talk_jump with dissolve
    stop music fadeout 1.0
    play music "Cool Vibes.mp3" loop fadein 1.0 volume 2
    $ location = 0

    meowth "Umm... and then, uhh..."
    show rocky face at right, talk_jump
    rocky "Seriously? That's how it ends?"
    rocky "What a disappointment."
    meowth "Wait, no! Hold on!"
    rocky "I guess your tall tales finally caught up with you."
    rocky "I was expecting you to be better at coming up with stuff on the fly."
    rocky "Oh well..."
    meowth "No, I... ahh, darn it."
    meowth "Ah well. Ol' Rocky just couldn't keep up with the inner machinations of my complex mind."
    show meowth sad at left
    meowth "Guess I'm blastin' off again..."

    return #FIN

