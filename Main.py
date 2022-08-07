# from pygame.locals import *
# import pygwidgets
import sys
import pygame
from BalloonManager import *

# BLACK = (0, 0, 0)
# GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
# PANEL_HEIGHT = 60
# USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Balloon Game')
clock = pygame.time.Clock()

balloon_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
balloon_manager = BalloonManager(window, balloon_rect)

# oScoreDisplay = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25),'Score: 0', textColor=BLACK, backgroundColor=None, width=140, fontSize=24)
# oStatusDisplay = pygwidgets.DisplayText(window, (180, USABLE_WINDOW_HEIGHT + 25), '', textColor=BLACK, backgroundColor=None, width=300, fontSize=24)
# oStartButton = pygwidgets.TextButton(window, (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10), 'Start')

# oBalloonMgr = BalloonMgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)

# playing = False
while True:
    balloon_manager.add()
    # nPointsEarned = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        balloon_manager.handle_events(event)
        
        # if playing:
        #     oBalloonMgr.handleEvent(event)
        #     theScore = oBalloonMgr.getScore()
        #     oScoreDisplay.setValue('Score: ' + str(theScore))
        # elif oStartButton.handleEvent(event):
        #     oBalloonMgr.start()
        #     oScoreDisplay.setValue('Score: 0')
        #     playing = True
        #     oStartButton.disable()

    # if playing:
    #     oBalloonMgr.update()
    #     nPopped = oBalloonMgr.getCountPopped()
    #     nMissed = oBalloonMgr.getCountMissed()
    #     oStatusDisplay.setValue('Popped: ' + str(nPopped) + ' Missed: ' + str(nMissed) + ' Out of: ' + str(N_BALLOONS))
    #     if (nPopped + nMissed) == N_BALLOONS:
    #         playing = False
    
    #         oStartButton.enable()
 
    balloon_manager.update()

    window.fill(BACKGROUND_COLOR)

    balloon_manager.draw()

    # if playing:
    #     oBalloonMgr.draw()

    # pygame.draw.rect(window, GRAY, pygame.Rect(0, USABLE_WINDOW_HEIGHT, WINDOW_WIDTH, PANEL_HEIGHT))
    # oScoreDisplay.draw()
    # oStatusDisplay.draw()
    # oStartButton.draw()

    pygame.display.flip()

    clock.tick(FRAMES_PER_SECOND)