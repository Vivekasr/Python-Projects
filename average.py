#A set is an unordered collection of elements without duplicate entries. 
#When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

def average(arr):
        new_arr = set(arr)
        total = 0
        
        for num in new_arr:
                total = total+num
                
        avg = total/len(new_arr)
        
        return(avg) 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
