import pygame


pygame.init()

white=(255,255,255)
blue=(0, 0, 255)
black=(0,0,0)

x1=400
y1=400

speed=10
clock =pygame.time.Clock()
#Display-------------------------------------------------------------------------------
size=(1200,800)
dis=pygame.display.set_mode(size)
pygame.display.set_caption("Wallking")
pygame.display.set_icon(pygame.image.load('icons8-games-64.png'))
bg=pygame.image.load('grass.png')
#Houses--------------------------------------------------------------------------------
house1=pygame.image.load('1.png').convert_alpha()
house1=pygame.transform.scale(house1,(house1.get_width()//6,house1.get_height()//6))
house1_size = pygame.Rect(130, 600, 88, 76)
house2=pygame.image.load('house4.png').convert_alpha()
house2=pygame.transform.scale(house2,(house2.get_width()//3,house2.get_height()//3))
house2_1=house2.set_colorkey((255,255,255))
house2_size = pygame.Rect(155, 130, 78, 40)
house3=pygame.image.load('house3.png').convert_alpha()
house3=pygame.transform.scale(house3,(house3.get_width()//3,house3.get_height()//3))
house3_size = pygame.Rect(728, 162, 92, 49)
house4=pygame.image.load('house1.png').convert_alpha()
house4_1=house4.set_colorkey((255,255,255))
house4_size = pygame.Rect(887, 570, 90, 64)

game_over=True

def drawWindow():
    global player
    player = pygame.Rect(x1, y1, 40, 60)
    pygame.draw.rect(dis, black, player)
    pygame.display.update()
    dis.blit(bg,(0,0))
    dis.blit(house2,(150,100))
    dis.blit(house1, (850, 500))
    dis.blit(house3,(700,100))
    dis.blit(house4,(100,550))

def game():
    global x1, y1,game_over
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y1 > 10:
        if player.colliderect(house2_size) or player.colliderect(house1_size) or player.colliderect(house3_size) or player.colliderect(house4_size):
            y1 += speed
        else:
            y1 -= speed
    if keys[pygame.K_DOWN] and y1 < 730:
        if player.colliderect(house2_size) or player.colliderect(house1_size) or player.colliderect(house3_size) or player.colliderect(house4_size):
            y1 -= speed
        else:
            y1 += speed
    if keys[pygame.K_LEFT] and x1 > 10:
        if player.colliderect(house2_size) or player.colliderect(house1_size) or player.colliderect(house3_size) or player.colliderect(house4_size):
            x1 += speed
        else:
            x1 -= speed
    if keys[pygame.K_RIGHT] and x1 < 1150:
        if player.colliderect(house2_size) or player.colliderect(house1_size) or player.colliderect(house3_size) or player.colliderect(house4_size):
            x1 -= speed
        else:
            x1 += speed


while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False


    clock.tick(10)
    drawWindow()
    game()


pygame=quit()
quit()
