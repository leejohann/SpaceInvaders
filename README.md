# SPACE INVADERS
Single-shooter game built using Pygame in Python. 
Use your left and right arrow keys to move your red spaceship, 
use your spacebar to shoot the angry pacmen and hit as many as possible. 
Don’t let them reach your spaceship!


## Technology
Python 3.7


## Visuals
![Image of gameplay](https://github.com/leejohann/SpaceInvaders/SpaceInvaders-gameplay.jpg)

## Resources
.png files for spaceship, angry pacmen and bullet from flaticon.com
.ttf file from dafont.com


## Notes
These notes break down the sections of code needed for the program. Mostly for personal reference.

### Elements:
  Player (Spaceship)
  Enemies (Angry Pacmen)
  Bullets
  Screen
  Scoreboard
  Game Over Screen

### Movements and generation:
  #### Player
    Starting Position - x-position: 370, y-position: 480
    To move the player with our left and right arrow key, we check for event types using Pygame
      - Key down + Left key ⇒ change x-position by -6
      - Key down + Right key ⇒ change x-position by 6
      - Key Up + Left Key OR Right key ⇒ stop moving the spaceship
    Prevent player from moving off screen
      - If statement used to restrict movement between 0 and 736
  
  #### Enemy
    Starting position - Using the random package, randomise position in the area 0 < x < 752, 50 < y < 350
    Movement change 
      - Horizontal: If pacman x-position < 0, change = 5, if pacman x-position > 752, change = -5
      - Vertical: Restrict enemy to screen width, then shift down by 40
    Game Over
      - When any one pacman reaches y-position = 480 (position of spaceship), game over.
      - Pacmen y-position = 2000 to move them all off screen
      - Display game over text
 
 #### Bullet
    Starting position: Use the spaceship’s current x and y coordinates
    Firing bullet:
      - Check that bullet state = “ready”
      - Event type: Key down + Space bar ⇒ fire bullet
    Movement 
      - x-change = 0, y-change = 15
      - If bulley_y < 0 (off-screen), then bullet_y = 480 and bullet state = “ready”
      - If bullet state = “fire”, fire bullet
      - Ensure bullet’s x-position does not change with spaceship movement
    Collision
      - Calculate distance between bullet and a pacman, if distance < 27, has_collided function is true, else false.
      - If has_collided = true, bullet_y = 480 and bullet state = “ready”, and score increases by 1.
      - Another pacman is regenerated randomly according to specifications above
