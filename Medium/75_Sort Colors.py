class Solution:
    def quickSort(self, arr: List[int]) -> List[int]:
        currentPointer = 0 # from left to right
        leftPointer = 0
        rightPointer = len(arr)-1
        if leftPointer == rightPointer: # len(arr)==1
            return arr
        while currentPointer <= rightPointer:
            if arr[currentPointer] == 0: # move all 0 to the left -> swap
                arr[currentPointer], arr[leftPointer] = arr[leftPointer], arr[currentPointer]
                leftPointer += 1 # avoid changing the value 0
                currentPointer += 1
            elif arr[currentPointer] == 2: # move all 2 to the right -> swap
                arr[currentPointer], arr[rightPointer] = arr[rightPointer], arr[currentPointer]
                rightPointer -= 1 # avoid changing the value 2
            else:
                currentPointer += 1
        return arr 
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        ---
        thought:
        - we know that 
            (1) only three colors -> {0: red, 1: white, 2: blue}
            (2) we cannot use library's sort function and we should modify in-place
        - use the skill `two-pointer` (need to sort in-place) with `quick sort`
        - NOTE. we can use `counting sort` or other algorithms too.
        - the code reference is as below:
            ```reference
            - url link : https://ithelp.ithome.com.tw/articles/10321989
            ```
        """
        nums = self.quickSort(nums)
