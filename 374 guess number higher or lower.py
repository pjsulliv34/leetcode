# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        print(guess(10))
        print(guess(6))
        l,r = 0, n
        while l <r:
            mid = (r+l)//2
            pick = guess(mid)
            if pick == 0: #pick == target
                return mid
            elif pick == -1: # pick > target
                r  = mid -1
            else:
                l = mid +1

        return l