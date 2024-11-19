import pygame
from entity import Entity

class Player(Entity):
    def __init__(self, x, y, screen, joystick=None):
        super().__init__(x, y, 50, 50, screen)  # Exemple de taille de 50x50
        self.joystick = joystick

        self.SPEED = (0.7, 0.2)
        self.JUMP_FORCE = 25  # Force du saut vers le haut
        self.MAX_BOOST_AMOUNT = 100
        self.BOOST_POWER = 1.5

        self.boost_amount = self.MAX_BOOST_AMOUNT
        self.is_planing = False
        self.force_x = 0
        self.force_y = 0

    def update(self, delta_time):
        # Gestion des inputs :
        if self.joystick:
            self.controller_control()
        else:
            self.keyboard_control()

        if self.on_ground and self.boost_amount < self.MAX_BOOST_AMOUNT:
            self.boost_amount += 10*delta_time
        if self.is_planing: self.plane(delta_time)
            

        # Appelle la méthode de mise à jour de la classe parent avec delta_time
        super().update(delta_time)

    def jump(self):
        if self.on_ground:
            self.apply_force(pygame.math.Vector2(0, -self.JUMP_FORCE))
            self.on_ground = False
    
    def boost(self):
        if self.boost_amount > 0:
            self.apply_force(pygame.math.Vector2(0, -self.BOOST_POWER))
            self.boost_amount -= 0.5

    def plane(self, delta_time):    #fonction non aboutie, le but est d'imiter le comportement d'un planneur
        coef = 2
        #self.rect.topleft += self.velocity * delta_time * 60
        if self.direction[1] > 0 :
            self.force_x = self.direction[1] / coef
        print(self.force_x)
          # * self.velocity[0]
        self.force_y = self.direction[1] / coef - self.GRAVITY
        self.apply_force(pygame.math.Vector2(self.force_x,self.force_y)) #mieux comme ça
        



    def keyboard_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            self.is_planing = True
        else: self.is_planing = False

        if not self.is_planing:
            if keys[pygame.K_q]: self.apply_force(pygame.math.Vector2(-self.SPEED[0], 0))
            if keys[pygame.K_d]: self.apply_force(pygame.math.Vector2(self.SPEED[0], 0))
            if keys[pygame.K_z]: self.apply_force(pygame.math.Vector2(0, -self.SPEED[1]))
            if keys[pygame.K_s]: self.apply_force(pygame.math.Vector2(0, self.SPEED[1]))

            if keys[pygame.K_LSHIFT]: self.boost()
        else :
            if keys[pygame.K_q]: self.direction[0] = -1
            if keys[pygame.K_d]: self.direction[0] = 1
            if keys[pygame.K_z]: self.direction[1] = -1
            if keys[pygame.K_s]: self.direction[1] = 1

        

    def controller_control(self):
        joystick_input = self.joystick
        joystick_x = joystick_input.get_axis(0)  # Axe horizontal
        joystick_y = joystick_input.get_axis(1)  # Axe vertical

        if self.joystick.get_button(1):
            self.is_planing = True
        else: self.is_planing = False
        if self.joystick.get_button(2):
            self.boost()
        if abs(joystick_x) > 0.1 or abs(joystick_y) > 0.1:  # Seulement si le joystick est en mouvement
            # Applique le mouvement du joystick
            if not self.is_planing: self.apply_force(pygame.math.Vector2(joystick_x * self.SPEED[0], joystick_y * self.SPEED[1]))
            else : self.direction = [joystick_x, joystick_y]
        elif self.is_planing: self.direction = [0,0]
        
