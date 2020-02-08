from State import *
import turtle
from turtle import *
import time


import turtle
from turtle import Screen

screen=Screen()
screen.screensize(2000, 1100)
screen.setup(width=1.0, height=1.0)

t = turtle.Turtle()
t.speed('fastest')
turtle.speed('fastest')
t.penup()
# ts = getscreen().getcanvas()
# ts.yview_moveto(450)

def conclusion(nodes, time):
    t.penup()
    t.setposition([-350, 350])
    t.pendown()
    t.write("Nodes Expanded: {} \nTime Taken: {}s".format(nodes, int(time)), font=("Arial", 16, "normal"))  
    t.penup()


def draw_rectangle(point, text, parent_point, fill_color):
    color('black', fill_color)
    t.penup()
    if parent_point is not None:
        t.setposition(parent_point)
        t.pendown()
        t.setposition(point)
        t.penup()
    t.setposition(point)
    t.pendown()
    t.forward(30) #Forward turtle by 150 units
    t.right(90) #Turn turtle by 90 degree
    t.forward(30) #Forward turtle by 80 units
    t.right(90) #Turn turtle by 90 degree
    t.forward(60) #Forward turtle by 150 units
    t.right(90) #Turn turtle by 90 degree
    t.forward(30) #Forward turtle by 80 units
    t.right(90) #Turn turtle by 90 degree
    t.forward(30)
    penup()
    setposition(point[0] - 18, point[1] - 23)
    write(text)
    t.penup()
    setposition(point)
    begin_fill()
    pendown()
    forward(30) #Forward turtle by 150 units
    right(90) #Turn turtle by 90 degree
    forward(30) #Forward turtle by 80 units
    right(90) #Turn turtle by 90 degree
    forward(60) #Forward turtle by 150 units
    right(90) #Turn turtle by 90 degree
    forward(30) #Forward turtle by 80 units
    right(90) #Turn turtle by 90 degree
    forward(30)
    end_fill()
    
    penup()
    setposition(point[0] - 18, point[1] - 23)
    write(text)

class Graph:

    def __init__(self):

        self.dfs_parent = {}
        self.dfs_child = {}
        self.bfs_parent = {}
        self.bfs_child = {}
        self.bfs_goal  = None
        self.dfs_goal = None

        self.expandedDFS = 0

    


    def BFS(self, s):
        self.expandedBFS = 0
        self.bfs_parent[s] = None
        self.visited = []

        queue = [s]
        while queue:
            u = queue.pop()

            self.visited.append(u)

            # print(self.dfs_parent[u] == None or self.dfs_parent[u])
            self.expandedBFS += 1

            if u.isGoalState():
                self.bfs_goal = u
                break

            for v in u.successors():
                self.bfs_parent[v] = u

                if (u == s or v.notParent(self.bfs_parent[u])):  
                    if u not in self.bfs_child.keys():
                        self.bfs_child[u] = [v]
                    elif v not in self.bfs_child[u]:
                        self.bfs_child[u].append(v)

                if v.isValidDead():				
                    if (u == s or v.notParent(self.bfs_parent[u])): 
                        queue = [v] + queue

        # for x in self.bfs_child.keys():
        #     print("{}: {}".format(x, self.bfs_child[x]))
        # print(self.expandedBFS)


    def printTreeBFS(self, start):
        depth_nodes = [1, 5, 3, 8, 5, 14, 11, 16, 11, 16, 19, 23]
        parent_position = [None]
        child_count = [1, 0]
        left_end = 500
        current_depth = 350
        current_length = 0
        queue = [start]
        currentNode = queue[0]
        break_condition = False
        bfs_path = []
        tempQueue = []
        dist = 80
        break_condition = False
        bfs_path = [self.bfs_goal]
        # for i in range(6):
        start = time.time()
        while self.bfs_parent[self.bfs_goal] is not None:
            bfs_path.append(self.bfs_parent[self.bfs_goal])
            self.bfs_goal = self.bfs_parent[self.bfs_goal]
        
        while True:
            if len(queue) == 0:
                current_depth -= 75

                queue.extend(tempQueue)
                tempQueue = []
                depth_nodes = depth_nodes[1:]
                current_length = -(80 * depth_nodes[0] - 20) / 2
                currentNode = queue[0]
            base_position = [current_length, current_depth]
            if not currentNode.isValidDead():
                draw_rectangle([base_position[0] + (depth_nodes[0] - len(queue)) * dist, current_depth], currentNode.stateValue(), parent_position[0], 'red')
            elif currentNode in bfs_path:
                draw_rectangle([base_position[0] + (depth_nodes[0] - len(queue)) * dist, current_depth], currentNode.stateValue(), parent_position[0], 'green')
            else:
                draw_rectangle([base_position[0] + (depth_nodes[0] - len(queue)) * dist, current_depth], currentNode.stateValue(), parent_position[0], 'white')
            if currentNode.isGoalState():
                break

            child_count[0] -=1
            if child_count[0] == 0:
                child_count = child_count[1:]
                parent_position = parent_position[1:]
            if currentNode in self.bfs_child.keys():
                for x in self.bfs_child[currentNode]:
                    child_count[-1] += 1
                    if break_condition:
                        break
                    tempQueue.append(x)
                    # if x.isGoalState():
                    #     break_condition = True
                child_count.append(0)
                parent_position.append([base_position[0] + (depth_nodes[0] - len(queue)) * dist, current_depth - 30])
                    
                #     if x.isGoalState():
                #         goal_state = x
                #         bfs_path.append(goal_state)
                #         break_condition = True
                #         break
                
            # if currentNode.isGoalState():
            #     break
            queue = queue[1:]
            
            if len(queue) != 0:
                currentNode = queue[0]
        end = time.time()
        conclusion(self.expandedBFS, end - start )
            
    def DFS(self, s):
        self.expandedDFS = 0
        self.dfs_parent[s] = None
        self.visited = []

        stack = [s]
        while stack:

            u = stack.pop()
            # print(u)
            self.visited.append(u)

            # print(self.dfs_parent[u] == None or self.dfs_parent[u])
            self.expandedDFS += 1

            if u.isGoalState():
                self.dfs_goal = u
                break

            for v in u.successors():
                self.dfs_parent[v] = u
                if (u == s or v.notParent(self.dfs_parent[u])):
                    for x in self.visited:
                        if x.isSame(v):
                            break
                    else:
                        if u not in self.dfs_child.keys():
                            self.dfs_child[u] = [v]
                        else:
                            self.dfs_child[u].append(v)

                if v.isValidDead():
                    for x in self.visited:
                        if x.isSame(v):
                            break
                    else:
                        if (u == s or v.notParent(self.dfs_parent[u])): 
                            stack.append(v)

    def printTreeDFS(self, start):
        stack = [start]
        parent_stack = []
        depth_nodes = {}
        for i in range(275, -476, -75):
            depth_nodes[i] = 5
        visited = []
        currentNode = stack[0]
        stack = stack[1:]
        nodes = 1
        current_depth = 350
        base_position = [0, current_depth]
        dfs_path = []


        dfs_path.append(self.dfs_goal)
        while self.dfs_parent[self.dfs_goal] is not None:
            dfs_path.append(self.dfs_parent[self.dfs_goal])
            self.dfs_goal = self.dfs_parent[self.dfs_goal]

        start = time.time()
        while True:
            if nodes == 1:
                nodes = 5
                parent_position = [base_position[0], base_position[1] - 30]
                draw_rectangle(base_position, currentNode.stateValue(), None, 'green')
            else:
                current_depth = parent_stack[-1][1] - 45
                if currentNode in dfs_path:
                    color_fill = 'green'
                elif not currentNode.isValidDead():
                    color_fill = 'red'
                else:
                    color_fill = 'white'
                draw_rectangle([-160 + (5 - depth_nodes[current_depth]) * 80, current_depth], currentNode.stateValue(), parent_stack.pop(), color_fill)
                depth_nodes[current_depth] -= 1
                # parent_stack = parent_stack[1:]
                parent_position = [-160 + (4 - depth_nodes[current_depth]) * 80, current_depth - 30]


            if currentNode.isGoalState():
                break
                
            if currentNode in self.dfs_child.keys():
                visited.append(currentNode)
                for x in self.dfs_child[currentNode]:
                    if x not in visited:
                        stack.append(x)
                        parent_stack.append(parent_position)


            currentNode = stack.pop()
            # stack = stack[1:]
        end = time.time()
        conclusion(self.expandedDFS, end - start)
        
        