class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        Thought:
        - Goal: Maximize the points earned from solving a sequence of questions, given that solving a question forces you to skip a certain number of subsequent questions.
        - Idea: Use Bottom-Up Dynamic Programming. By iterating backwards from the last question to the first, we can determine the optimal choice at each step. At any question `i`, we decide whether to solve it (gaining its points + the optimal result from the next available question) or skip it (relying entirely on the optimal result from the immediate next question).
        - Steps:
            1. Initialize a `dp` array of the same length as the `questions` array with zeros to store the maximum points achievable from index `i` to the end.
            2. Iterate backwards from the last index (`length - 1`) down to `0`.
            3. For each question, extract its points `p` and brainpower `b`.
            4. Calculate the `skip` value: lookup `dp[i+1]` (or 0 if out of bounds).
            5. Calculate the `solve` value: `p` + lookup `dp[i+b+1]` (or 0 if out of bounds).
            6. Store the maximum of `skip` and `solve` into `dp[i]`.
            7. Return `dp[0]`, which represents the maximum points achievable starting from the first question.
        - Time Complexity: O(n), where n is the number of questions. We iterate through the array exactly once, performing constant time O(1) operations at each step.
        - Space Complexity: O(n), as we need an array of size n to store the DP states.
        """
        length = len(questions)
        dp = [0] * length

        for i in range(length-1, -1, -1):
            p, b = questions[i]
            skip = dp[i+1] if i+1 < length else 0
            solve = p + (dp[i+b+1] if i+b+1 < length else 0)
            dp[i] = max(skip, solve)

        return dp[0]
