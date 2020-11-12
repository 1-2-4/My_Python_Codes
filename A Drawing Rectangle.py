# Opens The Pygame Window
import pygame

# To choose random color
import numpy

# Initialises all the python modules. (ex. "Mixer")
pygame.init()

# The pen coordinates and the speed of moving, growing in size, and changing color
x = 0
y = 0
size = 1
speed = 0.5 
red = 255
blue = 0
green = 255

# Helps to display the text in the place where its needed
X = 1366
Y = 675

# Decides window ratio and provides the surface for all the pygame elements
gameDisplay = pygame.display.set_mode((X, Y))

# The variables to break the infinite loop when needed
run = False
runer = True

# Plays the music forever
pygame.mixer.music.load(r'C:\Users\click\Desktop\KABEER\FUN\Python\Music.wav')
pygame.mixer.music.play(-1)

# Initiates the image file
logo = pygame.image.load(r'C:\Users\click\Desktop\KABEER\FUN\Pictures\Kabeer Studio.png')

# Font to be displayed as 'shift increases speed'
Rule_Font_Type = pygame.font.Font(r'C:\Users\click\Desktop\KABEER\FUN\Python\League Gothic.ttf',38)
Rule_Font = Rule_Font_Type.render("Holding Down 'Shift' will increase the speed of everything",True,(0,155,55))
Rule_Font_Space = Rule_Font.get_rect()
Rule_Font_Space.center = (X//2,Y//2)

Space_Font_Type = pygame.font.Font(r'C:\Users\click\Desktop\KABEER\FUN\Python\League Gothic.ttf',20)
Space_Font = Space_Font_Type.render("Press Space To Continue",True,(0,155,55))
Space_Font_Space = Space_Font.get_rect()
Space_Font_Space.center = (X//2,((Y//2)//2)//2)

# Loop to display "Shift increases speed"
while runer:

    # Quit on pressing cross
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runer = False
    
    # displays the font (Shift increases)
    gameDisplay.blit(Rule_Font,Rule_Font_Space)
    gameDisplay.blit(Space_Font,Space_Font_Space)

    # makes easier to take key inputs
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        runer = False
        run = True
        pygame.draw.rect(gameDisplay,(0,0,0),(0,0,X,Y))

    pygame.display.update()

# The loop
while run:
    # Quit the window when cross pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Blit the image of "Kabeer Studio"
    gameDisplay.blit(logo,(X-150,Y-150))

    # Makes it easier to take key inputs
    keys = pygame.key.get_pressed()

    # To move down
    if (keys[pygame.K_LSHIFT] and keys[pygame.K_DOWN]):
        y+= 1
    else:
        if keys[pygame.K_DOWN]:
            y+= 0.3

    # To move up
    if (keys[pygame.K_LSHIFT] and keys[pygame.K_UP]):
        y-= 1
    else:
        if keys[pygame.K_UP]:
            y-= 0.3

    # To move left
    if (keys[pygame.K_LSHIFT] and keys[pygame.K_LEFT]):
        x-= 1
    else:
        if keys[pygame.K_LEFT]:
            x-= 0.3

    # To move right
    if (keys[pygame.K_LSHIFT] and keys[pygame.K_RIGHT]):
        x+= 1
    else:
        if keys[pygame.K_RIGHT]:
            x+= 0.3

    # To increase size
    if keys[pygame.K_w]:
        size+= 0.1

    # To decrease size
    if keys[pygame.K_s]:
        size-= 0.1

    # COLOR_CHANGING:
    # To turn any color into blue if blue is lesser than 255
    if blue < 255:

        # Faster if holding shift
        if (keys[pygame.K_LSHIFT] and keys[pygame.K_d]):

            # Reduces red only if red is there
            if red>1:
                red-= 0.30
            # Reduces green only if green is there
            if green>1:
                green-= 0.30
            # Increases blue
            blue+= 0.30

        # Slower if not holding shift
        else:
            if keys[pygame.K_a]:
                # Reduces red only if red is there
                if red>1:
                    red-= 0.10
                # Reduces green only if green is there
                if green>1:
                    green-= 0.10
                # Increases blue
                blue+= 0.10

    # To turn any color into blue
    else:
        # Faster if holding shift
        if (keys[pygame.K_LSHIFT] and keys[pygame.K_a]):
            # Reduces red only if possible
            if red>1:
                red-= 0.30
            # Reduces green only if green if possible
            if green>1:
                green-= 0.30
        # Slower if not holding shift
        else:
            if keys[pygame.K_a]:
                # Reduces red only if possible
                if red>1:
                    red-= 0.10
                # Reduces green only if green if possible
                if green>1:
                    green-= 0.10
    # COLOR_CHANGING:
    if red < 255:
        if (keys[pygame.K_LSHIFT] and keys[pygame.K_a]):
            if blue>1:
                blue-= 0.30
            if green>1:
                green-= 0.30
            red+= 0.30
        else:
            if keys[pygame.K_a]:
                if blue>1:
                    blue-= 0.10
                if green>1:
                    green-= 0.10
                red+= 0.10
    else:
        if (keys[pygame.K_LSHIFT] and keys[pygame.K_a]):
            if blue>1:
                blue-= 0.30
            if green>1:
                green-= 0.30
        else:
            if keys[pygame.K_a]:
                if blue>1:
                    blue-= 0.10
                if green>1:
                    green-= 0.10
    # COLOR_CHANGING:
    if green < 255:
        if (keys[pygame.K_LSHIFT] and keys[pygame.K_q]):
            if blue>1:
                blue-= 0.30
            if red>1:
                red-= 0.30
            green+= 0.30
        else:
            if keys[pygame.K_q]:
                if blue>1:
                    blue-= 0.10
                if red>1:
                    red-= 0.10
                green+= 0.10
    else:
        if (keys[pygame.K_LSHIFT] and keys[pygame.K_q]):
            if blue>1:
                blue-= 0.30
            if red>1:
                red-= 0.30
        else:
            if keys[pygame.K_q]:
                if blue>1:
                    blue-= 0.10
                if red>1:
                    red-= 0.10
    # COLOR_CHANGING_2:
    # Chooses a random number through numpy
    if keys[pygame.K_e]:
        # For a random blue
        blue = numpy.random.randint(1,255,1)
        # For a random red
        red = numpy.random.randint(1,255,1)
        # For a random green
        green = numpy.random.randint(1,255,1)

    # COLOR_CHANGING_2:
    # To not confuse python to do it with shift or not. # JUST DO IT!!
    if (keys[pygame.K_LSHIFT] and keys[pygame.K_e]):
        blue = numpy.random.randint(1,255,1)
        red = numpy.random.randint(1,255,1)
        green = numpy.random.randint(1,255,1)
    # To draw a black rectangle on screen to give a effect of reloading
    if (keys[pygame.K_LCTRL] and keys[pygame.K_r]):
        gameDisplay.fill((0,0,0))

    # Draw the rectangle
    color=(red,green,blue)
    pygame.draw.rect(gameDisplay,(color),(x,y,size,size))

    # Decides the font type and size
    Font_Type = pygame.font.Font(r'C:\Users\click\Desktop\KABEER\FUN\Python\Font.ttf',40)

    # The Real Text
    Font = Font_Type.render("Start Drawing Now",True,(red,green,blue))

    # Makes a space for the text to appear
    Font_Space = Font.get_rect()

    # Decides the location for the text
    Font_Space.center = (X//2,75)

    gameDisplay.blit(Font,Font_Space)

    # Updates the display forever (as its in the while loop)
    pygame.display.update()

# Exits the window
pygame.quit()