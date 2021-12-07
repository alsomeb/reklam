import pygame     #import the module
from led import mlcdinit,mlcddraw

mlcdinit(16,3,3) # initialize a 16x3 display scaled 3x  

#draw the three lines passed as a list
mlcddraw(["Hello","Python", "What"])
antalSeks = 0
pygame.time.set_timer(pygame.USEREVENT, 1000)
while True:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            antalSeks = antalSeks +1
            mlcddraw(["Räknare","", str(antalSeks)])
       #test