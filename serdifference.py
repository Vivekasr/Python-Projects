
n = int(input())
nums1 = set(map(int, input().split())) 
b = int(input())
nums2 = set(map(int, input().split())) 
un = set.difference(nums1,nums2)
print(len(un))
