
class Stack:
    def __init__(self):
        self.list = []
        
    def push(self, node):
        #Currently this is normal forloop. 
        #Its fine for small list but for scalability, might be better to do binary search to find insertion index.
        for i in range(0,len(self.list)):
            if ( node.totalWeight < self.list[i].totalWeight ):
                self.list.insert(i,node)
                return
        self.list.append(node)
            
    def pop(self):
        return self.list.pop(0)
        
    def print(self):
        with open('test.txt','a') as file:
            file.write("==================\n")
            for i in self.list:
                file.write("__pos : {}, weight : {} ".format(i.position,i.totalWeight))
            file.write("\n")
