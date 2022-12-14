#import time
#start = time.perf_counter_ns()
data = open("/home/eva/Advent of Code/2022/Day7.txt").read().strip().split("$")

directory = ['']
directorysize = {}
for command in data[2:]:
    output = command.strip().split("\n")
    #print("/".join(directory) + "$ " + output[0]) # prints the "terminal" output
    if output[0] == "cd dcqnblb":
        print("break")
    if output[0].startswith("cd") and not(output[0].endswith("..")):
        cdto = output[0].split(' ')[1]
        #print(cdto)
        directory.append(cdto)

    elif output[0] == "cd ..":
        directory.pop()
        #temp = directory.copy()
        #for i in range(len(temp)):
        #    key = "/".join(temp)
        #    if key != '':
        #        directorysize[key] += size
        #    temp.pop()

    elif output[0] == "ls":
        size = 0
        if len(output) < 2:
            print("break")
        #print(output[1:])
        for line in output[1:]:
            if not(line.startswith("dir")):
                print(int(line.split(" ")[0]))
                size += int(line.split(" ")[0])
            else:
                key = "/".join(directory) + "/" + line.split(" ")[1]
                if key == '': key = '/'
                directorysize[key] = 0
        key = "/".join(directory)
        if key == '': key = '/'
        directorysize[key] = size
        print("\"" + "/".join(directory) + "\"" " Size: " + str(size))

#for keys in directory[::-1]:
#    if keys != '/' and keys.count('/') < 2:
#        directorysize['/'] += directorysize[keys]
#for i in range(len(directory)):
#    key = "/".join(directory)
#    if key != '':
#        directorysize[key] += size
#    directory.pop()
fuck = 0
for key in directorysize:
    #print(directorysize[size])
    if directorysize[key] <= 100000:
        fuck += directorysize[key]
print(fuck)
#print(directorysize)



#print(time.perf_counter_ns() - start)