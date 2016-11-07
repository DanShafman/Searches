import sys
import random as r
import math

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
    num = round(math.sqrt(len(arr)-1))
    numIts = 0
    while arr[num] < val:
            numIts += 1
            num += round(math.sqrt(len(arr)-1))
    while arr[num] >= val:
        numIts += 1
        num -= 1
    print("Found the word ", val, " after ", numIts, " iterations at index ", num, " (search interval ", math.sqrt(len(arr)), ")")
    return numIts
words = setUpDict("words.txt")

its = []
for i in range(0, 100):
    find = words[int(r.random() * (len(words) - 1))]
    its.append(skipSearch(words, find))
avg = sum(its) / 100
print(avg)

y = []
for i in its:
    y.append(abs(avg - i))
print(sum(y) / 100)