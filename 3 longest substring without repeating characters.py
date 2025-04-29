class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        seen = set()

        #loop through the string added to the seen set
        # add in seen.add s[right]
        # if value of right in seen, while loop to move left Point
        # to the right , removing the left from seen,
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l +=1

            seen.add(s[i])
            longest = max(longest, i - l +1)
        return longest