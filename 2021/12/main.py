from collections import defaultdict


class Graph(object):

    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.max_visits = 2
        self.paths = []

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] += 1
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path)
            self.paths.append(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if (visited[i] < self.max_visits or i.isupper()):
                    if i.islower() and visited[i]==(self.max_visits-1):
                        self.max_visits = 1

                    self.printAllPathsUtil(i, d, visited, path)
                    
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= 0

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

        def def_val():
            return 0
        # Mark all the vertices as not visited
        visited = defaultdict(def_val)

        # Create an array to store paths
        self.paths.clear()
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)

inputs = [x.split('-') for x in open('inputs_test.txt').read().split('\n')]

# Create a graph given in the above diagram
g = Graph()
for x in inputs:
    #if x[0] != "end" and x[1] != "start":
    g.addEdge(x[0], x[1])
    #if x[1] != "end" and x[0] != "start":
    g.addEdge(x[1], x[0])

# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(0, 3)
# g.addEdge(2, 0)
# g.addEdge(2, 1)
# g.addEdge(1, 3)ss

s = "start" ; d = "end"
g.printAllPaths(s, d)
print(len(g.paths))
# This code is contributed by Neelam Yadav
