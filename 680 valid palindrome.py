class Solution:
    def validPalindrome(self, s: str) -> bool:
        #initialize pointers
        l, r = 0 , len(s)-1
        # loop through string and check values
        while l < r:
            # if l ends  upbeing r then we can assume that the input is a valid palindrome
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                #check by deleting left
                if s[l+1:r+1]== s[l+1:r+1][::-1]:
                    return True
                #check by deleting right
                elif s[l:r] == s[l:r][::-1]:
                    return True
                else: 
                    return False
        return True


