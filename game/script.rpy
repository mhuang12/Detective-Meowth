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
    $ in_investigation = True

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
    if cf_1photo: # Check all flags have been collected
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
            show shy_gray at right

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
    return









