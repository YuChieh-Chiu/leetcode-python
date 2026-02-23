class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        Thought:
        - Goal: Determine if all possible binary codes of length k are present as substrings in string s.
        - Idea: The total number of unique binary strings of length k is 2^k. By collecting all substrings of length k from s into a set, we can check if the set's size reaches 2^k.
        - Steps:
            1. Slide a window of size k across the string s.
            2. Store each unique substring encountered into a hash set.
            3. Finally, compare the size of the set with 2^k.
        - Time Complexity: O(n * k), where n is the length of s, because each substring slice and hashing operation takes O(k).
        - Space Complexity: O(n * k), in the worst case, we store (n-k+1) substrings of length k.
        """
        codes = set()

        for i in range(len(s)-k+1):
            codes.add(s[i:i+k])

        # 1 << k 是位元操作，效能更佳，效果等同於 2^k
        return len(codes) == 1 << k
