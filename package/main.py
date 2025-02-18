import pygame
from player import Player

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() /2)

new_player = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        new_player.walk()
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        new_player.walk()
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        new_player.walk()
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        new_player.walk()


    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
