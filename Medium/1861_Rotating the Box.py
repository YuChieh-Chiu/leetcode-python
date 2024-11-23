class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
        thought:
        - The `box` contains three types of elements: stone (`#`), obstacle (`*`), and empty space (`.`).
        - When the box is rotated 90 degrees clockwise, stones (`#`) will always settle on top of an obstacle (`*`), another stone (`#`), or the bottom of the box.
        - Based on this behavior, we can solve the problem step-by-step:
            1. Treat each obstacle (`*`) as a divider. Focus only on the region below each `*`, extending to the next `*` or the bottom of the box, and consider the arrangement of `#` and `.` within that region.
            2. Rearrange the region by moving all empty spaces (`.`) to the top and all stones (`#`) to the bottom.
            3. Repeat this process for every region between obstacles.
            4. Once all regions are processed, rotate the entire matrix 90 degrees clockwise to get the final result.
        """

        for row in range(len(box)):
            right = len(box[row])-1
            left = len(box[row])-2
            while left >= 0:
                if box[row][left] != "*": # 還在區域內
                    if box[row][left] == "#":
                        if box[row][right] == ".":
                            box[row][left] = "."
                            box[row][right] = "#"
                            left -= 1
                            right -= 1
                        else:
                            left -= 2
                            right -= 2
                    else:
                        if box[row][right] == ".":
                            left -= 1
                        else:
                            left -= 1
                            right -= 1
                else:
                    right = left - 1 # IMPORTANT: move `right` to the left of `left` into a new checking area
                    left -= 2

        # `*` represents unpacking
        matrix = [list(row) for row in zip(*box[::-1])]

        return matrix
