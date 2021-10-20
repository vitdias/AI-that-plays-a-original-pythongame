import pygame, random, time

pygame.init()
print('[!] Game started Successfully!')

class VIT_GameAI:
    def __init__(self, win_w=750, win_h=500):
        self.win_w=win_w
        self.win_h=win_h
        self.reset()
        paddle_size = 75

        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        green = (0, 255, 0)

        win = pygame.display.set_mode((win_w, win_h))
        pygame.display.set_caption("Paddle_ball by VIT")

        # reset function
        def reset(self):
            lifes = 3
            paddle = Paddle()
            paddle.rect.x = win_w / 2
            paddle.rect.y = win_h - 25
            paddle_speed = 10

            fruit = Fruit()
            fruit_speed = 10
            enemy = Enemy()
            enemy_speed = 10

            summon_object()
            self.frame_iteartion = 0


        # reward
        # play(action -> direction
        # game_iteration
        # is_collision)

        # Create Classes
        class Paddle(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.Surface([paddle_size, 10])
                self.image.fill(white)
                self.rect = self.image.get_rect()
                self.score = 0

        class Fruit(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.Surface([10, 10])
                self.image.fill(red)
                self.rect = self.image.get_rect()

        class Enemy(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.Surface([10, 10])
                self.image.fill(green)
                self.rect = self.image.get_rect()


        class Direction:
            pass

        class Point:
            pass

        def play_step(self, action):
            pass

        def rest(self):
            pass

        lifes = 3
        paddle = Paddle()
        paddle.rect.x = win_w / 2
        paddle.rect.y = win_h - 25
        paddle_speed = 10

        fruit = Fruit()
        fruit_speed = 10
        enemy = Enemy()
        enemy_speed = 10


        def summon_object():
            fruit.rect.x = random.randint(0, win_w)
            fruit.rect.y = 0

            enemy.rect.x = random.randint(0, win_w)
            enemy.rect.y = 0
            while fruit.rect.x == enemy.rect.x:
                fruit.rect.x = random.randint(0, win_w)
                fruit.rect.y = 0

                enemy.rect.x = random.randint(0, win_w)
                enemy.rect.y = 0

        summon_object()

        all_sprites = pygame.sprite.Group()
        all_sprites.add(paddle, fruit, enemy)


        # Redraw
        def redraw():
            win.fill(black)

            # Title Font
            font = pygame.font.SysFont('Segoe UI', 30)
            text = font.render('PADDLE_VIT', False, white)
            textRect = text.get_rect()
            textRect.center = (win_w / 2, 25)
            win.blit(text, textRect)

            # Paddle Score
            text_score = font.render('Score: ' + str(paddle.score), False, white)
            scoreRect = text_score.get_rect()
            scoreRect.center = (win_w - 75, 25)
            win.blit(text_score, scoreRect)

            # Lifes text
            text_lifes = font.render('Lifes: ' + str(lifes), False, white)
            lifesRect = text_lifes.get_rect()
            lifesRect.x = 25
            win.blit(text_lifes, lifesRect)

            all_sprites.draw(win)
            pygame.display.update()

        running = True

        # Main Loop
        while running:
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("[X] Game closed")
                    print("[" + str(paddle.score) + "] Max Score !")

            # Objects Mechanics
            fruit.rect.y += fruit_speed
            enemy.rect.y += enemy_speed

            if paddle.rect.colliderect(fruit.rect):
                paddle.score += 1
                summon_object()

            if paddle.rect.colliderect(enemy.rect):
                lifes -= 1
                summon_object()


            if fruit.rect.y > 750:
                lifes -= 1
                summon_object()

            if enemy.rect.y > 750:
                summon_object()


            # Controls
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                paddle.rect.x += paddle_speed
                if paddle.rect.x < 10:
                    paddle.rect.x = 10
            if key[pygame.K_a]:
                paddle.rect.x += -paddle_speed

            if paddle.rect.x < 0:
                paddle.rect.x = 0
            if paddle.rect.x > win_w - paddle_size:
                paddle.rect.x = win_w - paddle_size

            # Game Over
            if lifes < 1:
                running = False
                print("[X] Game closed")
                print("[" + str(paddle.score) + "] is your Max Score !")
                # time.sleep(5)

            redraw()

        VIT_GameAI()

        pygame.quit()