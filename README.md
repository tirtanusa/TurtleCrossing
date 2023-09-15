# Turtle Crossing


## Overview
Turtle Crossing is a game where a player-controlled turtle tries to cross a busy road without getting hit by oncoming cars. The game consists of multiple components: Player, CarManager, Scoreboard, and main.

## Player Class
The Player class handles the player's turtle character. Here are its features:

- The player can only move forward at a specified speed.
- The player has a turtle shape.
- The player starts at the STARTING_POSITION (0, -280) at the beginning of each round.

## Scoreboard Class
The Scoreboard class manages the game's scoring and level progression. It includes:

- Displaying the current level.
- An update or refresh function when the player successfully passes a level.

## CarManager Class
The CarManager class is responsible for managing the cars on the road. It has the following features:

- Generating cars.
- Moving cars from right to left at a specified speed.
- Cars have a rectangular shape.
- Each car has a randomly selected color.
- The car speed increases as the player progresses through levels.

## Game Flow (main.py)
In main.py, the game flow is managed, including:

- Collision detection between the player and cars.
- Detection when the player successfully finishes a level.
- Handling game over situations.
- Implementing a generation delay for new cars.