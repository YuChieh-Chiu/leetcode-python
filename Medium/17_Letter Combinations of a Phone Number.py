class Solution:
    def recursion(self, index: int, eng_string: str, combinations: List[str], digit2eng: dict, digits: str) -> None:
        if index == len(digits):
            combinations.append(eng_string)
            return
        letters = digit2eng[digits[index]]
        for eng in letters:
            eng_string += eng
            self.recursion(index+1, eng_string, combinations, digit2eng, digits)
            eng_string = eng_string[:-1]
    def letterCombinations(self, digits: str) -> List[str]:
        """
        thought:
        - Based on the given information, we can know that `digits` is a string containing numbers from 2 to 9, or it may be an empty string.
        - Our objective is to find all possible letter combinations that can be formed by the digit keys in `digits`.
        - The key approach is to use a backtracking algorithm to efficiently generate **all** possible combinations.
        - Steps:
            (1) If `digits` is empty, return an empty list immediately.
            (2) Define a dictionary that maps each digit key to its corresponding letters, and initialize a `combinations` list to store the possible letter combinations.
            (3) Define a recursive function that selects letters at "each level" of the backtracking process.
                - Remember to use `str[:-1]` to "undo" the choice we've done.
            (4) Call the recursive function to generate and collect all possible letter combinations.
        """

        if digits == "":
            return []
        digit2eng = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        combinations = []
        self.recursion(index=0, eng_string="", combinations=combinations, digit2eng=digit2eng, digits=digits)
        return combinations
