class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
        thought:
        - from the problem description, we can infer that:
            (1) `s1` and `s2` do not have leading or trailing spaces, so we can split `s1` and `s2` by spaces without using .strip().
            (2) all words in `s1` and `s2` are separated by a single space, so we don't need to replace multiple spaces with a single space.
            (3) A word is considered uncommon only if it appears exactly once across both sentences.
        - therefore, we can follow these steps:
            (1) split `s1` and `s2` by spaces.
            (2) cncatenate the two lists into one list.
            (3) create an empty dictionary to count the occurrence of each word.
            (4) extract all words that appear exactly once as our answer.
        """
        l1 = s1.split(" ")
        l2 = s2.split(" ")
        lm = l1 + l2
        words_num = {}
        for word in lm:
            if word in words_num:
                words_num[word] += 1
            else:
                words_num[word] = 1
        return [key for key, val in words_num.items() if val == 1]
