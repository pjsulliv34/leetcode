class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # build a graph from edges

        #initialize trust
        trust_in = {i:[] for i in range(1,n+1)}
        outgoing_trust = {i:[] for i in range(1,n+1)}
    
        for a,b in trust:
            trust_in[b].append(a)
            outgoing_trust[a].append(b)

        print(trust_in)
        print(outgoing_trust)
        current_judge = None
        for i in trust_in:
            print(i)
            print(trust_in[i])
            if n-1 == len(trust_in[i]):
                current_judge = i
        if current_judge:
            #check
            if len(outgoing_trust[current_judge])== 0:
                return current_judge
            else:
                return -1
        else:
            return -1
        


