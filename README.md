# Fundamental of Artificial Intelligence - A* algorithm

This repository contains my `A* algorithm` assignment for the **Fundamental of Artificial Intelligence** course at [An-Najah National
University (NNU)](https://www.najah.edu/en/#).

## Overview

This assignment involves implementing the `A* algorithm` to find the shortest path on a 5x5 grid map. The grid consists
of
walkable cells, obstacles, a start position, and a goal position. The objective is to navigate from the start position
to the goal position using the `A* algorithm` while avoiding obstacles.

## Problem Description

You have a 5x5 grid representing a map. Each cell in the grid can either be empty (walkable) or contain an obstacle (
non-walkable). The grid is defined as follows:

```
S  .  .  #  .
.  #  .  #  .
.  #  .  .  .
.  .  #  #  .
.  .  .  #  G
```

- `S` marks the start position.
- `G` marks the goal position.
- `.` represents walkable cells.
- `#` represents obstacles.

## Strategy and Algorithm Choice

### Why A* Algorithm?

The A* algorithm is chosen for this problem because:

1. **Efficiency**: A* is known for being one of the most efficient pathfinding algorithms, combining the strengths of
   Dijkstra's algorithm and Greedy Best-First-Search.
2. **Optimality**: A* guarantees the shortest path if the heuristic used is admissible (never overestimates the cost to
   reach the goal).
3. **Heuristic Function**: The Manhattan distance heuristic is suitable for grid-based pathfinding where movement is
   restricted to horizontal and vertical directions.

### How A* Works

1. **Initialization**:
    - Define the start and goal positions.
    - Create a **heap queue** (priority queue) to keep track of nodes to be explored.
    - Initialize cost maps to track the cost to reach each node and the estimated total cost (current cost + heuristic
      cost).

2. **Exploration**:
    - Pop the node with the lowest estimated total cost from the priority queue.
    - For each neighbor, calculate the cost to reach it and update the priority queue accordingly.
    - Continue this process until the goal node is reached.

3. **Path Reconstruction**:
    - Once the goal is reached, reconstruct the path by tracing back from the goal to the start using the recorded
      paths.

### Heuristic Function

The heuristic function used is the **Manhattan Distance**:

```python
def heuristic(a, b):
    """
     Calculate the Manhattan distance between two points.
 
     :param a: The first point.
     :param b: The second point.
     :return: The Manhattan distance between the two points.
     """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
```

### Path Explanation

1. Start at (0, 0) (S):

```
[S, ., ., #, .]
[., #, ., #, .]
[., #, ., ., .]
[., ., #, #, .]
[., ., ., #, G]
```

2. Move to (0, 1):

```
[S, X, ., #, .]
[., #, ., #, .]
[., #, ., ., .]
[., ., #, #, .]
[., ., ., #, G]
```

3. Move to (0, 2):

```
[S, X, X, #, .]
[., #, ., #, .]
[., #, ., ., .]
[., ., #, #, .]
[., ., ., #, G]
```

4. Move to (1, 2):

```
[S, X, X, #, .]
[., #, X, #, .]
[., #, ., ., .]
[., ., #, #, .]
[., ., ., #, G]
```

5. Move to (2, 2):

```
[S, X, X, #, .]
[., #, X, #, .]
[., #, X, ., .]
[., ., #, #, .]
[., ., ., #, G]
```

6. Move to (2, 3):

```
[S, X, X, #, .]
[., #, X, #, .]
[., #, X, X, .]
[., ., #, #, .]
[., ., ., #, G]
```

7. Move to (2, 4):

```
[S, X, X, #, .]
[., #, X, #, .]
[., #, X, X, X]
[., ., #, #, .]
[., ., ., #, G]
```

8. Move to (3, 4):

```
[S, X, X, #, .]
[., #, X, #, .]
[., #, X, X, X]
[., ., #, #, X]
[., ., ., #, G]
```

9. Move to (4, 4) (G):

```
[S, X, X, #, .]
[., #, X, #, .]
[., #, X, X, X]
[., ., #, #, X]
[., ., ., #, X]
```

### Path Validation

- Each step in the path only moves horizontally or vertically by one position.
- The path avoids all obstacles (#).
- The path starts at S and ends at G.
- The path is the shortest possible route from (0, 0) to (4, 4) considering the constraints.

Therefore, the output provided by your `A*` search implementation is correct and reflects the optimal path.

### Output

```
The optimal path is: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
```

## Conclusion

The `A* algorithm` is an effective and efficient method for pathfinding on a grid with obstacles. By using the Manhattan
distance heuristic, it ensures that the path found is optimal. The provided implementation demonstrates the practical
application of `A*` in a simple 5x5 grid scenario.

