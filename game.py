import pygame
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen

        # Charger l'image d'arrière-plan au format JPG
        self.background = pygame.Surface((1280,720))
        self.background.fill((0, 50, 70))  # Couleur par défaut pour visualiser l'objet


        # Initialisation du joystick
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print(self.joystick.get_name(), " connected.")
        else:
            print("Aucun joystick détecté.")

        # Création du joueur
        self.player = Player(500, 300, self.screen, self.joystick)
        print(" ")

    def update(self, delta_time):
        

        # Efface l'écran
        self.screen.blit(self.background, (0, 0))  # Afficher l'arrière-plan

        # Met à jour le joueur
        self.player.update(delta_time)

        # Affiche l'entité du joueur
        self.screen.blit(self.player.image, self.player.rect)



    def get_screen(self):
        return self.screen
