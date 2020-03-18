"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("We can't create an edge based on this given vertex")


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue
        qq = Queue()
        # create list of visited nodes
        visited = set()
        # put starting node is the queue
        qq.enqueue(starting_vertex)
        # while queue not empty
        while qq.size() > 0:
        # pop first node out of queue
            vertex = qq.dequeue()
        # if not visited
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
        # Mark as visited
        # Get adjacent edges and add to list
                for next_vert in self.vertices[vertex]:
                    qq.enqueue(next_vert)
        # Go to top of loop
        


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack
        st = Stack()
        # create list of visited nodes
        visited = set()
        # put starting node in the stack
        st.push(starting_vertex)
        # while queue not empty
        while st.size() > 0:
        # pop first node out of stack
            vertex = st.pop()
        # if not visited
            if vertex not in visited:
                visited.add(vertex)
                print(vertex) 
                for next_vert in self.vertices[vertex]:
                    st.push(next_vert) 

    def dft_recursive(self, start_vert, visited=None):
        # if the visited structure is set to None
        if visited is None:
            # create a new set for visited
            visited = set()
        # add a starting vertex to the visited set
        visited.add(start_vert)
        # print the start vertex
        print(start_vert)
        # loop over every child vertex in vertices set at the start vertex
        for child_vert in self.vertices[start_vert]:
            # if child vertex is not in visited
            if child_vert not in visited:            
                # do a recursive call to dft_recursive
                # using the child vertex and the current visited set as arguments
                self.dft_recursive(child_vert, visited)
            

    def bfs(self, starting_vertex_id, target_value):
        # create a queue to hold the vertex ids
        q = Queue()
        # enqueue the start vertex id
        q.enqueue(starting_vertex_id)
        # create an empty visited set
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # set vert to the dequeued element
            vertex = q.dequeue()
            # if the vert is not in visited
            if vertex not in visited:
                # if vert is target value
                if vertex == target_value:
                    # return True
                    return True
                # add the vert to visited set
                visited.add(vertex)
                # loop over next vert in the vertices at the index of vert
                for next_vert in self.vertices[vertex]:
                    # enqueue the next vert
                    q.enqueue(next_vert)
        # return False
        return False

        def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack and push the starting vertex ID
        s = Stack()
        s.push([starting_vertex])
        # create a set to store the visited vertices
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            path = s.pop()
            v = path[-1]
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited (printing for a representation)
                if v == destination_vertex:
                  return path
                visited.add(v)
                # then add all of it's neighbors to the top of the stack
                for next_vertex in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
            if visited is None:
                visited = set()
            if path is None:
                path = []
            visited.add(starting_vertex)
            path = path + [starting_vertex]
            if starting_vertex == destination_vertex:
                return path
            for adj_vert in self.vertices[starting_vertex]:
                if adj_vert not in visited:
                    new_path = self.dfs_recursive(
                        adj_vert, destination_vertex, visited, path)
                    if new_path:
                        return new_path
            return None

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        # """
        # if visited is None
        if visited is None:
            # create a new set of visited
            visited = set()
        # add start vert to visited
        visited.add(starting_vertex)
        # if the start vert is equal to the target value
        if starting_vertex == self.dfs_recursive(starting_vertex):
            # return True
            return True
        # loop over every child vertex in vertices set at the start vertex
        for child_vert in self.vertices[starting_vertex]:
            # if child vert is not in visited
            if child_vert not in visited:
                # if the recursive call to dfs
                if self.dfs(self, child_vert):
                    # return True
                    return True
        # Return False
        return False

        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('starting BFT')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('starting DFT')
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
