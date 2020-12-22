
class Edge:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.weight = self.caculateWeight(start,end)
        
    def caculateWeight(self,x,y):
        weight = ( (x.position[0]-y.position[0])**2+(x.position[1]- y.position[1])**2)*0.001
        return weight+x.totalWeight+y.cost
    
        
    
    
        