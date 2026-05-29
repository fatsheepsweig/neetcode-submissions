class Solution:
    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append('#')
            parts.append(s)
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i, n = 0, len(s)

        while i < n:
            # parse length (digits) without int()
            length = 0
            while s[i] != '#':
                length = length * 10 + (ord(s[i]) - 48)
                i += 1

            i += 1  # skip '#'
            res.append(s[i:i + length])
            i += length

        return res