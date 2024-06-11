class Solution:
    def countingSort(self, arr: List[int], arr2: List[int]) -> List[int]:
        bucket = [0] * (sorted(arr2)[-1]+1)
        idx = 0
        for i in arr:
            bucket[i] += 1
        for j in arr2:
            while bucket[j]>0:
                arr[idx] = j
                idx += 1
                bucket[j] -= 1
        return arr
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        thought:
        - we need to rearrange `arr1` with the following conditions:
            (1) elements not in `arr2` should be appended at the end of `arr1` in ascending order
            (2) sort the elements of `arr1` such that the relative ordering of items in `arr1` are the same as in `arr2`
        - so the steps we should follow is as below:
            (1) seperate `arr1` into two part (in `arr2` / not in `arr2`)
            (2) not in `arr2` part : sort in asceding order
            (3) in `arr2` part : use algorithm like `counting sort` to sort the list
                - time complexity = O(n+k)
                - space complexity = O(k)
        """
        in_arr2 = []
        not_in_arr2 = []
        for i in arr1:
            if i in arr2:
                in_arr2.append(i)
            else:
                not_in_arr2.append(i)
        in_arr2 = self.countingSort(in_arr2, arr2)
        return (in_arr2 + sorted(not_in_arr2))
