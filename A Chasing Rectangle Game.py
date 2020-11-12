import pygame

# Initiates All The Pygame modules
pygame.init()

# The variable for the pygame screen ratio
X = 1366
Y = 625

# Defines the pygame screen ration and gives the variable for surface for all the elements
gameDisplay= pygame.display.set_mode((X,Y))

# Initiates the image file
logo = pygame.image.load(r'C:\Users\click\Desktop\KABEER\FUN\Pictures\Kabeer Studio.png')

# Initiates the font file and defines the size of the text
#  Provides the variables for Rendering the text
Font_Type = pygame.font.Font(r'C:\Users\click\Desktop\KABEER\FUN\Python\Font_2.ttf',600)

# By rendering, you define the text and the color of the font through a variable
Font_Y = Font_Type.render("Y",True,(140,140,140))
Font_1o =Font_Type.render("o",True,(140,140,140))
Font_u = Font_Type.render("u ",True,(140,140,140))
Font_L = Font_Type.render("L",True,(140,140,140))
Font_2o = Font_Type.render("o",True,(140,140,140))
Font_s = Font_Type.render("s",True,(140,140,140))
Font_t = Font_Type.render("t",True,(140,140,140))

# Makes a rectangle in which the text will appear, a kind of box in html
textRect_Y = Font_Y.get_rect()
textRect_1o = Font_1o.get_rect()
textRect_u = Font_u.get_rect()
textRect_L = Font_L.get_rect()
textRect_2o = Font_2o.get_rect()
textRect_s = Font_s.get_rect()
textRect_t = Font_t.get_rect()

# Defines the location of the text
textRect_Y.center = (110,Y//2)
textRect_1o.center = ((110+140),Y//2)
textRect_u.center = ((110+140+140+140),Y//2)
textRect_L.center = ((110+140+140+140+140+100),Y//2)
textRect_2o.center = ((110+140+140+140+140+140+140),Y//2)
textRect_s.center = ((110+140+140+140+140+140+140+140),Y//2)
textRect_t.center = ((110+140+140+140+140+140+140+140+140),Y//2)

# The location for the first rectangle
x= 0
y= 0

# The speed of changing the location for the first reactangle
speed= 1

# The location for the second rectangle
x2= 1000
y2= 600

# The speed of changing the location for the second reactangle
speed2= 0.8

# The variable to break and run the whille loop when needed
run = True

# Initiates the music file
pygame.mixer.music.load(r'C:\Users\click\Desktop\KABEER\FUN\Python\Music.wav')

# Plays the music indefinately, though we pause/stop it later
pygame.mixer.music.play(-1)

# The infinite loop
while run:

    # Holds the pygame window until we close it   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    # A variable to make it easy to get the input if a key is pressed
    keys= pygame.key.get_pressed()

    # IF loops for all the keys
        # Subtract or Adds the speed variable to change the location with respect to the keys
    if keys[pygame.K_LEFT]:
        x-= speed
    if keys[pygame.K_RIGHT]:
        x+= speed
    if keys[pygame.K_DOWN]:
        y+= speed
    if keys[pygame.K_UP]:
        y-= speed
    
    # IF loops for the python controlled rectangle
        # Subtract or Adds the speed variable to change the location with respect to the player's location
    if x < x2:
        x2-=speed2
    if x > x2:
        x2+=speed2
    if y < y2:
        y2-=speed2
    if y > y2:
        y2+=speed2

    # IF loop that decides to end the game when the location of both the rectangle is same
        # Displays the Backdrop image in any condition
        # Changes all the other colors to that one color as well
        # Also sets the speed of python controlled rectangle same as the speed of the player
        # Stops The music
        # Display our texts one by one and updates the python display each time
    if (x==int(x2) and y==int(y2)):
        gameDisplay.fill((0,0,0))
        blue= (0,0,0)
        red= (0,0,0)
        speed2=1
        pygame.mixer.music.stop()
        gameDisplay.blit(logo,(X-150,Y-150))
        pygame.display.update()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.time.wait(50)
            gameDisplay.blit(Font_Y,textRect_Y)
            pygame.display.update()
            pygame.time.wait(50)
            gameDisplay.blit(Font_1o,textRect_1o)
            pygame.display.update()
            pygame.time.wait(50)
            gameDisplay.blit(Font_u,textRect_u)
            pygame.display.update()
            pygame.time.wait(50)
            gameDisplay.blit(Font_L,textRect_L)
            pygame.display.update()
            pygame.time.wait(50)
            gameDisplay.blit(Font_2o,textRect_2o)
            pygame.display.update()
            pygame.time.wait(50)
            gameDisplay.blit(Font_s,textRect_s)
            pygame.display.update()
            pygame.time.wait(50)
            gameDisplay.blit(Font_t,textRect_t)
            pygame.display.update()
            pygame.time.wait(50)
            pygame.display.update()
    else:
        gameDisplay.fill((0,0,0))
        red= (140,140,140)
        blue=(208,208,208)
        speed2=0.8
        gameDisplay.blit(logo,(X-150,Y-150))

    # Player
    pygame.draw.rect(gameDisplay,red,(x2,y2,50,50))
    # Python Rectangle
    pygame.draw.rect(gameDisplay,blue,(x,y,50,50))

    # updates the python window forever
    pygame.display.update()

# Quit the pygame, python
pygame.quit()
