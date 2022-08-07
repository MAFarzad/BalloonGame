from tkinter import INSIDE
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
    sound_file = 'sounds/balloonPop.wav'
    image_file = 'images/Balloon.png'
    initiated = False
    max_speed = 1
    score = 10

    

    def __init__(self, window, rect, size_factor=1, speed_factor=1, score_factor=1, id=0):
        self.window = window
        self.rect = rect
        self.speed_x = Balloon.max_speed * speed_factor * random.uniform(-1, 1)
        self.speed_y = self.speed_x * random.uniform(-1, 1)
        self.score = Balloon.score * score_factor
        self.id = id
        
        if not Balloon.initiated:
            Balloon.initiated = True
            Balloon.sound = pygame.mixer.Sound(Balloon.sound_file)
            Balloon.image = pygame.image.load(Balloon.image_file)

        self.image_rect = pygame.Rect(0, 0, Balloon.image.get_width() * size_factor, Balloon.image.get_height() * size_factor )
        self.image = pygame.transform.scale(Balloon.image, (self.image_rect.width, self.image_rect.height))
        self.image_rect.center = (self.rect.centerx, self.rect.centery)
        self.state = State.INSIDE
        
        
    def check_click(self, mouse_location):
        if self.image_rect.collidepoint(mouse_location):
            Balloon.sound.play()
            return True
        return False
            
    def update(self):
        if self.state == State.INSIDE:
            self.image_rect.center = (self.image_rect.centerx + self.speed_x, self.image_rect.centery + self.speed_y)

        if self.image_rect.left < self.rect.left:
            self.state = State.HIT_LEFT
        elif self.image_rect.right > self.rect.right:
            self.state = State.HIT_RIGHT
        elif self.image_rect.top < self.rect.top:
            self.state = State.HIT_TOP
        elif self.image_rect.bottom > self.rect.bottom:
            self.state = State.HIT_BOTTOM
        

    def draw(self):
        self.window.blit(self.image, self.image_rect)

    def __del__(self):
        print(self.size, 'Balloon', self.id, 'is going away')
