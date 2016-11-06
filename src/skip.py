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

def skipSearch(arr, val):
    for i in range(5, 100, 5):
        num = i
        numIts = 0
        while arr[num] < val:
            numIts += 1
            num += i
        while arr[num] >= val:
            numIts += 1
            num -= 1
        print("Found the word ", val, " after ", numIts, " iterations at index ", num, " (search interval ", i, ")")
       
words = setUpDict("words.txt")
find = words[int(r.random() * (len(words) - 1))]
skipSearch(words, find)