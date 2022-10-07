from dino_runner.components.obstacles.obstacle import Obstacle
import random

class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)#de random lib
        super().__init__(image,self.type) #referencia a class padre
        self.rect.y = 325

    
        