from Stack import Stack
from shapely.geometry import Point, Polygon, LineString

def a_star(start, goal, adjacencyList, listOfObstacle):
    visted = []
    
    notVisted = []
    for key,value in adjacencyList.items():
        notVisted.append(key)
            
    stack = Stack()
    
    #This represents the node that was last visted.
    start.totalWeight = 0
    justVisted = start
    
    foundGoal = False
    while (not foundGoal):
        # print (justVisted.position)
        if (justVisted == goal):
            foundGoal = True
            return returnPath(justVisted)
                 
        for i in adjacencyList[justVisted]:
            #check to see if the node is already in stack.
            # if yes update
            # if no push to stack with new weights.
            if ( i in visted ):
                continue
            if not (i in adjacencyList):
                continue
            
            if ( i in stack.list ):
                i.updateWeight(justVisted)
            elif (checkValidPath(i,justVisted,listOfObstacle)):
                i.parent = justVisted
                i.totalWeight = i.cost + justVisted.totalWeight
                stack.push(i)
        
        parent = justVisted
        visted.append(justVisted)
        
        justVisted = stack.pop()
        
        while not checkValidPath(parent,justVisted,listOfObstacle):
            justVisted = stack.pop()
        # print ("{}, {}  : {}".format(justVisted.position,parent.position, checkValidPath(parent,justVisted,listOfObstacle)) ) 
        
        # UNCOMMEND THIS LINE IF YOU JUST WANT TO SEE THE PATH
        # Having this next line will show the explored node.
        
        # justVisted.parent = parent

def returnPath(node):
    path = []
    current = node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path

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


def checkIntersect_V2 ( x1, y1, x2, y2):
    
    # y = a x + b
    
    a1 = (x1.position[0] - y1.position[0]) / (x1.position[1] - y1.position[1])
    b1 = x1.position[1] - a1 * x1.position[0]
    
    a2 = (x2.position[0] - y2.position[0]) / (x2.position[1] - y2.position[1])
    b2 = x2.position[1] - a2 * x2.position[0]
    
    if (a1 == a2):
        #Its parrarell
        return False
    
