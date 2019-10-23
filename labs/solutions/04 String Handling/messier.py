#!/usr/local/bin/python
# Python 3 version

for line in open('messier.txt', encoding = 'latin_1'):
    if not line: break
    if line.startswith('M'):
        # Slice each field
        Mnum = line[:6].rstrip()
        Name = line[6:40].rstrip()
        if not Name: Name = 'no name'
        Type = line[40:64].rstrip()
        Cons = line[64:].rstrip()

        #print("|"+Mnum+"|"+Name+"|"+Type+"|"+Cons+"|")
        print(f"|{Mnum}|{Name}|{Type}|{Cons}|")
        

