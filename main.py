import sys
from Graph import *
from State import *


def main(g, INITIAL_STATE):
    g.BFS(INITIAL_STATE)
    g.printTreeBFS(INITIAL_STATE)
    # g.DFS(INITIAL_STATE)
    # g.printTreeDFS(INITIAL_STATE)
    screen.mainloop()


if __name__ == '__main__':
    INITIAL_STATE = State(3, 3, 1, 0) #(missionaries, cannibals, boat, nodeNumber)

    g = Graph()
    main(g, INITIAL_STATE)
