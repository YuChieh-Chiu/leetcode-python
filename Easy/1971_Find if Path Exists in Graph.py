class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        thought:
        - the description defines a `REAL GRAPH` with the following properties:
            - bi-directional, meaning it's an UNDIRECTED graph
            - every vertex pair is connected by at most one edge, making it a REAL graph
                # no duplicate edges
                # no self-loops
        - our goal is to determine if there is a valid path from vertex `source` to vertex `destination`
            - Note that the length of `edges` may be ZERO
        - we can use BFS or DFS algorithms to traverse the GRAPH
        - the steps are as follows:
            (1) check if the length of edges is ZERO
            (2) store vertices in an adjacency list
                # use an adjacency list instead of an adjacency matrix because the former can be traversed faster
            -------------------
            [ BFS version - queue x loop ]
            (3) use a queue data structure (FIFO) to store vertices in order
            (4) use a loop to traverse through the graph and find the route from `source` to the end vertex
            [ DFS version - stack x loop ]
            (3) use a stack data structure (LIFO) to store vertices in order
            (4) use a loop to traverse through the graph and find the route from `source` to the end vertex
            -------------------
            (5) check if the destination is in the route and return a boolean value
        """
        # check length
        if edges == []:
            if source == destination:
                return True
            else:
                return False
        # adjacency list store graph
        adjacency_list = {}
        for edge in edges:
            vertex1, vertex2 = edge[0], edge[1]
            if vertex1 in adjacency_list:
                adjacency_list[vertex1].append(vertex2)
            else:
                adjacency_list[vertex1] = [vertex2]
            if vertex2 in adjacency_list:
                adjacency_list[vertex2].append(vertex1)
            else:
                adjacency_list[vertex2] = [vertex1]
        # # BFS
        # queue = [source]
        # visited = {source:True} # to record those vertex already visited
        # route = []
        # while len(queue) > 0:
        #     current = queue.pop(0)
        #     route.append(current)
        #     for neighbor in adjacency_list[current]:
        #         if neighbor not in visited:
        #             queue.append(neighbor)
        #             visited[neighbor] = True
        # DFS
        stack = [source]
        visited = {source:True} # to record those vertex already visited
        route = []
        while len(stack) > 0:
            current = stack.pop()
            route.append(current)
            for neighbor in adjacency_list[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited[neighbor] = True
        # check whether destination in route or not and return boolean value 
        if destination in route:
            return True
        else:
            return False
