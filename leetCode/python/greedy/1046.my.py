# while 문 돌림
# list 안에서 최대값 2개 추출 (추출된 값 버림)
# 최대값 각각 뺀 수 list 안에 삽입 (뺀 수 0일 시 삽입 안 함)
#

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while stones != [1] or stones != [0]:
            first = max(stones)
            stones.remove(max(stones))
            second = max(stones)
            stones.remove(max(stones))
            smashed = first-second
            if smashed != 0:
                stones.append(smashed)
        return stones


solution = Solution()
print(solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))
