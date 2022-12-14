import time
start = time.perf_counter_ns()
data = open("/home/eva/Advent of Code/2022/Day6.txt").read()

for i in range(14,len(data)):
    #print(data[i-4:i])
    snippet = data[i-14:i]
    duplicate = 0
    for char in snippet:
        #print(char)
        #print(snippet.count(char)-1)
        duplicate += snippet.count(char)-1
    if duplicate == 0:
        print(i)
        break
print(time.perf_counter_ns() - start)