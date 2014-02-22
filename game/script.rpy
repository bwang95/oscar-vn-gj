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


# The game starts here.
label start:
    scene bg kitties
    play voice "../sound/voice/Slide0.mp3"
    b "I remember when you and he were just young’uns. 
       I remember the day your human stepped past my corner with a 
       basket in one arm and a bag of smell-goods in the other. You 
       two were barely balls of fur at first sight,hardly even breathin’."
    stop voice
    scene bg run with fade
    play voice "../sound/voice/Slide1.mp3"
    b "But boy could you run. Within a few nights, your brother Oscar was 
       leadin’ you every which way, even into my den on some occasions. 
       You and he were thick as thieves, you were."
    stop voice
    scene bg together with fade
    play voice "../sound/voice/Slide2.mp3"
    b " You did everything together. Played, ate, everything. Even played 
       jokes on this old man here. Boy, I remember when you kittens snuck 
       up on me and...well, I’m getting off track. You and he, I never saw 
       a family bond as strong as yours. Even the entrance of that fine feline 
       Rosemary didn’ change nothin’. "
    stop voice
    scene bg rose with fade
    play voice "../sound/voice/Slide3.mp3"
    b "She was the prettiest thing I ever saw, but she only had eyes for Oscar 
       and he sure had eyes for her as well. He loved her and she darn loved him 
       back, and you, were the happy third leg all the way."
    stop voice
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
    scene bg alley with dissolve
    
    return
    
    label badEnd:
        "-= BAD END =-"
