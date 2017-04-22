import createAll
import maze
import sound
soundList=sound.sounds # sounds list from sound module -> soundList

maze.MazeTurtle.level=1
def createLevel1():
    createAll.create_items(5)
    createAll.create_traps(5)
    createAll.create_wall(10)



