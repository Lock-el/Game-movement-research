import pygame
class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, screen):
        super().__init__()

        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # Configuration de la hitbox
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))  # Couleur par défaut pour visualiser l'objet
        self.rect = self.image.get_rect(topleft=(x, y))

        # Physique
        self.GRAVITY = 1  # Force de gravité
        self.AIR_RESISTANCE = 0.07  # Coefficient de résistance de l'air
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)

        self.direction = [0,0]
        self.on_ground = False  # État pour savoir si l'entité est au sol
        

    def apply_force(self, force):
        # Applique une force à l'entité (force est un Vector2)
        self.acceleration += force


    


    def update(self, delta_time):
        # Applique la gravité
        self.acceleration.y += self.GRAVITY # Applique la gravité sur delta_time

        # Applique la résistance de l'air
        air_resistance_force = -self.velocity * self.AIR_RESISTANCE
        self.acceleration += air_resistance_force

        # Mise à jour de la vitesse et de la position
        self.velocity += self.acceleration * delta_time * 60
        self.rect.topleft += self.velocity * delta_time * 60

        # Gestion des collisions avec les bords de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity.x = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
            self.velocity.x = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity.y = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
            self.velocity.y = 0
        if self.rect.bottom >= self.screen_height:
            self.on_ground = True
        else : self.on_ground = False

        # Réinitialise l'accélération
        self.acceleration = pygame.math.Vector2(0, 0)
