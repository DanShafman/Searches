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
    while True:
        m = round((min + max) / 2)
        if arr[m] < val:
            min = m + 1
        elif arr[m] > val:
            max = m - 1
        else:
            return m

words = setUpDict("words.txt")

find = words[int(r.random() * (len(words) - 1))]
print("The index of the word ", find, " is ", binSearch(words, find))


