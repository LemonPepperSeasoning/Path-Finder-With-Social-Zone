
class Node:
    def __init__(self, parent=None, position=None, nodeCost=0):
        self.parent = parent
        self.position = position
        
        #Current weight in the stack, could be fine setting it to be infinity at the begging
        self.totalWeight = 100000.0

        #The cost of the node itself
        self.cost = nodeCost

    def __hash__(self):
        return hash((self.position[0],self.position[1]))
    
    def updateWeight(self, parent):
        # When this is called, we also need to update the stack. 
        # (update the order.)
        if ( parent.totalWeight + self.cost < self.totalWeight ):
            self.parent = parent
            self.totalWeight = parent.totalWeight +self.cost