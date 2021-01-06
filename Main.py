
import math
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, LineString
import shapely.affinity

from Node import Node
from Person import Person
from A_star import a_star

from time import time

from CalculateWeight import calculateWeight
from A_star import checkValidPath
"""

python3 -m cProfile -s cumtime main.py 

"""

def timer(func):
    def f():
        startTime =time()
        func()
        stop = time()
        print ("Time elapsed : ", stop - startTime)
    return f

@timer
def main():
    with open('test.txt','w') as file:
        file.write("==================\n")
        
    start = Node(position=[0,27])

    end = Node(position=[150,150])

    kevin = Person(x=30,y=50,velocity=0,direction=0)
    john = Person(x=10,y=90,velocity=0,direction=0)
    sam = Person(x=80,y=20,velocity=0,direction=0)
    mike = Person(x=10,y=-20,velocity=0,direction=0)
    
    adjacencyList, listOfShape = createAdjacencyList_new( nodes =[start,end], people=[kevin,john,sam,mike])
             
    for i,j in adjacencyList.items():
        i.cost += calculateWeight(end,i)
    
    # plotAllPath(adjacencyList, listOfShape)
    

    listOfPath = a_star( start, end ,adjacencyList, listOfShape)
    # plot(listOfPath,adjacencyList)
      
def plotAllPath(adjacencyList, listOfShape):
    x_values = []
    y_values = []
    
    for x,j in adjacencyList.items():
        x_values.append(x.position[0])
        y_values.append(x.position[1])
        
        for y in j:
            if (checkValidPath(x,y,listOfShape)):
                plt.plot( [ x.position[0],y.position[0] ],[ x.position[1],y.position[1] ],'k-')
    
    plt.scatter(x_values, y_values, s=2)

    plt.show()
    
   
def plot(listOfPath,adjacencyList):
    x_values = []
    y_values = []
    
    for i in range(0,len(listOfPath)-1):
        plt.plot( [(listOfPath[i])[0],(listOfPath[i+1])[0]],[(listOfPath[i])[1],(listOfPath[i+1])[1]],'k-')
        
    for x,y in adjacencyList.items():
        x_values.append(x.position[0])
        y_values.append(x.position[1])
        
    # for p in y:
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
    main()
    


