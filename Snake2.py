import Score
import pygame
import time
import random

score = 0

# Define the color palette
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Set the display dimensions
DISP_WIDTH = 600
DISP_HEIGHT = 400

# Set the size and speed of the snake
SNAKE_SIZE = 16
SNAKE_SPEED = 15

class Snake:
    def __init__(self):
        self.size = SNAKE_SIZE
        self.direction = 'RIGHT'
        self.body = [(100, 50), (90, 50), (80, 50)]

    def update_direction(self, direction):
        """Update snake direction"""
        if direction == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        if direction == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        if direction == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        if direction == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'

    def update_position(self, apple_rect):
        """Update snake position"""
        if self.direction == 'RIGHT':
            new_head = (self.body[0][0] + self.size, self.body[0][1])
        if self.direction == 'LEFT':
            new_head = (self.body[0][0] - self.size, self.body[0][1])
        if self.direction == 'UP':
            new_head = (self.body[0][0], self.body[0][1] - self.size)
        if self.direction == 'DOWN':
            new_head = (self.body[0][0], self.body[0][1] + self.size)

        self.body.insert(0, new_head)
        head_rect = pygame.Rect(new_head[0], new_head[1], self.size, self.size)

        if head_rect.colliderect(apple_rect):
            return True
        else:
            self.body.pop()
            return False

    def draw(self, surface):
        for part in self.body:
            pygame.draw.rect(surface, GREEN, pygame.Rect(part[0], part[1], self.size, self.size))

    def check_collision(self):
        if self.body[0] in self.body[1:]:
            return True
        return False


class Apple:
    def __init__(self):
        self.position = (0, 0)
        self.color = WHITE
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (DISP_WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                         random.randint(0, (DISP_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE))

    def get_rect(self):
        return pygame.Rect(self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE)


def game_loop():
    global Score
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((DISP_WIDTH, DISP_HEIGHT))
    pygame.display.set_caption('Pygame Snake')

    snake = Snake()
    apple = Apple()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.update_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.update_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    snake.update_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.update_direction('RIGHT')

        apple_eaten = snake.update_position(apple.get_rect())
        if apple_eaten:
            apple.randomize_position()
            Score.increase_score(score)

        screen.fill(BLACK)
        snake.draw(screen)
        apple.draw(screen)
        pygame.display.update()

        if snake.check_collision() or \
                snake.body[0][0] < 0 or snake.body[0][1] < 0 or \
                snake.body[0][0] >= DISP_WIDTH or snake.body[0][1] >= DISP_HEIGHT:
            pygame.quit()
            quit()

        clock.tick(SNAKE_SPEED)


if __name__ == "__main__":
    game_loop()
