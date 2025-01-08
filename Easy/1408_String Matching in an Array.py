class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        Thought:
        - Goal:
            - Given an array of strings `words`, return all strings in `words` that are substrings of another word.
        - Problem Description:
            - Substring: A contiguous sequence of characters within a string. This implies the length of the substring must be less than or equal to the length of the original string.
        - Steps:
            1. Sort the list `words` by the length of its elements, ensuring longer words are checked first.
            2. Initialize a set to store all unique substrings found.
            3. Use nested loops to iterate through the list `words` and check for substrings:
                - For each word in the list `words`, compare it only with subsequent words in the list.
                - If the subsequent word is a substring of the current word, add it to the set using `.add()`.
            4. Convert the set into a list and return it.
        """

        # sort by length descendingly
        words = sorted(words, key=lambda x:len(x), reverse=True)
        
        # check for substring
        substrings = set()
        for i, word1 in enumerate(words):
            for word2 in words[i+1:]:
                if word2 in word1:
                    substrings.add(word2)

        return list(substrings)

# class Solution:
#     def __init__(self):
#         self.next = {}

#     def get_next(self, p: str) -> List[int]:
#         """
#         計算模式字串 p 的 next 陣列（failure function）
#         """
#         next = [0]  # 初始化 next 陣列
#         i_partial = 1  # 當前部分匹配的子字串結尾索引
#         i_whole = 0  # 當前部分匹配的前綴與後綴匹配長度

#         while i_partial < len(p):
#             if p[i_partial] == p[i_whole]:  # 若字符匹配
#                 i_partial += 1
#                 i_whole += 1
#                 next.append(i_whole)  # 記錄匹配的長度
#             elif i_whole <= 0:  # 若不匹配且無法回退，匹配長度為 0
#                 next.append(0)
#                 i_partial += 1
#             else:  # 若不匹配但可以回退，依據 next 陣列回退
#                 i_whole = next[i_whole - 1]

#         return next

#     def kmp(self, s: str, p: str) -> bool:
#         """
#         在字串 s 中尋找字串 p 的起始索引，若不存在則返回 -1
#         """
#         s_i = 0  # 文本索引
#         p_i = 0  # 模式索引

#         # 計算模式的 failure function（next 陣列）
#         next = self.next[p]

#         # 開始比對
#         while s_i < len(s) and p_i < len(p):
#             if s[s_i] == p[p_i]:  # 若字符匹配，兩個指標均前進
#                 s_i += 1
#                 p_i += 1
#             elif p_i <= 0:  # 若不匹配且模式指標已回退到頭，文本指標前進
#                 s_i += 1
#             else:  # 若不匹配且模式指標未回到頭，模式指標依照 next 陣列回退
#                 p_i = next[p_i - 1]

#         # 判斷是否成功匹配整個模式
#         if p_i >= len(p):
#             return True
#         else:
#             return False

#     def stringMatching(self, words: List[str]) -> List[str]:
#         """
#         KMP String Matching 演算法.
#         """

#         # sort by length descendingly
#         words = sorted(words, key=lambda x:len(x), reverse=True)
        
#         # record the failure function of all words
#         for word in words:
#             self.next[word] = self.get_next(word)

#         # check for substring
#         substrings = set()
#         for i, word1 in enumerate(words):
#             for word2 in words[i+1:]:
#                 if self.kmp(word1, word2):
#                     substrings.add(word2)

#         return list(substrings)
