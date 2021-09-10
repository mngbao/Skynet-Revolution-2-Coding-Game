import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def delEdge(self,u,v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
def output (node1, node2):
    print(node1,node2)
    g.delEdge(node1,node2)

def Compare(g,node,):
    return

def checkOutput (g,ap,dist_closest,gw_count):
    if gw_count[ap] == 1:
        node1 = 0
        for i in g.graph[ap]:
            if i in gw: 
                node1 = i
                break
        output(node1,ap)
    
    else:
        min = 99999
        node1 = 0
        node2 = 0
        for i in gw:
            if dist_closest[i]<min:
                min = dist_closest[i]
                node1 = i
        dist_closest_test = [999999] * n
        gw_count_test = [0] * n
        getDistance(g,node1,dist_closest_test,gw_count_test)
        multiGateNodeDist =[]                    
        for i in range(len(gw_count)):
            if gw_count[i] >= 2:
                multiGateNodeDist.append(i)
        if (min >= 2) and (max(gw_count) == 2):
            node1 = 0 
            if len(multiGateNodeDist) > 1: 
                temp = 999999    
                for i in range(len(dist_closest)):
                    if i in multiGateNodeDist:
                        if (dist_closest[i] >= dist_closest_test[i]):
                            if dist_closest[i] < temp:
                                temp = dist_closest_test[i]
                                node1 = i
            else:
                node1 = gw_count.index(max(gw_count))
            node2 = 0
            for i in g.graph[node1]:
                if i in gw:
                    node2 = i
            output(node1,node2)
        else:
            min = 99999
            for i in g.graph[node1]:
                if dist_closest[i] < min:
                    min = dist_closest[i]
                    node2 = i
                elif dist_closest[i] == min:
                    if gw_count[i] > gw_count[node2]:
                        node2 = i
            output(node1,node2)    

def getDistance(g,ap,dist_closest,gw_count):
    queue = []
    visited = []
    
    queue.append(ap)
    visited.append(ap)
    dist_closest[ap] = 0
    while queue:
        cur_node = queue.pop(0)
        
        for i in g.graph[cur_node]:
            
            if i not in visited:
                dist = dist_closest[cur_node]+1
                if (dist < dist_closest[i]):
                    dist_closest[i] = dist
                queue.append(i)
                visited.append(i)
            if i in gw:
                gw_count[cur_node] += 1
                    
                
    dist_closest[ap] = 99
    for i in gw:
        gw_count[i]=-1
        
g = Graph()
gw = []

n, l, e = [int(i) for i in input().split()]


for i in range(l): 
    n1, n2 = [int(j) for j in input().split()]
    g.addEdge(n1,n2)


for i in range(e):
    gw.append(int(input()))


        
# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    dist_closest = [999999] * n
    gw_count = [0] * n
    getDistance(g,si,dist_closest,gw_count)  
    checkOutput(g,si,dist_closest,gw_count)
    # Write an action using prin
    # Example: 3 4 are the indices of the nodes you wish to sever the link between
    
