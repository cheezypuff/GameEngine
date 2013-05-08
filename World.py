import pygame
from Sprite import *



class World:
    def __init__(self,size,rm):
        self.player = None
        self.rm=rm
        self.size=size
        self.s = size
        self.reset()
    def reset(self):
        self.sprites=[]
        #for x in range (20):
         #   self.sprites.append(Sprite(self.rm.getAnimation("ahhh"),self.size))
        #for x in range (20):
         #   self.sprites.append(Sprite(self.rm.getImage("cronoflip"),self.size))
        for x in range(1):
            self.player = Sprite(self.rm.getAnimation("left"), self.size)
    def update(self,dtime):
        self.player.update(dtime)
        for s in self.sprites:
            s.update(dtime)
    def draw(self,screen):
        for s in self.sprites:
            s.draw(screen)
            
        self.player.draw(screen)




    def jump(self):
        """Causes the player to start jumping"""
        pass

    def left(self):
        """starts the player from moving to the left"""
        self.player.velocity[0] = -30.0


    def right(self):
        """starts moving the player to the right"""
        self.player.velocity[0] = 30.0

    def stop(self):
        """stops the player sprite from moving horizontally"""
        self.player.velocity[0] = 0.0

    



