# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define meowth = Character("Detective Meowth", image="meowth")
define brewster = Character("Coffee Machine", image="brewster")
define shy = Character("Shy Guy", image="shy")
define kirby = Character("Kirby", image="kirby")
define ditto = Character("Jerry", image="ditto")
define annie = Character("Annie", image="annie")
define moe = Character("Moe", image="moe")
define rocky = Character("Bartender", image="rocky")

default clue_found_0 = False

image static = "static.png"



# The game starts here.
# INTRO
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene milkbar night

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show meowth at left
    meowth "The usual, please."

    show rocky at right
    rocky "The usual? Who're you?"
    meowth "Your finest Moomoo Milk, on the rocks pwease"

    rocky disappoint "..."
    rocky "Who do you think you are?"
    meowth "Who, me?"
    rocky "There's no one else sitting here."
    meowth "Why, I am the most legendary detective to ever walk the streets of this city -{w} the private eye who puts all other eyes to shame, especially that yellow rat!"
    meowth "DETECTIVE MEOWTH! THAT'S RIGHT!"
    rocky "Nope, doesn't ring a bell."
    meowth "..."
    meowth "Awright. News takes time to travel, I get it. My exploits - I mean, my heroic deeds will be known all across the world soon enough."
    rocky "Sure."
    meowth "What, ya don't believe me?"
    meowth "Fine. For you, my friend, I'll tell you about my most thrilling adventure yet.{w} Something that would make that yellow idiot turn his spiky tail and run. "
    meowth "This is stuff the press won't tell ya."
    rocky "I think I see another customer-{nw}"
    meowth "Listen closely to this shocking tale of deceit, love, and one noble cat's pursuit of the truth above all else!"
    rocky "No, really, that's quite alright-{nw}"
    meowth "It all started yesterday..."

    jump acti


# ACT I
label acti:

    scene apartment

    show meowth
    meowth "{i}I was going through my normal morning routine...{/i}"
    meowth "{i}Filing my claws, straightening my tie, drinking my coffee and eating cherry pie, when I received a call...{/i}"
    "*telephone rings*"
    meowth "Meowth Detective Agency, how may I help you?"
    moe "Oh god, please help us! There's been a-{nw}" #FIND A WAY TO TEMPORARILY CHANGE MOE'S NAME TO "VOICE"
    meowth "Brrzt - please wait while I transfer you over to the number one detective in the city!"
    meowth "..."
    meowth "Yello, detective Meowth speakin'. How can I help ya?"
    moe "It's awful, there's blood everywhere and-"
    moe "Wait... Meowth? I thought this was Detective Pika-{nw}"
    meowth "Zip it, pal! Tell me about the case. Ol' Meowth will have it solved before you can say \"Meowth, that's right!\""
    moe "Whatever! Just get over here quick!"
    meowth "{i}And so I went. Armed with nothing but my wits, my pen, and my dapper looks, off to solve the mystery of a lifetime...{/i}"
    rocky "Oh boy..."

    scene cafe
    show shy at left
    show kirby at center
    show annie at right

    meowth "Awright, Detective Meowth on the scene. What's all the ruckus?"
    shy "Who're you?"
    meowth "Why, me? I'm glad you asked...  Ahem! To-{nw}"
    annie "No... Brewster... he was so young..."
    kirby "Poyo... (wtf...)"
    shy "Take a look behind the counter."
    meowth "{i}And so I did. What I saw behind the counter was... the lifeless body of Brewster, the brand new coffee machi - I mean, barista at their office lobby's coffee shop. It was a grim sight...{/i}"
    
    # reality interject
    show static
    pause 0.33
    hide static

    
    rocky "A Brewster? I have one of those right here."
    meowth "No, no, it most definitely was not a coffee machine! It was actually Brewster!"
    meowth "Ahem... where was I? Oh, right..."

    # noir returns
    show static
    pause 0.33
    hide static

    meowth "Hmm... a troubling case indeed..."
    shy "So? Can you help us?"
    meowth "Can I help you? I'll take the case - and I'll crack it wide open!"

    jump investigate_0

label investigate_0:

    scene cafe_investigate # game background
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



label check_game_0: # Clue collection check for room 0, after player clicks leave button
    if clue_found_0: # Check all flags have been collected
        meowth "{i}Alright, I think I got everything I needed from here. Is it time to leave?{/i}" # Ask player to leave
        menu:
            "Leave":
                jump investigate_0e # Move on
            "Look for more clues":
                jump investigate_0 # Investigation loop

    else:
        meowth "{i}I can't quite put my paw on it, but I feel like I'm missing something...{/i}"
        jump investigate_0


label investigate_0e:

    scene cafe
    shy "That's it? You're not gonna do an autopsy or anything? Did you even figure it out yet?"
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

    rocky "Alright, hold on just a second."
    meowth "What?! Can'tcha save the questions 'til the end?"
    rocky "Who would ever hire a two-bit \"detective\" like you for a \"murder\" - if there even was one?"
    meowth "Watch it, pebble. Some may call me a stray, but I prefer the term...{w=0.2} \"free agent.\""