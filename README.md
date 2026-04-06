# Mr CAINE Mission

A 2D side-scrolling platformer game built with Python and Pygame Zero. Guide CAINE through a timed mission, collect coins, avoid enemies, and reach a score of 45 before time runs out.

<img width="989" height="777" alt="image" src="https://github.com/user-attachments/assets/9ca3d1a5-971c-43d1-ad22-006cc4cabf08" />


---

## Game Overview

- **Genre:** Platformer (inspired by Super Mario Bros., Sonic The Hedgehog)
- **Engine:** Pygame Zero (pgzero)
- **Goal:** Collect enough coins to reach a score of 45 before the 45-second timer expires
- **Scenes:** Main Menu and Scene One
- **Features:** Character animation, music toggle button, multiple enemy types, coin collection, lives system

---

## Requirements

- Python 3.8 or higher
- pip
- Visual Studio Code (recommended editor)

---

## Installation

### 1. Install Visual Studio Code

Download and install VS Code from the official website:

```
https://code.visualstudio.com/download
```

---

### 2. Install Python

Download and install Python 3.8 or higher from:

```
https://www.python.org/downloads/
```

During installation, make sure to check **"Add Python to PATH"**.

Verify the installation by opening a terminal and running:

```bash
python --version
```

---

### 3. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/Merve-1/Python-Games.git
cd Python-Games.git
```

---

### 4. Install Dependencies

Install the required Python libraries using pip:

```bash
pip install pgzero pygame
```

or 
```bash
pip install -r requirements.txt
```

---

## Running the Game

From the project root directory, run:

```bash
pgzrun game.py
```


---

## Project Structure

```
Python-Games/
│
├── game.py                         # Main entry point, initializes and runs all scenes
│
├── screens/
│   ├── menu.py                     # Main menu scene with play and quit options
│   └── sceneone.py                 # Game scene with gameplay logic, timer, and win/lose conditions
│
├── sprites/
│   ├── player/
│   │   └── CAINE.py                # Main playable character: movement, jumping, animation, lives
│   ├── enemies/
│   │   ├── Enemy1.py               # Ladybug enemy with patrol movement and animation
│   │   └── Enemy2.py               # Second enemy type with patrol movement
│   └── score/
│       └── Coin.py                 # Collectible coins with gold, silver, and bronze types
│
├── helpers/
│   ├── Animation.py                # Reusable frame-based animation controller
│   ├── Button.py                   # Reusable clickable button component
│   └── Background.py               # Background rendering helper
│
├── images/
│   ├── backgrounds/                # Background images for scenes
|   |   └── default/
|   |   └── double/                
│   ├── characters/
│   │   └── default/                # CAINE walk, idle, jump, and hit sprites
|   |   └── double/                
│   ├── enemies/
│   │   └── default/                # Enemy walk and idle sprites
|   |   └── double/                
│   └── tiles/
│       └── default/                # UI tiles including hearts (source: kenney.nl)
|       └── double/                
│
└── sounds/                         # Sound effects and music (source: mixkit.co)
```

---

## Asset Credits

- Tile and UI assets sourced from [Kenney Assets](https://kenney.nl/assets) — free to use
- Sound effects sourced from [Mixkit Free Sound Effects](https://mixkit.co/free-sound-effects/) — free to use

---

## Controls

| Key | Action |
|-----|--------|
| Arrow Left | Move left |
| Arrow Right | Move right |
| Space / Arrow Up | Jump |

---

## Win and Lose Conditions

- **Win:** Timer reaches 0 and score is 45 or above
- **Lose:** Timer reaches 0 and score is below 45, or all 3 lives are lost

## Resources 
- https://pygame-zero.readthedocs.io/en/stable/
