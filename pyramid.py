import pygame, sys
from pygame.locals import *


pygame.init()
# sets width and height to the dimensions of any screen
size = (width, height) = (700, 500)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
bg_color = (0, 102, 0)

def main():
  global screen
  while True:
    clock.tick(60)
    for event in pygame.index.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == KEYDOWN:
        #screen controls here!
        if event.key == K_f:
          screen = pregame.display.set_mode(size,FULLSCREEN)
        elif event.key == K_ESCAPE:
          screen = pygame.display.set_mode(size)
    screen.fill(bg_color)
    pygame.display.flip()


if __name__ == "__main__":
  main()
