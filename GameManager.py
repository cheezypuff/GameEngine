import pygame
import GameAction as ga
import World
from ResourceManager import *

class GameManager:

    def __init__(self, size, im):
        self.rm=ResourceManager()
        self.size=size
        self.x=0
        self.W=World.World(size,self.rm)
        self.im = im #copy the input manager passed to us by the core

    
        
        #input testing
        self.paused = False
        self.pause = ga.GameAction("Pause", ga.GameAction.DETECT_INITIAL_PRESS_ONLY) #create action
        self.im.mapToKey(self.pause, pygame.K_SPACE) #register it with the input manager for the space key

        self.reset = ga.GameAction ("Reset", ga.GameAction.DETECT_INITIAL_PRESS_ONLY)
        self.im.mapToKey(self.reset, pygame.K_r)

        self.w = ga.GameAction("Jump")
        self.im.mapToKey(self.w, pygame.K_w)

        self.a = ga.GameAction("Left")
        self.im.mapToKey(self.a, pygame.K_a)

        self.d = ga.GameAction("Right")
        self.im.mapToKey(self.d, pygame.K_d)
    def update(self,dtime):
        #check if the action was triggered
        if self.pause.getAmount() > 0:
            self.paused = not self.paused 
        
        if self.reset.getAmount() > 0:
            self.W.reset()

        if self.a.getAmount() > 0:
            self.W.left()
        elif self.d.getAmount() > 0:
            self.W.right()
        else:
            self.W.stop()

                
        if not self.paused: #only update the world if we are not paused
            self.W.update(dtime)

    def draw(self,screen):
        pygame.draw.rect(screen,[255,255,255],[0,0,self.size[0],self.size[1]])
        self.W.draw(screen)
