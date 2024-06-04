class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        thought: 
        - target 會等於 nums 中的某兩個數字相加
        - target 對 nums 中的每個數字做減法，得到新的 lack_nums 列表
        - 檢視 lack_nums 列表與 nums 列表重複的部份，即為加起來會等於 target 的兩個數字
        """
        lack_nums: List[int] = []
        # O(n)
        for num in nums:
            lack_nums.append(target-num)
        # O(n)
        inner = list(set(nums).intersection(set(lack_nums)))
        # O(n)
        if len(inner) == 1:
            index1 = nums.index(inner[0])
            index2 = nums.index(inner[0], index1+1)
        elif len(inner) == 2:
            index1 = nums.index(inner[0])
            index2 = nums.index(inner[1])
        elif len(inner) == 3:
            for i in inner:
                if i*2 == target:
                    inner.remove(i)
                    break
            index1 = nums.index(inner[0])
            index2 = nums.index(inner[1])
        else:
            print("length of `inner` is wrong.")
        return [index1, index2]
