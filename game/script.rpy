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
define fakeannie = Character("\"Annie\"")
define moe = Character("Moe", image="moe")
define rocky = Character("Bartender", image="rocky")
define phoneguy = Character("VOICE")

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

# GAME STATE TRACKER
# 0 - flashback
# 1 - investigation
# 2 - bar
default location = 0

# IMAGE DEFINITIONS

image static = "static.png"

image meowth = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth.png",
    "not _last_say_who=='meowth'", "meowth_dark.png"
)
image meowth happy = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_happy.png",
    "not _last_say_who=='meowth'", "meowth_happy_dark.png"
)
image meowth angry = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_angry.png",
    "not _last_say_who=='meowth'", "meowth_angry_dark.png"
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
    "_last_say_who=='meowth'", "meowth_sad.png",
    "not _last_say_who=='meowth'", "meowth_sad_dark.png"
)
image meowth gray= ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_gray.png",
    "not _last_say_who=='meowth'", "meowth_gray_dark.png"
)
image meowth grayhappy = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_grayhappy.png",
    "not _last_say_who=='meowth'", "meowth_grayhappy_dark.png"
)
image meowth grayangry = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_graymad.png",
    "not _last_say_who=='meowth'", "meowth_graymad_dark.png"
)
image meowth grayinquisitive = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_grayinquisitive.png",
    "not _last_say_who=='meowth'", "meowth_grayinquisitive_dark.png"
)
image meowth graysilly = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_graysilly.png",
    "not _last_say_who=='meowth'", "meowth_graysilly_dark.png"
)
image meowth grayconfused = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_grayconfused.png",
    "not _last_say_who=='meowth'", "meowth_grayconfused_dark.png"
)
image meowth graysad = ConditionSwitch(
    "_last_say_who=='meowth'", "meowth_graysad.png",
    "not _last_say_who=='meowth'", "meowth_graysad_dark.png"
)
image side meowth sidepfp = "meowth_side.png"
image side meowth2 sidepfp_angry = Placeholder("meowth_side_angry.png")
image side meowth2 sidepfp_happy = Placeholder("meowth_side_happy.png")
image side meowth2 sidepfp = Placeholder("meowth_side.png")

image rocky = ConditionSwitch(
    "_last_say_who=='rocky'", "rocky.png",
    "not _last_say_who=='rocky'", "rocky_dark.png"
)
image rocky face= ConditionSwitch(
    "_last_say_who=='rocky'", "rocky_eyebrow.png",
    "not _last_say_who=='rocky'", "rocky_eyebrow_dark.png"
)
image side rocky sidepfp = Placeholder("rocky_side.png")

image shy = ConditionSwitch(
    "_last_say_who=='shy'", Placeholder("shy.png"),
    "not _last_say_who=='shy'", Placeholder("shy_dark.png")
)
image shy mad = ConditionSwitch(
    "_last_say_who=='shy'", Placeholder("shy_mad.png"),
    "not _last_say_who=='shy'", Placeholder("shy_mad_dark.png")
)

image kirby = ConditionSwitch(
    "_last_say_who=='kirby'", "kirby.png",
    "not _last_say_who=='kirby'","kirby_dark.png"
)
image kirby confused = ConditionSwitch(
    "_last_say_who=='kirby'", Placeholder("kirby_confused.png"),
    "not _last_say_who=='kirby'", Placeholder("kirby_confused_dark.png")
)

image annie = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", Placeholder("annie.png"),
    "not _last_say_who=='annie' or _last_say_who=='moe'", Placeholder("annie_dark.png")
)
image annie shy = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", Placeholder("annie_shy.png"),
    "not _last_say_who=='annie' or _last_say_who=='moe'", Placeholder("annie_shy_dark.png")
)
image annie sad = ConditionSwitch(
    "_last_say_who=='annie' or _last_say_who=='moe'", Placeholder("annie_sad.png"),
    "not _last_say_who=='annie' or _last_say_who=='moe'", Placeholder("annie_sad_dark.png")
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

    show meowth gray at center, talk_jump
    meowth "{i}I was going through my normal morning routine...{/i}"
    meowth "{i}Filing my claws, straightening my tie, drinking my coffee and eating cherry pie, when I received a call...{/i}"
    "*telephone rings*"
    show meowth grayinquisitive at center, talk_jump
    meowth "Meowth Detective Agency, how may I help you?"
    phoneguy "Oh god, please help us! There's been a-{nw}" #FIND A WAY TO TEMPORARILY CHANGE MOE'S NAME TO "VOICE"
    meowth "Brrzt - please wait while I transfer you over to the number one detective in the city!"
    meowth "..."
    meowth "Yello, detective Meowth speakin'. How can I help ya?"
    phoneguy "It's awful, there's blood everywhere and-"
    phoneguy "Wait... Meowth? I thought this was Detective Pika-{nw}"
    show meowth grayangry at center, talk_jump
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

    
    rocky  "A Brewster? I have one of those right here."
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
    $ location = 1

    
    
# INVESTIGATION PRELIM
label investigate_1i: #interview
    meowth "{i}I should see what these guys know before I take a look around.{/i}"
    menu:
        "Shy Guy":
            scene cafe
            show meowth at left
            show shy at right
            $ shy1 = True
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
            jump investigate_1i_check
            
        "Kirby":
            scene cafe
            show meowth at left
            show kirby at right
            $ kirby1 = True
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
            jump investigate_1i_check

        "Annie":
            scene cafe
            show meowth at left
            show annie at right
            $ annie1 = True
            meowth "Alright, ma'am. What's your name, and what do you do here?"
            annie "I do IT."
            meowth "Woah, we got a smart guy over here, huh? Wanna tell me where you were last night?"
            annie "I went straight home. The less time I have to spend in this office the better."
            meowth "And you didn't see anything?"
            annie "Nope."
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
#check_game_x: see if player obtained all relevant clues in this room: ask to leave if Y, go back to investigation if N

label clue1table:
    scene cafe
    #show table
    meowth "{i}An ordinary table.{/i}"
    jump investigate_1

label clue1stain:
    scene cafe
    meowth sidepfp "{i}An ordinary ta- wait a minute. What's that on the side?{/i}" # Meowth explanation of clue
    meowth "{i}...A stain? It couldn't be...{/i}"
    $ cf_1stain = True # Clue flag setting
    jump investigate_1 # Jump to relevant clue collection check for this room

label clue1brewster:
    scene cafe
    meowth sidepfp "{i}Poor birdie... all he ever wanted was to make delicious coffee and they got 'im...{/i}"
    meowth "{i}It's enough to bring a cat to tears... I'll remember ya, pal...{/i}"
    meowth "{i}Hmm... I don't see any obvious causes of death. No sharp objects were used. His head is covered in blood... could it be...?{/i}"
    $ cf_1brewster = True
    jump investigate_1

label clue1coffee:
    scene cafe
    meowth "{i}Looks delicious... but I gotta focus!{/i}"
    jump investigate_1

label clue1painting:
    scene cafe
    meowth "{i}Real fancy place they got here. Feels pretentious.{/i}"
    jump investigate_1

label clue1ditto:
    scene cafe
    meowth "{i}What is this guy doing here? Go figure, they shill for DittoCoin...{/i}"
    jump investigate_1

label check_game_1: # Clue collection check for room 1, after player clicks leave button
    if cf_1stain and cf_1brewster: # Check all flags have been collected
        meowth sidepfp "{i}Alright, I think I got everything I needed from here. Is it time to leave?{/i}" # Ask player to leave
        menu:
            "Leave":
                jump investigate_1e # Move on
            "Look for more clues":
                jump investigate_1 # Investigation loop

    else:
        meowth sidepfp "{i}I can't quite put my paw on it, but I feel like I'm missing something...{/i}"
        jump investigate_1


label investigate_1e:
    stop music fadeout 1.0
    play music "Hard Boiled.mp3" loop fadein 1.0
    $ location = 0

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
    meowth2 "Off I went to investigate the workplace of these adorable but suspicious gaggle of workers..."
    meowth2 "Everyone keeps their claws out... I have to keep mine sharp."
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
    $ location = 1

label investigate_2:
    
    scene office
    call screen investigate_game_2

label clue_2drawer:
    meowth sidepfp "{i}I see a crumpled up love-letter to... Brewster?!{/i}"
    meowth "{i}It reads...{/i}"
    meowth "\"Dear Brewster,"
    meowth "I have been working in this office with you for quite a long time and I have always admired your bushy mustache."
    meowth "NO NO NO THEY CAN'T SEE THIS"
    meowth "HE CAN NEVER SEE THIS"
    meowth "NEVER NEVER NEVER\""
    meowth "{i}...Interesting.{/i}"
    jump reading_trigger

label clue_2photo:
    $ cf_1photo = True
    meowth sidepfp "{i}A picture with a bunch of DittoCoin employees...{/i}"
    meowth "{i}But the frame is cracked. Hmm...{/i}"
    meowth "{i}Who's this blue Ditto fella? I haven't seen him around town. No one must've introduced 'em to me.{/i}"
    jump investigate_2

label clue_2burger:
    meowth sidepfp "{i}Gross... and he ate the wrapper too.{/i}"
    "(The letters NNIE are visible on the wrapper)"
    jump investigate_2

label clue_2pencil:
    meowth sidepfp "{i}It's a number 4 pencil.{/i}"
    jump investigate_2

label clue_2computer:
    meowth sidepfp "{i}I see some game about monkeys popping balloons on the monitor… these employees sure are working hard.{/i}"
    jump investigate_2

label clue_2ditto:
    meowth sidepfp "Hey! How'd you get out of my satchel?! You might tamper with evidence."
    jump investigate_2


label check_game_2: # Clue collection check for room 1, after player clicks leave button
    if cf_2photo: # Check all flags have been collected
        meowth sidepfp "{i}Alright, I think I got everything I needed from here. Is it time to leave?{/i}" # Ask player to leave
        menu:
            "Leave":
                jump investigate_2i # Move on
            "Look for more clues":
                jump investigate_2 # Investigation loop

    else:
        meowth sidepfp "{i}I can't quite put my paw on it, but I feel like I'm missing something...{/i}"
        jump investigate_2

label reading_trigger:
    scene office
    show meowth at left
    show shy at right
            
    meowth "Alright, Mr. Guy. Care to explain this love letter?"
    shy "Hey! You can’t just go snooping through someone's desk!"
    meowth "Are you kiddin’? You just said nothing is off limits."
    shy "No, I did not! I told you to follow Kirby!" 
    meowth " That was before, bub "
    shy "No! That was the last thing I said to you!" 
    meowth "No it wasn’t."
    shy "Yes it was!" 
    meowth "No, I don’t think it was."
    shy "Yes it was!" 
    meowth "No, I really don’t think-"
    shy "Yes it was!" 
    meowth "Alright! Fine. But that doesn’t explain this note. You wrote in big letters that Brewster can never know about your secret."
    meowth "Dubious, is it not?"
    shy "What is that??"
    meowth "Playing dumb won’t get you out of this one, sport."
    shy "Um, I mean… That was just me writing to myself, I swear! It don’t mean nothing."
    meowth "Double negative, huh?"
    shy "No!! It does not mean no- I mean, anything!"
    meowth "Look, I get it. Love is fickle…  if anyone knows anything about unrequited love, it’s me. Oh, my sweet Meowzie… I miss you…"
    shy "Honestly… I just couldn’t bring myself to throw it away. I should probably do that."
    meowth "Hold it! Do you know who that blue guy is?"
    shy "You can ask Kirby…"
    "He runs away to dispose of his embarassing note"
    jump investigate_2


label investigate_2i:
    meowth "{i}I should see what these fellas know before I take a look around.{/i}"
    menu:
        "Kirby":
            scene office
            show meowth at left
            show kirby at right
            
            meowth "How’s it hangin’, my spherical friend?"
            kirby "Poyo!"
            meowth "Glad to hear it!"
            meowth "Hey, Kirbs. I saw this blue guy in one of those group photos, but I haven’t seen ‘em around. Do ya know anything about this?"
            kirby "Poyo!"
            meowth "I see. He’s da boss, the real Giovanni of the operation, huh?"
            kirby "Poyo!"
            meowth "So… where is this boss ‘a yours?"
            kirby "Poyo!"
            meowth "He just sends teams messages with ominous requests and rants about… cryptocurrency? What a real pain in the neck, huh?" # check this is ok
            kirby "Poyo!"
            meowth "Alright, guess that rules him out as quick as I suspected him."
            kirby "Poyo!"
            meowth "So… uhh… I’m outta leads."
            meowth "…"
            meowth "Did you do it?"
            kirby "Poyo." 
            meowth "Rats! You were supposed ta confess! This was gonna be my big break!"
            kirby "Poyo!"
            meowth "Yeah, yeah, I’ll keep lookin’."
            jump investigate_2i_check
        "Shy Guy":
            scene office
            show meowth at left
            show shy_dark at right

            shy "So did you find anything buddy?"
            meowth "Apart from that letter, not much."
            shy "What letter?"
            meowth "The one we just - never mind, forget it."
            shy "Hey… ya know, I really don’t trust that Annie."
            meowth "Why’s that?"
            shy "She’s just… weird. It’s almost like she talks to herself. "
            meowth "Does she now?"
            shy "I wouldn’t trust her if I was you."
            hide shy with dissolve
            meowth "{i}????{/i}"
            jump investigate_2i_check
        "Annie":
            scene office
            show meowth at left
            show annie at right

            meowth "Heya, Annie. Who do you think did it?"
            annie "Did what? Oh, you mean the murder?"
            annie "Uhh…."
            meowth "…"
            annie "Hmm…"
            annie "..."
            annie "What do you think?"
            meowth "Huh? Me, well I-"
            moe "I THINK IT WAS YOU!!!"       #add moe in the text bubble
            meowth "Whazzat? Who said that?!"
            moe "That’s me!!! The fish!!! I’m right here!!!"
            annie "Sorry, that’s Moe. He’s always with me."
            moe "That’s right!!! And I don’t trust you!!! Not one bit!!!"
            meowth "You think I’m fishy? That’s real funny comin’ from you."
            moe "WATCH IT!!!"
            meowth "You’ve got an attitude. You were reeeeal quiet downstairs, though."
            moe "Downstairs?"
            meowth "Yeah, when I got here."
            moe "What are you talkin’ about, you crazy cat?"
            annie "Shut it, Moe."
            annie "I don’t remember being downstairs."
            meowth "Huh?"
            annie "In fact, I never really leave this office. It’s just so cozy here, you know?"
            hide annie with dissolve
            meowth "{i}So these people have memory loss - AND they willingly stay at this nightmare workplace?{/i}"
            meowth "{i}These guys are nuts…{/i}"
            jump investigate_2i_check

label investigate_2i_check:
    if shy2 and kirby2 and annie2:
        jump end_investigate_2
    else:
        jump investigate_2i

label end_invesitgate_2:
    scene office
    show meowth at left

    meowth "Alright, I’m startin’ to see the bigger picture here."
    show shy at right
    shy "Are you really?"
    meowth "..." 
    meowth "Not at all." 
    show kirby at right
    kirby "Poyo…"
    meowth "You’re right, buddy."
    annie "Hey. Meowth."
    annie "I got an idea. Follow me."
    hide annie with dissolve
    meowth "Huh? You got an idea? Maybe you should leave it to the pro -"
    meowtghh "..."
    meowth "Hey! Wait up!"
    hide meowth with dissolve

label flashback_2:
    rocky "Okay, stop. What’s even going on anymore?"
    scene milkbar night
    show meowth at left
    show rocky at right
    meowth "Again?! Can you just let me tell my thrilling story?"
    rocky "First off, “thrilling” is stretching it."
    rocky "Secondly, you’re right - this definitely is some fantastical story. I mean, come on - getting through the day? Being energetic? Having drinks? This is obviously about a -"
    meowth "Pipe down, rocky! It’s just getting good!"
    rocky "This is ridiculous! You’re trying so hard to make it sound cool, but I know -"
    meowth "And so, Detective Meowth presses on, even though the case seems hopeless… As a true detective, you must fight on even with your back against the wall. Meowth knows this, of course, and he intends to get to the bottom of this mystery!"
    rocky "God…"
    meowth "Let’s get back to it…"
    
label actiii:
    scene server_room with dissolve
    show meowth with dissolve
    show annie with dissolve
    meowth "Woah, what is all this?"
    annie "This is the server room. It’s where the servers and stuff are."
    meowth "And stuff?"
    annie "To be honest, I barely know what’s going on in here either."
    meowth "Wait, isn’t this your job?"
    annie "What, you’ve never lied on a resume before?"
    moe sidepfp "True!"
    annie "You do not pay rent."
    moe "…"
    meowth "Hey, I get it. Ya gotta do what ya gotta do."
    meowth "Wait, didn’t you say you never leave the office?"
    annie "I just stay on this floor, I mean. Why go home if I just have to come back in the morning anyways?"
    meowth "I never thought of it like that…"
    annie "That’s beside the point."
    annie "I have an idea. Something you should’ve thought of right away."
    meowth "Huh? Me? I assure you, a professional like me would know what to check first."
    annie "Oh yeah? Well, clearly that’s not true. There’s something really obvious that can help us - {w} something we can find in this very room. "
    meowth "Uhh…"
    annie "…"
    meowth "…"
    annie "It’s the security -"
    meowth "THE CAMERAS!!! I KNEW IT ALL ALONG!!!"

    play music "464923__plasterbrain__jazz-loop-rusted-maid.flac" loop fadein 1.0 volume 0.5
    $ location = 1


label investigate_3:
    scene server_room
    call screen investigate_game_3

label clue_3headphones:
    meowth sidepfp "Huh, I thought she never comes down here… but these are definitely hers."
    meowth "Does this work?"
    $ cf_3headphones = True
    jump investigate_3

label clue_3wires:
    meowth sidepfp "I guess they plan on doing some maintenance."
    jump investigate_3

label clue_3graphics:
    meowth sidepfp "This looks important… I’m just gonna put this down now."
    jump investigate_3

label clue_3computer:
    $ cf_3computer = True
    meowth sidepfp "This is where the security footage is stored. Let’s take a look at the camera outside the cafe. I’ll just go ahead and skim through from closing time yesterday to opening time today…"
    meowth "..."
    meowth -sidepfp "On the screen, I see…"
    show meowth at left
    show annie at right
    meowth "No way… is that…"
    annie "Huh??? KIRBY???"
    meowth "I see Kirby entering the cafe at 8 AM… and he leaves at 8:05 AM. That was this morning! But… he looks a bit weird…"
    jump investigate_3

label clue_3ditto:
    meowth sidepfp "Ok, I’m starting to see a pattern here…"
    jump investigate_3

label check_game_3:
    if cf_3headphones and cf_3computer: # Check all flags have been collected
            meowth sidepfp "{i}Alright, I think I got everything I needed from here. Is it time to leave?{/i}" # Ask player to leave
            menu:
                "Leave":
                    jump investigate_3i # Move on
                "Look for more clues":
                    jump investigate_3 # Investigation loop

    else:
        meowth sidepfp "{i}I can't quite put my paw on it, but I feel like I'm missing something...{/i}"
        jump investigate_3

label investigate_3i:
    menu:
        "Annie":
            show meowth gray at left
            show annie at right
            annie "What do you think?"
            meowth "That definitely looks like the Kirby I know."
            annie "You’ve known him for, like, 15 minutes."
            meowth "It feels like a lifelong friend stabbed you in the back… sniff… oh, the heartache… I can’t bear it…"
            moe sidepfp "He’ll pay for what he’s done!!!"
            annie "Yeah. Brewster was expensive, you know."
            meowth "Hmm…"
            jump climax

label climax:

    stop music fadeout 1.0
    play music "Hard Boiled.mp3" loop fadein 1.0
    $ location = 0
    scene office with dissolve

    show meowth gray with dissolve

    meowth "Listen up, fellas! I know exactly who killed Brewster."
    moe sidepfp "Obviously! We saw it already!"
    annie "Just say it!"
    kirby "Poyo?"
    shy "Huh? Hold on, slow down a second! You actually figured it out??"
    meowth "Told ya to be patient and let me work my magic."
    meowth "Of course, this was a tough case. The toughest I’ve ever seen. But it was no match for my superior detective skills."
    meowth "Yes, indeed. It was only through my incredible ability that I was able to piece together the truth."
    moe "Come on already!! Spit it out!"
    meowth "The killer is…"

    menu:
        "Shy Guy":
            meowth "It’s… SHY GUY!"
            shy "What?! No way!"
            meowth "That’s right! You thought you were in the clear, bub."
            meowth "But I know you were the closest to Brewster!"
            annie "Wait, what?! But the camera-{nw}"
            meowth "Forget about the camera!"
            meowth "This is damning evidence!"
            shy "B-but… I really loved him…"
            moe sidepfp "Are you crazy?! The camera is the damning evidence!"
            kirby "Poyo!"
            meowth "If you really loved him, then…"
            jump bad_ending
        "Kirby":
            meowth "It’s… KIRBY!"
            kirby "Poyo?!"
            meowth "Care to explain what you were doing here between 8:00 and 8:05 AM this morning?"
            kirby "You weren’t here yet?"
            meowth "Heh, a likely story…"
            annie "Sorry, Kirby. We saw everything!"
            moe sidepfp "You might be cute, but you’re not cuter than me! I mean, uh, you monster!"
            moe "What’s wrong with you?!"
            kirby "P-poyo! Poyo!"
            meowth "You’re really innocent?"
            meowth "Hmm…"
            jump bad_ending
        "Annie":
            meowth "It’s… ANNIE!"
            annie "M-me? Wait!"
            moe sidepfp "Woah! No way! I was with her the whole time! I’m an airtight alibi!"
            meowth "Oh yeah? And how am I supposed to trust you, lil guppy?"
            moe "Well - {nw}"
            meowth "Deny it all you want - I know the truth."
            annie "B-but… I never leave the office! Right, guys?"
            shy "Now that you mention it…"
            kirby "Poyo!"
            meowth "Huh? Wait, hold on…"
            jump bad_ending
        "Moe":
            meowth "It’s… MOE!"
            moe sidepfp "Whuh? Are you kidding?"
            meowth "Absolutely not! I’m 100% certain that you are the killer!"
            shy "…"
            kirby "…"
            annie "…"
            meowth "…What?"
            moe "Look at me. Do you really think I coulda done it?"
            meowth "Uhh… Well, um…"
            jump bad_ending
        "None of the above":
            jump good_ending

label good_ending:
    meowth "The real killer… is none of you."
    shy "What?!"
    annie "Huh?"
    kirby "Poyo?"
    meowth "But at the same time… the killer is all of you."
    moe "You’re not making any sense!!"
    shy "Explain yourself!"
    meowth "Instead of telling, allow me to show you."
    meowth "Ahem. I know you’re there."
    meowth "Whoever you are… step forward. The jig is up, pal!"
    fakeannie "Hmph."
    annie "What?! Who is that?!"
    moe sidepfp "Hey! Why are there two of you?!"
    kirby "Poyo?!"
    shy "What’s going on? Meowth, explain!"
    meowth "Why don’t you explain yourself… Jerry?!"
    ditto "…not bad. I’m impressed."
    shy "Boss?! Where did you-"
    kirby "Poyo!"
    annie "Wait, were you - {nw}"
    ditto "Looks like you might be worth your salt, Detective."
    meowth "Aww, really?"
    meowth "I mean - flattery will get you nowhere! Now, spill the beans."
    ditto "Well… you’ve figured me out. That’s right - it was me. I killed Brewster."
    meowth "You slammed him against the table, which explains the stain… and you got in there by disgusing as Kirby!"
    kirby "Poyo?!"
    annie "Oh…"
    meowth "And you disguised as Shy Guy and Annie to try to throw me off… but you forgot two crucial things."
    meowth "One: You didn’t recognize Shy Guy’s love letter… because you didn’t know about it either!"
    meowth "Two: Annie hates leaving the office… so she wouldn’t be in the cafe investigating the body!"
    meowth "Am I right?"
    ditto "You’re quite sharp, detective."
    shy "But… but why? Why go this far?"
    ditto "I didn’t think I’d be revealing it this early, but… I might as well. "
    ditto "We’re in the red. It’s bad. We won’t be in business for much longer."
    annie "WHAT?"
    shy "You’re telling me our irrelevant meme cryptocurrency isn’t sustainable? How could this be happening?"
    ditto "I’ve been noticing some hostility between you guys recently."
    ditto "So, I wanted to do… I guess you could call it a team-building exercise. "
    shy "Team-building?! Taking away our coffee was supposed to be team-building?!"
    ditto "Well, yeah. I wanted you guys to work together to figure it out. You know, strengthen your bonds. Make friends along the way."
    ditto "But, nope. Instead, you panicked and called some random detective who started snooping around! Like, come on!"
    ditto "The more I think about it, the more I realize you guys don’t really care about this work! So you needed a wake-up call to take this stuff seriously!"
    $ preferences.text_cps = preferences.text_cps * 3
    ditto "You see, crypto is the best and only way forward. We are on the verge of a global financial crisis and once that happens, everyone is going to flock to crypto.{nw}"
    ditto "Two things will happen when the global economy collapses a) HODLErs will become absurdly wealthy beyond anyone’s wildest imagination and {nw}"
    ditto "b) cryptocurrency will start to become the new gold standard. 10 years from now, fiat won’t even be a thing. {nw}"
    ditto "This is hard for a lot of technically inert people to fathom but either way, it’s happening. A lot of people have difficultly fathoming that knowledge will be swallowed in pill form by 2025 {nw}"
    ditto "( see Nicholas Negropante Ted Talk, you will literally be able to swallow a pill to learn calculus a decade from now ) {nw}"
    ditto "but it doesn’t mean it’s not happening. A lot of people can’t fathom that, even today, you can literally hack your own DNA and code life forms{nw}"
    ditto "( like a T-Rex ) to scale using DNA Reprogramming ( Google it ). My buddy Austin Heinz had a company in SV called Cambrian Genomics( although everyone knows that’s a load of bs ) {nw}"
    ditto "where they were literally printing hackable DNA with 3D printers. The future is bright or bleak, depending on how you look at it. It will be very easy to get phased out if you don’t keep up with the times. {nw}"
    ditto "Ignorance will not be bliss is this particular situation. Sorry for the rant but it bothers me that people are still wondering how to transfer their money around {nw}"
    ditto "when you have this beautiful system in play called cryptocurrency that will do everything you’re looking for."
    $ preferences.text_cps = preferences.text_cps / 3
    annie "You can’t be serious…"
    shy "Yeah, I quit."
    ditto "Good! I was gonna fire you anyway!"
    kirby "Poyo!"
    ditto "What’d you say?!"
    annie "What a weirdo."
    ditto "You’re weird! You have a fish in your hair! What’s up with that?!"
    moe sidepfp "You got a problem with that?! Put em up, Jerry-boy!"
    meowth "So, about my fees… I’m gonna have to factor in the initial hiring fee, my rate per minute, room checking fee, clue finding fee, Meowth fee…"
    ditto "Get outta here!"
    meowth "{i}And so, I saved the day yet again. With the truth dragged out into the light, peace could return to the city…{/i}"
    meowth "{i}This was only the beginning of my rise to glory.{/i}"

    # reality interject
    show static
    pause 0.33
    hide static

    scene milkbar with dissolve
    show meowth at left with dissolve
    show rocky at right with dissolve

    meowth "And then, they all thanked me for being such a hero! Everyone started clapping, even all the bystanders!"
    meowth "The President himself showed up shortly after to give me a handshake, and he announced that I’d be lead investigator on the force!"
    meowth "But I turned him down… I’m a lone panther, roaming the streets of this city…"
    meowth "Then, he gave a bajillion pokedollars, and everyone was askin’ for my autograph, and-"
    rocky "Funny, I didn’t hear anything about a hero detective."
    meowth "Well, like I said, news takes time to travel - {nw}"
    rocky "Oh yeah? I’m sure you investigating who broke a coffee machine is extremely news-worthy."
    meowth "Ah…"
    rocky "That was some story you came up with on the fly. I’m almost impressed. But it needs some work - it’s too obvious what it was about!"
    meowth "W-well…"
    rocky "I mean, someone broke the coffee machine, right? And you saw the stain on the table - which was obviously a coffee stain, not a bloodstain. Then you made up the whole thing with Annie not leaving her office, and Shy Guy being in love with Brewster - and the Kirby on the cameras was a red herring. "
    rocky "And the mastermind was the head of the company, who happens to be a Ditto. But he showed up at the very end to reveal everything. Ya know what that sounds like?"
    rocky "What happened in reality was that you went around hardly investigating anything, then the boss showed up and admitted that it was him, and nobody knew it because he just hadn’t told them yet. The case was closed on its own, and you weren’t even needed."
    rocky "I do admit you had some creative clues in there - like the alleged memory loss which was explained by Jerry posing as the workers. But his motive could’ve used some work, and -"
    meowth "I dunno what you’re talkin about, buster… It all happened the way I said it…"
    rocky "…"
    rocky "Sure… yeah, ya know what, I believe you."
    rocky "Nice job, detective Meowth."
    meowth "You’re a good fella, Rocky… The best…"
    meowth "Heh, those crazy guys were arguin’ with their boss. I knew all along that work environment was a nightmare."
    meowth "Yeah… that was {i}some{/i} drama alright. "
    meowth "Guess you could even call it something like… real Nintendo drama."
    rocky "…"
    rocky "I take it back."
    rocky "Get out."

    return #FIN

label bad_ending:
    fakeannie "Ahem… If you’d excuse me."
    meowth "Whazzat?"
    annie "Wh-what?! Is that me?"
    ditto "It seems like this is going nowhere."
    shy "Wh- boss?!"
    kirby "Poyo?!"
    moe sidepfp "Mr. Jerry? Where were you?!"
    ditto "I was here all along."
    ditto "I must say… I’m disappointed, “detective”. Even with your tall tales, I thought you had what it takes to get to the bottom of this."
    ditto "Alas, it seems my hopes were misguided."
    ditto "Well, then. A good day to you, sir."
    meowth "W-wait… hold on… that’s not what happened!"
    meowth "I, uh, was joking! I know what actually went down here!"
    meowth "Give me another chance!"
    meowth "Uhh…"
    meowth "..."

    # reality interject
    show static
    pause 0.33
    hide static

    scene milkbar with dissolve
    show meowth at left with dissolve
    show rocky at right with dissolve

    meowth "Umm… and then, uhh…"
    rocky "Seriously? That’s how it ends?"
    rocky "What a disappointment."
    meowth "Wait, no! Hold on!"
    rocky "I guess your tall tales finally caught up with you. I was expecting you to be better at coming up with stuff on the fly."
    rocky "Oh well…"
    meowth "No, I… ahh, darn it."
    meowth "Ah well. Ol’ Rocky just couldn’t keep up with the inner machinations of my complex mind."
    meowth "Guess I’m blastin’ off again…"

    return #FIN

