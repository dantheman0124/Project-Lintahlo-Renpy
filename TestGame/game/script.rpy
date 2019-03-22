# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

$ playerName = "Daniel"

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
    
    
    scene bedroom_day with fade
    
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
    
    
    scene livingroom_day with fade
    "{i}I go into the kitchen and see that Hana has made some eggs, bacon, and rice for breakfast. Guess she wanted to eat with me, she should have just said so.{i}"
    "{i}We start eating our cold breakfast with nothing to say in particular to each other. Any reason for resentment has long since dissipated, as it always goes.{i}"
    "*Cellphone ringing*"
    "{i}Hm? Why am I getting a call this early in the morning?{i}"
    "{i}Ah.. an unknown number. No thanks.{i}"
    "*Click*"
    show hana cute at right:
        xalign 0.5
        yalign 1.0
    with fade
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

    
    scene black_screen with fade
    "{i}I strip down from my pajamas and grab my black Moe Boxer underwear from the top drawer of my dresser.{i}"
    "{i}I grab the nearest of all the clothes I need and throw them on. While I’m in the bathroom, simultaneously washing my face and brushing my teeth, Hana yells that she’s heading out, which means my time is running out.{i}"
    "{i}I quickly get my things together, grab my bag, and head out the door shortly after Hana leaves, making sure to lock the door behind me.{i}"
    
    scene road_morning with fade
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
    "{i}We walk at a quicker pace to make up for lost time during our conversation. Within a few minutes we finally reach the school.{i}"
    
    
    
    scene black_screen with fade
    "{i}The beginning of the school day went as normal. Kaz ended up being in my first period math class, so I just had to sit through my second class until lunch. Kaz met me in the hallway after second period ended.{i}"
    
    
    scene schoolhall_day with fade
    show kaz happy:
        xalign 0.5
        yalign 1.0
    Kaz "Hey dude! It's finally lunchtime!"
    show kaz upset:
        xalign 0.5
        yalign 1.0
    Kaz "I can't believe how tired I am of classes already... It's only been like three hours!"
    MC "Yeah I know... I almost fell asleep in second period. I guess I shouldn't have slept in so late, now I'm all sluggish and tired."
    show kaz smug:
        xalign 0.5
        yalign 1.0
    Kaz "You should really fix your sleep schedule man!"
    "{i}I can't believe how hypocritial he's being right now. He woke up late too... why is he lecturing me?{i}"
    show kaz happy:
        xalign 0.5
        yalign 1.0
    Kaz "Well let's not waste more of our lunch. Do you wanna go to the usual spot for lunch? I bet {b}she's{\b} already waiting there."
    MC "Yeah let's go then. No need to keep her waiting."
    
    
    scene black_screen with fade
    "{i}Kaz and I head up a few flights of stairs until we reach our usual lunch spot; the school rooftop.{i}"
    
    
    scene schoolroof_day with fade
    show kaz happy:
        xalign 0.5
        yalign 1.0
    Kaz "MAN what a nice day to be up here!"
    MC "Yeah the weather is pefect today. It's sunny, there's a slight breeze, it's not too hot... Almost like it's straight out of an anime or something."
    show kaz neutral:
        xalign 0.5
        yalign 1.0
    "{i}Kaz briefly looks around, admiring the beautiful view of the school rooftop. It's not often that the weather is like this during this time of year.{i}"
    show kaz surprised with hpunch:
        xalign 0.5
        yalign 1.0
    Kaz "Hey look! It's Kasumi!"
    "{i}I look over by the benches and see my childhood friend, Kasumi, sitting and waiting with her lunch. She notices us and comes over.{i}"
    
    # This ends the game.
    return