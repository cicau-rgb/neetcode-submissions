class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products_except_self = []
        for id in range(0, len(nums)):
            tmp = nums[id]
            nums[id] = 1
            products_except_self.append(math.prod(nums))
            nums[id] = tmp
        return products_except_self

            
        