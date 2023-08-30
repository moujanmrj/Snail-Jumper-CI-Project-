# Snail jumper
**Neuroevolution game assignment.**  
**Fall 2021 - Computer Intelligence.**  

This game has been developed as an assignment for students at Amirkabir University of Technology to apply neuroevolution using a simple game.  
![Snail Jumber](SnailJumper.png)


# Snail Jumper Game with Neuroevolution

Welcome to the Snail Jumper Game with Neuroevolution! This project combines a fun and addictive game with the power of neural networks and evolutionary algorithms. Evolve and train characters to overcome obstacles and achieve high scores.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Game Modes](#game-modes)
  - [Manual Mode](#manual-mode)
  - [Neuroevolution Mode](#neuroevolution-mode)
- [Neural Network Architecture](#neural-network-architecture)
- [Evolution Algorithm](#evolution-algorithm)
- [Game Controls](#game-controls)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Introduction
The Snail Jumper Game with Neuroevolution combines entertainment with AI training. In this game, players can either control the character manually or observe characters evolving over generations using neural networks. This project demonstrates the potential of evolutionary algorithms and neural networks in gaming.

## Features
- Interactive gameplay with manual controls.
- Automatic character evolution through neuroevolution.
- Dynamic obstacles and challenges.
- Fully connected neural network architecture.
- Evolution algorithm for selecting and evolving characters.
- User-friendly GUI for intuitive navigation.
- Learning curve tracking for observing AI improvement.

## Getting Started

### Prerequisites
- Python 3.x
- Pygame (Install using `pip install pygame`)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/snail-jumper.git
   cd snail-jumper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Game Modes

### Manual Mode
- Launch the game using `python main.py`.
- Click on the "Start Game" button on the main menu.
- Control the character's gravity using the spacebar.
- Avoid obstacles and aim for a high score.

### Neuroevolution Mode
- Launch the game using `python main.py`.
- Click on the "Start With Neuroevolution" button on the main menu.
- Watch characters evolve automatically using neural networks.
- Characters are trained to navigate obstacles and improve over generations.

## Neural Network Architecture
The game uses a fully connected neural network with adjustable architecture. The network processes inputs related to character and obstacle positions and outputs gravity direction.

## Evolution Algorithm
Characters in neuroevolution mode undergo an evolutionary algorithm process.
- Parent selection using roulette wheel or SUS.
- Crossover and mutation to create a new generation of characters.
- Fitness values drive the evolution process.

## Game Controls
- In manual mode: Use the spacebar to toggle the player's gravity and avoid obstacles.
- In neuroevolution mode: No direct controls are required. Characters evolve automatically.




