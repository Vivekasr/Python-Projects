


M = int(input())
input1 =input().split()
lst1 = []
for i1 in input1:
        lst1.append(int(i1))
        
N = int(input())
input2 =input().split()
lst2 = []
for i2 in input2:
        lst2.append(int(i2))
        
output = [i for i in lst1 if i not in lst2] + [i for i in lst2 if i not in lst1]
output.sort()

for element in output:
        print(element)
