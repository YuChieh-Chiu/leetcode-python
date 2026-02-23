# 方法一
# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         """
#         Thought:
#         - Goal: Determine if all possible binary codes of length k are present as substrings in string s.
#         - Idea: The total number of unique binary strings of length k is 2^k. By collecting all substrings of length k from s into a set, we can check if the set's size reaches 2^k.
#         - Steps:
#             1. Slide a window of size k across the string s.
#             2. Store each unique substring encountered into a hash set.
#             3. Finally, compare the size of the set with 2^k.
#         - Time Complexity: O(n * k), where n is the length of s, because each substring slice and hashing operation takes O(k).
#         - Space Complexity: O(n * k), in the worst case, we store (n-k+1) substrings of length k.
#         """
#         codes = set()

#         for i in range(len(s)-k+1):
#             codes.add(s[i:i+k])

#         # 1 << k 是位元操作，效能更佳，效果等同於 2^k
#         return len(codes) == 1 << k

# 方法二
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        Thought:
        - Goal: Check if the string 's' contains all possible binary codes of length 'k'.
        - Idea: Use a Rolling Hash (via bitwise sliding window) to track all unique substrings of length k efficiently.
        - Steps:
            1. Handle the edge case where s is shorter than k.
            2. Convert the first k-length substring into its integer representation.
            3. Use a bitmask to maintain a fixed-length window of size k while sliding.
            4. Slide through the string, updating the hash in O(1) using bit-shifting and bitwise AND.
            5. Store each encountered hash in a set and check if the set's size equals 2^k.
        - Time Complexity: O(n), where n is the length of string s. Each shift and set insertion is O(1).
        - Space Complexity: O(min(n, 2^k)), as we store at most (n-k+1) unique codes in the hash set.
        """
        if len(s) < k:
            return False
            
        num_codes = 1 << k
        window_hash = int(s[:k], 2)
        mask = (num_codes) - 1 
        codes = {window_hash}

        for i in range(k, len(s)):
            # Rolling update: shift left, add new bit, and apply mask
            new_bit = 1 if s[i] == '1' else 0
            window_hash = ((window_hash << 1) | new_bit) & mask
            codes.add(window_hash)

        return len(codes) == num_codes

"""
# Rolling Hash Cheatsheet

## 1. 核心定義
Rolling Hash 是將「滑動視窗」內的資料轉化為一個「整數雜湊值」。
其優勢在於：當視窗移動時，更新雜湊值的複雜度為 O(1) 而非 O(k)。

## 2. 運算邏輯 (以字串為例)
- 初始狀態：計算前 k 個字元的總和（依權重）。
- 滾動更新：
  1. 去頭：減去「離開視窗的字元」之權重。
  2. 移位：將剩餘值乘以「基底 (Base)」，為新字元騰出位子。
  3. 加尾：加上「進入視窗的字元」之數值。

## 3. 二進位特化版本 (Bitwise Rolling)
當資料僅含 0 與 1 時，效率最高：
- 移位與加尾：(current << 1) | new_bit
- 固定長度(去頭)：current & mask (其中 mask = (1 << k) - 1)
- 適用場景：LeetCode 1461 (此題), 子序列二進位判定。

## 4. 關鍵要素：Base 與 Mod
- Base (基底)：建議選擇質數 (例如小寫字母用 31，ASCII 用 257)。
- Mod (模數)：選擇大質數 (例如 10^9 + 7) 防止數值溢位。
- Double Hash：若怕碰撞，可用兩組不同的 (Base, Mod) 同時計算。

## 5. 實戰重點補充
- 空間複雜度：通常與「不重複子字串」數量相關，為 O(n)。
- 時間複雜度：預處理 O(k)，後續滾動更新 O(n-k)，總計 O(n)。
- 提早結束 (Early Exit)：在去重題目中，若 Set 大小已達到上限 (如 2^k)，可直接回傳 True 以節省時間。
- 負數處理：在 Python 以外的語言中，(a - b) % mod 可能產生負數，記得要加上 (hash + mod) % mod。
"""
