import createAll
import maze
import sound
soundList=sound.sounds # sounds list from sound module -> soundList

maze.MazeTurtle.level=2
def createLevel2():
    createAll.create_items(7)
    createAll.create_traps(7)
    createAll.create_wall(15)


