#!/usr/local/bin/python
# Python 3 version

# Construct an index
Index = []
fh = open('messier.txt', encoding='latin_1')

while True:
    line = fh.readline()
    if not line: break
    if line.startswith('M'):
        num = line[1:6].rstrip()
        Index.append(fh.tell() - len(line))
    
while True:
    num = input("Enter a Messier number(0 to exit): ")
    if num.startswith("M"):
        num = int(num[1:])
    elif num:
        num = int(num)
    else:
        num = 0
        
    if num < 1: break
    num = num - 1
    
    fh.seek(Index[num])
    print(fh.readline())
    
