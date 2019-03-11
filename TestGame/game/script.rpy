# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#characters
define MC = Character("You")
define Hana = Character("Hana")
define Kaz = Character("Kaz")
define mysterious = Character("???")

#character images
image hana happy = "hana_happy"
image hana staring = "hana_staring"
image hana mad = "hana_mad"
image hana cute = "hana_cute"
image hana worried = "hana_worried"
image kaz happy = "kaz_happy"
image kaz serious = "kaz_serious"
image kaz neutral = "kaz_neutral"
image kaz surprised = "kaz_surprised"
image kaz upset = "kaz_upset"
image kaz smug = "kaz_smug"





label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black_screen
    
    mysterious "..."
    mysterious "...get up..."
    MC "huh...?"
    mysterious "School starts in forty-five minutes."
    MC "I can make it in thirty."
    mysterious "This again? You’ve left me no choice."
    MC "{i}I feel someone climbing on top of my bed. What a strange dream I’m currently experiencing…{i}"
    "*WHAMMMMM!*"
    
    
    scene bedroom_day
    
    MC "Oww-! Okay, I'm up! I'm up!"
    "{i}I fumble and squirm to get my sister off of me - it’s no use. I turn my head, looking up at my sister as she towers over me.{i}"
    show hana mad at right:
        xalign 0.75
        yalign 1.0
    Hana "Get your life together."
    MC "Get off me! It’s my life, I’ll wake up when I want."
    "{i}Hana steps on my leg, bringing me great pain and sorrow{i}"
    Hana "Are you going to get up now??"
    MC "Ack-! FINE! Get off, I’ll get out of bed."
    "{i}Hana releases her foot from my body and leaves the room whistling an annoying tune, allowing me to get a hold of my surroundings. I stretch my arms out and head downstairs.{i}"
    
    
    scene livingroom_day
    "{i}I go into the kitchen and see that Hana has made some eggs, bacon, and rice for breakfast. Guess she wanted to eat with me, she should have just said so.{i}"
    "{i}We start eating our cold breakfast with nothing to say in particular to each other. Any reason for resentment has long since dissipated, as it always goes.{i}"
    "*Cellphone ringing*"
    "{i}Hm? Why am I getting a call this early in the morning?{i}"
    "{i}Ah.. an unknown number. No thanks.{i}"
    "*Click*"
    show hana cute at right:
        xalign 0.5
        yalign 1.0
    "{i}I look over and notice Hana shyly looking up at me - waiting for me to say something.{i}"
    
    menu:
        "Do you need something?":
            MC "Hm? Do you need something?"
            show hana mad at right:
                xalign 0.5
                yalign 1.0
            Hana "You could say thank you every once in a while ya know..."
            
            
        "Thanks for breakfast.":
            MC "Thanks for breakfast Hana. It's pretty good."
            "{i}Hana gives me a smile.{i}"
            show hana happy at right:
                xalign 0.5
                yalign 1.0
            Hana "You’re welcome! Next time you can wake up earlier and we can cook together!"
            

        "Breakfast is cold.":
            MC "Hana, my breakfast is cold."
            "{i}Hana's shoulders sink a little.{i}"
            show hana worried at right:
                xalign 0.5
                yalign 1.0
            Hana "It's not my fault..."
    
    hide hana worried
    "{i}We continue eating until Hana finally chimes in."
    
    show hana happy at right:
        xalign 0.5
        yalign 1.0
        
    Hana "Okay, I’m gonna go get ready. Just make sure you don’t fall asleep on your way to school!"
    "{i}Hana gets up and puts her plate into the sink, heading off.{i}"
    hide hana happy
    "{i}I finish my meal and do the same, heading upstairs to get dressed before brushing my teeth.{i}"

    
    scene black_screen
    "{i}I strip down from my pajamas and grab my black Moe Boxer underwear from the top drawer of my dresser.{i}"
    "{i}I grab the nearest of all the clothes I need and throw them on. While I’m in the bathroom, simultaneously washing my face and brushing my teeth, Hana yells that she’s heading out, which means my time is running out.{i}"
    "{i}I quickly get my things together, grab my bag, and head out the door shortly after Hana leaves, making sure to lock the door behind me.{i}"
    
    scene road_morning
    MC "*sigh* The start to another boring school year. I wonder if my friends have changed at all since last year..."
    "{size=-4}*tip tap tip tap*{/size}"
    "*tip tap tip tap*"
    "{size=+4}*tip tap tip tap*{/size}"
    "*WHAMMMMMMMM!!!*"
    "{i}I get knocked to the ground by someone behind me.{i}"
    MC "What the he-"
    show kaz smug:
        xalign 0.5
        yalign 1.0
    "{i}I look up to see my best friend Kaz standing triumphantly over me.{i}"
    MC "Oh, it's just you. What was that for?"
    show kaz happy:
        xalign 0.5
        yalign 1.0
    Kaz "Haha, just thought I’d surprise you. Thought you could really use something to wake you up, sleepy head!"
    "{i}That’s Kaz, one of my best friends I met 2 years ago in science class. We were partnered up for a chemistry lab one day when he farted over the bunsen burner and set my notes on fire. We had a nice chuckle about that and have been friends ever since.{i}" 
    MC "I see you haven’t changed a bit over the summer."
    "{i}I get up and dust myself off.{i}"
    MC "So what have you been up to all summer?"
    Kaz "Well, I went away for a few weeks. Other than that, mainly just chilling in my room playing video games."
    MC "Oh cool, where'd you go?"
    Kaz "My family had tickets for the worldwide Go Kart championship, so we stayed up in a hotel for a few weeks and went sightseeing and stuff, you know? How about you?"
    "{i}I didn’t really want to admit that I’ve done nothing all summer except stay inside, binging anime and playing video games, so I just tried to avoid the question.{i}"
    MC "Uhhh well you know, this and that. You’re on your way to school too? Why so late?"
    show kaz neutral:
        xalign 0.5
        yalign 1.0
    "{i}I feel so stupid. Of course he’s heading off to school. I hope he just skips over it.{i}"
    show kaz serious:
        xalign 0.5
        yalign 1.0
    Kaz "Why are YOU so late?"
    MC "I slept in, obviously."
    "{i}Phew, that was close.{i}"
    show kaz happy:
        xalign 0.5
        yalign 1.0
    Kaz "Typical of you. Let’s hurry, we shouldn’t be late on the first day of class."
    hide kaz happy
    "{i}We walk at a quicker pace to make up for lost time during our conversation. Within a few minutes we finally reach the front of the school.{i}"

    
    # This ends the game.
    return