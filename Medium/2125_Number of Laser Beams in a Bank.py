class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        Thought:
        - Goal: Calculate the total number of laser beams in the bank.
        - Idea:
            A laser beam exists between two security devices on different rows only if there are no devices on any row between them. Therefore, we track the count of devices in the current row and the previous non-empty row, multiplying them to get beams between these rows.
        - Steps:
            1. Initialize total beams counter and previous row device count
            2. For each row, count the number of security devices ('1's)
            3. If current row has devices and previous row had devices, add their product to total (this gives beams between them)
            4. Update previous count to current if current row has devices
            5. Return total number of beams
        - Time Complexity: O(m * n) where m is number of rows and n is row length
        - Space Complexity: O(1) as we only use constant extra space
        """
        total = 0
        prev = 0

        for row in bank:
            current = row.count('1')  # 使用內建方法處理
            
            if current > 0:  # 只有當前列有設備時才處理
                if prev > 0:  # 如果前一列也有設備，計算 beams
                    total += prev * current
                prev = current  # 更新 prev 為當前值
        
        return total
