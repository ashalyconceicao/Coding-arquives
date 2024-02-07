import random

# Set up the game
snake = [(0, 0)]
food = (random.randint(0, 9), random.randint(0, 9))
direction = (1, 0)

# Game loop
while True:
    # Display the game board
    for row in range(10):
        for col in range(10):
            if (row, col) in snake:
                print("O", end=" ")
            elif (row, col) == food:
                print("F", end=" ")
            else:
                print(".", end=" ")
        print()

    # Get user input
    move = input("Enter direction (W/A/S/D): ").upper()

    # Update snake direction
    if move == "W":
        direction = (-1, 0)
    elif move == "A":
        direction = (0, -1)
    elif move == "S":
        direction = (1, 0)
    elif move == "D":
        direction = (0, 1)

    # Move the snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    # Check for collisions with food
    if snake[0] == food:
        food = (random.randint(0, 9), random.randint(0, 9))
    else:
        snake.pop()

    # Check for collisions with walls
    if not (0 <= snake[0][0] < 10 and 0 <= snake[0][1] < 10):
        print("Game Over! Hit the wall.")
        break