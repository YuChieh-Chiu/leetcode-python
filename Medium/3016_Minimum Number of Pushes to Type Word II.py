class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        thought:
        - from the problem description, we know the following restrictions:
            # we can remap letters to the keys `2` to `9`.
            # each letter must be mapped to exactly one key.
            # each key can be mapped to any number of letters.
        - our goal is to find the minimum number of pushes required to type the `word`.
        - therefore, we can follow these steps:
            1. calculate the frequency of each letter.
            2. sort the letters by frequency in descending order.
            3. traverse the letters one by one:
                - for the first to eighth letters: `push` 1 time.
                - for the ninth to sixteenth letters: `push` 2 times.
                - and so on.
        """
        pushes = 0
        letter_number = {}
        for char in word:
            if char in letter_number:
                letter_number[char] += 1
            else:
                letter_number[char] = 1
        letter_number = sorted(letter_number.items(), key=lambda x:x[1], reverse=True)
        for idx, (_, num) in enumerate(letter_number):
            push = idx//8 + 1
            pushes += (push * num)
        return pushes
