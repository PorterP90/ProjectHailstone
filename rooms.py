import pygame


class Room():
    def __init__(self, topDoor, rightDoor, leftDoor, bottomDoor, image):
        self.topDoor = topDoor
        self.bottomDoor = bottomDoor
        self.rightDoor = rightDoor
        self.leftDoor = leftDoor
        self.image = pygame.image.load(image)
    
    def topPass(self):
        if self.topDoor == True:
            return True
        else:
            return False
    
    def bottomPass(self):
        if self.bottomDoor == True:
            return True
        else:
            return False
    def leftPass(self):
        if self.leftDoor == True:
            return True
        else:
            return False
    
    def rightPass(self):
        if self.rightDoor == True:
            return True
        else:
            return False
        

mainRoom = Room(True, True, True, True, 'assets/mainRoom.png')
middleLeft = Room(True, True, False, True, 'assets/middleLeft.png')
middleRight = Room(True, False, True, True, 'assets/middleRIght.png')
bottomMiddle = Room(True, True, True, False, 'assets/bottomMiddle.png')
bottomRight = Room(True, False, True, False, 'assets/bottomRightCorner.png')
bottomLeft = Room(True, True, False, False, 'assets/bottomLeftCorner.png')
topMiddle = Room(False, True, True, True, 'assets/topRightCorner.png')
topLeft = Room(False, True, False, True, 'assets/topLeftCorner.png')
topRight = middleRight
shopRoom = Room(False, False, False, True, 'assets/shopRoom.png')