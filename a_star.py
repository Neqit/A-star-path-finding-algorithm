# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:07:50 2020

@author: Nichita Vatamaniuc
"""

# Node class with g,h and f costs also includes parrent node for backtracking and current position
# __eq__ method is standart python method for equality overload
class Node():
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos
        
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.pos == other.pos


#function for getting distance between 2 nodes (euclidean metric)
def getDistance(nodeA, nodeB):
    distX = abs(nodeA.pos[1] - nodeB.pos[1])
    distY = abs(nodeA.pos[0] - nodeB.pos[0])
    
    if distX > distY:
        return 14*distY + 10 * (distX - distY)
    else:
        return 14*distX + 10 * (distY - distX)


def Astar_alg(observed_map, start, end):
    start_node = Node(None, start)
    start_node.g = 0
    start_node.h = 0
    start_node.f = start_node.g + start_node.h
    
    end_node = Node(None, end)
    end_node.g = 0
    end_node.h = 0
    end_node.f = end_node.g + end_node.h
    
    yet_to_explore = []
    explored = []
    
    yet_to_explore.append(start_node)
    
    while len(yet_to_explore) > 0:
        
        current_node = yet_to_explore[0]
        current_index = 0
        for index, node in enumerate(yet_to_explore):
            if node.f < current_node.f or node.f == current_node.f and node.h < current_node.h:
                current_node = node
                current_index = index
                
        
        #print(current_node.pos)
        yet_to_explore.pop(current_index)
        explored.append(current_node)
        
        
        if current_node == end_node:
            path = []
            current_copy = current_node
            while current_copy is not None:
                path.append(current_copy.pos)
                current_copy = current_copy.parent
            return path[::-1]


        neighbours = []
        for new_pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            neighbour_node_pos = (current_node.pos[0] + new_pos[0], current_node.pos[1] + new_pos[1])
            
            if neighbour_node_pos[0] > (len(observed_map) - 1) or neighbour_node_pos[0] < 0 or neighbour_node_pos[1] < 0 or neighbour_node_pos[1] > (len(observed_map[0])-1):
                continue
            
            if observed_map[neighbour_node_pos[0]][neighbour_node_pos[1]] != 0:
                continue
            
            new_neighbour_node = Node(current_node, neighbour_node_pos)
            
            if new_neighbour_node in explored:
                continue
            
            neighbours.append(new_neighbour_node)
            
            
        for neighbour_node in neighbours:
            new_movement_cost_to_neighbour = current_node.g + getDistance(current_node, neighbour_node)
            if new_movement_cost_to_neighbour < neighbour_node.g or not neighbour_node in yet_to_explore:
                neighbour_node.g = new_movement_cost_to_neighbour
                
                distX = abs(neighbour_node.pos[1] - end_node.pos[1])
                distY = abs(neighbour_node.pos[0] - end_node.pos[0])
                neighbour_node.h = min(distX,distY)*14 + max(distX,distY)*10
                neighbour_node.f = neighbour_node.g + neighbour_node.h
                
                if(not neighbour_node in yet_to_explore):
                    yet_to_explore.append(neighbour_node)


def main():
    
    search = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    start = (0,0)
    end = (6,5)
    
    path = Astar_alg(search, start, end)
    print(path)
    
    
if __name__ == '__main__':
    main()