'''
Created on Feb 20, 2015

@author: 33271
'''
import pygame, math

GREEN = [0,117,35]

screen = pygame.display.set_mode((800,600))

class Tower(pygame.sprite.Sprite):
    image = pygame.image.load("scare_crow.png")
    max_reload_time = 50

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        
        if Tower.image is None:
                # This is the first time this class has been
                # instantiated. So, load the image for this and
                # all subsequence tower instances.
                Tower.image = pygame.image.load("scare_crow.png")
        self.image = Tower.image

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        self.reload_time = 0 #time left to wait between shots
        self.reload_max = 150 #how long it should take between shots
        self.range = 150 #max pixels to balloon in order to shoot at it


    def shoot(self):
        self.reload_time = self.reload_max
   
    def canShoot(self):
        if self.reload_time <= 0:
            return True
        else:
            return False

    def decreaseReload(self,game_speed):
        self.reload_time = self.reload_time - game_speed

    def getCloseEnemy(self,enemy_list):
        for enemy in enemy_list:
            if self.distance(enemy) <= self.range:
                return enemy
        return None

    def distance(self,enemy):
        dist = (self.x-enemy.x)*(self.x-enemy.x) + (self.y-enemy.y)*(self.y-enemy.y)
        dist = math.sqrt(dist)
        return dist

