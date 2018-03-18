#!/usr/bin/env python

import sys

from voice import *
from graphics import *


def main():
     display = init_display()

     while True:
          for event in pygame.event.get():
               if event.type == KEYDOWN:
                    is_pressed = pygame.key.get_pressed()
                    if is_pressed[K_SPACE]:
                         draw(display, 'rec')
                         rec()
                         draw(display, 'wait')
                         play()
               elif event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit()


if __name__ == '__main__':
     main()

