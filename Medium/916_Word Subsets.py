class Solution:
    def getCharCnt(self, word: str):
        char_cnt = {}
        for char in word:
            if char in char_cnt:
                char_cnt[char] += 1
            else:
                char_cnt[char] = 1
        return char_cnt
        
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        Thought:
        - Goal:
            - Identify all universal strings in `words1`.
        - Definition of a universal string:
            - A string is universal if every string in `words2` is a subset of it.
            - A string `b` is a subset of string `a` if:
                1. Every letter in `b` appears in `a`.
                2. The occurrence count of each letter in `b` is less than or equal to that in `a`.
        - Key Concept:
            - To determine if a string in `words1` is universal:
                1. Each letter in `words2` must appear in the string from `words1`.
                2. The maximum occurrence of each letter in any string of `words2` must not exceed its occurrence in the string from `words1`.
        - Steps:
            1. Initialize a list to store universal strings.
            2. Define a helper function to count the occurrences of each letter in a string.
            3. Iterate through `words2` to calculate the maximum occurrence count of each letter across all its strings.
            4. For each string in `words1`, count the occurrences of its letters and check if these counts meet or exceed the maximum counts from `words2`. Add the string to the list if it satisfies the condition.
            5. Return the list of universal strings.
        """
        universals = []

        word2_cnt = {}
        for w2 in set(words2):
            w2_cnt = self.getCharCnt(w2)
            for k, v in w2_cnt.items():
                if k not in word2_cnt:
                    word2_cnt[k] = v
                else:
                    if k in word2_cnt:
                        if word2_cnt[k] < v:
                            word2_cnt[k] = v

        for w1 in set(words1):
            w1_cnt = self.getCharCnt(w1)
            is_subset = True
            for k, v in word2_cnt.items():
                if k in w1_cnt:
                    if w1_cnt[k] >= v:
                        continue
                    else:
                        is_subset = False
                        break
                else:
                    is_subset = False
                    break
            if is_subset:
                universals.append(w1)

        return universals
