# ICS3U
# Assignment 2: Action
# Faraz

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
pygame.init()

from snow import Snow

#Play background music
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load("bg.mp3")
pygame.mixer.music.play(-1)

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the screen size
SCREENWIDTH = 900
SCREENHEIGHT = 600

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Faraz Animation")

#Create sprite list
all_sprites_list = pygame.sprite.Group()


for i in range(5):
    tempFish = Fish([random.randint(20,255),random.randint(20,255),random.randint(20,255),], random.randint(10,100), random.randint(10,100))
    tempFish.rect.x = random.randint(40,300)
    tempFish.rect.y = random.randint(40,300)
    all_sprites_list.add(tempFish)


#Add the fish


# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
#Adding a background picture to the animation
background = pygame.image.load("bg.png")
#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE): # Player clicked close button
            carryOn = False
    #Adding a background picture to the animation
    screen.blit(background, (0, 0))
    # --- Game logic goes here
    
    # --- Draw code goes here

    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    #Draw all the sprites
    all_sprites_list.draw(screen)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
