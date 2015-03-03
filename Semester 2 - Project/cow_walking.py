'''
Created on Feb 18, 2015

@author: 33271
'''
import pygame
from healthBar import DrawHealthBar

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN    = (   0, 255,   0)
BLUE = (0, 128, 255)
 
class SpriteSheet(object):
    sprite_sheet = None
 
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name)
 
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height])
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(BLACK)
        return image
     
class Cow(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    
    direction_turn_points = [("right",244),("down",361),("right",505),("up",155),("right",715),("down",430),("down",550)]
    
    walking_frames_l = []
    walking_frames_r = []
    walking_frames_up = []
    walking_frames_down = []

    direction = "R"

    def __init__(self):
        super().__init__()
 
        sprite_sheet = SpriteSheet("cow_walk1.png")
        # Right Images
        image = sprite_sheet.get_image(25, 420, 83, 62)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(156, 420, 83, 62)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(287, 420, 83, 62)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(412, 420, 83, 62)
        self.walking_frames_r.append(image)
 
        # Left Images
        image = sprite_sheet.get_image(13, 164, 94, 59)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(139, 164, 94, 59)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(265, 164, 94, 59)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(398, 164, 94, 59)
        self.walking_frames_l.append(image)

        # Up Images
        image = sprite_sheet.get_image(50, 38, 29, 76)
        self.walking_frames_up.append(image)
        image = sprite_sheet.get_image(179, 38, 29, 76)
        self.walking_frames_up.append(image)
        image = sprite_sheet.get_image(306, 38, 29, 76)
        self.walking_frames_up.append(image)
        image = sprite_sheet.get_image(434, 38, 29, 76)
        self.walking_frames_up.append(image)        
 
        # Down Images
        image = sprite_sheet.get_image(50, 301, 28, 60)
        self.walking_frames_down.append(image)
        image = sprite_sheet.get_image(179, 301, 28, 60)
        self.walking_frames_down.append(image)
        image = sprite_sheet.get_image(306, 301, 28, 60)
        self.walking_frames_down.append(image)
        image = sprite_sheet.get_image(434, 301, 28, 60)
        self.walking_frames_down.append(image)    
 
        self.image = self.walking_frames_r[0]

        self.rect = self.image.get_rect()
        self.direction = 0
        self.x = -20
        self.y =25 
        self.rect.center = (self.x,self.y)
    
    def move(self, speed):
        self.rect.x += self.x
        pos = self.rect.x
        self.rect.y += self.y
        posy = self.rect.y
        
        #get the string for the current direction the balloon is traveling
        current_direction = Cow.direction_turn_points[self.direction][0]
        turn_pixel = Cow.direction_turn_points[self.direction][1]
        if current_direction == "left":
            self.x = self.x - speed
            if self.x < turn_pixel:
                self.direction = self.direction + 1
        elif current_direction == "right":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
            self.x = self.x + speed
            if self.x > turn_pixel:
                self.direction = self.direction + 1
        elif current_direction == "up":
            frame = (posy // 30) % len(self.walking_frames_up)
            self.image = self.walking_frames_up[frame]
            self.y = self.y - speed
            if self.y < turn_pixel:
                self.direction = self.direction + 1
        elif current_direction == "down":
            frame = (posy//30) % len(self.walking_frames_down)
            self.image = self.walking_frames_down[frame]
            self.y = self.y + speed
            if self.y > turn_pixel:
                self.direction = self.direction + 1
        self.rect.center = (self.x, self.y) 

        
class Pig(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    direction_turn_points = [("right",244),("down",361),("right",505),("up",155),("right",715),("down",400)]
    
    walking_frames_l = []
    walking_frames_r = []
    walking_frames_up = []
    walking_frames_down = []

    direction = "R"

    def __init__(self):
        super().__init__()
 
        sprite_sheet = SpriteSheet("pig_walk1.png")
        # Right Images
        image = sprite_sheet.get_image(34, 436, 63, 34)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(163, 436, 63, 34)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(292, 436, 63, 34)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(419, 436, 63, 34)
        self.walking_frames_r.append(image)
 
        # Left Images
        image = sprite_sheet.get_image(13, 164, 94, 59)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(139, 164, 94, 59)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(265, 164, 94, 59)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(398, 164, 94, 59)
        self.walking_frames_l.append(image)

        # Up Images
        image = sprite_sheet.get_image(50, 38, 29, 76)
        self.walking_frames_up.append(image)
        image = sprite_sheet.get_image(179, 38, 29, 76)
        self.walking_frames_up.append(image)
        image = sprite_sheet.get_image(306, 38, 29, 76)
        self.walking_frames_up.append(image)
        image = sprite_sheet.get_image(434, 38, 29, 76)
        self.walking_frames_up.append(image)        
 
        # Down Images
        image = sprite_sheet.get_image(50, 301, 28, 60)
        self.walking_frames_down.append(image)
        image = sprite_sheet.get_image(179, 301, 28, 60)
        self.walking_frames_down.append(image)
        image = sprite_sheet.get_image(306, 301, 28, 60)
        self.walking_frames_down.append(image)
        image = sprite_sheet.get_image(434, 301, 28, 60)
        self.walking_frames_down.append(image)    
 
        self.image = self.walking_frames_r[0]

        self.rect = self.image.get_rect()
        self.direction = 0
        self.x = -20
        self.y =25 
        self.rect.center = (self.x,self.y)
     
    def move(self, speed):
        self.rect.x += self.x
        pos = self.rect.x
        self.rect.y += self.y
        posy = self.rect.y
        
        #get the string for the current direction the balloon is traveling
        current_direction = Cow.direction_turn_points[self.direction][0]
        turn_pixel = Cow.direction_turn_points[self.direction][1]
        if current_direction == "left":
            self.x = self.x - speed
            if self.x < turn_pixel:
                self.direction = self.direction + 1
        elif current_direction == "right":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
            self.x = self.x + speed
            if self.x > turn_pixel:
                self.direction = self.direction + 1
        elif current_direction == "up":
            frame = (posy // 30) % len(self.walking_frames_up)
            self.image = self.walking_frames_up[frame]
            self.y = self.y - speed
            if self.y < turn_pixel:
                self.direction = self.direction + 1
        elif current_direction == "down":
            frame = (posy//30) % len(self.walking_frames_down)
            self.image = self.walking_frames_down[frame]
            self.y = self.y + speed
            if self.y > turn_pixel:
                self.direction = self.direction + 1
        self.rect.center = (self.x, self.y)
    
        
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)

clock= pygame.time.Clock()

cow = Cow()
pig = Pig()
