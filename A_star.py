from Stack import Stack

def a_star(start, goal, adjacencyList):
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
            print(len(visted))
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
            else:
                i.parent = justVisted
                i.totalWeight = i.cost + justVisted.totalWeight
                stack.push(i)
                    
        parent = justVisted
        visted.append(justVisted)
        justVisted = stack.pop()
        
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
