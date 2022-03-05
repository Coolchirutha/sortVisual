# Import and initialize pygame library
import pygame

pygame.init()

# Define the drawing window
screen = pygame.display.set_mode((500,500))

# Running till user quits
running = True
while running:

  # If user clicks close then stop running
  for event in pygame.event.get():
    if(event.type == pygame.QUIT):
      running = False

  # While running

  # Add a white background
  screen.fill((255,255,255))

  # Draw a circle for fun
  pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

  # Make stuff disappear
  pygame.display.flip()

# When user quits
pygame.quit()


