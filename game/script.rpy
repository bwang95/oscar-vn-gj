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
image Oscar worried="../art/char/Oscar-worried.gif"
#Flannery
image Flannery smile="../art/char/Flannery-happy.gif"
image Flannery sad="../art/char/Flannery-sad.gif"
image Flannery mad="../art/char/Flannery-mad.gif"
image Flannery evil="../art/char/Flannery-evil.gif"
#Rosemary
image Rosemary smile="../art/char/Rosemary-happy.gif"
image Rosemary worried="../art/char/Rosemary-worried.gif"
image Rose gang="../art/char/Rosemary-gang.gif"
image Rose sad="../art/char/Rosemary-gangSad.gif"
#Bernard
image Bernard norm="../art/char/Bernard.gif"
#Scar
image Scar angry="../art/char/scar-angry.gif"
image Scar happy="../art/char/scar-happy.gif"
image Scar mad="../art/char/scar-mad.gif"
image Scar regret="../art/char/scar-regret.gif"
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
image bg forest="../art/bg/forest.jpg"
#background SCENES
image bg dog="../art/Dog attack scene.png"
image bg die="../art/DIE.png"
# Declare characters used by this game.
define o = Character('Oscar', color="#3300CC")
define f = Character('Flannery', color="#FF0000")
define r= Character('Rosemary', color="#FF66FF")
define b= Character('Bernard', color="#CCCCFF")
define s= Character('Scar',color="#3300CC")
define ro= Character('Rose',color="#FF66FF")
define u = Character('???', color="#FFFFFF")
define t= Character('Thorn', color="#FFFFFF")

init python:
    config.has_autosave = True
    config.autosave_frequency = 10
    config.fade_music = 0.5

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
            f "Sorry, my friend. I didn’t mean to offend you." 
            f "I’m new here and don’t know anything about everything."
        "Yeah, right. Go back to where you came from!":
            show Flannery sad
            f "Sorry, my friend. I didn’t mean to offend you." 
            f "I’m new here and don’t know anything about everything."
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
    b "Looks like you and he are off to a good start." 
    b "It’s always good to see you young’uns makin’ new friends."
    b "Oh! And here comes your brother and his lovely playmate."
    
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
    show Rosemary worried at right with dissolve
    show Oscar frustrated at center with dissolve
    f "Hi there. I’m Flannery! Who might you be?"
    show Oscar angry at right
    o "Rosemary, get back. He might be dangerous."
    "Wait! He's my friend!"
    show Oscar confused at right
    o ".......oh..."
    show Oscar happy at center
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
    b " With Flannery at your side, you were no longer the third leg." 
    b "In fact, now you had all four legs! Ha." 
    b "You and your friends were my favorite part of the day."
    b "Days passed and as I was lazing in the sun, I spotted you and your newest friend wandering by."
    show Flannery smile at right
    f "Hey! Guess what? I had this great idea. Wanna hear it?"
    menu: 
        "What would I do that for?":
            f "...well I'm gonna tell you anyway!"
        "Sure, let’s hear it.":
            $i=0
    f "Well, it’s like this." 
    f "I heard there was this great get-together going on in the alleyway just 
       beyond this park." 
    f "You should invite your brother and 
       meet me there tonight at sundown." 
    f "It’ll be totally fun."
    menu:
        "That sounds like fun. We’ll definitely be there.":
            f " Awesome! I’ll see you there then. Don’t forget to invite Oscar!"
        "Like hell I’ll go there. Go by yourself.":
            stop music
            show Flannery mad
            f "Why are you bent on ruining my plans?"
            f "I just wanted to invite you to something nice and fun!" 
            f "You could just give me a chance!" 
            f "Fine. If you are so desperate to not be friends, then I’ll just leave." 
            f "Have a nice life!"
            
            # Bad ending
            scene bg blackness with dissolve
            b "Well, where did you go wrong?" 
            b "you lost a friend, but you were able to get over that and live a really happy life with Oscar and Rosemary."
            b "...Or do you?"
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
       river"
    b "in hopes to meet Flannery and have a nice time."
    
    # Dog Scene
    scene bg alley with dissolve
    show Oscar worried with dissolve
    o "Where is everybody?"
    "..."
    o "Something’s wrong. We should turn back."
    "No, Flannery should be here somewhere."
    stop music
    play sound "../sound/effect/growl.mp3"
    play music "../sound/music/Suspense 1.mp3"
    with hpunch
    scene bg dog 
    o "No! Help!"
    # TODO show Rosemary panic
    r "Do something; he's your brother! Get up and fight!"
    "..."
    label dogDecision:
        menu:
            "Save Oscar":
                # TODO exit Rosemary
                "Hey, flea-face! Get away from my brother!"
                b "The leader ignores you, but another dog roughly grabs you by the scruff"
                with hpunch
                "Let me go! Let me g-"
                b "Wind rushes through your pelt as you’re hurled through the air." 
                b "The sickening sound of bone being crushed is followed as your head collides with the alley wall." 
                b "The world becomes blurry and quickly begins to fade with each passing breath." 
                b "An agonizing screech of pain is the last thing you hear as your eyes slowly begin to droop."
                with vpunch
                "I'm sorry... Oscar..."
                scene bg blackness with dissolve
                jump badEnd
            "ACTIVATE SUPAH POWAH":
                b "By the way, you are the descendant of mighty and powerful jungle cats, these mere hounds got nothing on yer awesome bloodline." 
                b "You mess these dawgz up and jump on the scene leik a BAWSS."
                o "Brother! You've come to save me!"
                "Yeah, dawg. I’m da BAWSS! now stand back as I prepare to destroy these peasants!"
                with vpunch
                b "Whoa, that was a weird hallucination. You really should concentrate on the giant dogs, instead of thinking you have imaginary powers...weirdo."
                jump dogDecision
            "Run Away":
                # TODO Oscar in pain
                scene bg blackness
                with vpunch
                with hpunch
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
    b "I haven’t seen anyone besides you for days." 
    b "No offense, but it’s getting quite boring without everyone else." 
    b "And you haven’t really been yourself either." 
    b "Maybe you should get out and try to find your brother. Moping around here isn’t goin’ to solve nothin’."
    scene bg park with dissolve
    # TODO enter scar
    show Scar mad with dissolve
    o "Where were you?"
    "..."
    o "I could have died! If Rosemary hadn’t...I would be. What were you thinking?"
    "Oscar, I..."
    o "And that Flannery! I bet you anything he knew those dogs would be there! He probably set the whole thing up to get me out of the way!"
    
    label mistakeDecision:
        menu:
            "You don’t know that. It could have been just a mistake.":
                o "I can’t believe you’re taking his side! He’s been eyeing Rosemary since day one. You know what? Fine." 
                o "I’m done with you. I’m done with him. I done with the whole lot of you. I’ve found somewhere else where I belong."
                hide Scar mad with moveoutleft
            "You’re right. I’m so sorry. You’re my brother. I should have been there for you.":
                b "What a sap. Try again."
                jump mistakeDecision
    
    scene bg appartment with dissolve
    show Bernard norm with dissolve
    b "Ello’ there young’ un!"
    "Hello Bernard."
    b "Tis’ been a while since you’ve been out. You’ve begun to worry me."
    "Well don’t worry! I’m nothing but a coward and a traitor!"
    b "Young’un, no need to be so harsh on yourself, besides… Your brother, he’s not far from here. You should go see him, he needs you."
    
    menu:
        "Ignore Bernard and go back home":
            b "Yeah, go ahead. I’ll just stay here and stare at birds or something." 
            b "Just because I sometimes mistake benches for other cats doesn’t mean I’m not wise." 
            b "But fine." 
            b "You go home and live the rest of your days miserable and full of guilt. Doesn’t bother me anyway. You’re a pathetic kitten."
            jump badEnd
        "Ask Bernard where Oscar is":
            b "He’s out and about, past the park and near the forest."
            hide Bernard normal
            # TODO Exit Bernard
            hide Bernard
            b "Beware! Your brother is not the cat you once knew! Tread quietly and be careful!"
        "Do a silly dance":
            "Of course, no one can party as hard as you. You place a piece of toast on your head and become a famous interwebs sensation, whatever that nonsense is.  
             You eventually forget about your brother, because who needs good family relationships when you’re famous and rich?"
            jump badEnd

    scene bg park with dissolve
    show Flannery sad with dissolve
    f "Hey. I heard what happened that night. I’m really sorry about your brother."
    "Was it you?"
    f "Of course not. Why would you even think that? Anyway, listen." 
    f "I’ve heard some bad things about the group Oscar joined." 
    f "They lure people in by saying they’ll provide a new life, but in reality, they are vicious and I fear for Oscar’s safety," 
    f "especially since he’s dragged Rosemary into it as well."
    "What can we do?"
    f "You need to try and stop him before he goes too far. Come on. Hurry!"
    hide Flannery sad with dissolve
    
    scene bg blackness with dissolve
    u "Hello there, stranger..."
    "Wha? Who are you?"
    with vpunch
    u "Heh. what a weak little kitty. Now time to inform the boss of our special guest."
    
    #TODO Forest
    stop music
    scene bg forest with dissolve
    play music "../sound/music/Villain 1.mp3"
    "Ughhh, my head hurts. Where am I?"
    # TODO enter rose
    show Rose gang
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
    scene bg forest with fade
    # TODO enter rose
    show Rose gang
    ro "Stop. We're here."
    "Um...Are we waiting for someone?"
    ro "Scar, we’re waiting for Scar."
    s " Rose! I hear we have a guest, present him to me at once."
    ro "Why of course, Scar!"
    # TODO enter scar
    show Scar happy at right with moveinright
    s "Why hello there, brother."
    "OSCAR?!"
    s "Heh, it’s Scar now. A better name, don’t you think?"
    "I’m sorry! I know I should’ve been the one hurt instead of you. You had so much more to lose than I did..."
    s "You’re right. I did have a lot more to lose, and lose it all I did."
    ro "Scar..."
    s "Quiet Rose! Let me speak with my brother, it shouldn’t last long."
    # TODO exit rose
    hide Rose gang with dissolve
    "Oscar..."
    s "Like I said, it’s Scar now dear brother, wouldn’t want another one in the family to have a damaged face now do we?"
    "Oscar, what are you going to do to me?"
    s "Nothing, I swear brother. Just going to ask you a favor that’s all."
    "..."
    s "Join my crew, and become a stronger cat. Then, and only then, will you truly be forgiven for your crimes against me."
    
    menu:
        "Try to convince Oscar to come back home":
            "Oscar, this isn’t you! You’re not a cat capable of ruling a ruthless gang! You belong home, back with me, and Rose, hell, even crazy old Bernard!"
            show Scar mad at right
            s "I don’t want to go back to the place that welcomes that orange furball!"
            "Flannery?"
            s "He’s the reason you betrayed me! He’s the reason I have this scar! And he tried to take Rose from me!"
            "Oscar, please we can get through this together. Just come back home..."
            s "LEAVE! You obviously don’t want to join and you can’t live a day in this forest on your own."
            "But it’s night..."
            s "Then first thing in the morning. You will leave and never come back!"
        "Join him":
            "I will join your crew, brother."
            s "Good choice, brother, good choice."
            b "Scar welcomes you into the gang, and all the members begin to respect you." 
            b "However, as the days pass you begin to notice that no one has called you out on your lack of support." 
            b "You have no skills in fighting or hunting, so you’re nothing more than just an extra mouth to feed." 
            b "This seems fishy, and your suspicions are confirmed one evening when Rose approaches you."
            ro "Hello, little leech."
            "Little leech?"
            ro "Haven’t you noticed that no one has taught you the rules of the gang? And that we’ve just let you sit around?"
            "..."
            ro "It’s time for you to contribute. I have a task for you."
            "What?"
            ro "You must obtain… a SHRUBBERY!"
            menu:
                "Ni!":
                    b "And you had your eyes gouged out and your elbows broken, and had your kneecaps split and your body burned away, and your limbs all hacked and mangled… Oops. Wrong story."
                    jump badEnd
                "What? I can't do that!":
                    ro "Alright, in that case… WHAT is the airspeed velocity of an unladen swallow?"
                    menu:
                        "African or European?":
                            ro "If you're going to be a smart-aleck, you won’t need to worry about anything but the velocity of my claws!"
                            jump badEnd
                        "I don't know that!":
                            b "You were promptly kicked off a conveniently placed bridge into an equally conveniently placed chasm."
        "Give up":
            b "Are you serious?" 
            b "You’re almost done with the game and you decide to just go “durr hurrr derrr” and s
               elect the quit button?" 
            b "Well, you know what? Fine. Go ahead;"
            b "Just quit the game and go back to watching 
               cruddy channels on YouTube and surfing for Lolz on r/
               funny." 
            b "See if I care, not like I put hours into making 
               this game for your dumb self! *sniff*"
            b "You made me cry, you monster. I hope you saved" 
    hide Scar mad
    b "Trapped in the dark, you need to make the best of what you can." 
    b "But you’ve never been very good at that, have you?" 
    b "So instead of following my advice and being careful, you, of course, end up moving away from the safety of the den that Scar prepared for you." 
    b "There, you come across a scene that I would’ve run away from at my age."
    show Rose sad at right with dissolve
    show Scar mad at left with dissolve
    ro "Scar, I know you want revenge but there’s no point. What’s done is done. Besides we’re better off here; we can start over
       . We could even...start a family."
    s "Don’t be silly Rose, any kittens we would have would never be safe with that monster Flannery 
       on the loose!"
    ro " But how could he hurt us? We’re in a large and dark forest, inhabited by other cats that listen to your every command!"
    s "Rose, I refuse to lose you, much less bring kittens into that possibility."
    ro "Bu-"
    s "Enough! My decision is final, Flannery needs to be out of the picture."
    hide Rose gang with dissolve
    hide Scar mad with dissolve
    b "So you heard it; you might lose your only friend. What are you going to do about it?"
    menu:
        "Do nothing. He's a jerk anyway.":
            scene bg blackness
            t "What are you doing? Spying on our leader, are you? That’s punishable by death!"
            b "YOU DEAD"
            jump badEnd
        "Warn Flannery":
            "I need to run back and warn Flannery!"
    stop music
    play music "../sound/music/Cat Meows.MP3"
    scene bg alley with fade
    show Flannery smile
    f "Hey buddy! Why are you so out of breath??"
    "You...Oscar...trouble..."
    f "Whoa! Slow down, friend! What's going on?"
    "Oscar...going to...kill you. Blames you...for dogs..."
    f "What? But you know I had nothing to do with that right?"
    menu:
        "I'm not sure anymore...":
            f "What did I ever do to deserve this?"
        "Of course! You're my best friend~.":
            f "I knew I could count on you!"
    stop music
    play music "../sound/music/Suspense 1.MP3"
    show Scar mad at right with dissolve
    show Flannery mad at left
    s "Brother! I knew you would betray me again. There is no one I can 
       trust besides myself now, it seems."
    "Oscar..."
    s "Flannery, you fiend! I’ve come to finish what you started."
    f "What I started? I'm not the one responsible for any of this!"
    s "Don't play innocent with me, you're the reason my life went to hell!!
       I refuse to let you do further damage to it."
    f "Oh? And if I was hypothetically ruining your life how could I make it any worse?"
    show Scar happy at right
    s "Ha! You can't because Rose is mine and mine alone. No matter what you do
       you can never have her."
    f "While that is quite unfortunate as I do have something even more important to you"
    show Scar mad at right
    s "..."
    #TODO evil happy~ at left
    show Flannery evil at left
    f "My 'best friend'...your brother"
    b "Ouch...it seems those words hit a nerve, because Oscar went straight for Flannery’s throat."
    show Flannery mad at left
    b "However, it seems Flannery isn’t bad when it comes to dodging blows."
    b "But Flannery cannot keep it up for long, Oscar is definitely the stronger of the two." 
    b "So young’un who will you back up? Your dear brother or your best friend?"
label BROTHER:
    menu:
        "Back up your Bro":
            "Oscar! I would never fight you"
            s "Then whose side are you on: mine or his?"
            menu:
                   "Yours of course!":
                       s "Then fight with me!"
                       show Flannery mad at left
                       f "HOW DARE YOU DEFY ME!!!"
                       b  "Blood is thicker than water, or so they say." 
                       b  "You made the right choice." 
                       b  "However, you are a bit of a weakling, no offense."
                       b  "Flannery, your supposed best friend, turns against you and in the midst of the fighting that breaks 
                           out, he, unfortunately, snaps your neck." 
                       b  "Yeah, good job young’un. See you in heaven!"
                       jump badEnd
                   "His...I lied.":
                       show Scar regret at right
                       s "...How could you..." 
                       jump badEnd
        "Defend Flannery":
            f "You're quite the fighter!"
            s "Heh...you're pretty pathetic just dodging my blows and not being bothered to deliver your own."
            f "You're right but you forgot about your brother!"
            show Scar regret at right
            s "No..."
            "I'm sorry Oscar but I can't let you hurt my friend!"
            b "Seriously? You choose to defend someone you barely met about a week ago over your own brother?" 
            b "Are you stupid? Lucky for you I’ll let you make this choice again because seriously you just 
               end up dead in this one."
            jump BROTHER
        "Try to stop the fighting":
            b "Throughout this whole adventure, you’ve tried to find a way to keep both your friend and your brother." 
            b "All your attempts so far have failed, but even though you may not be the strongest kitty out there, 
               you sure are persistent." 
            b "So you run to the fight, not to support either side, but to stop the bloodshed
               between them." 
            b "You try to accomplish this by pushing Flannery to the side."
            "Please, stop you guys don’t have to this!"
    show Flannery mad at left
    f "What are you doing?! Can't you tell we're in an importan-"
    b "Small bits of rock begin to fall as you inadvertantly knock Flannery into the wall"
    show Scar angry at right
    s "WATCH OUT!" 
    hide Scar angry
    hide Flannery mad
    scene bg die
    b "Both you and Flannery stare as the large rock inevitably makes its way down;" 
    b "however, before it can reach you, you feel a sudden push from your right and watch as the rock smashes on top of both your friend and
       brother instead." 
    b "The instant was quick, and the damage from a distance seemed minimal." 
    b "Yet as you walked closer, the scent of blood filled the air and only a large pool of it was evidence of where Flannery once 
       stood." 
    b "Your brother,  on the other hand, managed to run fast enough to only have half of his body crushed."
    b "...But the damage was done."
    scene bg blackness with dissolve
    show Scar regret at center
    o "I’m sorry. I should have trusted you all along. I let my anger take a hold of me instead of leaving it 
       alone like you would have." 
    o "I’m so sorry...tell Rosemary I’m sorry...so sorry..."
    "Oscar! No...I...It's my...! No..."
    hide Scar regret with dissolve
    "-=End=-"
    return
    
    label badEnd:
        "-= BAD END =-"
