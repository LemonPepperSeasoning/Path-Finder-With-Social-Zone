
import math
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, LineString
import shapely.affinity

from Node import Node
from Person import Person
from A_star import a_star

import timeit

def main():
    with open('test.txt','w') as file:
            file.write("==================\n")
            
    start = Node(position=[-20,30])

    end = Node(position=[80,80])

    kevin = Person(x=30,y=50,velocity=0,direction=0)
    
    adjacencyList, listOfShape = createAdjacencyList_new( nodes =[start,end], people=[kevin])
             
    for i,j in adjacencyList.items():
        i.cost += ( (end.position[0]-i.position[0])**2+(end.position[1]-i.position[1])**2) *0.001
    
    listOfPath = a_star( start, end ,adjacencyList, listOfShape)
    
    x_values = []
    y_values = []
    
    for i in range(0,len(listOfPath)-1):
        plt.plot( [(listOfPath[i])[0],(listOfPath[i+1])[0]],[(listOfPath[i])[1],(listOfPath[i+1])[1]],'k-')


    # x_values = []
    # y_values = []
    for x,y in adjacencyList.items():
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
            if ( i!=j ):
                adjacencyList[i].append(j)
    
    return adjacencyList, listOfShape

# checkValidPath(i, j , listOfShape)

if __name__ == "__main__":

    startTime = timeit.default_timer()

    main()
    
    stop = timeit.default_timer()
    print('Time: ', stop - startTime)  


