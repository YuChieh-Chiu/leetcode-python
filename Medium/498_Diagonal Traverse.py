class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        Thought:
        - Goal: Return an array of all the elements of the matrix in diagonal order.
        - Idea: Use direction tracking ('up'/'down') with explicit boundary collision handling.
               When hitting edges, move to next position and flip direction, with coordinate correction for overshoots.
        - Steps:
            1. Initialize position (0,0) with direction = 'up'
            2. Add current element to result
            3. Check specific boundary conditions and handle movement:
               - At top edge + going up: move right, switch to 'down'
               - At bottom edge + going down: move right, switch to 'up'  
               - At left edge + going down: move down, switch to 'up'
               - At right edge + going up: move down, switch to 'down'
               - Otherwise: move diagonally based on current direction
            4. Apply coordinate correction for any overshoots (x<0, x>max_x, y<0, y>max_y)
            5. Continue until reaching bottom-right corner
        - Time Complexity: O(m × n) - visit each element exactly once
        - Space Complexity: O(m × n) for output array, O(1) extra space excluding output
        - Other Tips:
            1. Mathematical approach: Group elements by (i + j) sum, then reverse alternate groups
            2. Unified boundary handling: Use consistent logic for all edge cases instead of multiple conditions
            3. Direction vector approach: Use (-1,+1) and (+1,-1) vectors for cleaner movement logic
            4. Coordinate mapping: Calculate diagonal start/end points directly without step-by-step traversal
        """
        diagonal = []
        x = 0
        y = 0
        max_x = len(mat) - 1
        max_y = len(mat[0]) - 1
        direction = 'up'

        while x < max_x or y < max_y:
            diagonal.append(mat[x][y])
            if x == 0 and direction == 'up':
                y += 1
                direction = 'down'
            elif x == max_x and direction == 'down':
                y += 1
                direction = 'up'
            elif y == 0 and direction == 'down':
                x += 1
                direction = 'up'
            elif y == max_y and direction == 'up':
                x += 1
                direction = 'down'
            else:
                if direction == 'up':
                    x -= 1
                    y += 1
                else:
                    x += 1
                    y -= 1
            
            if x < 0:
                x = 0
                y -= 1
                direction = 'down'
            if x > max_x:
                x = max_x
                y += 1
                direction = 'up'
            if y < 0:
                y = 0
                x -= 1
                direction = 'up'
            if y > max_y:
                y = max_y
                x += 1
                direction = 'down'

        diagonal.append(mat[max_x][max_y])

        return diagonal
