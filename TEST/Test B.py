#Test Part A
#Submitted by Colton Dean c0741555
from statistics import mean
import math
import statistics

fileName = str(input('Please input the grading file name with .txt :'))

file_pointer = open(fileName, 'r') #opens file for READING 

data = [] #python list to store data from file

for line in file_pointer:

    line = line.rstrip() #removes trailing white space (i.e. \n) from line 
    
    stringParts = line.split(" ")

    data.append(float(stringParts[1])) #append line to end of list
    

file_pointer.close() #close access to the file


print("The average was", mean(data))
print("The highest increase was", max(data))
print("The lowest increase was", min(data))

#x = statistics.mean(data)
#print(x)

#y = statistics.median(data)
#print(y)

#z = statistics.mode(data)
#print(z)

#a = statistics.stdev(data)
#print(a)

#b = statistics.variance(data)
#print (b)
