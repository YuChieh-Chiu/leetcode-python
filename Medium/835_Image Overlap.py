class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """
        Thought:
        - Goal: Find the maximum number of overlapping 1s between two binary images after arbitrary translation.
        - Idea: Instead of scanning all possible (2n - 1) x (2n - 1) shifts, only pairs of 1s can contribute to the overlap. We can represent a translation by the vector difference between two coordinates: (r2 - r1, c2 - c1). The shift vector with the highest frequency gives the maximum overlap.
        - Steps:
            1. Collect the coordinates of all 1s from both img1 and img2.
            2. Compute the displacement vector between every pair of 1s (one from img1 and one from img2).
            3. Count the occurrences of each unique displacement vector using a hash map (Counter).
            4. Return the maximum frequency found, defaulting to 0 if no 1s exist in either matrix.
        - Time Complexity: O(n^2 + M1 * M2), where n is the grid dimension, and M1, M2 are the counts of 1s in img1 and img2, respectively.
        - Space Complexity: O(M1 * M2) in the worst case to store displacement counts (or O(M1 + M2 + min(n^2, M1 * M2))), plus O(M1 + M2) to store the coordinates of 1s.
        """
        ones1 = [(i,j) for i in range(len(img1)) for j in range(len(img1[0])) if img1[i][j] == 1]
        ones2 = [(i,j) for i in range(len(img2)) for j in range(len(img2[0])) if img2[i][j] == 1]
        
        shifts = Counter((x2-x1, y2-y1) for (x1,y1) in ones1 for (x2,y2) in ones2)
    
        return max(shifts.values(), default=0)
