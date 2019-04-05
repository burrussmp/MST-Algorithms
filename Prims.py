# Matthew P. Burruss
# 4/4/2019
# CS 5250
import math
# adjacency list for graph
class Adjacency_List:
    def __init__(self,vertices,edges):
        self.adj = [[] for i in range(len(vertices))]
        for edge in edges:
            self.adj[edge.u].append((edge.v,edge.weight))
            self.adj[edge.v].append((edge.u,edge.weight))

    def printMe(self):
        node = 0
        for list in self.adj:
            print("%d:" %node,end='')
            node = node + 1
            for edge in list:
                print(" (%d:%0.2f)" % (edge[0],edge[1]),end='')
            print('')

    def adjacentTo(self,u,index):
        # returns neighbor,weight
        return self.adj[u][index][0],self.adj[u][index][1]

    def numberOfNeighborsTo(self,u):
        return len(self.adj[u])

# undirected weighted edge between vertex u and v with specified weight
class Edge:
    def __init__(self,u,v,weight):
        self.u = u
        self.v = v
        self.weight = weight



# the elements of the minheap have a key-value pair
# the elements are sorted by the value and the key corresponds to 
# the vertex #
# the key-value pair represented by a tuple (vertex #, value)
class minHeapPrim():
    # initializes a minHeap where root (first node)
    # has value 0 and rest have value inf
    # Run-time of heapify: O(n)
    def __init__(self,vertices):
        self.list = []
        self.positions = [] # keeps track of vertex location in heap
        self.parents = []
        self.size = len(vertices)
        # list is indexed by vertex # and contains tuple (key value, index in heap)
        for i in range(len(vertices)):
            if (i == 0):
                self.list.append((0,0))
                self.positions.append(0)
                self.parents.append(-1)
            else:
                self.list.append((i,math.inf))
                self.positions.append(i)
                self.parents.append(-1)
        #self.printMe()
        self.totalCost = 0
    def printMe(self):
        for i in range(self.size):
            print("(v="+str(self.list[i][0])+" w=" + str(self.list[i][1])+") ",end='')
        print('')

    def setParent(self,vertex,parent):
        self.parents[vertex] = parent
    # returns smallest vertex-value pair and then restores heap O(lgn)
    def getMinNode(self):
        smallest = self.list[0][0]
        #print mst
        if (self.parents[smallest] != -1):
            print("New MST edge: {%d->%d weight:%d}" %(self.parents[smallest],smallest,self.list[0][1]),end='\n')
            #print("weight: %d" %self.list[0][1],end='')
            #print("arent: %d" %self.parents[smallest])
        #self.printMe()
        self.list[0] = self.list[self.size-1]
        self.positions[smallest] = -1
        self.positions[self.list[0][0]] = 0
        self.size = self.size - 1
        self.minHeapify(0)
        return smallest

    # takes O(logn)
    def minHeapify(self,index):
        # compare to children
        smallest = index
        # compare to children
        if (2*index + 1 < self.size and self.list[smallest][1] > self.list[2*index + 1][1]):
            smallest = 2*index + 1
        if (2*index + 2 < self.size and self.list[smallest][1] > self.list[2*index + 2][1]):
            smallest = 2*index + 2
        # stop if position found
        if (smallest != index):
            # swap elements in heap
            tmp = self.list[index]
            self.list[index] = self.list[smallest]
            self.list[smallest] = tmp
            # swap positions
            othervertex = self.list[smallest][0]
            myvertex = self.list[index][0]
            tmp = self.positions[myvertex]
            self.positions[myvertex] = self.positions[othervertex]
            self.positions[othervertex] = tmp
            # call heapify on smallest again
            self.minHeapify(smallest)

    # takes logn
    def decreaseKeyValue(self,index,vertex):
        positionFound = False
        while (not positionFound):
            # compare to parent
            parentWeight = self.list[int((index-1)/2)][1]
            parentIndex = int((index-1)/2)
            parentVertex = self.list[int((index-1)/2)][0]
            #print(parentIndex)
            mweight = self.list[index][1]
            if (parentWeight > mweight):
                # swap elements in heap
                tmp = self.list[index]
                self.list[index] = self.list[parentIndex]
                self.list[parentIndex] = tmp
                # swap positions
                tmp = self.positions[vertex]
                self.positions[vertex] = self.positions[parentVertex]
                self.positions[parentVertex] = tmp
            else:
                positionFound = True


    # checks if list is empty
    # run-time is O(1)
    def isEmpty(self):
        return self.size == 0

    # returns the weight of an item in the list
    # run-time is O(1)
    def getWeight(self,vertex):
        return self.list[self.positions[vertex]][1]

    def updateHeap(self,vertex,weight):
        index = self.positions[vertex]
        self.list[index] = (vertex,weight)
        # bubble the index up
        self.decreaseKeyValue(index,vertex)
        index = self.positions[vertex]

# takes in an adjacency list and vertices
# steps of algorithm that uses min heap to keep track of smallest distance connecting
# MST to nodes yet to be added to MST
# 1. Create a min heap of |V| with key value assigned
# inf to all nodes except node 0 (keyvalue = 0)
# 2. repeat
# 3.    find min value of node from min heap
# 4.    check all neighbors and see if not in G yet
# 5.    if not in G and weight > min node - itself, update

def prim(Adj,vertices):
    # initialize array for prim
    mstVertices = []
    mstEdges = []
    # initialize array to keep track of what's been added
    addedVertices = [0 for i in range(len(vertices))]
    # create a heap... operation O(n)
    minheap = minHeapPrim(vertices)
    # while heap not empty... O(n)
    while(not minheap.isEmpty()):
        u = minheap.getMinNode() # remove smallest (root) O(1)
        mstVertices.append(u)
        addedVertices[u] = 1
        # update all neighbors of u
        for i in range(Adj.numberOfNeighborsTo(u)): # walk through adjaecnt edges 
            neighbor,weight = Adj.adjacentTo(u,i)
            # if neighbor not in MST and key > weight to MST
            if (addedVertices[neighbor] == 0 and minheap.getWeight(neighbor) > weight): # get weight and check if already added O(1)
                # update weight
                minheap.setParent(neighbor,u) # update parent O(1)
                minheap.updateHeap(neighbor,weight) # update heap O(lgn)
    


if __name__ == '__main__':
    vertices = [0,1,2,3,4]
    edges = []
    edges.append(Edge(0,1,1))
    edges.append(Edge(0,2,3))
    edges.append(Edge(0,4,1))
    edges.append(Edge(1,2,5))
    edges.append(Edge(2,3,1))
    edges.append(Edge(3,4,1))
    edges.append(Edge(2,4,2))
    adj = Adjacency_List(vertices,edges)
    adj.printMe()
    prim(adj,vertices)