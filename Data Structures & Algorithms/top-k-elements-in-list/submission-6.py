class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 1
                continue
            hash[num] += 1
        
        klargest = heapq.nlargest(k, hash.values())

        most_freq_elements = []
        for k, v in hash.items():
            if v in klargest:
                most_freq_elements.append(k)

        return most_freq_elements
        