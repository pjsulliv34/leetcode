class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', ']':'[','}':'{'}
        stack = []

        for i in s:
            print(i)
            if i not in hashmap:
                stack.append(i)
            else:
                #stack have an item:
                if not stack: 
                    return False
                else:
                    top = stack.pop()
                    # check to see if top matches the closing
                    if top != hashmap[i]:
                        return False
        return not stack
