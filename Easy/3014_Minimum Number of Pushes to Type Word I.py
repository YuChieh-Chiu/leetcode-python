class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        Thought:
        - Goal: Calculate the minimum number of key presses needed to type the given word by remapping letters to 8 available keys (2-9).
        - Idea: Since we want to minimize pushes, we should assign the most frequent letters to the 1st position of each key, the next 8 most frequent to the 2nd position, and so on.
        - Steps:
            1. Count the frequency of each distinct letter in the word using a dictionary.
            2. Sort the frequencies in descending order.
            3. Iterate through the sorted frequencies, multiplying each by its required press count (determined by its index // 8 + 1).
            4. Sum and return the total pushes.
        - Time Complexity: O(n), where n is the length of the word (sorting 26 letters is constant).
        - Space Complexity: O(1), as the dictionary stores at most 26 letter frequencies.
        """
        freq_map = {}
        for char in word:
            freq_map[char] = freq_map.get(char, 0) + 1
        
        # 我們只需要頻率數值，不需要知道是哪個字母
        counts = sorted(freq_map.values(), reverse=True)

        total_pushes = 0
        for i, freq in enumerate(counts):
            total_pushes += freq * (i // 8 + 1)

        return total_pushes
