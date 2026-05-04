from collections import defaultdict, Counter
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Thought:
        - Goal: Group an array of strings such that all anagrams are stored together in the same sublist.
        - Idea: Two strings are anagrams if and only if their character frequencies are identical. By counting the occurrences of each character and generating a unique, standardized string representation of these counts, we can use it as a hash map key to group matching strings.
        - Steps:
            1. Initialize a hash map (dictionary) where the keys are string representations of character counts, and the values are lists of grouped strings.
            2. Iterate through each string in the input array.
            3. Count the frequency of each character in the current string.
            4. Sort the character counts and format them into a deterministic string key (e.g., 'a2b1c1').
            5. Append the original string to the corresponding key in the hash map.
            6. Return all the grouped lists from the hash map's values.
        - Time Complexity: O(M * N), where M is the number of strings and N is the maximum length of a string.
        - Space Complexity: O(M * N), for storing the output and the keys in the hash map.
        """
        anagrams = defaultdict(list)

        for string in strs:
            times = Counter(string)            
            sorted_times = sorted(times.items(), key=lambda x: (x[1], x[0]), reverse=True)
            key = "".join(f"{k}{v}" for k, v in sorted_times)            
            anagrams[key].append(string)
        
        return list(anagrams.values())
