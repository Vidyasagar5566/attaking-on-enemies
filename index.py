import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(("rocket game"))

# rocket
pImg = pygame.image.load(("img_1.png"))
pX=300
pY=480

def rocket(x, y):
    screen.blit(pImg, (x, y))

# enemy
eImg = []
eX = []
eY = []
ret=0
for i in range(10):
    eImg.append(pygame.image.load(("circular-space-ship.png")))
    eX.append(736-ret)
    eY.append(50)
    ret+=70

def enemy(i, x, y):
    screen.blit(eImg[i], (x, y))

# bullet
bImg = pygame.image.load("stone.png")
bY = 480

def bullet(x, y):
    screen.blit( bImg,(x+10, y))

# score printing
font = pygame.font.Font("freesansbold.ttf", 32)
tx, ty = 10, 10
def text(x, y):
    ll = font.render("score :" + str(score), True, (0, 0, 0))
    screen.blit(ll, (x, y))


count=0
def_bullet = "rest"
running = True
bully = 0
bullx = 0
score,stop = 0,0
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                count -= 1
            if event.key == pygame.K_RIGHT:
                count += 1
            if event.key == pygame.K_SPACE:
                if def_bullet == "rest":
                    def_bullet = "going"
                    bully = pY
                    bullx = pX
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                count=0


    # enemy diplay
    for i in range(10):
        if stop == 1:
            text(300, 280)
            continue
        enemy(i, eX[i], eY[i])
        if eX[i]<=0:
            eX[i]=736
            eY[i]+=50
        else:
            eX[i]-=0.7

        # bullet collision
        if eY[i]-30 <= bully <= eY[i]+30 and def_bullet == "going":
            if eX[i]-30 <= bullx <= eX[i]+30:
                score+=1
                eX[i], eY[i] = 736, 50
                def_bullet = "rest"

        # game over
        if eY[i]+64 >= 480:
            if eX[i] <= pX+60:
                stop = 1

    # space ship display
    pX += count
    if pX <= 0:
        pX = 0
    if pX >= 736:
        pX = 736

    # bullet display
    if def_bullet == "going":
        bullet(bullx, bully)
        bully-=1
        if bully<=0:
            def_bullet = "rest"

    # score
    text(tx, ty)

    rocket(pX, pY)
    pygame.display.update()
















