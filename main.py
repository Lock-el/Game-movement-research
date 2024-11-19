import pygame
import sys
from game import Game

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre en 720p
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mon Jeu")

# Définir le nombre de FPS
FPS = 60
clock = pygame.time.Clock()

# Création de l'instance de Game
game = Game(screen)


running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.player.jump()  # Appelle la fonction de saut
            if game.joystick and event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                     game.player.jump()
                
                    

    # Obtenir le temps écoulé depuis la dernière itération
    delta_time = clock.tick(FPS) / 1000.0  # En secondes

    # Appel de la fonction update de Game avec delta_time
    game.update(delta_time)

    pygame.display.flip()

pygame.quit()
sys.exit()
