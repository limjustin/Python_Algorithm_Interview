from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:

        for i in range(int(len(s)/2)) :
            # temp = s[i]
            # s[i] = s[-i-1]
            # s[-i-1] = temp

            # Python Swap
            s[i], s[-i-1] = s[-i-1], s[i]

        ## Q2. List Comprehension 이용하기
        res = [s[x] for x in range(len(s))]
        print(res)

s = Solution()
str = "Hannah"
s.reverseString(list(str))

## 얻어간 점 
## 1. 새로운 SWAP 방식
## 2. 슬라이싱 3번째 파라미터에 음수를 넣으면 반대 방향에서 탐색