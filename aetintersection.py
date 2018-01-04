
n = int(input())
nums1 = set(map(int, input().split())) 
b = int(input())
nums2 = set(map(int, input().split())) 
un = set.intersection(nums1,nums2)
print(len(un))
