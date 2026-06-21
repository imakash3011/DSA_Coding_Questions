def is_safe(x, y, maze, n, visited):
    # Check if x and y are within bounds, the cell is not blocked (1), and not visited
    return (0 <= x < n) and (0 <= y < n) and (maze[x][y] == 1) and (not visited[x][y])

def solve_maze_util(maze, n, x, y, sol, visited, path, result):
    # Base Case: If destination is reached, store the path
    if x == n - 1 and y == n - 1:
        result.append("".join(path))
        return

    # Mark the current cell as visited
    visited[x][y] = True

    # Define moves in lexicographical order: Down (D), Left (L), Right (R), Up (U)
    # This ensures paths are found in alphabetical order if needed.
    directions = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]

    for direction, dx, dy in directions:
        next_x = x + dx
        next_y = y + dy

        if is_safe(next_x, next_y, maze, n, visited):
            path.append(direction)
            solve_maze_util(maze, n, next_x, next_y, sol, visited, path, result)
            path.pop()  # Backtrack: remove the move before trying the next direction

    # Unmark the current cell for other possible paths
    visited[x][y] = False

def find_path(maze):
    n = len(maze)
    result = []
    
    # If the source or destination is blocked, no path is possible
    if maze[0][0] == 0 or maze[n-1][n-1] == 0:
        return result

    visited = [[False for _ in range(n)] for _ in range(n)]
    path = []
    
    solve_maze_util(maze, n, 0, 0, maze, visited, path, result)
    return result

# --- Example Usage ---
if __name__ == "__main__":
    # 4x4 Maze Example
    # 1 = Open path, 0 = Wall
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]

    paths = find_path(maze)
    
    if paths:
        print(f"Paths found ({len(paths)}):")
        for p in paths:
            print(p)
    else:
        print("No path exists.")