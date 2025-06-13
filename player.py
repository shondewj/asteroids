import pygame
from circleshape import *
from constants import *

# Base class for game objects
class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__(x,y,radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white",self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_w] or keys[pygame.K_UP]):
            self.move(dt)
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            self.rotate(-dt)
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            self.rotate(-dt)
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            self.rotate(dt)
