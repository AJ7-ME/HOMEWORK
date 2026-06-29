import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
BLUE = pygame.Color ('blue')
LIGHTBLUE = pygame.Color ('lightblue')
DARKBLUE = pygame.Color ('darkblue')
YELLOW = pygame.Color ('yellow')
MAGENTA = pygame.Color ('magenta')
ORANGE = pygame.Color ('orange')
WHITE = pygame.Color ('white')
BLACK = pygame.Color ('black')
RED = pygame.Color ('red')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.randint(-1, 1), random.randint(-1, 1)]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    def color_change(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
def change_background_color(self):
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])

    #Sprite 1
all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 380)
all_sprites_list.add(sp1)

#sprite 2
sp2 = Sprite(RED, 20, 30)
sp2.rect.x = random.randint(0, 480)
sp2.rect.y = random.randint(0, 380)
all_sprites_list.add(sp2)

screen = pygame.display.set_mode([500, 400])
pygame.display.set_caption('Colorful Bounce')
bg_color = BLUE
screen.fill(bg_color)
exit = False
clock = pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.color_change()
            sp2.color_change()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color(screen)
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()