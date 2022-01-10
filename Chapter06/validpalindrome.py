class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = list(s)
        p1 = 0
        p2 = len(a) - 1
        res = False

        while p1 <= p2 :
            while not a[p1].isalnum() and p1 < len(a) - 1 :
                p1 = p1 + 1
            while not a[p2].isalnum() and p2 > 0 :
                p2 = p2 - 1

            # print(p1, p2)

            if p1 >= p2 :
                return True

            elif a[p1].upper() != a[p2].upper() :
                return False

            elif p1 >= p2 :
                return True

            else :
                res = True
                p1 = p1 + 1
                p2 = p2 - 1

        return res