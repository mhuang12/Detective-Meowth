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

    rocky disappoint "…"
    rocky "Who do you think you are?"
    meowth "Who, me?"
    rocky "There's no one else sitting here."
    meowth "Why, I am the most legendary detective to ever walk the streets of this city -{w} the private eye who puts all other eyes to shame, especially that yellow rat!"
    meowth "DETECTIVE MEOWTH! THAT’S RIGHT!"
    rocky "Nope, doesn't ring a bell."
    meowth "…"
    meowth "Awright. News takes time to travel, I get it. My exploits - I mean, my heroic deeds will be known all across the world soon enough."
    rocky "Sure."
    meowth "What, ya don’t believe me?"
    meowth "Fine. For you, my friend, I'll tell you about my most thrilling adventure yet.{w} Something that would make that yellow idiot turn his spiky tail and run. "
    meowth "This is stuff the press won’t tell ya."
    rocky "I think I see another customer-{nw}"
    meowth "Listen closely to this shocking tale of deceit, love, and one noble cat’s pursuit of the truth above all else!"
    rocky "No, really, that's quite alright-{nw}"
    meowth "It all started yesterday…"

    jump acti


# ACT I
label acti:

    scene apartment

    show meowth
    meowth "{i}I was going through my normal morning routine…{/i}"
    meowth "{i}Filing my claws, straightening my tie, drinking my coffee and eating cherry pie, when I received a call…{/i}"
    "*telephone rings*"
    meowth "Meowth Detective Agency, how may I help you?"
    moe "Oh god, please help us! There's been a-{nw}" #FIND A WAY TO TEMPORARILY CHANGE MOE'S NAME TO "VOICE"
    meowth "Brrzt - please wait while I transfer you over to the number one detective in the city!"
    meowth "…"
    meowth "Yello, detective Meowth speakin’. How can I help ya?"
    moe ""


    # This ends the game.

    return
