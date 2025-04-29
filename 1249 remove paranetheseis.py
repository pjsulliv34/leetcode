class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l, r = 0,0
        stack = []
        # if r > l, don't keep right paranethes
        for i in s:
            if i == '(':
                l +=1
                stack.append(i)
            elif i == ')':
                if l > r:
                    r+=1
                    stack.append(i)
            else:
                stack.append(i)
        print(f'stack {stack}')
        print(f'l count {l}, r count {r}')
            
        if l == r:
            return ''.join(stack)
        else:
            #l must be larger than r due to way we set it up
            stack2 = []
            while stack:
                item = stack.pop()
                if l > r and item == '(':
                    l -=1
                    continue
                else: 
                    stack2.append(item)
            return ''.join(stack2)[::-1]