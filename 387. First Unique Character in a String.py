from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for idx, character in enumerate(s):
            if counter[character] == 1:
                return idx
        return -1