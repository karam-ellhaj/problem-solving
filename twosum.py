def twosum(arr,target):

    for i in range(arr.__len__()):
        for j in range(arr.__len__()):
            if i != j :
                if arr[i] + arr[j] == target :
                    return (i,j)
    return None
