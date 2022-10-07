import pygame
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_HEIGHT, BIRD

class FlyingDino(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image,self.type) #referencia a class padre
        self.rect.y = random.randrange(50, 330)
        self.rect.x = random.randrange(900,1000)
        #self.rect.x = random.randrange(900, 1100)
        