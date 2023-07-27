import Score
import pygame
import time
import random

score = 0


# Define the color palette
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Set the display dimensions
DISP_WIDTH = 600
DISP_HEIGHT = 400

# Set the size and speed of the snake
SNAKE_SIZE = 10
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

    def update_position(self, apple_pos):
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

        # Check if the new head of the snake collides with the apple
        if new_head[0] == apple_pos[0] and new_head[1] == apple_pos[1]:
            return True
        else:
            self.body.pop()
            return False

    def draw(self, surface):
        """Draw the snake"""
        for part in self.body:
            pygame.draw.rect(surface, GREEN, pygame.Rect(part[0], part[1], self.size, self.size))

    def check_collision(self):
        """Check for collision with itself"""
        if self.body[0] in self.body[11:]:
            return True
        return False


class Apple:
    def __init__(self):
        self.position = (0, 0)
        self.color = WHITE
        self.randomize_position()

    def randomize_position(self):
        """Position the apple in a random location within the boundaries of the display"""
        self.position = (random.randint(0, (DISP_WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                         random.randint(0, (DISP_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)

    def draw(self, surface):
        """Draw the apple"""
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE))


def check_collision(apple_pos, snake_body):
    """Check for collision with the apple"""
    head_rect = pygame.Rect(snake_body[0][0], snake_body[0][1], SNAKE_SIZE, SNAKE_SIZE)
    apple_rect = pygame.Rect(apple_pos[0], apple_pos[1], SNAKE_SIZE, SNAKE_SIZE)
    return head_rect.colliderect(apple_rect)


def game_loop():
    global score
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

        apple_eaten = snake.update_position(apple.position)
        if apple_eaten:
            apple.randomize_position()
            Score.increase_score(score)

        screen.fill(BLACK)
        snake.draw(screen)
        apple.draw(screen)
        pygame.display.update()

        # Check for collision with itself or the wall
        if snake.check_collision() or \
                snake.body[0][0] < 0 or snake.body[0][1] < 0 or \
                snake.body[0][0] >= DISP_WIDTH or snake.body[0][1] >= DISP_HEIGHT:
            pygame.quit()
            quit()

        clock.tick(SNAKE_SPEED)


if __name__ == "__main__":
    game_loop()
