import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            ran_angle = random.uniform(20, 50)
            velocity_split1 = self.velocity.rotate(ran_angle)
            velocity_split2 = self.velocity.rotate(-ran_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split1 = Asteroid(self.position.x, self.position.y, new_radius)
            split1.velocity = velocity_split1 * 1.2
            split2 = Asteroid(self.position.x, self.position.y, new_radius)
            split2.velocity = velocity_split2 * 1.2
