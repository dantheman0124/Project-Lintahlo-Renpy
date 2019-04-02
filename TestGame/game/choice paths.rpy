label day1_walk_akina:
    scene road_morning with fade
    show akina annoyed:
        xalign 0.5
        yalign 1.0
    Akina "Geez, Kaz is such a weirdo!"
    "Akina crosses her arms as she walks alongside me, pouting slightly."
    MC "Yeah… don’t let him get to you. He’s just fooling around."
    "Akina sighs, letting her shoulders sink before stretching her arms out."
    show akina thinking
    Akina "Yeahhh I’ll try. Oh, would you like to hear about my summer?"
    menu:
        "Not really":
            show akina neutral
            $ counter = 0
            $ answer = True
            while answer:
                if counter == 3:
                    $ answer = False
                elif counter%2 == 0:
                    Akina "..."
                    $ counter += 1
                else:
                    MC "..."
                    $ counter += 1
            show akina happy
            Akina "Well I’ll tell you anyways."
        
        "Alright":
            show akina happy
            "Akina’s face lights up."
        
    Akina "Our family took a trip to Cuba! We stayed at a resort on a beautiful beach, and spent lots of time relaxing and unwinding."
    MC "Really? You went to cuba? You didn’t even tan."
    show akina sad
    Akina "Well… I mean, I burn easily so I used gallons of sunscreen."
    show akina happy
    "Akina giggles."
    Akina "Why don’t you tell me what you’ve been up to all summer?"
    MC "Well, uh, you know. Nothing special."
    show akina neutral
    "Akina squints her eyes."
    Akina "Uh huh, go on."
    MC "Really, I didn’t do much this summer. I mainly just chilled at home and played games."
    show akina happy
    Akina "Well that sounds fun, when you come to the club we can play together!"
    MC "That sounds like something that’ll make me go to your club."
    show akina thinking
    Akina "I’m looking forward to it! I wonder who else is gonna join, you think we’re gonna get any first years? I’d love to get to mentor some of them."
    MC "I dunno. What can you even mentor them in? Anime?"
    show akina annoyed
    "Akina lightly flicks my arm."
    Akina "I’m great at computer science!"
    "Akina stops in her tracks once she reaches the crosswalk."
    show akina happy
    Akina "'Kay, my house is this way, I’ll see you tomorrow!"
    "Akina smiles and waves, as she walks towards her house. I wave back and head to my house."

    return

    

label day1_walk_kaz:
    scene schoolfront_day with fade
    MC "Did you really have to embarrass me like that?"
    show kaz upset:
        xalign 0.5
        yalign 1.0
    Kaz "Sorry, but it was too hard to stop myself. You and Akina really get along well. She’d never act so childish around anyone else."
    show kaz neutral
    "Kaz and I start walking side by side."
    "{i}Akina and I do get along pretty well, maybe it’ll be fun to be in the same club as her for this year.{i}"

    scene road_morning with fade
    show kaz happy
    Kaz "Anyways, I’m glad you’re joining a club. It’ll be fun, I promise."
    "{i}I still don’t understand why everyone is pressing me to join a club. Why can’t I just do what I want? Nothing.{i}"
    MC "Yeah, I get it! It’ll be so much fun, I can already tell. Geez."
    show kaz smug
    Kaz "Anyways, are you gonna come online tonight? There’s an update for Frag Out 2, they added a new game mode."
    MC "Sure, we’ll see."
    show kaz happy
    "Kaz throws a thumbs up before separating from me, drifting off onto his street."
    "I walk the rest of the way home, eager to get some time to myself after this grueling day."
    return

