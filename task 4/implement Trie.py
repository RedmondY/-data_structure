class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        
 
class ChainHash:
    def __init__(self,capacity):
         self.capacity=capacity
         self.table=[None]*capacity
    def buildHash(self,lista):
        for i in range(len(lista)):
            value=int(lista[i])
            key=value % 13
            print(key)
            node_=self.table[key]
        
            if node_ is None:
                self.table[key]=Node(key,value)
            else:
                while node_.next is not None:
                    if node_.key == key:
                        node_.value = value
                        return
                    node_ = node_.next
                node_.next = Node(key, value)
        
    
        
    def InsertHash(self,value):
        key=value % 13
        node_=self.table[key]
        if node_ is None:
            self.table[key]=Node(key,value)
        else:
            while node_.next is not None:
                if node_.key == key:
                    node_.value = value
                    return
                node_ = node_.next
            node_.next = Node(key, value)
            
    def SearchHash(self,key,value):
        node_ = self.table[key]
        while node_ is not None:
            if node_.value == value:
                return node_ # 返回该指针位置
            node_ = node_.next
        return None    # 若没有找到该数值，则返回空

if __name__ == '__main__':
    s=ChainHash(20)
    lista=[1,6,11,14,19]
    
    # In[]
    s.buildHash(lista)
        # In[]
    s.InsertHash(27)
#    print(s.table)
     # In[]
    print(s.SearchHash(1,17))
