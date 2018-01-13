from collections import Counter

X = int(input())
shoe = Counter(map(int, input().split()))
N = int(input())
total = []
for i in range(N):
        sizeav,price = map(int,input().split())
        if shoe[sizeav] > 0:
                total.append(price)
                shoe.subtract(Counter([sizeav]))
                
        else:
                pass
        
print(sum(total))
