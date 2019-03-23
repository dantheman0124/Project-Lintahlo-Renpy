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
image kasumi happy = "kasumi_happy"
image kasumi blushing = "kasumi_blushing"
image kasumi disappointed = "kasumi_disappointed"
image kasumi passive = "kasumi_passive"
image kasumi upset = "kasumi_upset"






label start:

    scene black_screen
    
    mysterious "..."
    mysterious "Hey..."
    MC "Huh...?"
    mysterious "Hey, wake up! You’ll be late for school."
    MC "..."
    mysterious "Fine, you leave me no choice."
    MC "{i}I feel someone climbing on top of my bed...{i}"
    mysterious "Hyaaaaaaaaaah!!!"
    
    
    scene bedroom_day with fade
    
    "{i}The wind and sleepiness is knocked out of me from my little sister’s cheap coercion tactics.{i}"
    MC "Oww-! Okay, I'm up! I'm up!"
    MC "Geez... I do have a spine you know."
    show hana staring at right:
        xalign 0.75
        yalign 1.0
    Hana "Don’t worry, I wouldn’t use a move on you if I didn’t know how to do it safely."
    "{i}Lately she’s been privy to the fact that now that we’re teenagers, her strength is starting to catch up to mine. Her long-time passive interest in wrestling is being put to use and frankly, I don’t appreciate it.{i}"
    show hana mad at right:
        xalign 0.75
        yalign 1.0
    Hana "School starts in forty-five minutes!"
    MC "Which means I have another fifteen until I’ll be late for sure."
    "{i}Wrapping myself in my blanket again I have a couple seconds more rest until I sense Hana readying another move. I throw off my blanket to signal my cooperation and head over to the kitchen.{i}"
    
    
    scene livingroom_day with fade
    "{i}Two cold plates of eggs, bacon and rice are on the dining table. Hana takes a seat and starts eating . If she wanted to eat with me she could have just said so. I guess she told me she’d be making breakfast last night though...{i}"
    "*Cellphone ringing*"
    "{i}Hm? Why am I getting a call this early in the morning?{i}"
    "{i}Our parents would always use the landline. Anyone at school would just text me if they needed to talk to me, not that I knew many people anyways.{i}"
    MC "Ah.. an unknown number. No thanks."
    "*Click*"
    "{i}I don't care. If it was something important they'll leave a message.{i}"
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
    show kaz happy:
        xalign 0.5
        yalign 1.0
    show kasumi happy:
        xalign 0.5
        yalign 1.0
    
    # This ends the game.
    return