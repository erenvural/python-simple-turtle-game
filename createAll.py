import ourTurtle
import random
import maze

def create_wall (wall_count):
    global walls
    walls = []
    while (wall_count > 0):
       i = rng.randint(-maze.width+1, maze.width-1) # inner walls not adjacent to outer walls
       j = rng.randint(-maze.height+1, maze.height-1)
       new_cell = maze.Cell(i,j)
       if ((i == 0 and j == 0) or new_cell in walls or new_cell in items):
          continue
       else:
          walls.append(new_cell)
          wall_count -= 1
    print(walls)
    drawer.color("black", "black")
    drawer.shape("square")
    drawer.shapesize(1)
    drawer.hideturtle()
    for cell in walls :
        (x,y) = cell.to_coord()
        drawer.goto(x,y)
        drawer.stamp()

def create_items (items_count):
    global items
    items= []
    while (items_count > 0):
        k = rng.randint(-maze.width+1, maze.width-1)
        l = rng.randint(-maze.height+1, maze.height-1)
        new_item = maze.Cell(k,l)
        if ((k==0 and l==0) or new_item in items):
            continue
        else:
            items.append(new_item)
            items_count -=1
    print (items)
    drawer.color("black", "darkgreen")
    drawer.shape("mouse")
    drawer.shapesize(0.8)
    drawer.hideturtle()
    for cell in items:
        (x,y) = cell.to_coord()
        drawer.goto(x,y)
        drawer.stamp()

def create_traps(traps_count):
    global traps
    traps=[]
    while (traps_count > 0):
        m = rng.randint(-maze.width+1, maze.width-1)
        n = rng.randint(-maze.height+1, maze.height-1)
        new_trap = maze.Cell(m,n)
        if ((m==0 and n==0) or new_trap in traps or new_trap in items):
            continue
        else:
            traps.append(new_trap)
            traps_count -=1
    print (traps)
    drawer.color("black", "red")
    drawer.shape("eagle")
    drawer.shapesize(0.8)
    for cell in traps:
        (x,y) = cell.to_coord()
        drawer.goto(x,y)
        drawer.stamp()

def create_key ():
    global key
    key=[]
    key_count=1
    while (key_count > 0):
        e = rng.randint(-maze.width+1, maze.width-1)
        f = rng.randint(-maze.height+1, maze.height-1)
        new_key = maze.Cell (e,f)
        if ((e==0 and f==0) or new_key in traps or new_key in walls):
            continue
        else:
            key.append(new_key)
            key_count -=1
    print (key)
    drawer.shape("key")
    (x,y) = key[0].to_coord()
    drawer.goto(x,y)
    drawer.stamp()

def create_door ():
    global doors
    doors=[]
    door_count=2
    while (door_count > 0):
        b = rng.randint(-maze.width+1, maze.width-1)
        c= rng.randint(-maze.height+1, maze.height-1)
        new_door = maze.Cell (b,c)
        if ((b==0 and c==0) or new_door in traps or new_door in walls or new_door in doors or new_door in items):
            continue
        else:
            doors.append(new_door)
            door_count -=1
    print (doors)
    drawer.shape("door")
    for cell in doors:
        (x,y) = cell.to_coord()
        drawer.goto(x,y)
        drawer.stamp()
    drawer.hideturtle()

drawer=ourTurtle.Turtle()
drawer.penup()
drawer.speed(0)
rng = random.Random()
