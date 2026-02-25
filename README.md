# Pure Pursuit Path Tracking Algorithm

This project implements the **Pure Pursuit** algorithm from scratch using Python and Pygame. The algorithm is a classic path tracking method used in autonomous vehicles and robotics.

##  What is Pure Pursuit?

Pure Pursuit is a path tracking algorithm that guides a vehicle along a predefined path. The vehicle continuously calculates the angle toward a target point on the path and moves in that direction. When it gets close enough to the target point, it moves on to the next one.

## How It Works

1. A path is defined as a list of waypoints (x, y coordinates).
2. The vehicle starts at the first waypoint.
3. Each frame, the algorithm:
   - Calculates the angle to the current target waypoint using `atan2`
   - Moves the vehicle in that direction using `cos` and `sin`
   - If the distance to the target is less than 10 pixels, advances to the next waypoint
4. The vehicle stops when it reaches the final waypoint.

## How to Run

1. Install pygame:
```bash
   pip install pygame
```
2. Run the script:
```bash
   python pure_pursuit.py
```

## Tech Stack
- Python
- Pygame
- Math (atan2, cos, sin)
