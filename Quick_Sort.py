def partition(arr,arr1,arr2,low,high,n=0): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high][n]     # pivot 
    # print(pivot)
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j][n] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]
            arr1[i],arr1[j] = arr1[j],arr1[i]
            arr2[i],arr2[j] = arr2[j],arr2[i]
  
    arr[i+1],arr[high] = arr[high],arr[i+1]
    arr1[i+1],arr1[high] = arr1[high],arr1[i+1]
    arr2[i+1],arr2[high] = arr2[high],arr2[i+1]
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,arr1,arr2,low,high,n=0): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,arr1,arr2,low,high,n) 
        # print(pi)
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr,arr1,arr2, low, pi-1,n) 
        quickSort(arr,arr1,arr2, pi+1, high,n) 
def binarySearch (arr, l, r, x,arr1=[]): 
  
    # Check base case 
    if r >= l: 
        a=len(x)
        mid = l + (r - l) // 2
        temp=arr.copy()
        # print(arr[mid][0],x)
        # If element is present at the middle itself 
        if arr[mid][0][0:a] == x and not arr[mid] in arr1: 
            arr1.append(arr[mid])
            temp.pop(mid)
            binarySearch(temp, 0, len(arr)-2, x,arr1)
            return arr1
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
            
        elif arr[mid][0] > x: 
            return binarySearch(arr, l, mid-1, x,arr1) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r,x,arr1) 
  
    else: 
        # Element is not present in the array 
        return arr1
  
# Driver Code 
# arr = [ "Tansang", "Sang", "Son", "sung", "40","" ] 
# arr.sort()
# print(arr)
# x = "S"
  
# # Function call 
# result = binarySearch(arr, 0, len(arr)-1, x) 
  
# print(result)
# print(arr)