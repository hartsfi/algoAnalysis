## Insersion sort
## Take in tList, go through, key is slot 1, k is slot 0. If slot key-1 is > key, swap their places, work all the way up tList
def insertionSort(tList):
    for i in range(1, len(tList)):
        key = tList[i]
        k = i - 1
        while k >= 0 and tList[k] > key:
            tList[k+1] = tList[k]
            k -= 1
        tList[k+1] = key
    return tList

## Randomized Quicksort



## Stable Counting Sort

