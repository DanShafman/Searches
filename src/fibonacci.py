import sys
import random as r

sys.setrecursionlimit(1000000)

def setUpDict(dict):
    with open(dict, "r") as myfile:
        words=myfile.read().replace("\n", " ").split(" ")
    words.sort()
    return words

def round(num):
    if(num + 0.5) >= (int(num) + 1):
        return int(num)+1
    else:
        return int(num)

def initFibs():
    fibs = [1, 1]
    for i in range(2, 1000):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs

def fibSearch(arr, val, fibArr):
    f = 0
    for num in range(0, len(fibArr)):
        if fibArr[num] >= len(arr):
            k = num
            break
    numIts = 0
    while True:
        if arr[fibArr[k-1]] > val:
            numIts += 1
            arr = arr[:(fibArr[k-1])]
            k -= 1
        elif arr[fibArr[k-1]] < val:
            numIts += 1
            arr = arr[fibArr[k-1]:]
            k -= 2
        else:
            return numIts

words = setUpDict("words.txt")
fibs = initFibs()
x = []
avg = 0
for i in range(0, 1000):
    find = words[int(r.random() * (len(words) - 1))]
    result = fibSearch(words, find, fibs)
    print("Found the word ", find, " after ", result, " iterations")
    x.append(result)
    
avg = sum(x) / 1000
print(avg)
y = []
for i in x:
    y.append(abs(avg - i))
print(sum(y) / 1000)

