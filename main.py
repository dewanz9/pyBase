import os
"""
text document format 
ID,first,last,age
"""

def createDataBase(name,*columns):
    stringToWrite = ""
    for item in columns:
        if len(stringToWrite)==0:
            stringToWrite = item
        else:
            stringToWrite = stringToWrite+","+item
    if os.path.exists("./" + name + ".txt"):
        print "ERROR- database allready exists"
    else:
        database = open("./" + name + ".txt","w")
        database.write(stringToWrite)
        database.close()
    
class workingBase(object):
    def __init__(self,name):
        self.filename = "./" + name + ".txt"
        if os.path.exists(self.filename):
            self.dataBase = open(self.filename)
            print "database opened successfully"
            test = self.dataBase.readline() 
            self.columns = test.split(",")
            self.dataBase.close()
        else:
            print "ERROR- database doesnt exist"
        
            
    def addEntry(self,*fields):
        if len(fields) < len(self.columns):
            print "not enough columns to add entry"
            
        elif len(fields) > len(self.columns):
            print "too many columns to add entry"
                
        else:
            pass
    

    
createDataBase("swag","first","last","age")
swag = workingBase("swag")
swag.addEntry("sean","connery",14)
