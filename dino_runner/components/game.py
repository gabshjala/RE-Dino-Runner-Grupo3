import pygame, sys
from dino_runner.components.obstacles.obstaclesmanager import ObstacleManager 
from dino_runner.components.dinosaur.dinosaur import Dinosaur
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        self.player = Dinosaur()#instanciar diniosaur

        self.obstacle_manager = ObstacleManager()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.updates()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                self.playing = False

    def updates(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
                #pygame.display.update()

      #        # bg_image = pygame.image.load("Track.png")
       # image_width = BG.get_width()
       
       # bg_track = transform.scale(SCREEN_WIDTH,SCREEN_HEIGHT)
        #time_done=0
        #self.screen.blit(BG, (time_done ,self.y_pos_bg))
        #self.screen.blit(BG, (self.x_pos_bg +image_width+time_done,self.y_pos_bg))
        #if time_done ==-image_width:
         #   self.screen.blit(BG, (self.x_pos_bg+time_done+image_width,self.y_pos_bg))
        #time_done-=time_done
        
        #pygame.display.update() 
       #
       # self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg ))
       # if self.x_pos_bg <=-image_width:
        #    self.screen.blit(BG, (1*image_width+self.x_pos_bg, self.y_pos_bg ))
       #     self.x_pos_bg=0