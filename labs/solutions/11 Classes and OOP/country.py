#!/usr/local/bin/python
class Country:

    index = {'name':0,'population':1,'capital':2,'citypop':3,'continent':4,
             'ind_date':5,'currency':6,'religion':7,'language':8}
    
    # Insert your code here
    # 1a) Implement a constructor    
    def __init__(self, row):
        self.__attr = row.split(',')
        
        # 1e) Added to support + and -
        self.__attr[Country.index['population']] = \
            int(self.__attr[Country.index['population']])
            
    # 1b) Implement a print method        
    def print(self):
        print(self.__attr[Country.index['name']])
        
    # 1c) Overloaded stringification
    def __str__(self):
        return self.__attr[Country.index['name']]
        # 1g) Formating the output
        #return "{0:<32} {1:>010}".format(self.name, self.population)
        
    # Getter methods
    # 1d) Implement a getter method for country name
    @property
    def name(self):
        return self.__attr[Country.index['name']]
    
    @property
    def population(self):
        return int(self.__attr[Country.index['population']])
        
    # 1e) Overloaded + and -
    def __add__(self,amount):
        self.__attr[Country.index['population']] += amount
        return self
        
    def __sub__(self,amount):
        self.__attr[Country.index['population']] -= amount
        return self
        
    # If time allows:
    # 1f)  Overloaded == (for index search)
    def __eq__(self,key):
        return (key == self.name)
