import json
import sys
import heapq

class fingerprint:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        return self.word > other.word

    def __gt__(self, other):
        return self.word < other.word

    def __eq__(self, other):
        return self.word == other.word
class heapnode:
    def __init__(self, item, fileHandler):
        self.item = item
        self.fileHandler = fileHandler
class heap:
    def __init__(self):
        self.tempFileHandlers = []
        self.files = []
    
    def heapify(self, arr, i, n):
        left = int(2 * i) + 1
        right = int(2 * i) + 2
        i = int(i)
        if left < n and arr[left].item < arr[i].item:
            smallest = left
        else:
            smallest = i

        if right < n and arr[right].item < arr[smallest].item:
            smallest = right

        if i != smallest:
            (arr[i], arr[smallest]) = (arr[smallest], arr[i])
            self.heapify(arr, smallest, n)

    def construct_heap(self, arr):
        l = len(arr) - 1
        mid = l / 2
        while mid >= 0:
            self.heapify(arr, mid, l)
            mid -= 1


