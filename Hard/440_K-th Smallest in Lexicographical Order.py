class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
        Thought:
        - Goal: Find the k-th smallest integer in lexicographical order within range [1, n]
        - Idea: 
            1. Observe lexicographical ordering (e.g., 1, 10, 11, ..., 20, 21, ...) - numbers can be treated as strings where each digit is a node, forming a Trie structure for efficient dictionary-order access
            2. Building an actual Trie has high space/time complexity. Since we only need the k-th smallest number, we can simulate Trie traversal without constructing it
            3. Pattern recognition between lexicographical order and Trie structure:
                > For top-level node 1:
                - Level 1: number 1 (range [prefix, prefix+1))
                - Level 2: numbers 10-19 (range [prefix×10, (prefix+1)×10))  
                - Level 3: numbers 100-199 (range [prefix×100, (prefix+1)×100))
                - And so on...
            4. Using this pattern, we can efficiently count numbers ≤ n with a given prefix
            5. Compare k with this count: if within range, search node by node; otherwise, jump to next prefix
            6. Obtain final answer
        - Steps:
            1. Build a function implementing count calculation from Idea #4
                - Input: prefix, n
                - Function: Layer by layer progression until value exceeds n, calculating node count at each level, return total count of numbers with given prefix that are ≤ n
                - Output: count
            2. Initialize values
                - current = 1: minimum value is 1  
                - k -= 1: loop uses 0-based comparison
            3. While k > 0 (haven't found k-th smallest number), continue comparison:
                - Call function from Step #1 to calculate count of numbers with current prefix
                - Compare count with k:
                    - count > k: k-th number is within this range, search node by node (k -= 1, current *= 10)
                    - count ≤ k: k-th number is not in this range, skip to next prefix (current += 1, k -= count)
            4. Return current
        """
        
        def count_numbers_with_prefix(prefix, n):
            count = 0
            first = prefix
            next_prefix = prefix + 1

            while first <= n:
                count += min(n+1, next_prefix) - first
                first *= 10
                next_prefix *= 10

            return count

        current = 1
        k -= 1

        while k > 0:
            count = count_numbers_with_prefix(current, n)
            if count > k:
                current *= 10
                k -= 1
            else:
                current += 1
                k -= count

        return current
