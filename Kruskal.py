# Matthew P. Burruss
# 4/11/2019
# CS 5250

import math

# Adjacency list class for graphs with weighted, undirected edges
class Adjacency_List:
    # initialize a simple adjacency list.
    # Requires vertices are known at init
    def __init__(self,vertices,edges):
        self.adj = [[] for i in range(len(vertices))]
        self.vertices = vertices
        self.edges = edges
        for edge in edges:
            self.adj[edge.u].append((edge.v,edge.weight))
            self.adj[edge.v].append((edge.u,edge.weight))
    # add an edge to the adjacency list
    def addEdge(self,edge):
        self.edges.append(edge)
        self.adj[edge.u].append((edge.v,edge.weight))
        self.adj[edge.v].append((edge.u,edge.weight))
    # print adjacency list and associated edges
    def printMe(self):
        node = 0
        for list in self.adj:
            print("%d:" %node,end='')
            node = node + 1
            for edge in list:
                print(" (%d:%0.2f)" % (edge[0],edge[1]),end='')
            print('')
    # return a specified neighbor of vertex u and that edge's weight
    def adjacentTo(self,u,index):
        # returns neighbor,weight
        return self.adj[u][index][0],self.adj[u][index][1]
    # return the number of neighbors vertex u
    def numberOfNeighborsTo(self,u):
        return len(self.adj[u])
    #get number of vertices
    def getNumberOfVertices(self):
        return len(self.vertices)
    # get array representation of all edges and vertices
    def getEdges(self):
        return self.edges
    def getVertices(self):
        return self.vertices

# undirected weighted edge between vertex u and v with specified weight
class Edge:
    def __init__(self,u,v,weight):
        self.u = u
        self.v = v
        self.weight = weight
    def printMe(self):
        print("edge:(" + str(self.u) + "--" + str(self.v) + ") with weight " + str(self.weight))
    

class UnionFind:
    # init
    # create |vertices| trees each with a single item and size 1
    def __init__(self,numVertices):
        # initialize n trees
        self.trees = []
        for i in range(numVertices):
            self.trees.append(Node(i,None))
    # find() operation takes O(logn) time
    # given a node i, follow it to its root and return root
    # implement tree compression
    def find(self,i):
        return self.trees[i].getRoot()
    # union() operation takes O(1) time
    # if size of setX < size of setY, make y point to x
    # keep track of rank or height
    def union(self,rootX,rootY,edge,MST):
        MST.addEdge(edge)
        if (rootX.rank <= rootY.rank):
            rootY.makeChildOf(rootX)
            rootY.rank = rootY.rank+1
        else:
            rootX.makeChildOf(rootY)
            rootX.rank = rootX.rank+1

class Node:
    def __init__(self,vertex,parent):
        self.vertex = vertex # vertex of node
        self.parent = parent # parent of node
        if (parent == None):
            self.rank = 1   # if root, set level of node to 1
        else:
            self.rank = self.parent.rank + 1 # if not root, set level to parent level + 1
    def getRoot(self):
        if (self.parent == None): # we are root, return self
            return self
        else:
            root = self.parent.getRoot() # climb up tree to find root node
            return root
    def printMeUpToParent(self):
        if (self.parent == None):
            return
        else:
            print(str(self.vertex)+ "--",end='')
            self.parent.printMeUpToParent()
    def makeChildOf(self,parent):
        self.parent = parent

# takes an array of Edge objects and returns sorted version
# runs in mlogn
def mergeSort(edges,low,high):
    if (low < high):
        middle = low+(high-low)/2
        mergeSort(edges,int(low),int(middle))
        mergeSort(edges,int(middle+1),int(high))
        merge(edges,int(low),int(middle),int(high))
def merge(edges,low,middle,high):
    left = middle - low + 1
    right = high - middle
    # create tmp arrays
    left_array = []
    right_array = []
    for i in range(left):
        left_array.append(edges[low+i])
    for j in range(right):
        right_array.append(edges[middle+1+j])
    i = j = 0
    k = low
    while(i < left and j < right):
        if (left_array[i].weight <= right_array[j].weight):
            edges[k] = left_array[i]
            i = i +1
        else:
            edges[k] = right_array[j]
            j = j +1
        k = k +1
    # copy remaining
    while(i < left):
        edges[k] = left_array[i]
        i = i +1
        k = k +1
    while(j < right):
        edges[k] = right_array[j]
        j = j +1
        k = k +1

# takes in an adjacency list and vertices
# Psuedo
# Sort edges increasing: O(mlogn) 
# Repeat until all vertices added to MST
#   select next smallest edge O(1)
#   see if vertex u and vertex v on different components (find(u) != find(v)): 2m times of logn
#       combine sets: union(u,v): n-1 unions of O(1) time
# Total running time
# mlogn + 2mlogn + n ~= mlogn
def Kruskal(Adj):
    # initialize array for prim
    MST = Adjacency_List(vertices,[])
    # initialize union find
    UF = UnionFind(Adj.getNumberOfVertices())
    # initialize array to keep track of what's been added
    # sort edges of input
    edges = Adj.getEdges()
    mergeSort(edges,0,len(edges)-1) # takes mlogn
    for edge in edges:
        #edge.printMe()
        setX = UF.find(edge.u)
        setY = UF.find(edge.v)
        if (setX.vertex != setY.vertex):
            UF.union(setX,setY,edge,MST)
    return MST


if __name__ == '__main__':
    """
    #input 1
    vertices = [0,1,2,3,4]
    edges = []
    edges.append(Edge(0,1,1))
    edges.append(Edge(0,2,3))
    edges.append(Edge(0,4,1))
    edges.append(Edge(1,2,5))
    edges.append(Edge(2,3,1))
    edges.append(Edge(3,4,1))
    edges.append(Edge(2,4,2))
    """
    #input 2
    vertices = [0,1,2,3,4,5,6,7,8,9]
    edges = []
    edges.append(Edge(0,1,5))
    edges.append(Edge(1,2,1))
    edges.append(Edge(2,3,5))
    edges.append(Edge(3,4,1))
    edges.append(Edge(4,5,1))
    edges.append(Edge(5,9,3))
    edges.append(Edge(8,9,8))
    edges.append(Edge(7,8,1))
    edges.append(Edge(7,9,3))
    edges.append(Edge(6,7,7))
    edges.append(Edge(0,6,1))
    edges.append(Edge(2,6,2))
    edges.append(Edge(6,5,20))
    
    adj = Adjacency_List(vertices,edges)
    print("##########################")
    print("Original Adjacency list")
    print("##########################")
    adj.printMe()
    MST = Kruskal(adj)
    # print MST
    print("##########################")
    print("MST: Kruskal Algorithm")
    print("##########################")
    MST.printMe()