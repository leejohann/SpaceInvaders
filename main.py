import pygame
import random
import math

# Initialising Pygame
pygame.init()

# Screen Creation
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('nightsky.jpg')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


# Player
player_image = pygame.image.load('player.png')
player_x = 370 # player position on the screen
player_y = 480
playerx_change = 0


# Enemy
# Since we want multiple enemies, we use lists to store all the information
enemy_image = []
enemy_x = []
enemy_y = []
enemyx_change = []
enemyy_change = []
number_of_enemies = 6

for i in range(number_of_enemies): # creates each of the 6 enemies
    enemy_image.append(pygame.image.load('red_guy.png'))
    # random enemy position from random package
    enemy_x.append(random.randint(0, 752))
    enemy_y.append(random.randint(50, 350))
    enemyx_change.append(5)
    enemyy_change.append(40)


# Bullet
# Ready state: cannot see bullet on screen
# Fire state: the bullet is moving
bullet_image = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bulletx_change = 0
bullety_change = 15
bullet_state = "ready"


# Score
score_value = 0
font = pygame.font.Font('Arcadepix Plus.ttf', 32) # to change the font, download and add a .ttf file
text_x = 10 # position of score board on screen
text_y = 10


# Game Over Text
game_over_font = pygame.font.Font('Arcadepix Plus.ttf', 100)

def show_score(x, y):
    # render the score
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    # draws the player on the screen using blit
    screen.blit(player_image, (x, y))

def enemy(x, y, i):
    # draws the enemy on the screen using blit
    screen.blit(enemy_image[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))

def has_collided(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow((enemy_x-bullet_x), 2) + math.pow((enemy_y-bullet_y), 2))
    if distance < 27:
        return True
    else:
        return False



# Game Loop:

# To ensure that the game window is always running
running = True
while running:

    # Screen - use RGB values (each with max 255)
    screen.fill((72,61,139))

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        # Closing the game
        if event.type == pygame.QUIT:
            running = False

        # Check if the left or right arrow key has been pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change =- 6
            if event.key == pygame.K_RIGHT:
                playerx_change = 6
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        # Check if the left or right arrow key has been released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    # To prevent the player from going off screen
    player_x += playerx_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Enemy movement
    for i in range(number_of_enemies):

        # Game Over
        if enemy_y[i] > 480:
            for j in range(number_of_enemies):
                enemy_y[j] = 2000 # moves all enemies out of screen
            game_over_text()
            break

        # To change the position of the enemy, and shift down when it reaches the edges
        enemy_x[i] += enemyx_change[i]
        if enemy_x[i] <= 0:
            enemyx_change[i] = 5
            enemy_y[i] += enemyy_change[i]
        elif enemy_x[i] >= 752:
            enemyx_change[i] = -5
            enemy_y[i] += enemyy_change[i]

        # Collision
        collision = has_collided(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, 752) # randomises the position of the new enemy
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullety_change


    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()