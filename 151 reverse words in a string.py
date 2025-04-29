class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        print(words)
        stack = []
        while words:
            item = words.pop()
            if item != '':
                stack.append(item)
        print(stack)
        return ' '.join(stack)