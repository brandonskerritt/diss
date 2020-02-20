"""
Class to make the maze in Python
"""

import numpy as np

class maze:
    def __init__(self):
        self.maze = np.array([
            [ 1.,  0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
            [ 1.,  1.,  1.,  1.,  1.,  0.,  1.,  1.,  1.,  1.],
            [ 1.,  1.,  1.,  1.,  1.,  0.,  1.,  1.,  1.,  1.],
            [ 0.,  0.,  1.,  0.,  0.,  1.,  0.,  1.,  1.,  1.],
            [ 1.,  1.,  0.,  1.,  0.,  1.,  0.,  0.,  0.,  1.],
            [ 1.,  1.,  0.,  1.,  0.,  1.,  1.,  1.,  1.,  1.],
            [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
            [ 1.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  0.],
            [ 1.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,  1.,  1.],
            [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,  1.,  1.]
        ])
        print(self.maze.shape)
    def getMaze():
        return self.maze
    def getSizeOfMaze():
        return len(self.maze)

m = maze()