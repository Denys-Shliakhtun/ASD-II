from random import shuffle

def sizeInput():
    n = int(input("Enter the amount of numbers: "))
    k = n + 1
    while k > n:
        k = int(input("Enter the amount of displayed numbers: "))
    return n, k

def arrGen(n):
    ch = 0
    while ch < 1 or ch > 3:
        ch = int(input("Input 1 for standart array, 2 for reversed or 3 for shuffled: "))
    if ch == 1:
        arr = [x + 1 for x in range(n)]
    elif ch == 2:
        arr = [x for x in range(n, 0, -1)]
    elif ch == 3:
        arr = [x + 1 for x in range(n)]
        shuffle(arr)
    return arr

def arrOutput(arr, k):
    for i in range(k):
        print(arr[i], end = ' ')

def arrBubbleSort(arr):
    length = len(arr)
    nSwap = nComp = 0
    for i in range(0, length):
        for j in range(0, length - i - 1):
            nComp +=1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                nSwap += 1
    return nComp, nSwap

def arrBubbleSortOptim(arr):
    length = len(arr)
    i = nSwap = nComp = 0
    flag = True
    while flag:
        swapped = False
        for j in range(0, length - i - 1):
            nComp +=1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                nSwap += 1
        i += 1
        if i == length or not swapped:
            flag = False
    return nComp, nSwap

def arrCombSort(arr):
    gap = length = len(arr)
    nComp = nSwap = 0
    swapped = True    
    while gap > 1 or swapped:
        gap = max(1, (gap * 10 // 13))
        if 8 < gap < 11:
            gap = 11
        swapped = False
        for i in range(length - gap):
            nComp +=1
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
                nSwap += 1        
    return nComp, nSwap

n, k = sizeInput()
arr = arrGen(n)


print("\nGenerated array:")
arrOutput(arr, k)

arrBubble = [arr[i] for i in range(len(arr))]
nCompBubble, nSwapBubble = arrBubbleSort(arrBubble)
print("\n\nBubble sort:")
arrOutput(arrBubble, k)
print("\nNumber of comparisons:", nCompBubble)
print("Number of swaps:", nSwapBubble)

arrBubbleOptim = [arr[i] for i in range(len(arr))]
nCompBubbleOptim, nSwapBubbleOptim = arrBubbleSortOptim(arrBubbleOptim)
print("\nBubble optimized sort:")
arrOutput(arrBubbleOptim, k)
print("\nNumber of comparisons:", nCompBubbleOptim)
print("Number of swaps:", nSwapBubbleOptim)

arrComb = [arr[i] for i in range(len(arr))]
nCompComb, nSwapComb = arrCombSort(arrComb)
print("\nComb sort:")
arrOutput(arrComb, k)
print("\nNumber of comparisons:", nCompComb)
print("Number of swaps:", nSwapComb)
