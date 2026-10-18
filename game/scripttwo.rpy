define e = Character("Coconut Popsicle", who_font = "fonts/regaltion_highter.ttf")

label cookieclicker:

    play music "audio/ominousMusic.mp3"
    "Long ago (like a few minutes ago)..."
    "A heartless beast discarded the sacred Coconut Popsicle"
    "And destroyed it!"
    "Little did they know that the entire codebase relied on that popsicle"
    "It's up to you to create more Coconut Popsicles!"
    "Make {b}at least five this time{/b}, just in case"
    "Good luck, soldier."
    stop music
    
    $ score = 1
    play music "audio/minigameMusic.mp3"
    call screen cookieClicker
    stop music 

    play sound "audio/victory.mp3"
    show coconut_popsicle at center:
        yoffset 0
        xalign 0.5
        yalign 0.5
        anchor (0.5, 0.5)
        zoom 0.5
    "You did it!"
    e "I live again!"
    play sound "audio/deltarune-explosion.mp3"
    e "I live again!"
    e "Ah, it never gets old..."

    return

screen cookieClicker():
    add "Backgrounds/bg_blueflower.png":
        xsize config.screen_width
        ysize config.screen_height

    imagebutton:
        auto "Icons/continue_%s.png"
        xalign 0.5
        yalign 0.9
        sensitive (score >= 5)
        action Return()

    textbutton "Make Popsicle":
        background "#00eeff"
        hover_background "#11369b"
        xalign 0.33
        yalign 0.5
        padding (50, 20)
        text_color "#08004d"       
        text_size 30              
        text_hover_color "#000000"
        sensitive(score < 1000)
        action Function(increment)

    textbutton "Destroy Popsicle":
        background "#FF0000"
        hover_background "#9B111E"
        xalign 0.66
        yalign 0.5
        padding (50, 20)
        text_color "#8f0058"       
        text_size 30              
        text_hover_color "#000000"
        action Function(decrement)

    vbox:
        text "{b}POPSICLE COUNT{/b}":
            size 60   
        text "{b}[score]{/b}":
            size 60   
            xalign 0.5
            yalign 0.5

        xalign 0.5 
        yalign 0.25
    

init python:
    def increment():
        global score
        score += 1

        if(score % 5 == 0):
            renpy.sound.play("audio/longPop.mp3")
        else:
            renpy.sound.play("audio/shortPop.mp3")

        renpy.restart_interaction() 
        return
    def decrement():
        global score
        if(score < 1):
            return

        score -= 1
        renpy.sound.play("audio/chomp-1.mp3")
        renpy.restart_interaction()
        return

