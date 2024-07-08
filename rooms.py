import pygame


class Room():
    def __init__(self, isTopDoor, isRightDoor, isLeftDoor, isBottomDoor, TR, RR, LR, BR, image):
        self.isTopDoor = isTopDoor
        self.isBottomDoor = isBottomDoor
        self.isRightDoor = isRightDoor
        self.isLeftDoor = isLeftDoor
        self.image = pygame.image.load(image)
        self.topRoom = TR
        self.bottomRoom = BR
        self.rightRoom = RR
        self.leftRoom = LR
    
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
middleLeft = Room(True, True, False, True, 'assets/roomLeft.png')
middleRight = Room(True, False, True, True, 'assets/middleRight.png')
bottomMiddle = Room(True, True, True, False, 'assets/bottomMiddle.png')
bottomRight = Room(True, False, True, False, 'assets/bottomRightCorner.png')
bottomLeft = Room(True, True, False, False, 'assets/bottomLeftCorner.png')
topMiddle = Room(False, True, True, True, 'assets/topRightCorner.png')
topLeft = Room(False, True, False, True, 'assets/topLeftCorner.png')
topRight = middleRight
shopRoom = Room(False, False, False, True, 'assets/shopRoom.png')

roomConnections = {
    mainRoom: [middleLeft, topMiddle, middleRight, bottomMiddle],
    topLeft: [None, None, topMiddle, middleLeft],
    topMiddle:[topLeft, None, topRight, mainRoom],
    topRight:[topMiddle, shopRoom, None, middleRight],
    middleLeft:[None, topLeft, mainRoom, bottomLeft],
    middleRight:[mainRoom, topRight, None, bottomRight],
    bottomLeft:[None, middleLeft, bottomMiddle, None],
    bottomMiddle:[bottomLeft, mainRoom, bottomRight, None],
    bottomRight:[bottomMiddle, middleRight, None, None],
    shopRoom:[None, None, topRight, None]
    
}