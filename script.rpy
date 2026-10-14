# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Jun")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_bedroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music "deltarune-explosion.mp3"

    show jun at right
    e"hey look i can teleport"
    show jun at truecenter
    e"isn't that cool?"
    show jun at left
    e"look i did it again"
    e"wanna see me duplicate myself?"
    show jun as jun2 at center 
    show jun as jun3 at right
    e"arent i cool"



    # These display lines of dialogue.


    # This ends the game.

    return
