# MST-Algorithms
Python implementation of Prim's, Kruskal's, and Sollin's algorithm
# Analysis of Prim's Algorithm Running Time
## Psuedo Code
Given a graph G with vertices V and undirected, weighted edges E

Create a min-heap of size |V| with key values assigned to infinity except for root assigned 0 O(|V|)

Repeat:
   <p>Select vertex u with minimum key from min heap O(1)</p>
    
   <p>Check neighbors of vertex u to see if not in tree</p>
    
   <p>if neighbor not in T, update key value if key > weight(u,neighbor)</p>
    
## Big-O Notation
Prim's algorithm was coded using a binary heap. The algorithm selects the smallest node based on key values which represent the edges connecting the MST to the graph G so long as there are vertices remaining to be added to the MST. It then looks at its neighbors which requires |E| looks for each vertex. The heapify() function and decreaseKeyFunction run in log(|V|) and are required to maintain the heap. Therefore, the outer-loop requires adding each vertex |V| and looking at each vertex neighbor |E| and performing log(V) operations. Therefore, the total run-time is O(|V+E|log(V)). If E > V, then this simplifies to O(ELogV).
# Analysis of Kruskal's Algorithm Running Time
## Psuedo Code
Given a graph G with vertices V and undirected, weighted edges E

Sort edges in increasing order O(ElogE)

Repeat for each edge in sorted list: O(|E|)

   For each vertex in edge (u,v) perform find() operations to see if vertex u and vertex v are in different sets O(log(|V|))
    
   If vertex u is in a different set than vertex v: union(u,v) O(1)
   
## Big-O Notation
Kruskal's algorithm uses a union and find operation to maintain the sets. The union/find operation is based on a tree structure to achieve O(1) union by making the rank of the larger tree (based on rank or height) the child of the smaller tree and then setting ranks in O(1) for each root. The find() operation takes log(|V|) time. This is because each tree has height h which is less than or equal to log(|V|) if |V| is the number of nodes in the tree. We can improve this for a large graph where several find() operations will be needed by using tree compression. Thus, the running time is ELogE+ELogV where ElogE is the running time for merge-sort on the array of edges.
Improvements can be acheived by maintaining a list of vertices along a path to the root during a find() and then re-assigning their parents directly to the root node. In detailed analysis, this can be found to run in time proportional to the inverse Ackermann function or alpha(|V|); therefore, the running time would be ElogE+Ealpha(n)
# Analysis of Sollin's Algorithm Running Time
## Psuedo Code
Given a grpah G with vertices V and undirected, weighted edges E

Initialize a forest of components of size |V| where each tree's root is a vertex in G O(V)

Repeat while number of components > 1

    Initialize an array to indicate cheapest edge leaving each
    
    component to infinity: around log(V)
    
    Repeat for each edge in G: O(E)
    
        If vertices u and v in edge (u,v) are in different components
        
            If w(u,v) < cheapest edge in component of u
            
                Set cheapest edge in component of u to w(u,v)
                
            If w(u,v) < cheapest edge in component of v
            
                Set cheapest edge in component of v to w(u,v)
                
    Repeat for each component: at most O(V)
    
        If cheapest edge not infinity, add edge to MST
        

Further details
To maintain the components, the union and find operations are used. The union operation runs in O(1) and the find runs in O(logV) or O(alpha(n)) when tree compression is used.
## Big-O Notation
Sollin's algorithm above is about combining components until there is one component and the MST has formed. The big-O notation is the same as Prim and Kruskal's and runs in approximately ELogV although tree compression can imporve performance..
Big-O = V+E(logV)+E(logV) which simplifies to ELogV
