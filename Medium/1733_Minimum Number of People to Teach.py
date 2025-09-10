from collections import defaultdict

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        """
        Thought:
        - Goal: Find the minimum number of users to teach **one** language so all friends can communicate
        - Idea: For each possible language, calculate how many users need to learn it to solve all communication gaps. Choose the language requiring the fewest users.
        - Steps: 
            1. Find all friendship pairs that cannot communicate (no common language)
            2. For each language (1 to n), count how many users in speechless pairs don't know this language
            3. Return the minimum count across all languages
        - Time Complexity: O(F * L + n * F * L) where F = friendships, L = average languages per user
        - Space Complexity: O(F + n * U) where U = total users who need to learn languages
        """
        # 先找出所有無法溝通的對
        speechless_pairs = []
        for (u1, u2) in friendships:
            if not set(languages[u1-1]).intersection(set(languages[u2-1])):
                speechless_pairs.append((u1, u2))

        # 再紀錄如果教某語言，需要教的人有誰
        lang_count = defaultdict(set)
        for lang in range(1, n+1):
            for (u1, u2) in speechless_pairs:
                lang_u1 = set(languages[u1-1])
                lang_u2 = set(languages[u2-1])
                if lang not in lang_u1:
                    lang_count[lang].add(u1)
                if lang not in lang_u2:
                    lang_count[lang].add(u2)

        lang_count = sorted(lang_count.items(), key= lambda x: len(x[1]), reverse=False)        

        # 回傳需要教的人數最少的語言，所要教的人數
        # 注意邊界狀況：沒有任何無法溝通的對
        return len(lang_count[0][1]) if lang_count else 0
