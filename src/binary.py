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

def binSearch(arr, val):
    min = 0
    max = len(arr) - 1
    numIts = 0
    while True:
        m = round((min + max) / 2)
        if arr[m] < val:
            numIts += 1
            min = m + 1
        elif arr[m] > val:
            numIts += 1
            max = m - 1
        else:
            return [numIts, m]

words = setUpDict("words.txt")

find = words[int(r.random() * (len(words) - 1))]
results = binSearch(words, find)
print("Found the word ", find, " after ", results[0], " iterations at index ", results[1])


