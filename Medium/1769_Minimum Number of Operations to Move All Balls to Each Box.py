class Solution:
    def calculateMovements(self, boxes: str, i: int) -> int:
        moves = [abs(index-i) for index, char in enumerate(boxes) if char == '1']
        return sum(moves)

    def minOperations(self, boxes: str) -> List[int]:
        """ 
        Thought:
        - Goal:  
            Return an array of size `n`, where the i-th element represents the minimum number of operations needed to move all balls to the i-th box.
        - Problem Description:  
            - Boxes: A binary string where the i-th character is '0' if the box is empty, and '1' if it contains a ball.  
            - Operation: In one operation, a ball can be moved from one box to an adjacent box.  
        - Idea:  
            - Divide the goal into sub-goals:  
                - Calculate the minimum number of operations required for each box (`i-th` box).  
            - Since each operation moves one ball one step, the problem reduces to calculating the total distance between the i-th box and all boxes containing balls.  
        - Steps:  
            1. Initialize an empty list, `answers`, to store the results.  
            2. Define a function to calculate the minimum operations for the i-th box:  
                - Identify all indices where the value in `boxes` is '1'.  
                - Compute the absolute difference between each index and the index of the i-th box.  
                - Sum these differences to determine the total number of operations for the i-th box.  
            3. Use a loop to iterate through all boxes and call the function from Step 2 for each box.  
        """
        answers: List[int] = []
        
        for i in range(len(boxes)):
            total_moves = self.calculateMovements(boxes, i)
            answers.append(total_moves)

        return answers
