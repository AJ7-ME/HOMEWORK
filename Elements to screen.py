import sys
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Squares")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
clock = pygame.time.Clock()
done = False
font = pygame.font.SysFont(None, 35)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(30, 30, 100, 100)) #Red square
    ts = font.render("Red", True, BLUE)
    screen.blit(ts, (40, 50)) # Position the text
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(240, 30, 100, 100)) #Blue square
    ts = font.render("Green", True, RED)
    screen.blit(ts, (250, 50)) # Position the text
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(480, 30, 100, 100)) #Green square
    ts = font.render("Blue", True, GREEN)
    screen.blit(ts, (490, 50)) # Position the text
    pygame.display.flip()
    clock.tick(60)






    