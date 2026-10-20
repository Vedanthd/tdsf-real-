label cookie_clicker:
  $ cool_points = 0 
  stop music
  call screen Cookie
  return



  screen Cookie():
    add "coolimage.jpg":
      xsize config.screen_width
      ysize config.screen_height


    textbutton "VERY COOL!":
      xalign 0.2
      background "#ff00ea"
      yalign 0.7
      action Function(increment)

    textbutton "NOT COOL!!!":
      xalign 0.7
      yalign 0.7
      background "#ff00ea"
      action Function(decrement)
    
    vbox:
      xalign 0.5
      yalign 0.2
      text "{b}COOL POINTS{/b}":
        color "#FF0000"
        size 60
      text "[cool_points]":
        color "#FF0000"
        xalign 0.5
      text "GET TO 100 IF YOU WANT TO LIVE":
        color "#8000FF"



  init python:
    def increment():
      global cool_points
      cool_points += 1
      renpy.sound.play("deltarune-explosion.mp3")
      if cool_points >= 100:
        return True

    def decrement():
      global cool_points
      if cool_points > 0:
        cool_points -= 1
      renpy.sound.play("sadtrombone.mp3")
      
        
