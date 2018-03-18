import pygame

WIDTH=300
HEIGHT = 400
BG_COLOR = (25, 2, 25)

IMG_POS = (15,40)
TXT_POS = (15, 350)

img = {}
txt = {}

def init_display():
     global img, txt

     display = pygame.display.set_mode((WIDTH, HEIGHT))
     pygame.display.set_caption('Record My Voice')
     pygame.font.init()
     font = pygame.font.Font('font.ttf', 25)
     txt['wait'] = font.render('Press Space to start record', True, (255, 255, 255))
     txt['rec'] = font.render('Release key to stop record', True, (255, 0, 0))
     img['wait'] = pygame.image.load('wait.png')
     img['rec'] = pygame.image.load('rec.png')

     draw(display, 'wait')
     
     return display

def draw(display, state):
     global img, txt
     display.fill(BG_COLOR)
     display.blit(img[state], IMG_POS)
     display.blit(txt[state], TXT_POS)
     pygame.display.flip()
