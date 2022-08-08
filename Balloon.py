from tkinter import INSIDE, N
from tkinter.messagebox import NO
import pygame
import random
from enum import Enum

class State(Enum):
    INSIDE = 0
    HIT_TOP = 1
    HIT_BOTTOM = 2
    HIT_LEFT = 3
    HIT_RIGHT = 4

class Balloon():
    POP_SOUND_FILE = 'sounds/balloonPop.wav'
    HIT_SOUND_FILE = 'sounds/boing.wav'
    IMAGE_FILE = 'images/Balloon.png'
    MAX_SPEED = 1
    SCORE = 10
    SPEED_MULTIPLIER_LIST = [i/10 for i in range (-10, 11) if i != 0]
    
    initiated = False
    pop_sound = None
    hit_sound = None
    image = None

    def __init__(self, window, rect, color, size_factor=1, speed_factor=1, score_factor=1, id=0):
        self.window = window
        self.rect = rect       
        self.speed_x = Balloon.MAX_SPEED * speed_factor * random.choice(Balloon.SPEED_MULTIPLIER_LIST)
        self.speed_y = Balloon.MAX_SPEED * speed_factor * random.choice(Balloon.SPEED_MULTIPLIER_LIST)
        self.score = Balloon.SCORE * score_factor
        self.id = id
        
        if not Balloon.initiated:
            Balloon.initiated = True
            Balloon.pop_sound = pygame.mixer.Sound(Balloon.POP_SOUND_FILE)
            Balloon.hit_sound = pygame.mixer.Sound(Balloon.HIT_SOUND_FILE)
            Balloon.image = pygame.image.load(Balloon.IMAGE_FILE)

        self.image_rect = pygame.Rect(0, 0, Balloon.image.get_width() * size_factor, Balloon.image.get_height() * size_factor )
        self.image = pygame.transform.scale(Balloon.image, (self.image_rect.width, self.image_rect.height))
        self.image.fill(color, special_flags=pygame.BLEND_MIN)
        self.image_rect.center = (self.rect.centerx, self.rect.centery)
        self.state = State.INSIDE
        
        
    def check_click(self, mouse_location):
        if self.image_rect.collidepoint(mouse_location):
            Balloon.pop_sound.play()
            return True
        return False
            
    def update(self):
        if self.state == State.INSIDE:
            self.image_rect.center = (self.image_rect.centerx + self.speed_x, self.image_rect.centery + self.speed_y)
        else:
            return

        if self.image_rect.left < self.rect.left:
            self.state = State.HIT_LEFT
            Balloon.hit_sound.play()
        elif self.image_rect.right > self.rect.right:
            self.state = State.HIT_RIGHT
            Balloon.hit_sound.play()
        elif self.image_rect.top < self.rect.top:
            self.state = State.HIT_TOP
            Balloon.hit_sound.play()
        elif self.image_rect.bottom > self.rect.bottom:
            self.state = State.HIT_BOTTOM
            Balloon.hit_sound.play()
        

    def draw(self):
        self.window.blit(self.image, self.image_rect)

    def __del__(self):
        pass
        # print(f'{self.speed_x},{self.speed_y}')
