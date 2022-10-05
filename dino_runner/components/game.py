import pygame
from dino_runner.utils.constants import ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        print("test")
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()


        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.game_speed=0

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.updates()
            self.draw()

        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing=False
    
    def updates(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((225,255,255))
        self.draw_background()
        self.player.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
    
    def draw_background(self):
        image_with = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_with+ self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg<=-image_with:
            self.screen.blit(BG, (image_with+self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed