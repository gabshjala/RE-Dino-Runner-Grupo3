class ObstacleManager:
    def __init__(self):
        self.obstacles=[]

    def update(self,game ):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw(self):
        for obstacle in self.obstacles:
            obstacle.draw(screen)