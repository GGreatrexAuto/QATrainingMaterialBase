#!/usr/local/bin/python
import getprocs

   
###################################################################

def igetprocs():
    
    Retn = getprocs.getfirstproc()
    yield Retn
    
    while Retn:
        Retn = getprocs.getnextproc()
        if Retn:
            yield Retn

###################################################################

pids = {pid:value for pid,*value in igetprocs()}
print(pids)
       
