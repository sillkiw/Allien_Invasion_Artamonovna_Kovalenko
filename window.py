import pygame



def run_game():
    pygame.init()
    pygame.display.set_mode((600,400))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.flip()

run_game()