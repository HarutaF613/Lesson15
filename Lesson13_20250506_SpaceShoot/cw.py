






import pgzrun
import pygame

WIDTH = 1200
HEIGHT = 750
TITLE = "Space Shoot"

#bg = pygame.image.load("background.jpeg")
#bg_scale = pygame.transform.scale(bg,(WIDTH,HEIGHT))

score = 0
ship = Actor("ship")
#ship.pos = (WIDTH//2,HEIGHT-100)
ship.pos = (WIDTH/2,675)
buglist = []
shootlist = []
rgb = ((0,255,0))

#def spawnbugs():
for i in range(7):
    for f in range(4):
        buglist.append(Actor("bug"))
        buglist[-1].x = 450+60*i
        buglist[-1].y = 80+50*f
#spawnbugs()

def update():
    if keyboard.right:
        if ship.x <= WIDTH:
            ship.x += 10
    elif keyboard.left:
        if ship.x >= 0:
            ship.x -= 10

    if keyboard.space:
        print("Pressing space")
        shootlist.append(Actor('bullet'))
        #the last bullet added , set its position
        shootlist[-1].x = ship.x
        shootlist[-1].y = ship.y

    for i in shootlist:
        #if the bullet reaches the top of the screen it should get removed
        # #else the list will becom  e huge
        if i.y <=0 :
            shootlist.remove(i)
            print("deleted the bullet")
        else:
            i.y -= 10

        #print(shootlist)
        #shoot = Actor("bullet")
        #shoot.pos = (ship.x,675)
        #shootlist.append(shoot)
        #for i in range(10):
        #    for shoot in shootlist:
        #        shoot.y -= 50

def draw():
    screen.clear()
    #screen.blit(bg_scale,(0,0))
    #screen.fill(rgb)
    ship.draw()
    for bug in buglist:
        bug.draw()
    for i in shootlist:
        i.draw()

pgzrun.go()