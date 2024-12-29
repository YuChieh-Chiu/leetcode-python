class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def addNewParentheses(self, pair: str) -> set:
        new_pair = set()
        for i in range(len(pair)+1):
            for j in range(i, len(pair)+1):
                new = pair[:i] + '(' + pair[i:j] + ')' + pair[j:]
                new_pair.add(new)
        return new_pair

    def generateParenthesis(self, n: int) -> List[str]:
        """
        Thought:  
        - Goal:  
            - Given an integer `n`, generate all combinations of well-formed parentheses.  
        - Definition of well-formed parentheses:  
            - Each opening bracket '(' has a corresponding closing bracket ')'.  
            - Parentheses must be correctly nested.  
        - Examples:  
            - INPUT: `n=1`  
            - OUTPUT: `['()']`  
            
            - INPUT: `n=2`  
            - OUTPUT: `['(())', '()()']`  

            - INPUT: `n=3`  
            - OUTPUT: `['((()))', '(())()', '(()())', '()(())', '()()()']`  
        - Idea:  
            - The combinations of well-formed parentheses for `n` can be derived from those for `n-1`.  
            - The core question is how to determine the positions for the most recently added pair of parentheses.
                - Using recursion, we can construct all valid combinations by adding pairs of parentheses step by step.  
        - Steps:  
            1. Initialization:  
                - Create a dictionary `self.memo = {}` to store combinations of well-formed parentheses for each value of `n`.  
                - Example: `{n: [combinations]}`.  
            2. Recursive Function:  
                - Base Case: When `n=1`, the only combination is `['()']`.  
                - Recursive Relation: For `n > 1`, generate new combinations by inserting the latest pair of parentheses into all possible positions within the combinations from `n-1`.  
                    - Tip: Always ensure that a closing parenthesis follows its corresponding opening parenthesis to maintain validity.  
            3. Output:  
                - Call the function with the given input `n` to obtain the result.  
        - Topics:  
            - Dynamic Programming, Memoization.  
        """

        def dfs(n: int) -> List[str]:
            # Base case
            if n == 1:
                return ['()']

            # Memoization
            if str(n) in self.memo:
                return self.memo[str(n)]

            # Recursion relation
            all_new_pair = set()
            for pair in dfs(n-1): # Key point: recursion relationship should be defined here.
                new_pair = self.addNewParentheses(pair)
                all_new_pair.update(new_pair)

            self.memo[str(n)] = list(all_new_pair)

            return self.memo[str(n)]

        return dfs(n)
