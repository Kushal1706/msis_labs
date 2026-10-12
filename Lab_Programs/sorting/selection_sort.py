arr=[2,4,6,1,5]
n=len(arr)

def selection_sort(arr):
    for i in range(n):
        minidx=i
        for j in range(i+1,n):
            if arr[j]<arr[minidx]:
                minidx=j
        arr[i],arr[minidx]=arr[minidx],arr[i]
    return arr

print(selection_sort(arr))