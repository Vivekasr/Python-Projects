
from itertools import combinations
s,n = input().split()
for x in range(1,int(n)+1):
        print(*[''.join(i) for i in combinations(sorted(s),int(x))],sep='\n')
