# Eren VURAL 120709027
# Mahmut KOCAKER 120709041

import maze
import ourTurtle
import random
import createAll
import level1,level2, level3
import sound

soundList=sound.sounds # sounds list from sound module -> soundList

def turn_left():
   mario.dir = maze.LEFT

def turn_right():
   mario.dir = maze.RIGHT

def turn_up():
   mario.dir = maze.UP

def turn_down():
   mario.dir = maze.DOWN

def is_wall(cell):
    """Returns true if the given cell contains an outer on inner wall"""
    return (abs(cell.x) == maze.width + 1)   or   \
           (abs(cell.y) == maze.height + 1)  or   \
           cell in createAll.walls   # inner wall

def debug():
    maze.clear_cell(drawer, maze.Cell(6,6))
    mario.move_to_cell(maze.Cell(0,0))

timerCount=0
def timeUpdate(controller):
   if controller:
      global timerCount
      while timerCount>0:
         timerCount-=1/5
         timer_drawer.undo()
         timer_drawer.write("TIME = {0}".format(int(timerCount)), move=False,
                                align="center", font=("Arial", 9, "normal"))
         return timerCount
      return timerCount

#   wn.ontimer(timeUpdate, 200)
def update():
   timeUpdate(True)
   if (mario.dir != maze.STAND):
       old_heading = mario.heading()
       if (mario.dir == maze.LEFT): new_heading = 180
       elif (mario.dir == maze.RIGHT): new_heading = 0
       elif (mario.dir == maze.UP): new_heading = 90
       else: new_heading = 270
       if (old_heading != new_heading):  # turn mario
          old_speed = mario.speed()
          mario.speed(0)  # turn off animation
          mario.setheading(new_heading)
          mario.speed(old_speed)
#############################################################################
       # determine new cell assuming mario can move
       new_cell = maze.Cell(mario.cell.x, mario.cell.y)  # copy current cell
       if (mario.dir == maze.LEFT): new_cell.x -= 1
       elif (mario.dir == maze.RIGHT): new_cell.x += 1
       elif (mario.dir == maze.UP): new_cell.y += 1
       else: new_cell.y -= 1
       if (not is_wall(new_cell)):
          mario.forward(maze.cell_size)
          mario.cell = new_cell
#############################################################################
          if (userLevel==2 and mario.score==70):
            if (mario.cell in createAll.key):
                maze.clear_cell(drawer, mario.cell)
                createAll.key.remove(mario.cell)
                mario.score +=20
                score_drawer.undo()  # clear latest text
                score_drawer.write("SCORE = {0}".format(mario.score), move=False,
                                    align="center", font=("Arial", 9, "normal"))
                achieveLevel(3)
                print("Level 2 completed")
                controller=False
          if (userLevel==1 and mario.score==120):
            if (mario.cell in createAll.key):
                maze.clear_cell(drawer, mario.cell)
                createAll.key.remove(mario.cell)
                mario.score +=20
                score_drawer.undo()  # clear latest text
                score_drawer.write("SCORE = {0}".format(mario.score), move=False,
                                    align="center", font=("Arial", 9, "normal"))
                achieveLevel(3)
                print("Level 2 completed")
                controller=False
################################################################################
          if userLevel==3:
            if mario.cell in createAll.doors:
                value=createAll.doors.index(mario.cell)
                if value==1:
                 mario.cell=createAll.doors[0]
                 old_speed = mario.speed()
                 mario.speed(0)  # turn off animation
                 mario.hideturtle()
                 (x,y) = createAll.doors[0].to_coord()
                 mario.goto(x,y)
                 mario.speed(old_speed)
                 mario.showturtle()
                else:
                 mario.cell=createAll.doors[1]
                 old_speed = mario.speed()
                 mario.speed(0)  # turn off animation
                 mario.hideturtle()
                 (x,y) = createAll.doors[1].to_coord()
                 mario.goto(x,y)
                 mario.speed(old_speed)
                 mario.showturtle()
          if userLevel==1 and mario.score>=140:
             if mario.cell in createAll.doors:
                value=createAll.doors.index(mario.cell)
                if value==1:
                 mario.cell=createAll.doors[0]
                 old_speed = mario.speed()
                 mario.speed(0)  # turn off animation
                 mario.hideturtle()
                 (x,y) = createAll.doors[0].to_coord()
                 mario.goto(x,y)
                 mario.speed(old_speed)
                 mario.showturtle()
                else:
                 mario.cell=createAll.doors[1]
                 old_speed = mario.speed()
                 mario.speed(0)  # turn off animation
                 mario.hideturtle()
                 (x,y) = createAll.doors[1].to_coord()
                 mario.goto(x,y)
                 mario.speed(old_speed)
                 mario.showturtle()
          if userLevel==2 and mario.score>=90:
             if mario.cell in createAll.doors:
                value=createAll.doors.index(mario.cell)
                if value==1:
                 mario.cell=createAll.doors[0]
                 old_speed = mario.speed()
                 mario.speed(0)  # turn off animation
                 mario.hideturtle()
                 (x,y) = createAll.doors[0].to_coord()
                 mario.goto(x,y)
                 mario.speed(old_speed)
                 mario.showturtle()
                else:
                 mario.cell=createAll.doors[1]
                 old_speed = mario.speed()
                 mario.speed(0)  # turn off animation
                 mario.hideturtle()
                 (x,y) = createAll.doors[1].to_coord()
                 mario.goto(x,y)
                 mario.speed(old_speed)
                 mario.showturtle()
####################################################################################

          if(mario.cell in createAll.items):
            maze.clear_cell(drawer, mario.cell)
            createAll.items.remove(mario.cell)
            mario.score += 10
            score_drawer.undo()  # clear latest text
            score_drawer.write("SCORE = {0}".format(mario.score), move=False,
                                align="center", font=("Arial", 9, "normal"))

######################################################################################
            if userLevel==1:
               if mario.score==50:
                  print("Level 1 Completed")
                  achieveLevel(2)
               if mario.score==120:
                  createAll.create_key()
                  controller=False
               if mario.score==240:
                  print("Level 3 Completed")
                  achieveLevel(0)
                  controller=False

            elif userLevel==2:
               if mario.score==70:
                  createAll.create_key()
               if mario.score==190:
                  print("Level 3 Completed")
                  achieveLevel(0)
                  controller=False
            else:
                 if mario.score==100:
                  print("Level 3 Completed")
                  achieveLevel(0)
                  controller=False
######################################################################################
          if (mario.cell in createAll.traps):
            sound.beep(soundList[3])
            maze.clear_cell(drawer, mario.cell)
            createAll.traps.remove(mario.cell)
            reset()
            mario.move_to_home()
            mario.lives -= 1
            live_drawer.undo()
            if mario.lives<=0:
                live_drawer.write("LIVES = {0}".format(mario.lives), move=False,
                                    align="center", font=("Arial", 9, "normal"))
                wn.title("GAME OVER")
                endGame("GAME OVER")
                sound.beep(soundList[1])
            else:
                live_drawer.write("LIVES = {0}".format(mario.lives), move=False,
                                    align="center", font=("Times New Roman", 9, "normal"))

          if int(timerCount)==0:
            #wn.title("GAME OVER")
            endGame("GAME OVER")
            sound.beep(soundList[1])

       else:  # mario can't move
          mario.dir = maze.STAND   # until the user presses another arrow key, just stand
       msg="Mario at ({0}, {1})  SCORE={2}   LIVES={3}".format(mario.cell.x, mario.cell.y, mario.score, mario.lives)
       if mario.lives<=0:
          msg="GAME OVER"
       if userLevel==1 and mario.score==220:
          msg="CONGRATULATIONS"
          controller=False
       elif userLevel==2 and mario.score==170:
          msg="CONGRATULATIONS"
          controller=False
       elif userLevel==3 and mario.score==100:
          msg="CONGRATULATIONS"
          controller=False
       if int(timerCount)==0:
          msg="GAME OVER"
       wn.title(msg)
   wn.ontimer(update, 200)
######################################################################################
def reset():
    mario.dir = maze.STAND
    mario.setheading(0)

def endGame(msg):
    mario.hideturtle()
    mario.speed(1)
    mario.goto(0,0)
    mario.color("red")
    mario.write("{0}".format(msg), move=False,
                    align="center",font=("Verdana", 27, "bold"))
    mario.goto(-600,600)

def achieveLevel(nextLevel):
    reset()
    if nextLevel==2:
       sound.beep(soundList[6])
       maze.clear_screen(drawer)
       level2.createLevel2()
       mario.move_to_home()
       level_drawer.undo()
       level_drawer.write("LEVEL = {0}".format(2), move=False,
                            align="center", font=("Verdana", 9, "normal"))
    elif nextLevel==3:
            sound.beep(soundList[6])
            maze.clear_screen(drawer)
            level3.createLevel3()
            mario.move_to_home()
            level_drawer.undo()
            level_drawer.write("LEVEL = {0}".format(3), move=False,
                                align="center", font=("Verdana", 9, "normal"))
    elif nextLevel==0:
       endGame("CONGRATULATIONS")
       sound.beep(soundList[-1])

def start():
   s_drawer.undo()
   sound.beep(soundList[5])
   mario.showturtle()
   wn.onkey(turn_left, "Left")
   wn.onkey(turn_right, "Right")
   wn.onkey(turn_up, "Up")
   wn.onkey(turn_down, "Down")

wn = ourTurtle.Screen()
wn.bgcolor(maze.bg_color)
wn.title("Maze")
wn.setup(710,710)
wn.screensize(700,700)

wn.onkey(start,"s")

#OurTurtles
drawer = ourTurtle.Turtle()
s_drawer = ourTurtle.Turtle()
score_drawer =  ourTurtle.Turtle()
live_drawer = ourTurtle.Turtle()
level_drawer = ourTurtle.Turtle()
timer_drawer= ourTurtle.Turtle()
for t in [drawer, score_drawer, live_drawer, level_drawer, s_drawer, timer_drawer]:
    t.fillcolor("black")
    t.speed(0)
    t.hideturtle()
    t.penup()

# draw outer walls
short_side = maze.cell_size
long_side_w = (2*maze.width+3)*maze.cell_size
long_side_h = (2*maze.height+3)*maze.cell_size
(x,y) = maze.Cell(-maze.width-1, maze.height+1).to_coord(True)
maze.fill_rect(drawer,x,y,short_side, long_side_h)
maze.fill_rect(drawer,x,y,long_side_w,short_side)
(x,y) = maze.Cell(-maze.width-1, -maze.height-1).to_coord(True)
maze.fill_rect(drawer,x,y,long_side_w,short_side)
(x,y) = maze.Cell(maze.width+1, maze.height+1).to_coord(True)
maze.fill_rect(drawer,x,y,short_side,long_side_h)

sound.beep(soundList[2])
# draw inner walls
controller=True
while controller:
    userLevel=int(wn.numinput("Which level do you want to start?", "Please write '1' for Level 1 (Beginner)\nPlease write '2' for Level 2 (Amateur\nPlease write '3' for Level 3 (Professional)"))
    if (userLevel<=3 and userLevel>=1):
        if userLevel==1:
            level1.createLevel1()
            timerCount=60
            controller=False
        elif userLevel==2:
            level2.createLevel2()
            timerCount=45
            controller=False
        elif userLevel==3:
            level3.createLevel3()
            timerCount=30
            controller=False
        break

mario = maze.MazeTurtle()
mario.hideturtle()
mario.shape("snake") #-----> hero ---->snake
mario.shapesize(1.5)
mario.color("darkblue", "blue")

(x,y) = maze.Cell(0,maze.height+2).to_coord()
score_drawer.goto(x,y-8)
score_drawer.write("SCORE = {0}".format(mario.score), move=False,
                    align="center", font=("Arial", 9, "normal"))
live_drawer.goto(253,y-8)
live_drawer.write("LIVES = {0}".format(mario.lives), move=False,
                    align="center", font=("Times New Roman", 9, "normal"))
level_drawer.goto(-244,y-8)
level_drawer.write("LEVEL = {0}".format(userLevel), move=False,
                    align="center", font=("Verdana", 9, "normal"))
timer_drawer.goto(x,y-(maze.height*2*maze.cell_size)-101)
timer_drawer.write("TIME = {0}".format(int(timerCount)), move=False,
                    align="center", font=("Arial", 9, "normal"))
drawer.shape("eagle")
drawer.goto(-((maze.width+1)*maze.cell_size),y-(maze.height*2*maze.cell_size)-101)
drawer.stamp()
drawer.goto(-((maze.width+1)*maze.cell_size)+23,y-(maze.height*2*maze.cell_size)-110)
drawer.write("--> Predator", move=False, align="left", font=("Verdana", 9, "normal"))
drawer.shape("mouse")
drawer.goto(((maze.width+1)*maze.cell_size),y-(maze.height*2*maze.cell_size)-101)
drawer.stamp()
drawer.goto(((maze.width+1)*maze.cell_size)-23,y-(maze.height*2*maze.cell_size)-110)
drawer.write("Food <--", move=False, align="right", font=("Verdana", 9, "normal"))
##################################################################################
s_drawer.goto(0,-0.8*23)
s_drawer.color("white smoke")
s_drawer.write("Press 's' to start the game", move=False,
                align="center", font=("Verdana", 23, "normal"))

update()
timeUpdate(True)

wn.listen()  # listen events on this window
wn.mainloop()   # keep the window open
