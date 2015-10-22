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
    database = open(name+".txt","w")
    database.write(stringToWrite+"\n")
    database.close()
    
createDataBase("swag","first","last","age")
