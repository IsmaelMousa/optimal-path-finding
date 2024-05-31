import heapq


def heuristic(a: tuple[int, int], b: tuple[int, int]) -> int:
    """
    Calculate the Manhattan distance between two points.

    :param a: The first point.
    :param b: The second point.
    :return: The Manhattan distance between the two points.
    """

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_search(grid: list[list[str]],
                  start: tuple[int, int],
                  goal: tuple[int, int]) -> list[tuple[int, int]] | None:
    """
    Perform A* search to find the shortest path in a grid.


    :param grid: The 5x5 grid representing the map.
    :param start: The start position in the grid.
    :param goal: The goal position in the grid.

    :return: The optimal path from start to goal as a list of location pairs, or None if no path is found.
    """

    rows = len(grid)
    columns = len(grid[0])

    open_list = []

    priority = 0
    heapq.heappush(open_list, (priority, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < columns and grid[neighbor[0]][neighbor[1]] != "#":
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current

                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None


if __name__ == "__main__":
    grid = [["S", ".", ".", "#", "."],
            [".", "#", ".", "#", "."],
            [".", "#", ".", ".", "."],
            [".", ".", "#", "#", "."],
            [".", ".", ".", "#", "G"]]

    start = (0, 0)
    goal = (4, 4)

    path = a_star_search(grid=grid,
                         start=start,
                         goal=goal)

    if path:
        print("The optimal path is:", path)
    else:
        print("Path not found!")
