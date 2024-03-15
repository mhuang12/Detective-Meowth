# The script of the game goes in this file. let the spaghettification commence

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define meowth = Character("Detective Meowth", image="meowth")
define meowth2 = Character("Detective Meowth", image="meowth2") # meowth's evil twin! >:)
define brewster = Character("Coffee Machine")
define shy = Character("Shy Guy", image="shy")
define kirby = Character("Kirby")
define ditto = Character("Jerry")
define annie = Character("Annie")
define moe = Character("Moe", image="moe")
define rocky = Character("Bartender", image="rocky")
define phoneguy = Character("VOICE")

default shy0 = False
default kirby0 = False
default annie0 = False

# CLUE TRACKING FLAGS
default cf_0stain = False
default cf_0brewster = False
default cf_1photo = False

# GAME STATE TRACKER
# 0 - flashback
# 1 - investigation
# 2 - bar
default location = 0

# IMAGE DEFINITIONS

image static = "static.png"

image meowth = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth.png",
    "not _last_say_who=='meowth'", "meowth_gray.png"
)
image meowth happy = ConditionSwitch(
    "_last_say_who=='meowth'", Placeholder("meowth_happy.png"),
    "not _last_say_who=='meowth'", Placeholder("meowth_happy_gray.png")
)
image meowth angry = ConditionSwitch(
    "_last_say_who=='meowth'", Placeholder("meowth_angry.png"),
    "not _last_say_who=='meowth'", Placeholder("meowth_angry_gray.png")
)
image meowth inquisitive = ConditionSwitch(
    "_last_say_who=='meowth'", Placeholder("meowth_inquisitive.png"),
    "not _last_say_who=='meowth'", Placeholder("meowth_inquisitive_gray.png")
)
image meowth silly = ConditionSwitch(
    "_last_say_who=='meowth'", Placeholder("meowth_silly.png"),
    "not _last_say_who=='meowth'", Placeholder("meowth_silly_gray.png")
)
image meowth confused = ConditionSwitch(
    "_last_say_who=='meowth'", Placeholder("meowth_confused.png"),
    "not _last_say_who=='meowth'", Placeholder("meowth_confused_gray.png")
)
image meowth sad = ConditionSwitch(
    "_last_say_who=='meowth'", Placeholder("meowth_sad.png"),
    "not _last_say_who=='meowth'", Placeholder("meowth_sad_gray.png")
)
image side meowth sidepfp = "meowth_side.png"
image side meowth2 sidepfp_angry = Placeholder("meowth_side_angry.png")
image side meowth2 sidepfp_happy = Placeholder("meowth_side_happy.png")
image side meowth2 sidepfp = Placeholder("meowth_side.png")

image rocky = ConditionSwitch(
    "_last_say_who=='rocky'", Placeholder("rocky.png"),
    "not _last_say_who=='rocky'", Placeholder("rocky_gray.png")
)
image rocky face= ConditionSwitch(
    "_last_say_who=='rocky'", Placeholder("rocky_face.png"),
    "not _last_say_who=='rocky'", Placeholder("rocky_face_gray.png")
)
image side rocky sidepfp = Placeholder("rocky_side.png")

image shy = ConditionSwitch(
    "_last_say_who=='shy'", Placeholder("shy.png"),
    "not _last_say_who=='shy'", Placeholder("shy_gray.png")
)
image shy mad = ConditionSwitch(
    "_last_say_who=='shy'", Placeholder("shy_mad.png"),
    "not _last_say_who=='shy'", Placeholder("shy_mad_gray.png")
)

image kirby = ConditionSwitch(
    "_last_say_who=='kirby'", Placeholder("kirby.png"),
    "not _last_say_who=='kirby'", Placeholder("kirby_gray.png")
)
image kirby confused = ConditionSwitch(
    "_last_say_who=='kirby'", Placeholder("kirby_confused.png"),
    "not _last_say_who=='kirby'", Placeholder("kirby_confused_gray.png")
)

image annie = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", Placeholder("annie.png"),
    "not _last_say_who=='annie' or _last_say_who=='moe'", Placeholder("annie_gray.png")
)
image annie shy = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", Placeholder("annie_shy.png"),
    "not _last_say_who=='annie' or _last_say_who=='moe'", Placeholder("annie_shy_gray.png")
)
image annie sad = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", Placeholder("annie_sad.png"),
    "not _last_say_who=='annie' or _last_say_who=='moe'", Placeholder("annie_sad_gray.png")
)

image side moe = Placeholder("moe.png") # MOE IS INTENDED TO BE A SIDE IMAGE
image side moe angry = Placeholder("moe_angry.png")

# fun little jump when they talk
transform talk_jump:
    ease .06 yoffset 15
    ease .06 yoffset -15
    ease .05 yoffset 7
    ease .05 yoffset -7
    ease .01 yoffset 0

# preserving bgm after loading in from save
label after_load:
    if location == 1:
        play music "464923__plasterbrain__jazz-loop-rusted-maid.flac" loop fadein 1.0 volume 0.5
    elif location == 0:
        play music "Hard Boiled.mp3" loop fadein 1.0
    else:
        play music "Hard Boiled.mp3" loop fadein 1.0 #TEMP
    return


# The game starts here.
# INTRO
label start:

    play music "Hard Boiled.mp3" loop fadein 1.0
    play audio "main-door-opening-closing-38280.mp3" volume 1.5
    play audio "doorbell.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene milkbar night with dissolve

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
    show rocky at right, talk_jump
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
    show meowth at left, talk_jump
    meowth "..."
    meowth "Awright. News takes time to travel, I get it. My exploits - {w=0.1}I mean, my heroic deeds will be known all across the world soon enough."
    rocky "Sure."
    meowth "What, ya don't believe me?"
    meowth "Fine. For you, my friend, I'll tell you about my most thrilling adventure yet.{w} Something that would make that yellow idiot turn his spiky tail and run. "
    show meowth happy at left, talk_jump
    meowth "This is stuff the press won't tell ya."
    rocky "I think I see another customer-{nw}"
    meowth "Listen closely to this shocking tale of deceit, love, and one noble cat's pursuit of the truth above all else!"
    rocky "No, really, that's quite alright-{nw}"
    meowth "It all started yesterday..."

    jump acti


# ACT I
label acti:

    scene apartment with fade

    show meowth at center, talk_jump
    meowth "{i}I was going through my normal morning routine...{/i}"
    meowth "{i}Filing my claws, straightening my tie, drinking my coffee and eating cherry pie, when I received a call...{/i}"
    "*telephone rings*"
    meowth inquisitive "Meowth Detective Agency, how may I help you?"
    phoneguy "Oh god, please help us! There's been a-{nw}" #FIND A WAY TO TEMPORARILY CHANGE MOE'S NAME TO "VOICE"
    meowth "Brrzt - please wait while I transfer you over to the number one detective in the city!"
    meowth "..."
    meowth "Yello, detective Meowth speakin'. How can I help ya?"
    phoneguy "It's awful, there's blood everywhere and-"
    phoneguy "Wait... Meowth? I thought this was Detective Pika-{nw}"
    meowth "Zip it, pal! Tell me about the case. Ol' Meowth will have it solved before you can say \"Meowth, that's right!\""
    phoneguy "Whatever! Just get over here quick!"
    meowth "{i}And so I went. Armed with nothing but my wits, my pen, and my dapper looks, off to solve the mystery of a lifetime...{/i}"
    rocky "Oh boy..."

    scene cafe with dissolve
    show shy at left with dissolve
    show kirby at center with dissolve
    show annie at right with dissolve

    meowth "Awright, Detective Meowth on the scene. What's all the ruckus?"
    shy "Who're you?"
    meowth "Why, me? I'm glad you asked...  Ahem! To-{nw}"
    annie "No... Brewster... he was so young..."
    kirby "Poyo..."
    shy "Take a look behind the counter."
    meowth "{i}And so I did. What I saw behind the counter was... the lifeless body of Brewster, the brand new coffee machi - I mean, barista at their office lobby's coffee shop. It was a grim sight...{/i}"
    
    # reality interject
    show static
    pause 0.33
    hide static

    
    rocky sidepfp "A Brewster? I have one of those right here."
    meowth sidepfp "No, no, it most definitely was not a coffee machine! It was actually Brewster!"
    meowth "Ahem... where was I? Oh, right..."

    # noir returns
    show static
    pause 0.33
    hide static

    meowth -sidepfp "Hmm... a troubling case indeed..."
    shy "So? Can you help us?"
    meowth "Can I help you? I'll take the case - and I'll crack it wide open!"

    stop music fadeout 1.0
    play music "464923__plasterbrain__jazz-loop-rusted-maid.flac" loop fadein 1.0 volume 0.5
    $ in_investigation = True

    
    
# INVESTIGATION PRELIM
label investigate_0i: #interview
    meowth "{i}I should see what these guys know before I take a look around.{/i}"
    menu:
        "Shy Guy":
            scene cafe
            show meowth at left
            show shy at right
            $ shy0 = True
            meowth "First things first. What's your name, and what do you do here?"
            shy "Uhh, I'm Shy Guy. I work in marketing."
            meowth "Tough luck, huh?"
            shy "Tell me about it."
            meowth "Alright, Mr. Guy. I'm gonna need to know where you were last night."
            shy "Last night? Well... I stayed late to finish up work. I'm the only one our crazy boss hired for marketing, so I have to do everything myself."
            meowth "Stayed late, huh? Interesting. And just who is this boss of yours?"
            shy "Well, the thing is, he hardly comes into work. In fact, the last time I saw him was when I got hired."
            meowth "You should consider a career change, pal."
            shy "Yeah..."
            jump investigate_0i_check
            
        "Kirby":
            scene cafe
            show meowth at left
            show kirby at right
            $ kirby0 = True
            meowth "What's up with you, beach ball?"
            kirby "Poyo!"
            meowth "Well, it's a pleasure to meet you too, Kirby."
            meowth "You're the intern, huh? Lemme guess. Unpaid?"
            kirby "Poyo..."
            meowth "Figures. Now, what was a lil guy like you doin' last night?"
            kirby "Poyo!"
            meowth "You... went back to your home planet after work? Using a star?"
            kirby "Poyo!"
            meowth "You commute from Planet Popstar? Sure, kid. I'll take it you saw nothin', then."
            jump investigate_0i_check

        "Annie":
            scene cafe
            show meowth at left
            show annie at right
            $ annie0 = True
            meowth "Alright, ma'am. What's your name, and what do you do here?"
            annie "I do IT."
            meowth "Woah, we got a smart guy over here, huh? Wanna tell me where you were last night?"
            annie "I went straight home. The less time I have to spend in this office the better."
            meowth "And you didn't see anything?"
            annie "Nope."
            meowth "Great."
            annie "Yeah."
            meowth "Uh-huh."
            jump investigate_0i_check


label investigate_0i_check:
    if shy0 and kirby0 and annie0:
        jump investigate_0
    else:
        jump investigate_0i

label investigate_0:

    scene cafe # game background
    call screen investigate_game_0 # clues as imagebutton overlay
    # starts game screen, pauses VN
    # each clue is a button to be pressed
    # each clue jumps to its own scene with explanation
    # after explanation ends, go back to investigation
    # once player clicks leave button, meowth checks relevant clues
    # if yes, he asks the player if player wants to leave
    # if player does not want to leave or if not all relevant clues found, return to jump back to this label


# CLUES - format: xy where x is the room number and y is the clue number
# Rooms: 0 - cafe
#        1 - office
#        2 - server room
#check_game_x: see if player obtained all relevant clues in this room: ask to leave if Y, go back to investigation if N

label clue00: # Clue 0 of room 0
    meowth "wrong clue idiot" # Meowth explanation of clue
    $ clue_found_0 = True # Clue flag setting
    jump investigate_0 # Jump to relevant clue collection check for this room

label clue0table:
    scene cafe
    #show table
    meowth sidepfp "{i}An ordinary table.{/i}"
    jump investigate_0

label clue0stain:
    scene cafe
    meowth sidepfp "{i}An ordinary ta- wait a minute. What's that on the side?{/i}" # Meowth explanation of clue
    meowth "{i}...A stain? It couldn't be...{/i}"
    $ cf_0stain = True # Clue flag setting
    jump investigate_0 # Jump to relevant clue collection check for this room

label clue0brewster:
    scene cafe
    meowth sidepfp "{i}Poor birdie... all he ever wanted was to make delicious coffee and they got 'im...{/i}"
    meowth "{i}It's enough to bring a cat to tears... I'll remember ya, pal...{/i}"
    meowth "{i}Hmm... I don't see any obvious causes of death. No sharp objects were used. His head is covered in blood... could it be...?{/i}"
    $ cf_0brewster = True
    jump investigate_0

label clue0coffee:
    scene cafe
    meowth sidepfp "{i}Looks delicious... but I gotta focus!{/i}"
    jump investigate_0

label clue0painting:
    scene cafe
    meowth sidepfp "{i}Real fancy place they got here. Feels pretentious.{/i}"
    jump investigate_0

label clue0ditto:
    scene cafe
    meowth sidepfp "{i}What is this guy doing here? Go figure, they shill for DittoCoin...{/i}"
    jump investigate_0

label check_game_0: # Clue collection check for room 0, after player clicks leave button
    if cf_0stain and cf_0brewster: # Check all flags have been collected
        meowth sidepfp "{i}Alright, I think I got everything I needed from here. Is it time to leave?{/i}" # Ask player to leave
        menu:
            "Leave":
                jump investigate_0e # Move on
            "Look for more clues":
                jump investigate_0 # Investigation loop

    else:
        meowth "{i}I can't quite put my paw on it, but I feel like I'm missing something...{/i}"
        jump investigate_0


label investigate_0e:
    stop music fadeout 1.0
    play music "Hard Boiled.mp3" loop fadein 1.0
    $ in_investigation = False

    scene cafe
    show shy at right, talk_jump
    show meowth at left
    shy "That's it? You're not gonna do an autopsy or anything? Did you even figure it out yet?"
    show meowth at left, talk_jump
    meowth "Cool it, Mr. Guy. There's only so much I can do without my equipment."
    meowth "This was pretty short notice, so I had to reschedule all my other cases - I'm busy, ya know."
    annie "I knew we should've just called the cops instead. How did this... quack even get here?"
    meowth "Woah, don't call the heat. Just let me work my magic."
    shy "This guy..."
    meowth "Why don'tcha show me your office, tough guy?"
    shy "Go on ahead without me. Annie and Kirby can show you."
    meowth "{i}At that time, I was so naive. I had no clue what I was gettin' myself into. The game...{w=0.2} had only just begun.{/i}"

    # reality interject
    show static
    pause 0.33
    hide static

    rocky sidepfp "Alright, hold on just a second."
    meowth2 sidepfp_angry "What?! Can'tcha save the questions 'til the end?"
    rocky "Who would ever hire a two-bit \"detective\" like you for a \"murder\" - if there even was one?"
    meowth2 sidepfp_happy "Watch it, pebble. Some may call me a stray, but I prefer the term...{w=0.2} \"free agent.\""
    meowth2 "A private eye like me sees what everyone else can't - the cold, hard truth."
    rocky "Really? Why in the world didn't those office workers just... call the police?"
    meowth2 sidepfp_angry "The fuzz kill the vibe! They're not gonna get anything done!"
    meowth2 sidepfp "Besides, all those Growlithe and Arcanine give me the creeps... I mean, I'm not scared! Nope, not me!"
    rocky "Sure..."
    meowth2 "Anyways - where was I? Oh, right..."
    meowth "Off I went to investigate the workplace of these adorable but suspicious gaggle of workers..."
    meowth "Everyone keeps their claws out... I have to keep mine sharp."
    rocky "Whatever that means."

    # noir returns
    show static
    pause 0.33
    hide static

label actii:

    scene office with dissolve
    show meowth at left with dissolve
    show kirby at right with dissolve

    meowth "So... what do you do here, exactly?"
    kirby "Poyo."
    meowth "DittoCoin? Sounds like a scam."
    annie "Hey, can you guys keep it down? I'm trying to get some work done."
    meowth "Annie? Weren't you just -"
    annie "Shhh."
    meowth "Tough crowd, huh."
    kirby "Poyo?"
    meowth "Yeah, I was wonderin' where Mr. Guy ran off to..."
    shy "I'm right here."
    meowth "Woah! Caught up quick, huh?"
    shy "What are you doing here?"
    meowth "Well, didn't I just tell ya? I'm here to investigate your office. Jeez, what is with everyone forgettin' things today?"
    shy "Well, go ahead and look around. Nothing is off limits for our detective, uh... friend."

    play music "464923__plasterbrain__jazz-loop-rusted-maid.flac" loop fadein 1.0 volume 0.5
    $ in_investigation = True

label investigate_1:
    
    scene office
    call screen investigate_game_1

label clue_1drawer:
    meowth "{i}I see a crumpled up love-letter to... Brewster?!{/i}"
    meowth "{i}It reads...{/i}"
    meowth "\"Dear Brewster,"
    meowth "I have been working in this office with you for quite a long time and I have always admired your bushy mustache."
    meowth "NO NO NO THEY CAN'T SEE THIS"
    meowth "HE CAN NEVER SEE THIS"
    meowth "NEVER NEVER NEVER\""
    meowth "{i}...Interesting.{/i}"
    jump investigate_1

label clue_1photo:
    $ cf_1photo = True
    meowth "{i}A picture with a bunch of DittoCoin employees...{/i}"
    meowth "{i}But the frame is cracked. Hmm...{/i}"
    meowth "{i}Who's this blue Ditto fella? I haven't seen him around town. No one must've introduced 'em to me.{/i}"
    jump investigate_1

label clue_1burger:
    meowth "{i}Gross... and he ate the wrapper too.{/i}"
    "(The letters NNIE are visible on the wrapper)"
    jump investigate_1

label clue_1pencil:
    meowth "{i}It's a number 4 pencil.{/i}"
    jump investigate_1

label clue_1computer:
    meowth "{i}I see some game about monkeys popping balloons on the monitor… these employees sure are working hard.{/i}"

label clue_1ditto:
    meowth "Hey! How'd you get out of my satchel?! You might tamper with evidence."
    jump investigate_1


label check_game_1: # Clue collection check for room 1, after player clicks leave button
    if cf_1photo: # Check all flags have been collected
        meowth "{i}Alright, I think I got everything I needed from here. Is it time to leave?{/i}" # Ask player to leave
        menu:
            "Leave":
                jump investigate_1i # Move on
            "Look for more clues":
                jump investigate_1 # Investigation loop

    else:
        meowth "{i}I can't quite put my paw on it, but I feel like I'm missing something...{/i}"
        jump investigate_1

label investigate_1i:
    menu:
        "Kirby":
            return
        "Shy Guy":
            return
        "Annie":
            return