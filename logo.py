# ICS3U
# Assignment 2: Logo
# Faraz

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (48, 155, 221)
# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here
    

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue different shapes and lines to be drawn
    # Draw the circle around the logo
    pygame.draw.ellipse(screen, BLACK, [10, 10, 375, 375], 0)
    pygame.draw.ellipse(screen, WHITE, [25, 25, 345, 345], 0)
    
    #Draw the polygon that will go inside the circle
    pygame.draw.polygon(screen, BLACK, [(50, 315), (200, 220), (350, 310), (220, 185), (200, 15), (180, 185), (50, 310)], 0)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
