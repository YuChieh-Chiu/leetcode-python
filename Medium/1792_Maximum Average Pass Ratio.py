from heapq import *

class Solution:
    def calculateNegGain(self, passed: int, total: int) -> float:
        return (-1) * ((total-passed)/(total**2 + total))

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        Thought:
        - Goal: Maximize the average pass ratio across all classes by optimally assigning extra students.

        - Idea: Use greedy approach with max heap. Each time, assign one extra student to the class that gives the maximum improvement in pass ratio. The improvement when adding one student to class [pass, total] is: (total - pass) / [total × (total + 1)].

        - Steps:
            1. Initialize a max heap (using negative values since Python heapq is min heap)
            2. For each class, calculate improvement value and push (-improvement, pass, total) to heap
            3. For each extra student:
                - Pop the class with maximum improvement
                - Add one student to that class (pass+1, total+1)
                - Calculate new improvement and push back to heap
            4. Calculate final average pass ratio by iterating through all classes in heap

        - Time Complexity: O((classes + extraStudents) × log classes)
        - Space Complexity: O(classes)
        """
        max_heap = []
        passed_ratio = 0

        for class_info in classes:
            neg_improvement = self.calculateNegGain(class_info[0], class_info[1])
            heappush(max_heap, (neg_improvement, class_info[0], class_info[1]))

        for _ in range(extraStudents):
            neg_improvement, passed, total = heappop(max_heap)
            neg_improvement = self.calculateNegGain(passed+1, total+1)
            heappush(max_heap, (neg_improvement, passed+1, total+1))

        while max_heap:
            _, passed, total = heappop(max_heap)
            passed_ratio += passed / total

        return round(passed_ratio/len(classes), 5)
