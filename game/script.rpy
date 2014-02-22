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
image bg alley="../art/bg/Alley.jpg"
image bg kitties="../art/bg/Kittens.jpg"
image bg run="../art/bg/running kitties.jpg."
image bg together="../art/bg/syblings.jpg."
image bg rose="../art/bg/rosemary.jpg."
image bg truck="../art/bg/moving truck.jpg."
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
    b "I remember when you and he were just young’uns. 
       I remember the day your human stepped past my corner with a 
       basket in one arm and a bag of smell-goods in the other. You 
       two were barely balls of fur at first sight,hardly even breathin’."
    scene bg run with fade
    b "But boy could you run. Within a few nights, your brother Oscar was 
       leadin’ you every which way, even into my den on some occasions. 
       You and he were thick as thieves, you were."
    scene bg together with fade
    b " You did everything together. Played, ate, everything. Even played 
       jokes on this old man here. Boy, I remember when you kittens snuck 
       up on me and...well, I’m getting off track. You and he, I never saw 
       a family bond as strong as yours. Even the entrance of that fine feline 
       Rosemary didn’ change nothin’. "
    scene bg rose with fade
    b "She was the prettiest thing I ever saw, but she only had eyes for Oscar 
       and he sure had eyes for her back. He loved her and she darn loved him 
       back, and you, were the happy third leg all the way."
    scene bg truck with fade
    b "Well lookie here, young’un. I think you might have a new playmate. More 
       humans are movin’ in and they have a young’un with them too. You should
       go say hi."
    show Flannery smile with moveinleft
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
           f "Flannery: Oh! Would you introduce me?"
       "None of your business.": 
           f "Flannery: Oh! Would you introduce me?"
       "Her name is Rosemary.":
           f "Flannery: Oh! Would you introduce me?"
 
    return
