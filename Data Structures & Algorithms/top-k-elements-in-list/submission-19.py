class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 1
                continue
            hash[num] += 1
        
        sorted_hash = sorted(hash.items(), key=lambda x: x[1], reverse=True)

        return [k for k, v in sorted_hash[0:k]]
        