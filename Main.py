
# Given a Map with circle/eclipse.
# Find all points that are tangent to the circle.
# Those will be the edges. 
 
import math
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, LineString
import shapely.affinity

from Node import Node
from Person import Person
from A_star import a_star

## Represent graph with adjacency list.

# Each node will have list of nodes that has edges with
# ex. x1 = [ x2, x3 , x4]   ,  x2 = [x1]

def main():
    start = Node(position=[1,1])

    end = Node(position=[80,80])

    kevin = Person(x=30,y=30,velocity=0,direction=0)
    aL = createAdjacencyList_new( nodes =[start,end], people=[kevin])
        
    for i,j in aL.items():
        i.totalWeight += ((abs(end.position[0]-i.position[0])+abs(end.position[1]-i.position[1]))*0.001)
    
    listOfPath = a_star( start, end ,aL)
    
    x_values = []
    y_values = []
    
    for i in range(0,len(listOfPath)-1):
        plt.plot( [(listOfPath[i])[0],(listOfPath[i+1])[0]],[(listOfPath[i])[1],(listOfPath[i+1])[1]],'k-')


    # x_values = []
    # y_values = []
    for x,y in aL.items():
        x_values.append(x.position[0])
        y_values.append(x.position[1])
        
    #     for p in y:
    #         plt.plot([x.position[0],p.position[0]],[x.position[1],p.position[1]],'k-')
    #         x_values.append(p.position[0])
    #         y_values.append(p.position[1])

    plt.scatter(x_values, y_values, s=5)
    plt.show()    
    
def createAdjacencyList_new(nodes, people):
    listOfShape = []
    
    for p in people : 
        nodes.extend(p.getKeyNodes())
        p.makeSocialZone()
        for circle in p.listOfCicle:
            listOfShape.append(circle)
            for node in circle:
                nodes.append(node)
    
    # for o in obstacles:
    #     listOfShape.append(obstacles.makeSocialZone)
        
    adjacencyList = {}
    for i in nodes:
        adjacencyList[i] = []
        for j in nodes :
            if ( checkValidPath(i, j , listOfShape) and i!=j):
                adjacencyList[i].append(j)
    
    return adjacencyList

# x,y are both node
def checkValidPath(x, y ,obstacles):
    doesNotCross = True
    for obstacle in obstacles:
        
        for i in range(0,len(obstacle)-1):
            if (checkIntersect(x,y,obstacle[i],obstacle[i+1])):
                return False

    return True
     

# Line 1 = x1 to y1
# Line 2 = x2 to y2
def checkIntersect ( x1, y1, x2, y2):

    line1 = LineString([(x1.position[0],x1.position[1]),(y1.position[0],y1.position[1])])
    line2 = LineString([(x2.position[0],x2.position[1]),(y2.position[0],y2.position[1])])
    return (line1.intersects(line2))

        
if __name__ == "__main__":
    main()


