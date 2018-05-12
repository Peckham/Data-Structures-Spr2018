import copy


def maze_solver(maze):
    ''' return a list of moves showing the correct steps to solve the given
        maze
        @maze: list of list, representing the maze

        return: list of correct moves to solve the maze.

        1. Find the position of the maze.
        2. Check the adjacent positions.
        3. If we reach e, return our list.
    '''
    start = checkPos(maze, findStart(maze), [])

    def _nextIter(posDict, e=False, build=[], traversed=[]):
        ''' Takes as input the dictionary returned by checkPos, and a build
            of the current pathwayself.
            Returns a call _nextInter with the potential options added to
            build, until the boolean value returned by checkPos is True.
            Then, return the completed build. '''
        if e:
            print("Passed!")
            build += posDict.keys()
            return build

        for i in posDict.keys():
            newBuild = build[:]
            newBuild.append(i)
            nextPos = checkPos(maze, posDict[i], traversed)
            return _nextIter(nextPos[0], nextPos[1], newBuild)

    return _nextIter(start[0], start[1])


def checkPos(maze, coords, traversed):
    ''' Takes as input a maze to traverse and the coordinates of a starting
        position. Also takes a list of coordinate tuples for places to not
        include in results.
        Return a dictionary and a boolean value. The dictionary
        contains a string direction (up, down, left right) of possible moves
        as a key, and the coordinate of the position. The boolean value is
        True if the value we are returning is e, thus signalling the end of
        the traversal. '''

    x, y = coords[0], coords[1]
    options = {"up": (maze[y - 1][x], (y - 1, x)),
               "left": (maze[y][x - 1], (y, x - 1)),
               "right": (maze[y][x + 1], (y, x + 1))}
    try:
        options["down"] = (maze[y + 1][x], (y + 1, x))
    except IndexError:
        pass

    selections = {i: options[i][1] for i in options.keys()
                  if options[i][0] in [".", "e"] and options[i][1] not in
                  traversed}
    traversed += [selections[i][1] for i in selections.keys()]

    for i in selections.keys():
        if selections[i][0] is "e":
            return {i: options[1]}, True

    return selections, False, traversed


def findStart(maze):
    ''' Return s, the starting position of the maze.
    '''
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "s":
                return [x, y]


def main():
    file = open("maze.txt", 'r')
    maze = []
    for line in file:       # Read input maze, store into a 2-D list
        maze.append([])
        for character in line:
            maze[-1].append(character)
    # print(maze)
    print(maze_solver(maze))
    '''
    Result should be something like this, not unique solution though.
    ['right', 'down', 'down', 'right', 'right', 'up', 'up', 'right', 'right', 'down',
    'down', 'down', 'right', 'up', 'right', 'up', 'up', 'right', 'right', 'right', 'down',
    'down', 'down', 'down', 'right', 'up', 'right', 'up', 'up', 'up', 'right', 'right', 'right']
    '''


main()
