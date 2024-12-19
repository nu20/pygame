import pygame

# Initialize Pygame and screen dimensions
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

# Load and scale images directly
background_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image = pygame.transform.scale(pygame.image.load('hello penguin.png').convert_alpha(), (200, 200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2,SCREEN_HEIGHT // 2 - 30))


def game_loop():
  clock = pygame.time.Clock()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    display_surface.blit(background_image, (0, 0))
    display_surface.blit(penguin_image, penguin_rect)


    pygame.display.flip()
    clock.tick(30)

  pygame.quit()


if __name__ == '__main__':
  game_loop()
