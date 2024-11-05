import pygame

pygame.init()


screen=pygame.display.set_mode((800,400))
#setting the tile
pygame.display.set_caption('Runner')

clock = pygame.time.Clock()

#using the default font
#test_font=pygame.font.Font(None,50)
test_font=pygame.font.Font('Runner/font/Pixeltype.ttf',50)

#AA is anti alias= smooth the edges on the text
#In our case its a pixel art so we r going to leave it as it is
text_surface=test_font.render("My game", False, 'Black')
#after adding the text show them

#*
#if the while true is not here not stay up for very long


#two types on surfaces in pygame display surface and regular surface
#can only have one display surface and always visible
#regular surface can have many, only displayed when connect to display surface
#can be image or a constant color

#show them the color
#test_surface=pygame.Surface((100,50))
#in window the its starts at (0,0) top left
#test_surface.fill('Red')

#in pygame when you want to display images you first convert it to 
#image then u show it in the screen
#.convert makes it faster and more compatible with pygame
sky_surface=pygame.image.load('Runner\Sky.png').convert()
ground_surface=pygame.image.load('Runner\ground.png').convert()
#when you see white background when you use .convert use .convert_alpha to remove the extra black and white
snail_surface = pygame.image.load('Runner\graphics\snail\snail1.png').convert_alpha()
#This is a way to create a rectangle
# player_rect=pygame.Rect(left, top, width, height)

#use rectangle to place objects at precise locations and also detect collisons
player_surf=pygame.image.load('Runner\graphics\Player\player_walk_1.png').convert_alpha()
#need to make it work
#player_rect=player_surf.get_rect(midLeft= (80,200))

snail_x_pos=600
snail_y_pos=270
vel=3


jumping = False

#gravity must be divisible by jump height
Y_Gravity=1
JumpHeight=20
Y_velocity=JumpHeight

while True:
    #show it running
    #going throught every events in pygame and looks to see if one of them is pygame.QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #its like the opposite of inilization
            pygame.quit()
            #stops the loop
            exit()

    #draw all our elements

    #block image transfer
    #means putting a surface on top of another surface
    #*
    #change the 0,0
    #put ground above the sky
    #the order at which you put sky and ground does matter
    #if you comment out the both ground and sky the snail will look wierd
    #since it shows how the snails frame gets updates. So make sure to have a layer below it
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300,50))
    #show snail moving the right
    #if - then it moves left
    
    #stores keys pressed
    # creating a new dictornary
    keys=pygame.key.get_pressed()

    #if left arrow key is pressed
    if keys[pygame.K_LEFT] and x>0:
        snail_x_pos -=vel
    
    # if left arrow key is pressed 
    if keys[pygame.K_RIGHT] and x<500-width: 
          
        # increment in x co-ordinate 
        snail_x_pos += vel 
         
    # if left arrow key is pressed    
    if keys[pygame.K_UP] and y>0: 
        jumping=True
    
    if keys[pygame.K_SPACE] and y>0: 
        jumping=True

    if jumping:
        #subtracting actually moves it up
        snail_y_pos -=Y_velocity
        #bring it down
        Y_velocity -= Y_Gravity

        #Y_velocity increases jump up
        #Y_velocity decreases as you come down

        if Y_velocity < -JumpHeight:
            jumping=False
            Y_velocity=JumpHeight
          
    # if left arrow key is pressed    
    #if keys[pygame.K_DOWN] and y<500-height: 
        # increment in y co-ordinate 
     #   snail_x_pos -= vel 

    #now it goes of the screen
    #show the snail reappreaing
    if snail_x_pos<-100: snail_x_pos=800

    #show the snail static
    screen.blit(snail_surface,(snail_x_pos, snail_y_pos))
    #screen.blit(snail_surface, player_rect)

    #updates everything
    #only have to call it once
    pygame.display.update()
    #setting the maximum frame rate 

    #its updating constantly but we r not changing the objects position
    #if you change this the snail is going to be very fast
    clock.tick(60)