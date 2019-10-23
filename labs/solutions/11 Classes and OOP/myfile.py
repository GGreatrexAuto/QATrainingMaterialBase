import os.path

class MyFile:
   def __init__(self,filename):
       self.__fname = filename

   def __str__(self):
       s = open(self.__fname).read()
       return s

   def __len__(self):
       return os.path.getsize(self.__fname)    

   def get_fname(self):
       return self.__fname
  
