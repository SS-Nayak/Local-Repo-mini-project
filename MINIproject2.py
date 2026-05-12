import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the player's car
car_width = 73
car_height = 82
car_img = pygame.image.load("D:\PROGRAMMING\PYTHON Programming\CAR.jpeg")  # Replace "car.png" with your car image file path
car_img = pygame.transform.scale(car_img, (car_width, car_height))
car_x = (screen_width - car_width) // 2
car_y = screen_height - car_height - 10
car_dx = 0

# Set up the other cars
other_car_width = 73
other_car_height = 82
other_car_img = pygame.image.load("D:\PROGRAMMING\PYTHON Programming\CAR2")  # Replace "car.png" with the other car image file path
other_car_img = pygame.transform.scale(other_car_img, (other_car_width, other_car_height))
other_car_x = random.randint(0, screen_width - other_car_width)
other_car_y = -other_car_height
other_car_dy = 5

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle keypress events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_dx = -5
            elif event.key == pygame.K_RIGHT:
                car_dx = 5

        # Handle key release events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_dx = 0

    # Update player's car position
    car_x += car_dx

    # Boundary checking for player's car
    if car_x < 0:
        car_x = 0
    elif car_x > screen_width - car_width:
        car_x = screen_width - car_width

    # Update other cars position
    other_car_y += other_car_dy

    # Reset other car if it goes off the screen
    if other_car_y > screen_height:
        other_car_x = random.randint(0, screen_width - other_car_width)
        other_car_y = -other_car_height

    # Collision detection
    if car_x < other_car_x + other_car_width and car_x + car_width > other_car_x and car_y < other_car_y + other_car_height and car_y + car_height > other_car_y:
        running = False

    # Clear the screen
    screen.fill(white)
    
    # Draw the player's car
    screen.blit(car_img, (car_x, car_y))
    
    # Draw the other car
    screen.blit(other_car_img, (other_car_x, other_car_y))
    
    # Update the display
    pygame.display.update()
    
    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()