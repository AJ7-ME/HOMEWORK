import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1066.666666666666, 666.666666666666
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('BG')
backround_image = pygame.transform.scale(
    pygame.image.load('../Module 6/Images for pygame/BG.png').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))
penguin_image = pygame.transform.scale(
    pygame.image.load('../Module 6/Images for pygame/Sprite.png').convert_alpha(), (600, 650))
penguin_rect = penguin_image.get_rect(center=(300, SCREEN_HEIGHT // 2))
text = pygame.font.Font(None, 36).render('', True,
                                         pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(backround_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    game_loop()