import copy
def maze_solver(maze):
    ''' return a list of moves showing the correct steps to solve the given maze 
        @maze: list of list, representing the maze

        return: list of correct moves to solve the maze.
    '''
    # To do
    pass

def main():
    file = open("maze.txt", 'r') 
    maze = []
    for line in file:       # Read input maze, store into a 2-D list
        maze.append([])
        for character in line:
            maze[-1].append(character)
    
    print(maze_solver(maze))
    '''
    Result should be something like this, not unique solution though.
    ['right', 'down', 'down', 'right', 'right', 'up', 'up', 'right', 'right', 'down', 
    'down', 'down', 'right', 'up', 'right', 'up', 'up', 'right', 'right', 'right', 'down', 
    'down', 'down', 'down', 'right', 'up', 'right', 'up', 'up', 'up', 'right', 'right', 'right']
    '''


main()