# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
#Oscar
image Oscar smile="../art/char/Oscar-happyMouthClosed.gif"
image Oscar happy="../art/char/Oscar-happyMouthOpen.gif"
image Oscar sad="../art/char/Oscar-sad.gif"
image Oscar angry="../art/char/Oscar-mad.gif"
image Oscar confused="../art/char/Oscar-confuse.gif"
image Oscar frustrated="../art/char/Oscar-frustrated.gif"
#Flannery
image Flannery smile="../art/char/Flannery-happy.gif"
image Flannery sad="../art/char/Flannery-sad.gif"
#Rosemary
image Rosemary smile="../art/char/Rosemary-happy.gif"
image Rosemary worried="../art/char/Rosemary-worried.gif"

#backgrounds
image bg blackness="../art/bg/Blackness.jpg."
image bg alley="../art/bg/Alley.jpg"
image bg kitties="../art/bg/Kittens.jpg"
image bg run="../art/bg/running kitties.jpg."
image bg together="../art/bg/syblings.jpg."
image bg rose="../art/bg/rosemary.jpg."
image bg truck="../art/bg/moving truck.jpg."
image bg park= "../art/bg/park.jpg."
image bg appartment= "../art/bg/appartment.jpg."
# Declare characters used by this game.
define o = Character('Oscar', color="#3300CC")
define f = Character('Flannery', color="#FF0000")
define r= Character('Rosemary', color="#FF66FF")
define b= Character('Bernard', color="#CCCCFF")
define s= Character('Scar',color="#3300CC")
define ro= Character('Rose',color="#FF66FF")
define u = Character('???', color="#FFFFFF")


# The game starts here.
label start:
    # Intro 0
    scene bg kitties
    play voice "../sound/voice/Slide0.mp3"
    b "I remember when you and he were just young’uns. 
       I remember the day your human stepped past my corner with a 
       basket in one arm and a bag of smell-goods in the other. You 
       two were barely balls of fur at first sight,hardly even breathin’."
    stop voice
    
    # Intro 1
    scene bg run with fade
    play voice "../sound/voice/Slide1.mp3"
    b "But boy could you run. Within a few nights, your brother Oscar was 
       leadin’ you every which way, even into my den on some occasions. 
       You and he were thick as thieves, you were."
    stop voice
    scene bg together with fade
    
    # Intro 2
    play voice "../sound/voice/Slide2.mp3"
    b " You did everything together. Played, ate, everything. Even played 
       jokes on this old man here. Boy, I remember when you kittens snuck 
       up on me and...well, I’m getting off track. You and he, I never saw 
       a family bond as strong as yours. Even the entrance of that fine feline 
       Rosemary didn’ change nothin’. "
    stop voice
    
    # Intro 3
    scene bg rose with fade
    play voice "../sound/voice/Slide3.mp3"
    b "She was the prettiest thing I ever saw, but she only had eyes for Oscar 
       and he sure had eyes for her as well. He loved her and she darn loved him 
       back, and you, were the happy third leg all the way."
    stop voice
    
    # Start Novel Proper
    scene bg truck with fade
    b "Well lookie here, young’un. I think you might have a new playmate. More 
       humans are movin’ in and they have a young’un with them too. You should
       go say hi."
    show Flannery smile with moveinleft
    play music "../sound/music/Cat Meows.mp3"
    f "Hi ya there, neighbor! I’m Flannery. Nice to meet you!"
    menu:
        f "Hi ya there, neighbor! I’m Flannery. Nice to meet you!"
        "Likewise!":
            $ i=0
        "(Ignore him)":
            show Flannery sad
            f "Sorry, my friend. I didn’t mean to offend you. I’m 
               new here and don’t know anything about everything."
        "Yeah, right. Go back to where you came from!":
            show Flannery sad
            f "Sorry, my friend. I didn’t mean to offend you. I’m 
               new here and don’t know anything about everything."
        "Why do you have glasses?":
            f "Because my insurance didn’t pay for contacts!"
    show Flannery smile
    f "Could you perhaps show me around, friend?"
    menu:
            "Yeah, Sure...":
                f "Well then..."
                with vpunch
                f "LET'S GO!!!"
            "Show yourself!":
                f "Well then..."
                f "LET'S GO!!!"
    hide Flannery smile with moveoutright
    b "Looks like you and he are off to a good start. It’s 
       always good to see you young’uns makin’ new friends.
       Oh! And here comes your brother and his lovely playmate."
    
    # Alley Scene with Oscar
    scene bg alley with dissolve
    show Rosemary worried at left with moveinleft
    show Oscar frustrated at right with moveinright
    r "Oscar, you really shouldn’t do that, you know."
    o "Look, I’ve made my choice and there’s nothing you can say to change that."
    r "Oh, Oscar…"
    hide Rosemary worried with dissolve
    hide Oscar frustrated with dissolve
    show Flannery smile with dissolve
    menu:
       f "Who is that gorgeous she-cat?" 
       "My brother’s mate.":
           f "Oh! Would you introduce me?"
       "None of your business.": 
           f "Oh! Would you introduce me?"
       "Her name is Rosemary.":
           f "Oh! Would you introduce me?"
    show Flannery smile at left with dissolve
    show Rosemary worried at center with dissolve
    show Oscar frustrated at right with dissolve
    f "Hi there. I’m Flannery! Who might you be?"
    show Oscar angry at right
    o "Rosemary, get back. He might be dangerous."
    "Wait! He's my friend!"
    show Oscar confused at right
    o ".......oh..."
    show Oscar happy at right
    o "Okay then, I’m Oscar and this is Rosemary."
    r "Hi..."
    o "Come on Rosemary, I want to show you something."
    hide Oscar happy with moveoutright
    hide Rosemary worried with moveoutright
    hide Flannery smile
    show Flannery smile at center
    f "Oh, Rosemary! Where have you been all my life? Deny your false lover, 
       you are not Oscar’s. Who is Oscar anyway? No paw nor tail nor any other 
       part belongs to a tom. What is in a protector? That which we call a master
       by any other name would claim as much. So Rosemary, would you not be that 
       Oscar’s! And from that tom cat, I must take you for my own."
    menu:
        "Whaaaa?":
            f "I kid; I kid."
        "William Shakespeare much?":
            f "Impressive!"
            
    #Park Scene
    scene bg park with dissolve
    b " With Flannery at your side, you were no longer the third leg. 
       In fact, now you had all four legs! Ha. You and your friends were 
       my favorite part of the day. Days passed and as I was lazing in the sun, 
       I spotted you and your newest friend wandering by."
    show Flannery smile at right
    f "Hey! Guess what? I had this great idea. Wanna hear it?"
    menu: 
        "What would I do that for?":
            f "...well I'm gonna tell you anyway!"
        "Sure, let’s hear it.":
            $i=0
    f "Well, it’s like this. I heard there was this 
       great get-together going on in the alleyway just 
       beyond this park. You should invite your brother and 
       meet me there tonight at sundown. It’ll be totally fun."
    menu:
        "That sounds like fun. We’ll definitely be there.":
            f " Awesome! I’ll see you there then. Don’t forget to invite Oscar!"
        "Like hell I’ll go there. Go by yourself.":
            stop music
            show Flannery sad
            f "Why are you bent on ruining my plans? I just wanted to invite you to 
            something nice and fun! You could just give me a chance! 
            Fine. If you are so desperate to not be friends, then I’ll just leave. 
            Have a nice life!"
            
            # Bad ending
            scene bg blackness with dissolve
            b "Well, where did you go wrong? you lost a friend, but you were able to 
               get over that and live a really happy life with Oscar and Rosemary. ...Or do you?"
            jump badEnd
    hide Flannery with moveoutleft
    show Oscar smile with moveinright
    o "Hey. What’s up?"
    "Flannery invited us to a party tonight"
    show Oscar confused 
    o " Are you sure that’s a good idea?"
    menu: 
        " Not really, but who knows?":
            show Oscar smile
            o "Hm. Well, I guess we can go. Just be on your guard."
        "Yeah, sure. Why not?":
            show Oscar smile
            o "Hm. Well, I guess we can go. Just be on your guard."
    hide Oscar with moveoutright
    b "So at sundown, I watched you and your brother leave your human’s 
       den and hurry along towards the alleyway past the park down by the 
       river in hopes to meet Flannery and have a nice time."
    
    # Dog Scene
    scene bg alley with dissolve
    # TODO Oscar Worried
    o "Where is everybody?"
    "..."
    o "Something’s wrong. We should turn back."
    "No, Flannery should be here somewhere."
    # TODO show dog
    # TODO show Oscar scared
    stop music
    play music "../sound/music/Suspense 1.mp3"
    with hpunch
    o "No! Help!"
    # TODO show Rosemary panic
    r "Do something; he's your brother! Get up and fight!"
    "..."
    label dogDecision:
        menu:
            "Save Oscar":
                # TODO exit Rosemary
                "Hey, flea-face! Get away from my brother!"
                "(The leader ignores you, but another dog roughly grabs you by the scruff)"
                with hpunch
                "Let me go! Let me g-"
                "(Wind rushes through your pelt as you’re hurled through the air. The sickening sound of bone being crushed is followed as your head collides with the alley wall. The world becomes blurry and quickly begins to fade with each passing breath. An agonizing screech of pain is the last thing you hear as your eyes slowly begin to droop.)"
                with vpunch
                "I'm sorry... Oscar..."
                scene bg blackness with dissolve
                jump badEnd
            "ACTIVATE SUPAH POWAH":
                b "By the way, you are the descendant of mighty and powerful jungle cats, these mere hounds got nothing on yer awesome bloodline. You mess these dawgz up and jump on the scene leik a BAWSS."
                o "Brother! You've come to save me!"
                "Yeah, dawg. I’m da BAWSS! now stand back as I prepare to destroy these peasants!"
                with vpunch
                b "Whoa, that was a weird hallucination. You really should concentrate on the giant dogs, instead of thinking you have imaginary powers...weirdo."
                jump dogDecision
            "Run Away":
                # TODO Oscar in pain
                o "HELP!!!"
                r "OSCAR!!"
                "Rosemary..."
                r "You COWARD! How could you not defend your own blood!? He’s always been there for you, and you just left him there!"
                "I'm sorry. There's nothing I could've done."
                # TODO exit rosemary
                scene bg blackness with dissolve
    
    stop music
    scene bg appartment with dissolve
    play music "../sound/music/Cat Meows.mp3"
    b "I haven’t seen anyone besides you for days. No offense, but it’s getting quite boring without everyone else. And you haven’t really been yourself either. Maybe you should get out and try to find your brother. Moping around here isn’t goin’ to solve nothin’."
    scene bg park with dissolve
    # TODO enter scar
    o "Where were you?"
    "..."
    o "I could have died! If Rosemary hadn’t...I would be. What were you thinking?"
    "Oscar, I..."
    o "And that Flannery! I bet you anything he knew those dogs would be there! He probably set the whole thing up to get me out of the way!"
    
    label mistakeDecision:
        menu:
            "You don’t know that. It could have been just a mistake.":
                o "I can’t believe you’re taking his side! He’s been eyeing Rosemary since day one. You know what? Fine. I’m done with you. I’m done with him. I done with the whole lot of you. I’ve found somewhere else where I belong."
                # TODO Oscar exit left
            "You’re right. I’m so sorry. You’re my brother. I should have been there for you.":
                b "What a sap. Try again."
                jump mistakeDecision
    
    scene bg appartment with dissolve
    # TODO enter Bernard
    b "Ello’ there young’ un!"
    "Hello Bernard."
    b "Tis’ been a while since you’ve been out. You’ve begun to worry me."
    "Well don’t worry! I’m nothing but a coward and a traitor!"
    b "Young’un, no need to be so harsh on yourself, besides… Your brother, he’s not far from here. You should go see him, he needs you."
    
    menu:
        "Ignore Bernard and go back home":
            b "Yeah, go ahead. I’ll just stay here and stare at birds or something. Just because I sometimes mistake benches for other cats doesn’t mean I’m not wise. But fine. You go home and live the rest of your days miserable and full of guilt. Doesn’t bother me anyway. You’re a pathetic kitten."
            jump badEnd
        "Ask Bernard where Oscar is":
            b "He’s out and about, past the park and near the forest."
            # TODO Exit Bernard
            b "Beware! Your brother is not the cat you once knew! Tread quietly and be careful!"
        "Do a silly dance":
            "Of course, no one can party as hard as you. You place a piece of toast on your head and become a famous interwebs sensation, whatever that nonsense is.  You eventually forget about your brother, because who needs good family relationships when you’re famous and rich?"
            jump badEnd

    scene bg park with dissolve
    # TODO enter Flannery
    f "Hey. I heard what happened that night. I’m really sorry about your brother."
    "Was it you?"
    f "Of course not. Why would you even think that? Anyway, listen. I’ve heard some bad things about the group Oscar joined. They lure people in by saying they’ll provide a new life, but in reality, they are vicious and I fear for Oscar’s safety, especially since he’s dragged Rosemary into it as well."
    "What can we do?"
    f "You need to try and stop him before he goes too far. Come on. Hurry!"
    # TODO exit Flannery
    
    scene bg blackness with dissolve
    u "Hello there, stranger..."
    "Wha? Who are you?"
    with vpunch
    u "Heh. what a weak little kitty. Now time to inform the boss of our special guest."
    
    #TODO Forest
    stop music
    scene bg blackness with dissolve
    play music "../sound/music/Villain 1.mp3"
    "Ughhh, my head hurts. Where am I?"
    # TODO enter rose
    r "Wake up, coward!"
    "R-Rosemary?"
    r "I go by Rose here now, so call me by the right name or I’ll claw your face off."
    "Were you the one who attacked me?"
    ro "I wish! Thorn was the one who got to you. I don’t understand why she didn’t flay your pathetic pelt."
    "Thorn?"
    ro "One of the many members of Scar's gang."
    "Scar?"
    ro "Ugh, just shut your yap and follow me."
    
    menu:
        "Follow Rosemary":
            scene bg blackness with dissolve
        "Run Away":
            with hpunch
            "Ha! Of course the little scaredy cat would trip up at completing simple orders. Fit for the Ministry of Silly Walks, you are. Get up and follow me, you idiot!"
    
    # TODO define fade
    
    # TODO enter rose
    ro "Stop. We're here."
    "Um...Are we waiting for someone?"
    ro "Scar, we’re waiting for Scar."
    s " Rose! I hear we have a guest, present him to me at once."
    ro "Why of course, Scar!"
    # TODO enter scar
    s "Why hello there, brother."
    "OSCAR?!"
    s "heh, it’s Scar now. A better name, don’t you think?"
    "I’m sorry! I know I should’ve been the one hurt instead of you. You had so much more to lose than I did..."
    s "You’re right. I did have a lot more to lose, and lose it all I did."
    ro "Scar..."
    s "Quiet Rose! Let me speak with my brother, it shouldn’t last long."
    # TODO exit rose
    "Oscar..."
    s "Like I said, it’s Scar now dear brother, wouldn’t want another one in the family to have a damaged face now do we?"
    "Scar, what are you going to do to me?"
    s "Nothing, I swear brother. Just going to ask you a favor that’s all."
    "..."
    s "Join my crew, and become a stronger cat. Then and only then will you truly be forgiven for your crimes against me."
    
    menu:
        "Try to convince Oscar to come back home":
            "Scar, this isn’t you! You’re not a cat capable of ruling a ruthless gang! You belong home, back with me, and Rose, hell, even crazy old Bernard!"
            s "I don’t want to go back to the place that welcomes that orange furball!"
            "Flannery?"
            s "He’s the reason you betrayed me! He’s the reason I have this scar! And he’s tried to take Rose from me!"
            "Oscar, please we can get through this together. Just come back home..."
            s "LEAVE! You obviously don’t want to join and you can’t live a day in this forest on your own."
            "But it’s night..."
            s "Then first thing in the morning. You will leave and never come back!"
        "Join him":
            "I will join your crew, brother."
            s "Good choice, brother, good choice."
            b "Scar welcomes you into the gang, and all the members begin to respect you. However, as the days pass you begin to notice that no one has called you out on your lack of support. You have no skills in fighting or hunting, so you’re nothing more than just an extra mouth to feed. This seems fishy, and your suspicions are confirmed one evening when Rose approaches you."
            r "Hello, little leech."
            "Little leech?"
            r "Haven’t you noticed that no one has taught you the rules of the gang? And that we’ve just let you sit around?"
            "..."
            r "It’s time for you to contribute. I have a task for you."
            "What?"
            r "You must obtain… a SHRUBBERY!"
            menu:
                "Ni!":
                    b "And you had your eyes gouged out and your elbows broken, and had your kneecaps split and your body burned away, and your limbs all hacked and mangled… Oops. Wrong story."
                    jump badEnd
                "What? I can't do that!":
                    r "Alright, in that case… WHAT is the airspeed velocity of an unladen swallow?"
                    menu:
                        "African or European?":
                            r "If you're going to be a smart-aleck, you won’t need to worry about anything but the velocity of my claws!"
                            jump badEnd
                        "I don't know that!":
                            b "You were promptly kicked off a conveniently placed bridge into an equally conveniently placed chasm."
                        
            
    return
    
    label badEnd:
        "-= BAD END =-"
