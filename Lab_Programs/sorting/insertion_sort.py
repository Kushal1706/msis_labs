arr=[2,4,6,1,5]
n=len(arr)

def insertion_sort(arr):
    for i in range(1,n-1):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

print(insertion_sort(arr))