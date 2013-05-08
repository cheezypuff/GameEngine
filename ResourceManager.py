import pygame
from Animation import *
import copy

class ResourceManager:
    def __init__(self):
        """constructor, makes empty dictionaries, and then calls functions to fill them"""
        self.images={}
        self.animations={}

        self.loadImages()
        self.loadAnimations()

    def loadAnimations(self):
        """Loads all animations for game given the images are already loaded"""
        flash=Animation()
        flash.addFrame(self.getImage("crono"),500)
        flash.addFrame(self.getImage("cronoflip"),500)
        self.animations["ahhh"]=flash

        leftRun = Animation()
        leftRun.addFrame(self.getImage("left1"), 200)
        leftRun.addFrame(self.getImage("left2"), 200)
        leftRun.addFrame(self.getImage("left3"), 200)
        self.animations["left"] = leftRun
        
        

    def loadImages(self):
        """Loads all images for game"""
        self.loadImage("crono", 
                       "./Resources/Images/crono.gif",
                       (255,255,255,0)) #third argument is a key, white, and zero alpha meaning white is going to be transparent
        self.loadImage("cronoflip", 
                       "./Resources/Images/cronoflip.gif",
                       (255,255,255,0))
        self.loadImage("left1", 
                       "./Resources/Images/left1.gif",
                       (255,255,255,0))
        self.loadImage("left2", 
                       "./Resources/Images/left2.gif",
                       (255,255,255,0))
        self.loadImage("left3", 
                       "./Resources/Images/left3.gif",
                       (255,255,255,0))
        self.loadImage("right1", 
                       "./Resources/Images/right1.gif",
                       (255,255,255,0))
        self.loadImage("right2", 
                       "./Resources/Images/right2.gif",
                       (255,255,255,0))
        self.loadImage("right3", 
                       "./Resources/Images/right3.gif",
                       (255,255,255,0))
           







        



    def loadImage(self, name, path, key=None):
        """Loads an image with a name at a given path, and gives it a colorkey"""
        t = pygame.image.load(path).convert()
        t.set_colorkey(key)
        self.images[name]=t

    def getImage(self,name,copy=True):
        """Gets an image from the resource manager with a given name, can make a copy of it"""
        if copy:
        #if just copy it will will be true already since copy is already a true statement
            return self.images[name].copy()
        return self.images[name]

    def getAnimation (self,name):
        """Returns an animation with a given name, all frames data is shared amongst copies"""
        return copy.deepcopy(self.animations[name])
    
