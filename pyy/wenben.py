from os import error


filename = 'the.txt'
try:
    with open(filename)as fb:
        contents = fb.read()
except error:
    print(error)
else:
    words = contents.split()
    numwords = len(words)
    print(filename+" has "+str(numwords)+" words.")