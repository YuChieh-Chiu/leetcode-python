class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """
        Thought:
        - Goal: Calculate the final value of X after performing all operations (X starts at 0).
        - Definition of string operations:
            - ++X and X++ increment the value of X by 1
            - --X and X-- decrement the value of X by 1
        - Idea: Use a dictionary to map each operation to its value change.
        - Steps:
            1. Create a dictionary mapping each operation to its value change (+1 or -1).
            2. Initialize `final_value` to 0 to represent X.
            3. Iterate through `operations` and accumulate the value changes.
            4. Return `final_value`.
        - Time Complexity: O(n), where n is the length of operations.
        - Space Complexity: O(1), using a fixed-size dictionary.
        """
        op_val_mapping = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1
        }

        final_value = 0

        for op in operations:
            final_value += op_val_mapping.get(op)

        return final_value
