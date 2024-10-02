class Solution:
    def filter(self, img: List[List[int]], row: int, col: int) -> int:
        tot = 0
        cnt = 0
        for ud_move in [-1,0,1]: # move up or down
            for lr_move in [-1,0,1]: # move left or right
                row_i = row + ud_move
                col_i = col + lr_move
                if (row_i < 0) | (row_i >= len(img)): 
                    continue
                if (col_i < 0) | (col_i >= len(img[0])):
                    continue
                tot += img[row_i][col_i]
                cnt += 1
        print(tot, cnt)
        return tot // cnt # get the floor of average 
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """
        thought:
        - based on the problem description, we can gather the following information:
            - `img` is a grayscale image, meaning it only has length and width, and is a `matrix`.
                - `img` is represented as a two-dimensional nested list.
            - the image smoother is a 3x3 matrix, which is used to update position i by averaging the values within the 3x3 region around it, rounding down the result.
                - in the image smoother, if the region goes beyond the image boundary, those areas are excluded from the averaging.
        - therefore, we can follow these steps:
            (1) initialize a matrix `new_img` filled with zeros.
            (2) define function `filter` as image smoother:
                - Input: the current position i.
                - Output: the value of position i after applying the image smoother and rounding down.
                - Function: retrieve the values within the 3x3 region around position i and compute the average.
            (3) traverse the entire `img`, apply the function `filter` to each position i to perform the image smoother transformation, and store the result in `new_img`.

        """
        new_img = [[0 for j in range(len(img[0]))] for i in range(len(img))] # initialize a new matrix with 0
        for row in range(len(img)):
            for col in range(len(img[0])):
                new_img[row][col] = self.filter(img, row, col)
        return new_img
