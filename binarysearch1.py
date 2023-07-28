def binarySearch(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:

        mid=(left+right)//2
        
        #check if x is present at mid or not
        if arr[mid]==target:
            return mid
        #check if x is greater ,ignore the left half
        elif arr[mid]< target:
            left=mid+1
        #if x is smaller,ignore the right half
        else:
            right=mid-1
    #if we reach here element is not present 
    return -1

arr=[1,2,3,4,5,6]
target=6

result=binarySearch(arr,target)

if result !=-1:
    print("element is present at index %d" % result)
else:
    print("element us not present in the array")
