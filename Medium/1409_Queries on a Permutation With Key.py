class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        """
        Thought:
        - Goal: Process a list of queries on a dynamic permutation P = [1, 2, ..., m] by finding the 0-indexed position of each query value and moving that value to the front of P. Return the positions for all queries.
        - Idea: Simulate the "Move-to-Front" operation directly using a list to represent P. For each query value, locate its index in P, append the index to the result, and update P by removing the element from its current position and inserting it at the front (index 0).
        - Steps:
            1. Initialize array `P` with numbers from 1 to `m`.
            2. Iterate through each value `q` in `queries`:
                a. Find the current 0-based index of `q` in `P`.
                b. Append this index to the `output` array.
                c. Remove `q` from `P` and insert `q` at the beginning of `P` (index 0).
            3. Return the `output` array.
        - Time Complexity: O(N * M), where N is the length of `queries` and M is `m`. For each of the N queries, linear search (`index`) and list modifications (`pop`/`insert`) take O(M) time.
        - Space Complexity: O(N + M) auxiliary space for storing the permutation `P` of size `m` and the output array of size N.
        """
        output = []
        positions = [i+1 for i in range(m)]

        for q in queries:
            i = positions.index(q)
            output.append(i)
            positions.pop(i)
            positions.insert(0, q)

        return output
