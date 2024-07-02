class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        thought:
        - we want to find elements in both arrays
        - the times of elements = min(the times of elements in `nums1`, the times of elements in `nums2`)
        - so there are some strategies that we can consider:
            (1) traverse one array to check whether the element `i` in it is also in another array or not; if `i` in both array, get the times by `min()` -> O(nm)
            (2) sort `nums1` & `nums2`, and use `two pointers (fast-slow pointers)` to get the intersection list -> O(n) where n>m
        """
        # # method 1
        # intersection_list = []
        # for i in nums1:
        #     if i in intersection_list:
        #         continue
        #     if i in nums2:
        #         times = min(nums1.count(i), nums2.count(i))
        #         intersection_list.extend([i]*times)
        # return intersection_list

        # method 2
        intersection_list = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        pointer_2 = 0
        for i in range(len(nums1)): # `i` is pointer_1
            for j in range(pointer_2, len(nums2)):
                if nums2[j] < nums1[i]:
                    pass
                elif nums2[j] == nums1[i]:
                    intersection_list.append(nums1[i])
                    pointer_2 = j+1
                    break
                else:
                    pointer_2 = j
                    break
        return intersection_list
