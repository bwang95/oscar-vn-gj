# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image Oscar smile="../art/char/Oscar-happyMouthClosed.gif"
image Oscar happy="../art/char/Oscar-happyMouthOpen.gif"
image Oscar sad="../art/char/Oscar-sad.gif"

#backgrounds
image bg alley="../art/bg/Alley.jpg"
# Declare characters used by this game.
define o = Character('Oscar', color="#3300CC")
define f = Character('Flannery', color="#FF0000")
define r= Character('Rosemary', color="#FF66FF")
define b= Character('Bernard', color="#CCCCFF")


# The game starts here.
label start:
    scene bg alley
    show Oscar smile
    o "Hi Im a cat! im gonna keep talkin and maybe
       this goes to another line? asfkjsdflkjas;dl
       fkjas;dlfkjas;dlfkjas;dfklja;sdlfkj;salkdjf"
    hide Oscar smile
    o "I'm hiding"
    o "Can you find me?"
    show Oscar happy
    o "I'm Back!"
    show Oscar smile
    o "TEST TEST TEST"
    show Oscar sad
    o "Why do you want to kill me so badly?"
    return
