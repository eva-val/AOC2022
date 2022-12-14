#import time
#start = time.perf_counter_ns()
data = open("/home/eva/Advent of Code/2022/Day7.txt").read().strip().split("$")

rootdir = {"files": []}
depth = 0
directory = []
for command in data[2:]:
    output = command.strip().split("\n")
    #print(output[0])
    if depth == 0:
        currentdir = rootdir
        #print("setting root dir")
    if output[0].startswith("cd") and not(output[0].endswith("..")):
        cdto = output[0].split(' ')[1]
        #print(cdto)
        directory.append(cdto)
        currentdir = currentdir[cdto]
        depth += 1
    elif output[0] == "cd ..":
        #for path in directory:
        #    previousdir = rootdir
        #cdto = directory.pop()
        #currentdir = currentdir[cdto]
        depth -= 1

    if output[0] == "ls":
        #print(output[1:])
        for line in output[1:]:
            if line.startswith("dir"):
                name = str(line.split(" ")[1])
                currentdir[name] = {"files": []}

                #print("adding dir " + name)
            else:
                currentdir["files"].append(line)
    print(directory)

print(rootdir)



#print(time.perf_counter_ns() - start)