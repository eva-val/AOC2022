import time
import numpy as np
data = open("/home/eva/Advent of Code/2022/Day8.txt").read()
start = time.perf_counter_ns()
data = data.split("\n")
height = len(data)
width = len(data[0])
treez = np.zeros(shape=(height,width),dtype=int)
visible = 0

for i in range(len(data)):
    treez[i] = list(data[i])

visible = (width * 2) + (height * 2 - 4)

for row in range(1, height -1):
    for column in range(1, width -1):
        tree = treez[row, column]
        up = (treez[:row, column] < tree).all()
        down = (treez[row+1:, column] < tree).all()
        left = (treez[row, :column] < tree).all()
        right = (treez[row, column+1:] < tree).all()
        if not(not(up) and not(down) and not(left) and not(right)): #gross
            visible += 1
print(time.perf_counter_ns() - start)
print(visible)