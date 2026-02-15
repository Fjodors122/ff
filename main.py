import pygame
import asyncio


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mein Web Game")

clock = pygame.time.Clock()

x = 100
y = 100

async def main():
    global x, y
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= 5
        if keys[pygame.K_RIGHT]:
            x += 5
        if keys[pygame.K_UP]:
            y -= 5
        if keys[pygame.K_DOWN]:
            y += 5

        screen.fill((20, 20, 40))
        pygame.draw.rect(screen, (0, 200, 100), (x, y, 50, 50))

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

    pygame.quit()
    pygame.exit()

asyncio.run(main())
