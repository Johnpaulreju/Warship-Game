import pygame
import os
import random
import math

#### MAIN GAME 
pygame.init()

###score

score = 0
fo = pygame.font.Font('freesansbold.ttf',32)  
x=10
y=10

def text(x,y):
    s=fo.render("Score-:" +str(score),True,(255,0,45))
    screen.blit(s , (x,y))




#### All images import
icon=pygame.image.load("image//icon.png")
border=pygame.image.load("image//border.png")
#warship
warship=pygame.image.load("image//warship1.png")
warship_x=300
warship_y=500
warship_speed = 1

def warship_disp(x,y):
    screen.blit(warship,(x,y))

####### alies
alien=[]
alien_x = []
alien_y = []
alien_posx = []
alien_posy = []

num_of_aliens = 3
for i in range(num_of_aliens):
    alien.append(pygame.image.load("image//alien.png"))
    alien_x.append(random.randint(50,500))
    alien_y.append(random.randint(50,200))
    alien_posx .append(1)
    alien_posy .append(1)



def alien_disp(x,y , i):
    screen.blit(alien[i],(x,y))

####collision
def strike(alien_x,alien_y,bullet_x,bullet_y):
    dist = math.sqrt(math.pow(alien_x-bullet_x,2) + math.pow(alien_y-bullet_y,2))
    if dist < 20:      
        return True
    else:
        return False

####### alies
bullet=pygame.image.load("image//bullet.png")
bullet_x = 0
bullet_y = 480
bullet_posx = 10

b_state = False

def bulletshow(x,y):
    screen.blit(bullet,(x,y))


    

screen=pygame.display.set_caption("Spacewarship")
pygame.display.set_icon(icon)
screen=pygame.display.set_mode((600,700))
done=True
clock = pygame.time.Clock()

pygame.mixer.music.load("song//song.mp3")
pygame.mixer.music.play(0)

while done:
    screen.blit(border,(0,0))
    
    for event in pygame.event.get():
        if event.type== pygame.QUIT :
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT or event.key== ord('d'):
                warship_speed += 3
            if event.key==pygame.K_LEFT or event.key==ord('a') :
                warship_speed -= 3
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0] and b_state == False:
                pygame.mixer.music.load("song//bulletsoung.mp3")
                pygame.mixer.music.play(0)
                bullet_x =warship_x
                b_state = True

        
  


        if event.type == pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key== ord('d'):
                warship_speed += 0
            if event.key==pygame.K_LEFT or event.key==ord('a') :
                warship_speed -= 0

    for i in range(num_of_aliens):
        alien_x[i] += alien_posx [i]
        if alien_x[i]<=22:
            alien_posx[i] = 3
            alien_y[i] += alien_posy[i]
        if alien_x[i]>=500:
            alien_posx[i] = -3
            alien_y[i] += alien_posy[i]
        
        if strike(alien_x[i],alien_y[i],bullet_x,bullet_y):
            bullet_y = 480
            pygame.mixer.music.load("song//blast.mp3")
            pygame.mixer.music.play(0)
            score += 1
            b_state = False

        alien_disp(alien_x[i],alien_y[i], i)


    warship_x += warship_speed 
    if warship_x<=22:
        warship_x=22
    if warship_x>=500:
        warship_x=500 
    warship_disp(warship_x,warship_y)

    if b_state:
        bullet_y -= bullet_posx
        bulletshow(bullet_x+35,bullet_y+10)
    if bullet_y<=0:
        bullet_y = 480
        b_state = False
  
    text(x,y)

    pygame.display.update()
    
pygame.quit()