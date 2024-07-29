class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        thought:
        - the `center of a star graph` must be a vertex that is connected to all other vertices.
        - this means it will appear in all combinations of `edges`.
        - since in a `star graph`, all vertices except the center vertex will only appear once, the vertex that appears more than once is the `center of the star graph`.
        - therefore, we can follow these steps:
            (1) extract the first two edges from the `edges`.
            (2) determine which vertex appears more than once and return that vertex.
        """
        edge_1_2 = edges[0] + edges[1]
        for vertex in set(edge_1_2):
            if edge_1_2.count(vertex) > 1:
                return vertex
