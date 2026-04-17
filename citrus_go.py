import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("Citrus Go")
#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Character setup
character = pygame.image.load("assets/character.png") # Load a character image representing the player
character = pygame.transform.scale(character, (80, 80)) # Scale the character image to a smaller size
character = pygame.transform.flip(character, True, False) # Create a flipped version of the character for left movement

player_x = 100
player_y = 350
player_rect = pygame.Rect(player_x, player_y, 80, 80) # Create a rectangle for the character's position and size

ground_y = 430
ground_rects = [
    pygame.Rect(0, ground_y, 1200, 70), # Ground platform
    pygame.Rect(300, 350, 200, 20), # First platform
    pygame.Rect(600, 300, 200, 20), # Second platform
    pygame.Rect(900, 250, 200, 20) # Third platform
]

velocity_y = 0
gravity = 0.8

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    screen.fill(WHITE) # Fill the screen with white background

    for ground in ground_rects:
        pygame.draw.rect(screen, BLACK, ground)

    velocity_y += gravity
    player_y += velocity_y
    player_rect = pygame.Rect(player_x, player_y, 80, 80)

    for ground in ground_rects:
        if player_rect.colliderect(ground):
            player_y = ground.top - 80
            velocity_y = 0
    
    screen.blit(character, (player_x, player_y)) # Draw the character at a specific position
    pygame.display.update()


pygame.quit()

