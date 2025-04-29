class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs)==1:
            return strs[0]
        if not strs:
            return 
        # sorted_word = sorted(strs, key = len)
        min_word = min(strs,key = len)
        if min_word == "":
            return ""

        for i in range(len(min_word)):
            letter_check = min_word[i]
            for word in strs:
                # print(f'word_i {word[i]}')
                if letter_check != word[i]:
                    return min_word[:i]
        return min_word
        