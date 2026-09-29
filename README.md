# ProjectHailstone

A top-down zombie shooter game built with Python and Pygame.

## Features

- **Multiple Weapons:** M4A4 assault rifle and M1911 pistol with distinct fire rates and damage
- **Ammo System:** Realistic magazine management with reload mechanics
- **Room Progression:** Navigate through multiple rooms with increasing difficulty
- **Enemy AI:** Zombies track and pursue the player
- **Audio:** Sound effects for weapons, reloads, and background music

## Screenshots

*(Add a screenshot or GIF here)*

## How to Run

```bash
# Clone the repository
git clone https://github.com/PorterP90/ProjectHailstone.git
cd ProjectHailstone

# Install dependencies
pip install pygame

# Run the game
python main.py
```

## Controls

- **WASD** — Movement
- **Mouse** — Aim
- **Left Click** — Shoot
- **R** — Reload
- **1/2** — Switch weapons

## Project Structure

```
ProjectHailstone/
├── main.py          # Game loop and core logic
├── player.py        # Player class and movement
├── enemies.py       # Zombie AI and behavior
├── weapons.py       # Weapon mechanics
├── ammoBoxs.py      # Ammo pickup system
├── rooms.py         # Level/room management
└── functions.py     # Utility functions
```

## What I Learned

- Game development fundamentals: main loops, delta time, sprite management
- Collision detection and response
- State management across game objects
- Self-taught Pygame through official documentation

## License

MIT
