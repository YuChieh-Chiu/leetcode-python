class Solution:
    def mirrorFrequency(self, s: str) -> int:
        """
        Thought:
        - Goal: Compute the sum of absolute frequency differences |freq(c) - freq(m)| for each unique mirror pair (c, m) present in the string, ensuring each pair is counted exactly once.
        - Idea: Precompute mirror mappings for both lowercase English letters ('a' <-> 'z') and digits ('0' <-> '9') using lookup tables. Count character occurrences with Counter. Iterate through the distinct characters present in the frequency map. Since each character in the map is processed only once, we only need to add its mirror counterpart `m` to a `visited` set so that if `m` appears later during iteration, it will be skipped to avoid double counting.
        - Steps:
            1. Build a combined lookup dictionary `mirror` mapping characters ('a'-'z', '0'-'9') to their respective reverse mirror counterparts.
            2. Compute character frequencies `freq` of the input string `s` using `Counter`.
            3. Initialize an accumulator `total = 0` and an empty set `visited`.
            4. Iterate over each unique character `c` in `freq`:
                a. If `c` is in `visited`, skip it (the mirror pair was already calculated).
                b. Retrieve the mirror character `m = mirror[c]`.
                c. Add `m` to `visited` to prevent duplicate processing.
                d. Add |freq[c] - freq[m]| to `total` (Counter defaults missing keys to 0).
            5. Return `total`.
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        """
        en_mirror = dict(zip(string.ascii_lowercase, reversed(string.ascii_lowercase)))
        digit_mirror = {str(i): str(9 - i) for i in range(10)}
        mirror = en_mirror | digit_mirror

        freq = Counter(s)
        total = 0
        visited = set()
        
        for c in freq:
            if c in visited:
                continue
            m = mirror[c]
            visited.add(m)
            total += abs(freq[c] - freq[m])

        return total
