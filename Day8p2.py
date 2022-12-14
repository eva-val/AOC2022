import time
import numpy as np
data = open("/home/eva/Advent of Code/2022/Day8.txt").read()
start = time.perf_counter_ns()
data = data.split("\n")
height = len(data)
width = len(data[0])
treez = np.zeros(shape=(height,width),dtype=int)
highscore = 0
for i in range(len(data)):
    treez[i] = list(data[i])

for row in range(0,height): #0, height
    for column in range(0, width): #0, width
        score = 0 
        uscore = 0; dscore = 0; lscore = 0; rscore = 0
        tree = treez[row, column]
        up = treez[:row, column][::-1]
        down = treez[row+1:, column]
        left = treez[row, :column]
        left = left[::-1]
        right = treez[row, column+1:]
        if up.size > 0:
            for num in up:
                uscore += 1
                if num >= tree: 
                    break

        if down.size > 0:
            for num in down:
                dscore += 1
                if num >= tree: 
                    break
     
        if left.size > 0:
            for num in left:
                lscore += 1
                if num >= tree: 
                    break

        if right.size > 0:
            for num in right:
                rscore += 1
                if num >= tree: 
                    break 

        score = uscore * dscore * lscore * rscore
        if score > highscore: 
            highscore = score

print(time.perf_counter_ns() - start)
print(highscore)