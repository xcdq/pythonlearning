import os
# with open(age.txt, 'r') as fp:
#     fp.read()
f = open("age.txt")
line = f.readline()
num = 1
while line:

    line = line.strip()
    # print(line)
    # print(line, line[6:10])
    print(num, line, int(line[6:10]), 2021-int(line[6:10]))
    strrr = str(2021-int(line[6:10]))+'\n'
    with open("hello.txt", 'a')as fp:
        fp.write(strrr)
    line = f.readline()
    num += 1
