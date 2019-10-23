#!/usr/local/bin/python
import sys
import mytimer
#import mymodules.mytimer2 as mytimer

mytimer.start_timer()
lines = 0
try:
    for row in open ("words"):
        lines += 1
except IOError as err: 
    print ("Could not open:", 
           err.filename, err.args[1],
           file=sys.stderr)           
    
mytimer.end_timer()
print ("Number of lines:",lines)

try:
    mytimer.end_timer()
except SystemError as err:
    print ("end_timer error:",err, file=sys.stderr)

print ("We are all done")
