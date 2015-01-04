import pygame
import random

pygame.init()

window = pygame.display.set_mode((800,600))
pygame.display.set_caption('Chechi Game')

BLACK  = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
ROAD = (200,200,240)
bulletColor = GREEN

player = pygame.Rect(453,460,60,120)
wall = pygame.Rect(0,600,800,10)
roadLeft = pygame.Rect(270,0,8,700)
roadRight = pygame.Rect(540,0,8,700)
median = 50

pygame.mixer.music.load('helicopter_loop.wav')
bulletSound = pygame.mixer.Sound('gunshot5.wav')


treeImage = pygame.image.load('AN034.gif')
treeStretchedImage = pygame.transform.scale(treeImage,(50,50))
treeImage2 = pygame.image.load('download.jpg')
treeStretchedImage2 = pygame.transform.scale(treeImage2,(100,100))
#treeImage3 = pygame.image.load('tree3.jpg')
#treeStretchedImage3 = pygame.transform.scale(treeImage3,(100,100))
playerImage = pygame.image.load('cr.png')
playerStretchedImage = pygame.transform.scale(playerImage,(60,120))

carImage1 = pygame.image.load('Viper.bmp')
carStretchedImage1 = pygame.transform.scale(carImage1,(60,120))
carImage2 = pygame.image.load('car5.png')
carStretchedImage2 = pygame.transform.scale(carImage2,(60,120))
carImage3 = pygame.image.load('beetle.bmp')
carStretchedImage3 = pygame.transform.scale(carImage3,(60,120))

moveleft = False
moveright = False
moveup = False
movedown = False

gameScore = 0
score = 0
FOODSPEED = 50
foodCounter = 0
carCounter = 0
foods = []
roads = []
cars1 = []
cars2 = []
cars3 = []
trees1 = []
trees2 = []
bullets = []
movespeed = 4
movespeed2 = 6
movespeed3 = 5
collisions = 0

clock = pygame.time.Clock()
gameLoop = True

while gameLoop:
    window.fill(WHITE)
    pygame.mixer.music.play(-1,0.0)
    if (collisions > 3):
        pygame.quit()
    if (score > 800):
        pygame.mixer.music.stop()
        pygame.quit()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveleft = True
            if event.key == pygame.K_RIGHT:
                moveright = True
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.left + 20,player.top,3,10))
            if event.key == pygame.K_UP:
                movespeed2 = 10
                #median = 150
            if event.key == pygame.K_DOWN:
                movespeed2 = 4
           

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveleft = False
            if event.key == pygame.K_RIGHT:
                moveright = False
            if event.key == pygame.K_UP:
                movespeed2 = 6
                #median = 50
            if event.key == pygame.K_DOWN:
                movespeed2 = 6

        if event.type == pygame.MOUSEBUTTONUP:
            bullets.append(pygame.Rect(player.left + 20,player.top,3,10))

    if moveleft == True and player.left > 280 :
        player.left -= movespeed
    if moveright == True and player.right < 538:
        player.left += movespeed

    pygame.draw.rect(window,ROAD,roadLeft)
    pygame.draw.rect(window,ROAD,roadRight)
    foodCounter += 1
    if foodCounter >= FOODSPEED:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(50,200),random.randint(0,40),40,40))
        foods.append(pygame.Rect(random.randint(500,750),random.randint(0,40),40,40))
        trees1.append(pygame.Rect(random.randint(50,200),random.randint(-150,-40),100,100))
        trees1.append(pygame.Rect(random.randint(500,750),random.randint(-100,-40),100,100))
        #trees2.append(pygame.Rect(random.randint(50,200),random.randint(-200,-40),100,100))
        roads.append(pygame.Rect(403,0,6,median))

    carCounter += 1
    if carCounter >= 50 and carCounter < 51:
        cars1.append(pygame.Rect(random.randint(300,500),-10,40,40))
    if carCounter > 150 and carCounter <= 151:
        cars2.append(pygame.Rect(random.randint(300,500),-10,40,40))
    if carCounter > 280 and carCounter <= 300:
        carCounter = 0
        cars3.append(pygame.Rect(random.randint(300,500),-10,40,40))

    for tree in trees1 :
        window.blit(treeStretchedImage2,tree)
        tree.top += movespeed2
    for i in range(len(foods)):
        window.blit(treeStretchedImage,foods[i])
        foods[i].top += movespeed2
        
    for road in roads:
        pygame.draw.rect(window,BLACK,road)
        road.top += movespeed2

    carStyle = random.randint(1,4)
    
    
    
    for car in cars1:
        if car.top > 800:
            cars1.remove(car)
        if player.colliderect(car):
            bulletSound.play()
            collisions += 1
            cars1.remove(car)
        window.blit(carStretchedImage1,car)
        car.top += movespeed2

    for car in cars2:
        if car.top > 800:
            cars2.remove(car)
        if player.colliderect(car):
            cars2.remove(car)
            bulletSound.play()
            collisions += 1
        window.blit(carStretchedImage2,car)
        car.top += movespeed2

    for car in cars3:
        if car.top > 800:
            cars3.remove(car)
        if player.colliderect(car):
            cars3.remove(car)
            bulletSound.play()
            collisions += 1
        window.blit(carStretchedImage3,car)
        car.top += movespeed2
        
    for road in roads:
        if (road.top > 700):
            roads.remove(road)
    window.blit(playerStretchedImage,player)
    clock.tick(70)
    pygame.display.update()
pygame.quit()    
