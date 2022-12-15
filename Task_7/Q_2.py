class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            Max_Stone = max(stones)
            stones.remove(Max_Stone)
            Next_Max_Stone = max(stones)
            stones.remove(Next_Max_Stone)
            if Max_Stone - Next_Max_Stone > 0:
                stones.append(Max_Stone - Next_Max_Stone)
        if len(stones)==1:
            return stones[0]
        return 0
