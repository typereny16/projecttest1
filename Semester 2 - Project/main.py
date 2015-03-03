import pygame
import random
import math
from healthBar import DrawHealthBar
import gui
from cow_walking import Cow, Pig
from bullet_test import Projectile
from tower import Tower

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0,255,   0)
RED      = ( 255,   0,   0)
MONEY_GOLD = (218,174,31)
SCORE_ORANGE= (255,120,0)
HEALTH_RED  =(190,55,49)
pygame.init()

size=[1076,600]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("SEMESTER 2 - PROJECT")
BACKGROUND = pygame.image.load('map_withhouse.png')
side_bar =pygame.image.load("sideBar.png")
back_color =pygame.image.load("back_color.png")
door_open = pygame.image.load("door_open.png")
clock = pygame.time.Clock()

def towerInHand():
   mouse =pygame.mouse.get_pressed()
   posx,posy = pygame.mouse.get_pos()
   scarecrow_cursor=pygame.image.load("scare_crow.png")
   for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN and posx>835 and posy>339 and posx<876 and posy<372:
         print("True")
         screen.blit(scarecrow_cursor,[posx,posy])
         return True

def isValidTowerSpot(x,y):
   for tower_rect in tower_list: 
      pygame_rect = pygame.Rect(tower_rect)
      if pygame_rect.collidepoint(x,y):
            return False
   for track_rect in track_rectangles:
      pygame_rect = pygame.Rect(track_rect[0]-10,track_rect[1]-10,track_rect[2]+20,track_rect[3]+20,)
      if pygame_rect.collidepoint(x,y):
         return False
   return True

def createTowerIfAllowed(x,y):
   global money
   if money >= 200 and isValidTowerSpot(x,y) and towerInHand():
      new_tower = Tower(x,y)
      tower_list.append(new_tower)
      money -= 200

def towerDialouge():
   tower_label = myfont.render('Click on a tower below',5,WHITE)
   tower_label2 = myfont.render('to build.',5,WHITE)
   screen.blit(tower_label,(843,157))
   screen.blit(tower_label2,(845,182))

def draw_everything():
   pygame.mouse.set_visible(1)
   screen.blit(back_color,[25,0])
   screen.blit(BACKGROUND, [0, 0])
   screen.blit(side_bar, (813,-8))
   money_label = myfont.render(""+str(money), 1, MONEY_GOLD)
   screen.blit(money_label, (868, 27))
   health_label = myfont.render(""+str(health), 1,HEALTH_RED)
   screen.blit(health_label, (973, 57))
   wave_label = myfont.render(""+str(current_wave), 1, WHITE)
   screen.blit(wave_label, (888, 57))
   towerDialouge()
   for enemy in enemy_list:
      if enemy.y > 540:
         print("Opened")
         screen.blit(door_open, [657,545])
        #DrawHealthBar(enemy.rect.x, enemy.rect.y)
      screen.blit(enemy.image, enemy.rect)
   for tower in tower_list:
      screen.blit(tower.image, tower.rect)
   for bullet in bullet_list:
      screen.blit(bullet.image, bullet.rect)
    #update the entire display
   pygame.display.update()
    
gui.LoadingBar()

font = pygame.font.Font(None, 36)
menu_font = pygame.font.Font(None, 48)
myfont = pygame.font.SysFont("Arial", 22)

done = False
colliding_enemy = False
money = 200
health = 10
enemy_list = []
bullet_list = []
tower_list = []
enemies_created = 0
enemy_gameloop_counter = 0
track_rectangles = [[0, 0, 290, 114], [158, 114, 131, 332], [289, 318, 257, 130], [417,87, 127, 232],[544,87,225,154],[635,241,133,303],[768,415,32,131],[800,0,277,608]]
waves = [(0,0),(30,15),(25,20),(20,40),(15,80),(10,160)] #(creation rate, amount of enemies per wave) 
current_wave = 1
# -------- Main Program Loop -----------
while done==False:
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT:
         done=True
      if event.type == pygame.MOUSEBUTTONDOWN:
         mouse_x,mouse_y = pygame.mouse.get_pos()
         createTowerIfAllowed(mouse_x, mouse_y)

   enemy_creation_rate = waves[current_wave][0]
   max_enemies = waves[current_wave][1]
   #determine whether to create a new enemy
   if enemy_gameloop_counter == enemy_creation_rate and enemies_created < max_enemies:
      enemy_gameloop_counter = 0
      new_enemy = random.randrange(1,3)
      if new_enemy == 1:
         new_enemy = Cow()
      else:
         new_enemy = Pig()
      enemy_list.append(new_enemy)
      enemies_created = enemies_created + 1
      #if all the enemies are created and there is another wave
      if enemies_created == max_enemies and current_wave < len(waves)-1:
         current_wave += 1
         enemy_gameloop_counter = -500 #the pause between waves
         enemies_created = 0
   enemy_gameloop_counter = enemy_gameloop_counter + 1

   for enemy in enemy_list:
      enemy.move(3)
      if enemy.y > 540:
         enemy_list.remove(enemy)
         health = health - 1
         print(health)
            
   for tower in tower_list:
      tower.decreaseReload(3)
      if tower.canShoot():
            #determine if a ballon is in range
            target = tower.getCloseEnemy(enemy_list)
            if target != None:
               new_bullet = Projectile(tower,target)
               bullet_list.append(new_bullet)
               tower.shoot()
                

   for bullet in bullet_list:
      bullet.move(3)
        #-1 = nothing hit
      colliding_enemy_index = bullet.rect.collidelist(enemy_list)
      if  colliding_enemy_index != -1:
         colliding_enemy = enemy_list[colliding_enemy_index]
         enemy_list.remove(colliding_enemy)
         bullet_list.remove(bullet)
         money += 10

   draw_everything()

   for track_rect in track_rectangles:
      pos = pygame.mouse.get_pos()
      track_rects = pygame.Rect(track_rect[0]-20,track_rect[1]-20,track_rect[2]+40,track_rect[3]+40,)
      posx,posy = pygame.mouse.get_pos()
      if track_rects.collidepoint(posx,posy) and towerInHand():
         mouse= pygame.image.load("noplace.png")    
         screen.blit(mouse,[posx-10,posy-10])
   for tower_rect in tower_list: 
      tower_rects = pygame.Rect(tower_rect)
      posx,posy=pygame.mouse.get_pos()
      if tower_rects.collidepoint(posx,posy) and towerInHand():
         mouse=pygame.image.load("noplace.png")
         screen.blit(mouse,[posx-10,posy-10])
            
   pygame.display.flip()
            
   clock.tick(20)
    
pygame.quit()
