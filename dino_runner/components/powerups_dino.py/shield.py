from dino_runner.utils.constants import SHIELD,SHIELD_TYPE
from dino_runner.components.powerups_dino.powerup import PowerUp

class Shield(PowerUp):
    def __init__(self):
        self.image=SHIELD
        self.type=SHIELD_TYPE
        super().__init__(self.image,self.type)
        