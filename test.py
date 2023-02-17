from collections import deque #TODO make it an application


def path_finder(maze):
    maze = maze.splitlines()
    start_y, start_x = find_start(maze)
    bag = deque(((start_y, start_x, 0),))
    seen = set((start_y, start_x))
    while bag:
        cy, cx, c_moves = bag.popleft()
        for py, px in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ty, tx, t_moves = cy + py, cx + px, c_moves + 1
            if ty < 0 or tx < 0 or tx > len(maze)-1 or ty > len(maze)-1 or (ty, tx) in seen:
                continue
            square = maze[ty][tx]
            if square == "E":
                return t_moves
            if square != "W":
                bag.append((ty, tx, t_moves))
                seen.add((ty, tx))
    return "Impossible mze"


def find_start(maze):
    for y, row in enumerate(maze):
        for x, square in enumerate(row):
            if square == "S":
                return y, x
    raise Exception("No starting point")


if __name__ == "__main__": 
    #Create the maze with "S" as the starting point, "E" as the finishing point, "W" as walls and "." as empty spaces. 
    #If the maze is possible, it should output how many steps it took to reach the end point.
    #Some examples are below
    print(path_finder("\n".join([
        "S.....",
        "......",
        "......",
        "......",
        ".....W",
        "....WE"
    ]))) #Impossible maze as the end point is blocked of with walls

    print(path_finder("\n".join([
        "SW.",
        ".WE",
        "..."
    ]))) #takes 5 steps to reach

    print(path_finder("\n".join([
        "S.W.W.WW...W..WW.....",
        "...W......WW..W.W....",
        "...W.W....W.......W..",
        ".W................W.W",
        "......WW.W....W...WW.",
        "....WW..........W....",
        ".W.....WW..WW..W..W..",
        "..........WW...W.WW.W",
        "........W........W...",
        "W..........W.........",
        "......W..W...........",
        ".........W....WW...W.",
        "W.W....WW....WW......",
        ".W...W....W.WWW...WW.",
        "W..W.W...W...WW..W...",
        "W.WW...W..W.W.....WW.",
        ".WWW..............WW.",
        ".........W.....W.W.E.",
        "WW..........W...W....",
        "...W.W.WW..WW......WW",
        "..W.W.........W.....",
    ]))) #A more complex example
