class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if num in map.keys():
                return True
            else:
                map[num] = 1
        return False
                   