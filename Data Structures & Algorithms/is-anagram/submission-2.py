class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for ch in s:
            ch = ch.lower()
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            ch = ch.lower()
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] == 0:
                del count[ch]

        return not count