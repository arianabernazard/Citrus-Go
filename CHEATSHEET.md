# Citrus-Go

Absolutely. Here’s a **simple cheat sheet Ariana can follow** so **Citrus Go** stays organized and also hits the AP CSP-style requirements.

# Citrus Go Pygame Cheat Sheet

## 1. Basic structure to follow

Every Pygame game should be built in this order:

### A. Imports and setup

This is where she:

* imports pygame
* starts pygame
* creates screen
* sets title
* creates clock

```python
import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Citrus Go")

clock = pygame.time.Clock()
```

---

### B. Variables

This is where she stores game data.

Examples:

* player position
* jump velocity
* score
* game over
* obstacle list

```python
player_x = 100
player_y = 300
player_size = 40
player_velocity_y = 0
gravity = 1
jump_strength = -15
on_ground = True

obstacles = []
score = 0
game_over = False
```

## AP requirement hit here:

* **List**: `obstacles = []`

---

### C. Functions

She should put repeated behavior into functions.

Good functions for Citrus Go:

* `draw_player()`
* `draw_obstacles()`
* `move_obstacles()`
* `spawn_obstacle(speed)`
* `check_collision(player_rect, obstacle_rects)`
* `reset_game()`

Example:

```python
def spawn_obstacle(speed):
    obstacle = {"x": WIDTH, "y": 320, "width": 30, "height": 50, "speed": speed}
    obstacles.append(obstacle)
```

## AP requirement hit here:

* **Function with a parameter**: `speed`

---

### D. Game loop

This is the heart of the game.

Inside the loop she should do these in order:

1. handle events
2. read key input
3. update player
4. update obstacles
5. check collisions
6. update score
7. draw everything
8. refresh screen

Basic pattern:

```python
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

## AP requirement hit here:

* **Iteration**: `while running:`

---

## 2. The exact coding sections she should build

### Section 1: Create the window

Goal:

* blank game window opens
* closes correctly

---

### Section 2: Draw the orange

Goal:

* orange appears on screen

She can start with a circle or rectangle.

```python
pygame.draw.circle(screen, (255, 165, 0), (player_x, player_y), 20)
```

---

### Section 3: Add jumping

Goal:

* press space to jump
* gravity pulls orange back down

This is one of the most important parts.

Example logic:

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_SPACE] and on_ground:
    player_velocity_y = jump_strength
    on_ground = False

player_velocity_y += gravity
player_y += player_velocity_y

if player_y >= 300:
    player_y = 300
    player_velocity_y = 0
    on_ground = True
```

## AP requirement hit here:

* **Selection**: `if keys[...] and on_ground`
* **Sequence**: velocity changes, then y changes, then ground check

---

### Section 4: Add obstacles

Goal:

* obstacles appear
* move left across screen

Example obstacle list item:

```python
{"x": 800, "y": 320, "width": 30, "height": 50, "speed": 5}
```

Move them:

```python
for obstacle in obstacles:
    obstacle["x"] -= obstacle["speed"]
```

---

### Section 5: Remove off-screen obstacles

Goal:

* obstacles that leave screen get deleted

```python
obstacles = [ob for ob in obstacles if ob["x"] + ob["width"] > 0]
```

---

### Section 6: Collision detection

Goal:

* if orange hits obstacle, game ends

```python
player_rect = pygame.Rect(player_x - 20, player_y - 20, 40, 40)

for obstacle in obstacles:
    obstacle_rect = pygame.Rect(obstacle["x"], obstacle["y"], obstacle["width"], obstacle["height"])
    if player_rect.colliderect(obstacle_rect):
        game_over = True
```

## AP requirement hit here:

* **Selection**: collision check with `if`

---

### Section 7: Score

Goal:

* score increases while surviving

```python
score += 1
```

Later she can draw it on screen with a font.

---

### Section 8: Restart

Goal:

* press R to restart after game over

```python
if game_over and keys[pygame.K_r]:
    reset_game()
```

---

## 3. Best structure for the final program

This is the structure I’d want her to follow:

```python
# 1. imports
# 2. pygame setup
# 3. colors / constants
# 4. game variables
# 5. functions
# 6. main game loop
# 7. quit pygame
```

That keeps the code readable and easier to explain.

---

## 4. Minimum features she should include

To keep the project realistic, I’d make this her minimum target:

* game window
* orange player
* jump mechanic
* obstacle list
* obstacles move
* collision detection
* score
* restart

That is enough.

---

## 5. What she can say for AP-style explanation

She should be able to explain these parts clearly:

### Her list

> I used a list called `obstacles` to store all the obstacles currently on the screen.

### Her function with parameter

> I made a function like `spawn_obstacle(speed)` so I could create obstacles with different speeds.

### Her algorithm

> My program uses sequencing, selection, and iteration. It updates the player, moves obstacles, checks for collisions, and updates the score inside the game loop.

---

## 6. Simple “do not get stuck” rules

Tell her to follow these rules:

* get one thing working before adding the next thing
* do not try to make it pretty first
* save often
* test after every small change
* if something breaks, go back to the last working version

---

## 7. Suggested ticket order

She should code in this order:

1. Create game window
2. Draw orange player
3. Add jump mechanic
4. Create obstacle list
5. Spawn obstacles
6. Move obstacles
7. Check collision
8. Add score
9. Add restart
10. Polish visuals

---

## 8. Easiest AP-safe pieces to make sure are included

These are the three big ones she should not forget:

```python
obstacles = []
```

```python
def spawn_obstacle(speed):
    ...
```

```python
while running:
    ...
    if player_rect.colliderect(obstacle_rect):
        game_over = True
```

If those are in there and she understands them, she is in good shape.

If you want, I can turn this into a **clean one-page cheat sheet written directly for Ariana** in a more kid-friendly format she can keep next to her while coding.
