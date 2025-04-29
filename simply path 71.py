class Solution:
    def simplifyPath(self, path: str) -> str:
        if path == '/':
            return path
        #first create a list separted by '/'
        path_list = path.split('/')
        # print(path_list)
        stack1 = []
        while path_list:
            item = path_list.pop()
            if item not in ['','.']:
                stack1.append(item)
        print(stack1)
        stack2 = []
        while stack1:
            print(f'stack 1 {stack1}')
            print(f'stack 2 {stack2}')
            item = stack1.pop()
            print(f'item {item}')
            if item == '..':
                if stack2:
                    stack2.pop()
                continue
            stack2.append(item)
            print(f'final stack1 {stack1}')
            print(f' final stack2 {stack2}')
            print('-------------------')
        
        print('/'.join(stack2))
        return  '/'+'/'.join(stack2)

    

    