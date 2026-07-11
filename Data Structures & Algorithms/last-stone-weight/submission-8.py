class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            m1, m2 = heapq.nlargest(2, stones)

            stones.remove(m1)
            stones.remove(m2)

            if m1 == m2:
                pass
            else:
                stones.append(m1 - m2)
    
        return stones[0] if len(stones) > 0 else 0