# Alien Invasion – Artamonovna Kovalenko

**Alien Invasion** is a classic arcade-style space shooter game developed in Python.
Players control a spaceship to destroy waves of enemy ships while progressing through increasingly challenging levels.

## 🎮 Gameplay Overview

- **Objective**: Destroy enemy ships using your spaceship's bullets.
- **Levels**: The game consists of multiple levels, each more challenging than the last.
- **Lives**: Players have a limited number of lives; the game continues until all lives are lost.
- **Enemy Behavior**:
  - From level 3 onwards, enemy ships begin to fire bullets at the player's ship.
  - Starting at level 5, enemy ships are equipped with shields that require multiple hits to break.
- **Scoring**: The game tracks the player's score and records the highest score achieved.

## 🛠️ Features

- Smooth animations and responsive controls.
- Progressive difficulty with each level.
- Enemy ships with offensive capabilities and defensive shields.
- Real-time score tracking and high score saving.
- Interactive menu system for game navigation.

## 📁 Project Structure

- `allien.py`: Main game loop and initialization.
- `ship.py`: Player's spaceship class and behavior.
- `bullet.py`: Bullet mechanics for both player and enemies.
- `allienbuller.py`: Enemy bullet behavior.
- `animated_sprite.py`: Handles sprite animations.
- `button.py`: UI button elements.
- `game_stats.py`: Tracks game statistics like score and lives.
- `menu.py`: Game menu interface.
- `scoreboard.py`: Displays current and high scores.
- `settings.py`: Game settings and configurations.
- `window.py`: Manages the game window and display.
- `images/`: Directory containing image assets.
- `sounds/`: Directory containing sound effects and music.

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Required Python libraries (e.g., `pygame`).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sillkiw/Allien_Invasion_Artamonovna_Kovalenko.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Allien_Invasion_Artamonovna_Kovalenko
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Game

Execute the main game script:

```bash
python allien.py
```

## 🖼️ Screenshots

*Include screenshots of the game here to showcase gameplay and interface.*

## 📄 License

*Specify the license under which the game is distributed, if any.*

## 🙌 Acknowledgements

- Developed by Artamonovna Kovalenko.
- Inspired by classic arcade space shooter games.
