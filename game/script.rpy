# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Coconut Popsicle", who_font = "fonts/regaltion_highter.ttf")

transform bop:
    yoffset 0
    xalign 0.5
    yalign 0.5
    anchor (0.5, 0.5)
    zoom 0.5

    block:
        easein 1 yoffset -150
        easeout 1 yoffset 0
        repeat

transform inventory_space:
    yoffset 0
    xalign 0.5
    yalign 0.5
    anchor (0.5, 0.5)
    zoom 0.5

    ease 0.8:
        xalign 0.03
        yalign 0.95
        zoom 0.1 

image bg beach:
    "Backgrounds/bg_beach.jpg"
    xsize config.screen_width
    ysize config.screen_height
 

# The game starts here.

label start:
    scene bg beach

    show coconut_popsicle at bop

    # These display lines of dialogue.
    
    play sound "audio/deltarune-explosion.mp3"

    e "{b}BEHOLD!{b}"
    e "I am the one who pops."
    e "Impressed? I can tell"
    e "Fine, since you're practically {i}begging{/i} for it"
    e "I suppose I could join you on your quest"

    hide coconut_popsicle
    show coconut_popsicle at center, inventory_space

    e "I'm in your inventory now"

    play sound "audio/HS_SE_036.wav"
    "Coconut Popsicle has been added to your inventory."
    e "(:"
    e "Ok! I'm ready"
    e "Let's go!"
    e "{cps=2}...{/cps}"
    e "Let's gooooooooo!"
    e "{cps=2}...{/cps}"
    e "You do not seem particularly enthused"
    e "Do you not like popsicles?"

    e "{cps=2}...{/cps}"

    e "{font=fonts/regaltion_highter.ttf}FINE! I DON'T NEED YOU ANYWAYS{/font}"

    hide coconut_popsicle

    play sound "audio/HS_SE_037.wav"
    "Coconut Popsicle has been removed to your inventory."
    "You absolute monster."

    "Think about what you've done{cps=3}...{/cps}"

    scene black with dissolve 
    call cookieclicker

    return