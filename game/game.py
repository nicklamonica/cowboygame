import pygame

class Game:
    def __init__(self):
        return
    
    def startGame(self):
        pygame.init()

        win = pygame.display.set_mode((500, 500))

        pygame.display.set_caption("Rootin Tootin Yeehaw Simulator")

        run = True

        vel = 10
        x = 250
        y = 250

        while run:

            pygame.time.delay(50)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                x -= vel
            if keys[pygame.K_RIGHT]:
                x += vel
            if keys[pygame.K_UP]:
                y -= vel
            if keys[pygame.K_DOWN]:
                y += vel
            
            win.fill((0, 0, 0))
            pygame.draw.rect(win, (255, 0, 0), (x, y, 20, 20) )
            pygame.display.update()

        pygame.quit()
