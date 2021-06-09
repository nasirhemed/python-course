import pygame
import random
import time

WIDTH = 288
HEIGHT = 512

FPS = 30

class Pipe:
    def __init__(self, images):
        pipe_gap = 100
        BASE = 414
        x = WIDTH + 10

        gap_position = random.randrange(int(BASE * 0.2), int(BASE * 0.6 - pipe_gap))

        pipeHeight = images[0].get_height()

        self.top_posn = (x, gap_position - pipeHeight)
        self.bottom_posn = (x, gap_position + pipe_gap)
        self.images = images

        self.velocity_x = 4


    def get_x_position(self):
        return self.top_posn[0]

    def get_width(self):
        return self.images[0].get_width()

    def update(self):
        x, top_y = self.top_posn
        x, bottom_y = self.bottom_posn

        new_x = x- self.velocity_x
        self.top_posn = (new_x, top_y)
        self.bottom_posn = (new_x, bottom_y)


    def draw(self, screen):
        screen.blit(self.images[1], self.top_posn)
        screen.blit(self.images[0], self.bottom_posn)

class FlappyBird:
    def __init__(self, posn, images, score_images):
        self.posn = posn # (x, y)
        self.images = images
        self.alive = True
        self.score = 0

        self.start = False

        self.velocity_y = 0
        self.max_velocity_y = 10
        self.min_velocity_y = -8
        self.gravity_y = 1
        self.floor_y = 490

        self.flap_sound = pygame.mixer.Sound('assets/audio/wing.wav')
        self.hit_sound = pygame.mixer.Sound('assets/audio/hit.wav')
        self.score_sound = pygame.mixer.Sound('assets/audio/point.wav')
        self.death_sound = pygame.mixer.Sound('assets/audio/die.wav')

        self.score_images = score_images
        self.score_y = HEIGHT * 0.1 

    def update(self):

        if self.alive and self.start:
            x, y = self.posn
            new_y = y + self.velocity_y

            if new_y > self.floor_y:
                self.velocity_y = 0
                self.alive = False
                self.posn = (x, y)
            else:
                self.posn = (x, new_y)
                self.velocity_y = min(self.velocity_y + self.gravity_y, self.max_velocity_y)


    def draw(self, screen):
        if self.velocity_y > 0:
            screen.blit(self.images[2], self.posn)
        elif self.velocity_y < 0:
            screen.blit(self.images[0], self.posn)
        else:
            screen.blit(self.images[1], self.posn)

    
    def display_score(self, screen):
        score_str = str(self.score)
        digit_width = self.score_images[0].get_width()

        score_width = len(score_str) * digit_width
        offset = (WIDTH - score_width) / 2

        for number in score_str:
            screen.blit(self.score_images[int(number)], (offset, self.score_y))
            offset += digit_width


    def pipe_check(self, pipe):

        flappy_x, flappy_y = self.posn
        flappy_height = self.images[0].get_height()
        flappy_x += self.images[0].get_width()
        tp_x, tp_y = pipe.top_posn
        bp_x, bp_y = pipe.bottom_posn

        pipe_width = pipe.get_width()

        if tp_x <= flappy_x <= tp_x + pipe_width:  
            if 0 <= flappy_y <= bp_y - 100:
                self.alive = False
            elif bp_y <= flappy_y + flappy_height <= self.floor_y:
                self.alive = False
            elif flappy_x - 2 <= bp_x <= flappy_x + 2:
                self.score += 1
                self.score_sound.play()
                

    def bounce(self):
        self.start = True
        self.flap_sound.play()
        self.velocity_y = max(self.velocity_y - 12, self.min_velocity_y)

    def play_hit_sound(self):
        self.hit_sound.play()
        self.death_sound.play()
        time.sleep(2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pipes = []

    start_game = False

    FPS_CLOCK = pygame.time.Clock()

    background = pygame.image.load("assets/sprites/background-day.png")

    numbers = (
        pygame.image.load('assets/sprites/0.png').convert_alpha(),
        pygame.image.load('assets/sprites/1.png').convert_alpha(),
        pygame.image.load('assets/sprites/2.png').convert_alpha(),
        pygame.image.load('assets/sprites/3.png').convert_alpha(),
        pygame.image.load('assets/sprites/4.png').convert_alpha(),
        pygame.image.load('assets/sprites/5.png').convert_alpha(),
        pygame.image.load('assets/sprites/6.png').convert_alpha(),
        pygame.image.load('assets/sprites/7.png').convert_alpha(),
        pygame.image.load('assets/sprites/8.png').convert_alpha(),
        pygame.image.load('assets/sprites/9.png').convert_alpha()
    )

    bird_images = (
        pygame.image.load("assets/sprites/yellowbird-upflap.png"),
        pygame.image.load("assets/sprites/yellowbird-midflap.png"),
        pygame.image.load("assets/sprites/yellowbird-downflap.png")
    )
    pipe_images = (
        pygame.image.load("assets/sprites/pipe-green.png"),
        pygame.transform.flip(pygame.image.load("assets/sprites/pipe-green.png"), False, True)
    )


    flappy_position = (
        WIDTH / 2 - bird_images[0].get_width(),
        HEIGHT / 2 - bird_images[0].get_height()
    )

    flappy = FlappyBird(flappy_position, bird_images, numbers)
    pipe = Pipe(pipe_images)
    pipes.append(pipe)

    while True:

        # Step for handling events
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_game = True
                flappy.bounce()

        if start_game:
            # We need to update the state of the game
            if len(pipes) > 0:
                pipe = pipes[0]
                if pipe.get_x_position() < -pipe.get_width():
                    pipes.remove(pipe)
                    newPipe = Pipe(pipe_images)
                    pipes.append(newPipe)

            # Need to check if bird has crashed
            if not flappy.alive:
                flappy.play_hit_sound()
                return

            flappy.update() 
            flappy.pipe_check(pipes[0])
            for pipe in pipes:
                pipe.update()

        # Draw the game
        screen.blit(background, (0, 0))
        for pipe in pipes:
            pipe.draw(screen)
        flappy.draw(screen)
        flappy.display_score(screen)





        pygame.display.flip()
        FPS_CLOCK.tick(30)


if __name__ == '__main__':
    main()