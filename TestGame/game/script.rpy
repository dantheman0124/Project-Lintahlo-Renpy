$ playerName = "Daniel"

#friendship counters
define kasumiFriendship = 0
define kazFriendship = 0
define akinaFriendship = 0
define hanaFriendship = 0
define miyoFriendship = 0
define bigReward = 10
define smallReward = 5

#characters
define MC = Character("You", color="#BDB76B")
define Hana = Character("Hana", color="#B22222")
define Kaz = Character("Kaz", color="#FFA500")
define mysterious = Character("???")
define Kasumi = Character("Kasumi", color="#ADD8E6")
define Teacher = Character("Teacher")
define Akina = Character("Akina",color="ffae42")

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
image akina annoyed = "akina_annoyed"
image akina flustered = "akina_flustered"
image akina happy = "akina_happy"
image akina neutral = "akina_neutral"
image akina sad = "akina_sad"
image akina thinking = "akina_thinking"
image miyo shadow = "miyo_shadow"



label start:

#    scene black_screen
    
#    mysterious "..."
#    mysterious "Hey..."
#    MC "Huh...?"
#    mysterious "Hey, wake up! You’ll be late for school."
#    MC "..."
#    mysterious "Fine, you leave me no choice."
#    "I feel someone climbing on top of my bed..."
#    mysterious "Hyaaaaaaaaaah!!!"
    
    
#    scene bedroom_day with fade
    
#    "The wind and sleepiness is knocked out of me from my little sister’s cheap coercion tactics."
#    MC "Oww-! Okay, I'm up! I'm up!"
#    MC "Geez... I do have a spine you know."
#    show hana staring at right:
#        xalign 0.75
#        yalign 1.0
#    Hana "Don’t worry, I wouldn’t use a move on you if I didn’t know how to do it safely."
#    "Lately she’s been privy to the fact that now that we’re teenagers, her strength is starting to catch up to mine. Her long-time passive interest in wrestling is being put to use and frankly, I don’t appreciate it."
#    show hana mad at right:
#        xalign 0.75
#        yalign 1.0
#    Hana "School starts in forty-five minutes!"
#    MC "Which means I have another fifteen until I’ll be late for sure."
#    "Wrapping myself in my blanket again I have a couple seconds more rest until I sense Hana readying another move. I throw off my blanket to signal my cooperation and head over to the kitchen.{i}"
    
    
#    scene livingroom_day with fade
#    "Two cold plates of eggs, bacon and rice are on the dining table. Hana takes a seat and starts eating . If she wanted to eat with me she could have just said so. I guess she told me she’d be making breakfast last night though..."
#    "*Cellphone ringing*"
#    "{i}Hm? Why am I getting a call this early in the morning?{i}"
#    "{i}Our parents would always use the landline. Anyone at school would just text me if they needed to talk to me, not that I knew many people anyways.{i}"
#    MC "Ah.. an unknown number. No thanks."
#    "*Click*"
#    "{i}I don't care. If it was something important they'll leave a message.{i}"
#    show hana cute at right:
#        xalign 0.5
#        yalign 1.0
#    with fade
#    "{i}I look over and notice Hana shyly looking up at me - waiting for me to say something.{i}"
    
#    menu:
#        "Do you need something?":
#            MC "Hm? Do you need something?"
#            show hana mad at right:
#                xalign 0.5
#                yalign 1.0            
#            Hana "You could say thank you every once in a while ya know..."
            
            
#        "Thanks for breakfast.":
#            MC "Thanks for breakfast Hana. It's pretty good."
#            "{i}Hana gives me a smile.{i}"
#            show hana happy at right:
#                xalign 0.5
#                yalign 1.0
#            Hana "You’re welcome! Next time you can wake up earlier and we can cook together!"
#            $ hanaFriendship += bigReward
            

#        "Breakfast is cold.":
#            MC "Hana, my breakfast is cold."
#            "{i}Hana's shoulders sink a little.{i}"
#            show hana worried at right:
#                xalign 0.5
#                yalign 1.0
#            Hana "It's not my fault..."
    
#    hide hana worried
#    "{i}We continue eating until Hana finally chimes in."
    
#    show hana happy at right:
#        xalign 0.5
#        yalign 1.0
        
#    Hana "Okay, I’m gonna go get ready. Just make sure you don’t fall asleep on your way to school!"
#    "{i}Hana gets up and puts her plate into the sink, heading off.{i}"
#    hide hana happy
#    "{i}I finish my meal and do the same, heading upstairs to get dressed before brushing my teeth.{i}"

    
#    scene black_screen with fade
#    "{i}I strip down from my pajamas and grab my black Moe Boxer underwear from the top drawer of my dresser.{i}"
#    "{i}I grab the nearest of all the clothes I need and throw them on. While I’m in the bathroom, simultaneously washing my face and brushing my teeth, Hana yells that she’s heading out, which means my time is running out.{i}"
#    "{i}I quickly get my things together, grab my bag, and head out the door shortly after Hana leaves, making sure to lock the door behind me.{i}"
    
#    scene road_morning with fade
#    MC "*sigh* The start to another boring school year. I wonder if my friends have changed at all since last year..."
#    "{size=-4}*tip tap tip tap*{/size}"
#    "*tip tap tip tap*"
#    "{size=+4}*tip tap tip tap*{/size}"
#    "*WHAMMMMMMMM!!!*"
#    "{i}I get knocked to the ground by someone behind me.{i}"
#    MC "What the he-"
#    show kaz smug:
#        xalign 0.5
#        yalign 1.0
#    "{i}I look up to see my best friend Kaz standing triumphantly over me.{i}"
#    MC "Oh, it's just you. What was that for?"
#    show kaz happy:
#        xalign 0.5
#        yalign 1.0
#    Kaz "Haha, just thought I’d surprise you. Thought you could really use something to wake you up, sleepy head!"
#    "{i}That’s Kaz, one of my best friends I met 2 years ago in science class. We were partnered up for a chemistry lab one day when he farted over the bunsen burner and set my notes on fire. We had a nice chuckle about that and have been friends ever since.{i}" 
#    MC "I see you haven’t changed a bit over the summer."
#    "{i}I get up and dust myself off.{i}"
#    MC "So what have you been up to all summer?"
#    Kaz "Well, I went away for a few weeks. Other than that, mainly just chilling in my room playing video games."
#    MC "Oh cool, where'd you go?"
#    Kaz "My family had tickets for the worldwide Go Kart championship, so we stayed up in a hotel for a few weeks and went sightseeing and stuff, you know? How about you?"
#    "{i}I didn’t really want to admit that I’ve done nothing all summer except stay inside, binging anime and playing video games, so I just tried to avoid the question.{i}"
#    MC "Uhhh well you know, this and that. You’re on your way to school too? Why so late?"
#    show kaz neutral:
#        xalign 0.5
#        yalign 1.0
#    "{i}I feel so stupid. Of course he’s heading off to school. I hope he just skips over it.{i}"
#    show kaz serious:
#        xalign 0.5
#        yalign 1.0
#    Kaz "Why are YOU so late?"
#    MC "I slept in, obviously."
#    "{i}Phew, that was close.{i}"
#    show kaz happy:
#        xalign 0.5
#        yalign 1.0
#    Kaz "Typical of you. Let’s hurry, we shouldn’t be late on the first day of class."
#    hide kaz happy
#    "{i}We walk at a quicker pace to make up for lost time during our conversation. Within a few minutes we finally reach the school.{i}"
    
    
#    scene classroom_day with fade
#    Teacher "Alright everyone, quiet down please."

#    "{i}Everyone gradually stops their conversations and my first class of the school year begins.{i}"

#    Teacher "Before starting any teaching you’ll be getting the rest of your timetables. Come grab them at the table up here."

#    "{i}Everyone rushes up to the front of the class with excitement, grabbing their schedules and comparing with their friends.{i}"

#    "{i}I reluctantly grab mine and return to my seat.{i}"
    
#    show kaz happy:
#        xalign 0.5
#        yalign 1.0

#    Kaz "Hey dude, let me see your timetable!"

#    "{i}Before I have a chance to look at my timetable, Kaz butts in and swipes it from my hand.{i}"
    
#    show kaz surprised:
#        xalign 0.5
#        yalign 1.0

#    Kaz "Heeeey we have our last class together! We also have the same lunches too!"
    
#    show kaz happy:
#        xalign 0.5
#        yalign 1.0

#    "{i}Kaz happily hands back my timetable. I glance over it, noticing I have a good balance between heavy and easy courses.{i}"

#    "{i}It doesn’t seem like Kaz was so lucky though.{i}"
    
#    show kaz upset:
#        xalign 0.5
#        yalign 1.0

#    Kaz "Aww man… I have 2 math courses this semester. It’s gonna be rough!"
    
#    hide kaz upset

#    "{i}As the class slowly starts to calm down, the noise returns to normal as the teacher continues his introduction.{i}"
#    "{i}I mainly just gaze out the window for the duration of the class until the bell rings. I head off to my next class.{i}"



#    scene black_screen with fade

#    "{i}I sit through my second period, not paying attention again, just waiting for the bell to liberate me to my lunch break.{i}"

#    "{i}Once the bell rings, I take a minute to gather my things and walk out of the classroom. I find Kaz waiting for me in the hallway.{i}"



#    scene schoolhall_day with fade

#    show kaz happy:
#        xalign 0.5
#        yalign 1.0
        
#    Kaz "Hey dude! It's finally lunchtime!"

#    show kaz upset:
#        xalign 0.5
#        yalign 1.0
    
#    Kaz "I can't believe how tired I am of classes already... It's only   been like three hours!"

#    MC "Yeah I know... I almost fell asleep in second period. I guess I shouldn't have slept in so late, now I'm all sluggish and tired."

#    show kaz smug:
#        xalign 0.5
#        yalign 1.0
        
#    Kaz "You should really fix your sleep schedule man!"

#    "{i}I can't believe how hypocritical he's being right now. He woke up late too... why is he lecturing me?{i}"

#    show kaz happy:
#        xalign 0.5
#        yalign 1.0
        
#    Kaz "Well let's not waste more of our lunch. Do you wanna go to the usual spot for lunch?"

#    MC "Yeah sure, let's go."



#    scene black_screen with fade:
#    "{i}Kaz and I head up a few flights of stairs until we reach our usual lunch spot; the school rooftop.{i}"

    
    
    scene schoolroof_day with fade
#    show kaz happy:
#        xalign 0.5
#        yalign 1.0
#    Kaz "MAN what a nice day to be up here!"
#    MC "Yeah the weather is perfect today. It's sunny, there's a slight breeze, it's not too hot... Almost like it's straight out of an anime or something."
#    show kaz neutral:
#        xalign 0.5
#        yalign 1.0
#    "Kaz briefly looks around, admiring the beautiful view of the school rooftop. It's not often that the weather is like this during this time of year."
#    "{i}I take a moment to appreciate the blissful sound of the wind, and as I look up at the sky I can’t help but wish this moment lasted forever.{i}"
#    show kaz surprised with hpunch:
#        xalign 0.5
#        yalign 1.0
#    mysterious "AHHHHHHHH~"
#    "I suddenly feel someone pushing against my back, along with two arms locking me in."
#    MC "H-hey!"
#    show kaz happy:
#        xalign 0.75
#        yalign 1.0
#    show kasumi happy:
#        xalign 0.25
#        yalign 1.0
#    Kasumi "Hey ya big doof! It’s been so long! How was your summer?"
#    MC "I-it was okay I guess..."
#    "Flustered at Kasumi’s sudden attack, that was all I managed to spit out."
#    MC "Um.. anyways, how was your summer?"
#    show kaz neutral:
#        xalign 0.75
#        yalign 1.0
#    "Kasumi began talking in great detail about her amazing and interesting summer excursions. I just slightly nodded my head up and down as if I was paying attention - but I wasn’t."
#    Kasumi "...after that we..."
#    MC "Oh wow… that’s so cool..."
#    show kasumi passive:
#        xalign 0.25
#        yalign 1.0
#    "At some point, Kasumi finishes talking and ends up sitting with Kaz and myself, eating her own lunch."
#    Kasumi "Oh hey, can I see your timetable?"
#    "I let out a faint sigh as I bring out my folded timetable sheet and hand it to her."
#    "She carefully studies it, and as her eyes glance over the last class she can’t help but look thrilled."
#    show kasumi happy:
#        xalign 0.25
#        yalign 1.0
#    Kasumi "Ooo we have our last class together!"
#    show kaz happy:
#        xalign 0.75
#        yalign 1.0
#    Kaz "Woah, really? Me too!"
#    hide kaz happy
#    show kasumi happy:
#        xalign 0.5
#        yalign 1.0
#    "Kasumi smiled, handing back the sheet, giving me a puzzled look."
#    show kasumi passive:
#        xalign 0.5
#        yalign 1.0
#    Kasumi "Do you know what you wanna do after high school? Your courses don’t seem to focus on any specific field."
#    MC "Yeah. I’m not sure what I wanna do yet. I haven’t really put much thought into it."
#    Kasumi "Huh? What do you mean you ‘haven’t really put much thought into it.’? Don’t you have a dream job?"
#    "I shrug my shoulders, briefly looking down as I give it some thought."
#    "Nothing comes to mind."
#    MC "I dunno… what’s your dream job?"
#    "Kasumi tenses up with her gaze locked onto me. I see frustration in her eyes."
#    show kasumi upset:
#        xalign 0.5
#        yalign 1.0
#    Kasumi "Ugh- I talked about it all the time last year... It’s as if you weren’t listening!"
#    MC "Well, I forgot. Can’t you just tell me?"
#    show kasumi disappointed:
#        xalign 0.5
#        yalign 1.0
#    Kasumi "No. You’ll have to guess."
#    "Kasumi crosses her arms, looking up at the sky as if she can no longer see me."
#    "{i}Let’s hope I guess correctly.{i}"
#    hide kasumi disappointed
    
#    menu:
#        "Chef":
#            MC "Well you really like cooking so obviously you wanna become a chef, right?"
#            show kasumi happy:
#                xalign 0.5
#                yalign 1.0
#            Kasumi "So you {i}were{i} listening!"
#            "Kasumi smiles warmly at me, giving a few golf claps."
#            hide kasumi happy
        
#        "Nurse":
#            MC "Well you always seem to be so kind and caring… Being a nurse would fit you perfectly!"
#            show kasumi blushing:
#                xalign 0.5
#                yalign 1.0
#            "{i}Kasumi’s face turns red, and she shoots me an embarrassed look, quickly darting her eyes away.{i}"
#            Kasumi "Well... I mean..."
#            show kasumi passive:
#                xalign 0.5
#                yalign 1.0
#            "Kasumi’s at a complete loss for words, her eyes scanning around as she twirls her fingers."
#            "She gains her composure and smiles warmly at me."
#            show kasumi happy:
#                xalign 0.5
#                yalign 1.0
#            Kasumi "That’s really sweet of you to say… thank you!"
#            "{i}YES I was right!{i}"
#            Kasumi "But you’re dead wrong! I wanna be a chef silly!"
#            MC "Damn, I was so confident in my answer."
#            hide kasumi happy
        
#        "Teacher":
#            MC "Well… when we were little kids all you talked about was being a teacher."
#            show kasumi disappointed:
#                xalign 0.5
#                yalign 1.0
#            "Kasumi lets out a big sigh, tilting her head slightly."
#            Kasumi "I mean, I guess I did talk about being a teacher… in the fourth grade."
#            show kasumi happy:
#                xalign 0.5
#                yalign 1.0
#            Kasumi "I wanna be a chef, but being a teacher is a close second."
#            hide kasumi happy
        
#        "Gardener":
#            MC "You’re a girl so you must like flowers. You want to be a gardener don’t you?"
#            show kasumi upset:
#                xalign 0.5
#                yalign 1.0
#            Kasumi "What? Is that even a job?!"
#            "Kasumi’s face turns red with suppressed anger."
#            Kasumi "Don't you know that I want to be a chef?!"
#            "{i}I guess I should have chosen a different one…{i}"
#            hide kasumi upset
    
#    show kaz happy:
#        xalign 0.5
#        yalign 1.0
#    Kaz "What about me dude? You remember what I wanna do right?"
#    "{i}Why is everyone on my case today?? I didn’t ask to play 20 questions.{i}"
#    hide kaz happy
    
#    menu:
#        "Race car driver":
#            MC "You wanna be a race car driver obviously. You love that stuff."
#            show kaz serious:
#                xalign 0.5
#                yalign 1.0
#            Kaz "Just because we talked about it on our way to school?"
#            "{i}Kaz shakes his head.{i}"
#            show kaz upset
#            Kaz "Tsk tsk… geez man. I thought you knew I wanted to be a professional basketball player."
#            "{i}Welp, I tried.{i}"
#            hide kaz upset
        
#        "Basketball player":
#            MC "Oh! I know this one for sure. You want to become a professional basketball player, right?"
#            show kaz happy:
#                xalign 0.5
#                yalign 1.0
#            "Kaz gives me a smile."
#            Kaz "Damn you actually knew the answer! I didn’t expect that from you."
#            "{i}Phew. That was a complete guess, I got lucky. {i}"
#            hide kaz happy
            
#        "Chemist":
#            MC "Uhhhh… You want to be a chemist right?"
#            show kaz serious:
#                xalign 0.5
#                yalign 1.0
#            Kaz "Dude, I hate chemistry. You should know this, we were in grade 10 chemistry class together!"
#            "{i}Kaz gives me a disappointed look.{i}"
#            show kaz upset
#            Kaz "I thought it was obvious I wanted to become a professional basketball player."
#            "{i}Damn, I should have known. He’s on the school basketball team after all.{i}"
#            hide kaz upset
        
#        "Chef":
#            MC "Dude, of course I know what you want to do! You wanna be a chef."
#            show kaz upset:
#                xalign 0.75
#                yalign 1.0
#            show kasumi disappointed:
#                xalign 0.25
#                yalign 1.0
#            "Both Kasumi and Kaz let out a sigh, slapping the palm of their hand against their face."
#            "{i}They think I’m completely clueless… maybe from now on I should pay attention.{i}"
#            hide kaz upset
#            hide kasumi disappointed
#    
    "We continue eating our lunches for a bit until Kaz straightens up and says something."
    show kaz happy:
        xalign 0.5
        yalign 1.0
    Kaz "Anyways, doesn’t it feel underwhelming now that we’re in fourth year? It’s not like I’ll put more effort in this year compared to the last one."
    MC "Yeah you’d think it’d be exciting, but now everything kinda just meshes together. Doesn’t really mean anything anymore."
    show kaz neutral:
        xalign 0.25
        yalign 1.0
    show kasumi passive:
        xalign 0.75
        yalign 1.0
    "Kasumi raises an eyebrow at the two of us."
    Kasumi "I don’t feel that way at all, I’m kinda scared about it actually."
    Kasumi "I’ve gotten so used to everything, and now I have to worry about my marks so I can get into culinary school. I don’t know if I’ll even survive!"
    "Kasumi looks down at her phone before standing up."
    show kasumi happy
    Kasumi "Lunch is about to end so I’m gonna head off. I’ll see you guys at fourth period!"
    "Kaz gets up as well, we part ways before heading to our next class."
    
    
    scene black_screen with fade
    "{i}I somehow managed to stay awake through the usual ‘this is what this course is going to be about’ jargon.{i}"
    "{i}I’ve heard it so many times... why must they bring about great pain and sorrow every year?{i}"
    "{i}Before I know it, third period slips by and everyone is starting to pack up their bags.{i}"
    "*DING DONG BING BONG*"
    "{i}Guess it’s time for last period. If I remember correctly Kaz and Kasumi should also be in there. I guess it won’t be that bad.{i}"
    
    
    scene classroom_day
    "I walk into my last period class, tech. Maybe this will actually be fun."
    "Kaz notices me enter and calls me over. I see Kasumi is sitting a seat away from him - placing me right in between the two."
    show kaz smug:
        xalign 0.25
        yalign 1.0
    show kasumi passive:
        xalign 0.75
        yalign 1.0
    Kaz "This class is gonna be a breeze."
    show kasumi happy
    "Kasumi nods her head."
    Kasumi "It’ll be a great mark booster, you better do well."
    MC "Yeah, yeah. I know."
    hide kaz smug
    hide kasumi happy
    Teacher "Alright class, I’m supposed to mention that tomorrow is when you’re all supposed to pick your clubs."
    Teacher "You can take a look at the list online, it shows when they meet and whatnot."
    "Everyone starts pulling up their phones, reading through the list. Constant chatter rings throughout the class. I couldn’t care less."
    show kasumi disappointed:
        xalign 0.5
        yalign 1.0
    "Kasumi glares at me with her concerned eyes."
    Kasumi "Don’t you wanna join a club?"
    MC "I mean… I dunno. I have other things to do."
    "Kasumi looks a little disappointed, looking down at her phone."
    Kasumi "I see… if that’s what you want."
    "{i}Why does Kasumi want me to join a club? Looks like she cares about it more than me. Sheesh.{i}"
    show kasumi passive:
        xalign 0.75
        yalign 1.0
    show kaz happy:
        xalign 0.25
        yalign 1.0
    Kaz "Well, I’m gonna join the media club. Sounds like it’ll be a fun excuse to fool around."
    MC "Meh."
    show kaz serious
    "Kaz shakes his head."
    Kaz "Whatever man."
    hide kaz serious
    hide kasumi passive
    "I decide to go on my phone the rest of the class, chuckling at memes and sending them to group chats. It was a productive class."

        
    
    scene black_screen with fade
    "I didn’t even realize how quickly time flew by. I opted to head out with Kaz to go to our lockers before we went home."
    "We walk through the herd of students, bumping shoulders and struggling to get to our lockers."
    "Once I arrive at my destination, I accidentally bump into a girl."
    
    scene lockers_day with hpunch
    mysterious "OOF~!"
    MC "Ahh!"
    show akina annoyed:
        xalign 0.5
        yalign 1.0 
    Akina "Oww-! Watch where you’re going!"
    show akina happy:
        xalign 0.5
        yalign 1.0
    "Akina’s stern and frustrated face face lights up once she recognizes me."
    Akina "Oh, hey! It's you! I haven’t seen you today. We have so much catching up to do!"
    "{i} Woah. Akina really changed over the summer. She looks totally different, and she really *ahem* ‘matured’.{i}"
    MC "Yeah, definitely. But there isn’t that much to talk about. I haven’t really done anything noteworthy this summer."
    Akina "Well I have some stuff to tell you about. Oh! Forget summer for now, have you decided what club you wanted to join?"
    "Akina slightly tilts her head, placing her arms behind her back."
    MC "Well, I’m not really gonna join a club this year."
    "Akina raises her eyebrows at me, amazed at the very idea of not joining a club."
    show akina flustered:
        xalign 0.5
        yalign 1.0
    Akina "Whaat!? But this is your last chance, you gotta join a club!"
    "Akina crosses her arms and gives me a discerning look."
    show akina annoyed:
        xalign 0.5
        yalign 1.0
    Akina "You’re joining the media club with me, whether you want to or not."
    MC "Huh?? You serious?"
    show akina flustered:
        xalign 0.5
        yalign 1.0
    Akina "Yes, I’m serious! I’m not gonna let you sulk in your room this year."
    
    $ answer = False
    $ counter  = 0
    while answer != True:
        menu:
            "Fine":
                show akina happy
                MC "Yeah, sure."
                Akina "Perfect! Now you better not dip. You're coming to every meeting, sick or not!"
                MC "Ugh... Seriously?"
                $ answer = True
                
            "No":
                show akina neutral
                Akina "DOES NOT COMPUTE!"
                "Akina’s eyes widen as she looks dead ahead, motioning her arms as if she’s a stiff robot."
                Akina "I WILL SAY IT AGAIN: YOU WILL JOIN THE MEDIA CLUB THIS YEAR."
                $ counter+=1
                if counter >= 3:
                    "Akina bops you on the head."

                    MC "Ow~!"

                    Akina "STOP RESISTING."
    
    show akina happy
    "Akina smiles, quickly nodding her head."
    Akina "And I’ll hold you to that. We’re gonna be doing lots of fun activities. It’s the media club so we can even do video games if you like!"
    "{i}Hmm… Maybe this media club won’t be so bad after all.{i}"
    show akina happy:
        xalign 0.75
        yalign 1.0
    show kaz happy:
        xalign 0.25
        yalign 1.0
    Kaz "Hey stop flirting and let’s go home, I wanna skedaddle outta here."
    show akina flustered
    "Akina’s face turns a light shade of pink as she glares at Kaz."
    
    menu:
        "Walk home with Akina":
            MC "Actually, I think I wanna catch up with Akina a little bit."
            show akina happy
            Kaz "Alright dude, I’ll catch up with you later. You better be online tonight!"
            show kaz smug
            "Kaz playfully nudges me as he raises his eyebrows."
            $ akinaFriendship += bigReward
            call day1_walk_akina
        
        "Walk home with Kaz":
            MC "What? I wasn’t- ugh. I’ll see you tomorrow Akina."
            show akina happy
            Akina "Yep! Don’t forget about your promise! Let’s catch up another time."
            "{i}The heck? I didn’t promise anything.{i}"
            MC "{size=-12}Uh, yeah! Whatever… {/size}"
            $ kazFriendship += bigReward
            call day1_walk_kaz


    scene livingroom_day with fade
    "I finally arrive home, completely exhausted. I place my bag down and collapse face-first onto the couch."

    show hana happy:
        xalign 0.5
        yalign 1.0
    Hana "How was your day?"
    MC "Mmmnn..."
    show hana mad
    "Hana sighs."
    Hana "I have the {i}worst{/i} brother. First day back and you feel tired? It’s 3 o’clock."
    show hana cute
    MC "It was fine. Got to see old friends again. How was yours?"
    show hana happy
    Hana "Pretty good! I already met some new friends, you’re joining a club right?"
    "{i}Why is everyone in my life so obsessed about clubs? This town is so damn weird.{i}"
    MC "Yes, I’m joining a club. If you must know it’s the media club."
    show hana mad
    "Hana raises an eyebrow."
    Hana "That just sounds like an excuse to fool around."
    MC "Yep."
    hide hana mad
    "Hana shakes her head and turns around, walking off into the kitchen."
    Hana "That’s just like you!" 
    Hana "I’ll let you know when dinner is ready."
    MC "'Kay, I’ll just be upstairs."
    "I lazily lift myself up, grabbing my bag and slinging it over my shoulder." 
    "I head upstairs into my room, continuing to chip away at my important tasks, like looking at my phone."
    
    scene bedroom_evening with fade
    "{i}Oh, let me go download the new Frag Out 2 update, that way I can just hop on after dinner with Kaz.{i}"
    "Instead of watching the download bar slowly fill, I decide to take a nap to pass the time."
    
    scene black_screen with fade
    MC "..."
    "As I drift off to sleep, I begin to think of the school year ahead of me."
    "{i}Will this year be any different?{i}"

    $ counter = 0
    $ stillLooping = True
    
    while stillLooping:
        if counter > 2:
            $ stillLooping = False
        else:
            MC "..."
            $ counter += 1
    
    "A few hours pass before I hear a faint voice echo through the house."
    Hana "{size=-10}Dinner's ready~!{/size}"
    
    scene bedroom_evening with fade
    "My eyes slowly open, and much like a little kid waking up from a nap in the car - I too am a little grumpy and groggy."
    MC "{i}Ugh.{/i} Yeah, yeah I’m up. I’ll be down in a minute."
    
    scene black_screen with fade
    "I hurry down the stairs and head towards the dining room."
    "As sleepy as I was, the smell of dinner helped wake me up."
    
    scene livingroom_evening with fade
    show hana cute
    "I grab some plates and help set the table before sitting down, and watch as Hana brings our dinner to the table."
    
    menu: 
        "Wow, that smells really good.":
            show hana happy
            Hana "Thanks~! I can’t wait to hear what you think. I think I nailed it this time."
            "Hana happily places down a plate of pasta."
            $ hanaFriendship += smallReward
            hide hana happy
        
        "Finally…":
            Hana "You know, it’d go faster if I had some help…"
            "Hana places down a plate of pasta."
            hide hana cute
            
        "I hope this is better than breakfast.":
            show hana mad
            "Hana frowns, her eyes staring deep into mine."
            Hana "Seriously?? You’re the reason why it was so cold!"
            Hana "God, sometimes I can’t even stand you. You {i}could{/i} just be nice for once."
            $ hanaFriendship -= smallReward
            "Hana reluctantly places the pasta on the table, almost dropping it. She turns around to rub her eyes a little before collecting herself and sitting down."
            hide hana mad
    
    "The room is filled with silence except for the constant clatter of our utensils as we dig in to our meal."
    "As I focus on my food I notice a pair of eyes lock onto my face."
    show hana cute
    Hana "So, how is it?"
    
    menu:
        "It’s great! The noodles are exactly how I like them. Maybe I can help you next time.":
            show hana happy
            "Hana’s eyes glow as she pumps her fist in the air."
            Hana "Yes! I knew I nailed it!"
            "Hana happily hums to herself as she stuffs her face with pasta."
            
        "It’s a little dry...":
            show hana mad
            "Hana looks upset."
            Hana "Dry? How can pasta be dry? It’s noodles and sauce, both of which use plenty of water! I bet you’re just being mean for the sake of it."
            "Hana ignores the comment, feeling content with her work."
            
    show hana cute
    Hana "Anyways, did anything else exciting happen on your first day of school?"
    MC "Not really, just found out about my classes and got bombarded to join a club."
    Hana "It wouldn’t be like that if you wanted to actually be involved in something this year."
    "I brush off her snarky comment and continue eating."
    MC "... How was your day?"
    show hana worried
    Hana "You’re actually interested in what I did?"
    "{i}More like just trying to be polite for once. It feels weird.{i}"
    MC "Yeah, tell me about what you did today."
    show hana cute
    Hana "Well for starters I still haven’t decided what club I want to join. There’s book club, music club, photography club… Oh! And I have an {i}amazing{/i} homeroom teacher! She’s really nice and seems invested…"
    "Hana rambles as I half-listen to what she’s saying. I really only caught on to her interest in clubs."
    MC "You haven’t decided on a club yet? Of all people I would’ve thought that you decided already."
    show hana happy
    Hana "There’s just so many! It’s kind of overwhelming to think about. It’s my first year!"
    "Akina’s words echo in the back of my mind. Something about her wanting to mentor first years." 
    MC "Why not join the media club with me?"
    "{i}Uh oh. Did I really just say that?{i}"
    show hana worried
    Hana "Whaaaat? You want me to be in the same club as you?"
    "{i}Maybe I should have been more careful with my words…{i}"
    MC "Yeeeeaaaaahhh… Sure, why not?"
    "{i}Damn it.{i}"
    show hana cute
    Hana "I’ll definitely think about it. That could be fun!"
    "Hana and I finish eating the pasta, so she gets up and brings the dishes over to the sink."
    MC "Thanks for the dinner, Hana."
    show hana happy
    "Hana smiles at me."
    Hana "No problem! Thanks for talking with me!"
    "I slowly get up and trudge off to my room. Maybe having my sister in the same club as me won’t be as bad as I thought."
    
    scene bedroom_latenight with fade
    "I message Kaz as soon as I get to my room, quickly sliding my slick pro-gamer headset on as I turn on my laptop and boot up the game."
    "The hours blissfully slip by as we play Frag Out 2 together. Before I know it, the clock reads 12 pm."
    "I quickly shower and brush my teeth before crawling into bed."
    
    scene black_screen with fade
    scene bedroom_night_dark with fade
    "My weary head sinks into the soft pillow."
    show miyo shadow:
        xalign 0.5
        yalign 1.0
    "As my eyes start to feel heavy, I notice a dark figure standing over me."
    hide miyo shadow
    scene bedroom_night_dark with hpunch
    "I spring up, my eyes scanning around the room as my heart races."
    "{i}It's gone."
    "{i}..."
    "{i}Was I just hallucinating?"
    "I slowly lower my body back into bed, trying to forget about what just happened."
    
    scene black_screen with fade
    "Almost instantly, I feel a wave of exhaustion fall over me, and I drift off into a deep sleep."
    
    scene bedroom_day with fade
    "The birds chirp in the background as the morning sun starts to ease in through the windows, casting onto my eyes and waking me up."
    "{i}I actually had a good sleep, either because yesterday was tiring, or because I’m actually looking forward to today.{i}"
    "I gaze at my alarm clock, realizing I actually woke up slightly before my alarm."

    
    

    

    
    # This ends the game.
    return