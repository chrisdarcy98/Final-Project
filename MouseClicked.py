#MouseClicked Event

from pygame import *

pygame.init()
screen = display.set_mode((640, 480))

display.set_caption("Location: "+pygame.mouse.get_pos())
