from turtle import Screen
import pygame
from dino_runner.utils.constants import SHIELD_TYPE, RUNNING_SHIELD, DEFAULT_TYPE, JUMPING_SHIELD, DUCKING_SHIELD, RUNNING, DUCKING, JUMPING
from pygame.sprite import Sprite

Black=(0,0,0)
class Dinosaur(Sprite):
    X_POS=80
    Y_POS=310
    Y_POS_DUCK=340 #AGACHADO Y SERA USADO UNA VEZ IMPLEMENTADO LOS EVENTS
    JUMP_LEVEL=8.5

    def __init__(self):
        self.duck_img={DEFAULT_TYPE: DUCKING, SHIELD_TYPE:DUCKING_SHIELD}
        self.run_img={DEFAULT_TYPE:RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
        self.jump_img={DEFAULT_TYPE:JUMPING,SHIELD_TYPE:JUMPING_SHIELD}
       
        self.type=DEFAULT_TYPE
        self.image=self.run_img[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS
        self. step_index=0
        #operaciones
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_LEVEL
        self.setup_states_boolenas()

    def setup_states_boolenas(self):
        self.has_powerup=False
        self.shield=False
        self.show_text=False
        self.shield_time_up=0
        

    def update(self,user_input):
        if self.dino_run:
            self.run()
        if self.dino_duck:
            self.duck()
        if self.dino_jump:
            self.jump()

        if user_input[pygame.K_DOWN] and not self.dino_jump: #2do es falso y entra
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        if not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index>=10:
            self.step_index =0

    def run(self):
        #self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.image= self.run_img[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index +=1
        
    def duck(self):
        #self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.image=self.duck_img[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X.POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index+=1

    def jump(self):
        #self.image = JUMPING
        self.image=self.jump_img[self.type]
        if self.dino_jump:
            self.dino_rect.y -= (self.jump_vel*4)
            self.jump_vel-=1

        if self.jump_vel<- self.JUMP_LEVEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump =False
            self.jump_vel = self.JUMP_LEVEL



    def draw(self,screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def check_invincibility(self,screen):
        if self.shield:
            time_to_show = round((self.shield_time_up- pygame.time.get_ticks())/1000,2)
            print()
            if time_to_show>=0:
                if self.show_text:
                    fond=pygame.font.Font("freesansbold.ttf",18)
                    text=fond.render(f"Shield enable for {time_to_show}",True,(Black))
                    text_rect=text.get_rect()
                    text_rect.center=(500,40)
                    screen.blit(text,text_rect)
            

            else:
                self.shield=False
                self.update_to_default(SHIELD_TYPE)

            print()
    def update_to_default(self, current_type):
        print()
        if self.type==current_type:
            self.type=DEFAULT_TYPE