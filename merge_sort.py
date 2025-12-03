arr = list(map(int,input("Enter a array : ").split(" ")))


def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid_index = len(arr) //2
    left_arr = merge_sort(arr[:mid_index])
    right_arr = merge_sort(arr[mid_index:])
    return merge(left_arr,right_arr)
def merge(left_arr,right_arr):
    result = []
    i=j=0
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i+=1
        else:
            result.append(right_arr[j])
            j+=1
    result.extend(left_arr[i:])
    result.extend(right_arr[j:])

    return result
print(merge_sort(arr))