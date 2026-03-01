
# Dynamic Pathfinding Agent (Pygame)

## 📌 Project Overview

This project implements a **Dynamic Pathfinding Agent** using:

* A* Search Algorithm
* Greedy Best-First Search (GBFS)

The system is built using **Pygame** and runs on a 20×20 grid.
It supports:

* Random obstacle generation
* Manual obstacle placement
* Dynamic obstacle spawning
* Real-time visualization
* Algorithm switching
* Heuristic switching
* Performance metrics display

---

# 📦 Requirements

You must have:

* Python 3.8 or higher

Check Python version:

```
python --version
```

---

# 🔧 Install Dependencies

Install pygame using:

```
pip install pygame
```

If you are using Python 3 specifically:

```
pip3 install pygame
```

---

# ▶️ How to Run the Project

### Step 1: Open terminal in project folder

Navigate to your project directory:

```
cd path_to_your_project_folder
```

### Step 2: Run the file

```
python dynamic_pathfinding_pygame.py
```

If using Python 3:

```
python3 dynamic_pathfinding_pygame.py
```

---

# 🎮 Controls (Keyboard + Mouse)

| Key / Action | Function                        |
| ------------ | ------------------------------- |
| R            | Generate new random grid        |
| SPACE        | Start search                    |
| A            | Select A* algorithm             |
| G            | Select Greedy Best-First Search |
| M            | Select Manhattan heuristic      |
| E            | Select Euclidean heuristic      |
| D            | Toggle dynamic obstacle mode    |
| Mouse Click  | Add/remove obstacle manually    |
| Close Window | Exit program                    |

---

# 🧠 Algorithms Used

## A* Search

* Uses: f(n) = g(n) + h(n)
* Guarantees optimal path
* Slower but more accurate

## Greedy Best-First Search (GBFS)

* Uses: f(n) = h(n)
* Faster in simple grids
* Does not guarantee shortest path



# 📏 Heuristics Used

### Manhattan Distance

|x1 - x2| + |y1 - y2|

### Euclidean Distance

√((x1 - x2)² + (y1 - y2)²)


# 📊 Performance Metrics Displayed

At the bottom of the window:

* Nodes Visited
* Path Cost
* Execution Time (milliseconds)



# Dynamic Mode

When Dynamic Mode is ON (press D):

* Random obstacles may appear during execution
* Agent re-plans path if blocked
* Simulates real-world changing environments



#  Suggested Test Cases

For evaluation:

1. A* – Low obstacle density (Best case)
2. A* – High obstacle density (Worst case)
3. GBFS – Open grid (Best case)
4. GBFS – Dense obstacles (Worst case)


#  Notes

* Default obstacle density: 30%
* Grid size: 20 × 20
* Start: (0,0)
* Goal: (19,19)

