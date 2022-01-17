class Solution:
    def isPalindrome(self, s: str) -> bool:

        a = list(s)
        b = []
        
        for i in range(len(a)) :
            if a[i].isalnum() :
                b.append(a[i].lower())

        i = 0
        
        while i < len(b)/2 :
            if b[i] != b[-i-1] :
                return False
            else  :
                i = i + 1

        return True