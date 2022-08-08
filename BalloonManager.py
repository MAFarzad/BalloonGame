import pygame
# import random
# from pygame.locals import *
# import pygwidgets
# from BalloonConstants import *
from Balloon import *

class BalloonManager():
    def __init__(self, window, rect, max_balloon_number=10):
        self.window = window
        self.rect = rect
        self.max_balloon_number = max_balloon_number

        self.balloon_list = []
        self.score = 0

    def add(self):
        if len(self.balloon_list) < self.max_balloon_number:
            color = pygame.Color(random.randint(0, 256), random.randint(0, 256),random.randint(0, 256))
            balloon = Balloon(self.window, self.rect, color)
            self.balloon_list.append(balloon)
      
#         self.nPopped = 0
#         self.nMissed = 0
#         self.score = 0
        

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for balloon_item in reversed(self.balloon_list):
                if balloon_item.check_click(event.pos):
                    self.balloon_list.remove(balloon_item)
                    self.score = self.score + balloon_item.score
                    print (self.score)
                    break
#                 wasHit, nPoints = oBalloon.clickedInside(event.pos)
#                 if wasHit:
#                     if nPoints > 0: # remove this balloon
#                         self.balloonList.remove(oBalloon)
#                         self.nPopped = self.nPopped + 1
#                         self.score = self.score + nPoints
#                     return # no need to check others

    def update(self):
        for balloon_item in reversed(self.balloon_list):
            balloon_item.update()
            if balloon_item.state != State.INSIDE:
                self.balloon_list.remove(balloon_item)
                self.score = self.score - balloon_item.score
                print (self.score)

            # status = oBalloon.update()
            # if status == BALLOON_MISSED:
            #     # Balloon went off the top, remove it
            #     self.balloonList.remove(oBalloon)
            #     self.nMissed = self.nMissed + 1

#     def getScore(self):
#         return self.score

#     def getCountPopped(self):
#         return self.nPopped

#     def getCountMissed(self):
#         return self.nMissed

    def draw(self):
        for balloon_item in reversed(self.balloon_list):
            balloon_item.draw()