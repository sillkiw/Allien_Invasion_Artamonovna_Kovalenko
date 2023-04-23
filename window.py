import pygame



def run_game():
    pygame.init()
    window =pygame.display.set_mode((600,400))
    background = pygame.image.load("background.jpg")
    background = pygame.transform.scale(background,(600,400))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        window.blit(background,(0,0))
        pygame.display.flip()

run_game()