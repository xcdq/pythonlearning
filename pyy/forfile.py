with open('pyy/pi.txt') as fb:
    # contents = fb.read()
    # print(contents.rstrip())
    # for line in fb:
    #     print(line.rstrip())
    lines = fb.readlines()
pi = ''
for line in lines:
    # print(line.rstrip())
    # pi += line.rstrip()
    pi += line.strip()
print(pi)
