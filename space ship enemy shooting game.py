import pygame
pygame.init()

# screen display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("game invention")

# spaceship
pImg = pygame.image.load('spaceship.png')
pX = 600
pY = 480
change = 0

def spaceship(x, y):
    screen.blit(pImg, (x, y))

# enemy space ship
eImg = []
eX = []
eY = []
num, no = 0, 0
for i in range(10):
    eImg.append(pygame.image.load('circular-space-ship.png'))
    eX.append(736-num)
    eY.append(50+no)
    num = num+70
    if i >= 6:
        no = 40

def enemy(i, x, y):
    screen.blit(eImg[i], (x,y))


# bullet
bImg = pygame.image.load('stone.png')
bY = 450
b_position = "rest"
score = 0
pX_bullet_fix =- 100

def bullet(x, y):
    screen.blit(bImg, (x+16,y-16))

# score
font = pygame.font.Font("freesansbold.ttf", 32)
tx, ty = 10, 10
def text(x, y):
    ll = font.render("score: " + str(score), True, (0,0,0))
    screen.blit(ll, (x, y))
    ll = font.render("LEVEL :" + str(level), True, (0, 0, 0))
    if x == 350:
        screen.blit(ll, (x, y+50))
        return
    screen.blit(ll, (x+600, y))

stop=0
ret=0
level=1
running = True
while running:

    screen.fill((255, 255, 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change = -1
            if event.key == pygame.K_RIGHT:
                change = 1
            if event.key == pygame.K_SPACE:

                # space ship monvement
                if b_position == "rest":
                    pX_bullet_fix=pX
                    b_position = "going"
                    if score % 50 == 0:
                        if score >= 50:
                            ret += 0.3
                            level += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change = 0

    #  boundries conditions
    if pX < 0:
        pX = 0
    if pX > 736:
        pX = 736

    # enemy space ship display
    for i in range(10):
        if stop == 1:
            text(350, 250)
            continue
        enemy(i, eX[i], eY[i])

        #enemy movement going down and movinfg left
        if eX[i] < 0:
            eY[i] += 40
            eX[i] = 736
        else:
            eX[i] -= 0.6 + ret

        # bullet collision with space ship
        if eX[i] - 20 <= pX_bullet_fix <= eX[i] + 50:
            if eY[i] <= bY <= eY[i] + 64:
                b_position = "rest"
                bY = 480
                score += 1
                eX[i] = 736
                eY[i] = 50
        # collision enemy and space ship
        if pX <= eX[i] <= pX+60:
            if pY <= eY[i]+60 <= pY+60:
                stop = 1

    # bullet display and moving upside
    if b_position == "going":
        bullet(pX_bullet_fix, bY)
        bY-= 1.2+ret
        if bY < 0:
            b_position = "rest"
            bY=480

    # space ship display
    pX = pX+change
    spaceship(pX, pY)
    text(tx, ty)
    pygame.display.update()




