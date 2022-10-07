from dino_runner.utils.constants import BIRD, HAMMER,SCREEN_WIDTH,SCREEN_HEIGHT
import pygame, random
y =random.randint(0,2)
Color = [(0,0,0),(255,255,255),(164,196,0)]
class Hammer():
    def __init__(self):
        super().__init__()
        self.image=HAMMER
        self.image.set_colorkey(BLACK)#quiat fondo blanco
        self.rect= self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=BIRD
        self.rect=self.image.get_rect()

pygame.init()

screen= pygame.display.set_mode(SCREEN_WIDTH,SCREEN_HEIGHT)
clock = pygame.time.Clock()
done=False
score=0
hammer_list=pygame.sprite.Group()
player_hammers_sprite_list=pygame.sprite.Group()
for x in range(50):
    hammer=Hammer()
    hammer.rect.x = random.randrange(100, 1000)
    hammer.rect.y = random.randrange(100,500)
    hammer_list.append(meteor)
    player_hammers_sprite_list.append(meteor)

player= Player()
player_hammers_sprite_list.append(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    
    pyr_pos = pygame.mouse.get_pos()
    player.rect.x = pyr_pos[0]
    player.rect.y = pyr_pos[1]

    hammers_collect_list= pygame.spritecollide(player,hammer_list,True)


    for hammer in hammers_collect_list:
        score+=1
        print(score)
    
    screen.fill(Color[y])
    player_hammers_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(70)

pygame.quit()


