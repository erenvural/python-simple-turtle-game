import createAll
import maze
import sound
soundList=sound.sounds # sounds list from sound module -> soundList

maze.MazeTurtle.level=3
def createLevel3():
    createAll.create_items(10)
    createAll.create_traps(10)
    createAll.create_wall(20)
    createAll.create_door()
    sound.beep(soundList[0])