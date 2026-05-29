class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        counts = {}
        for num in nums:
            if num in counts.keys():
                counts[num] += 1
            else:
                counts[num] = 1
        return max(counts.values()) > 1