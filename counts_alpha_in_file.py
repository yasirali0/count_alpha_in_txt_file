'''
This program takes a txt file as input and prints the
the frequency of alphabets in the file in a pretty manner
'''

from os import strerror

fn = input("Enter the file name: ")
try:
    file = open(fn, 'r')
except IOError as e:
    print("Can't open the file", strerror(e.errno))
    exit(e.errno)

cnts = {}
line = file.readline()

try:
    while line != '':
        line = line.lower()
        for alpha in line:
            if not alpha.isalpha():
                continue
            if alpha not in cnts.keys():
                cnts[alpha] = 1
            else:
                cnts[alpha] += 1
        line = file.readline()
        
    file.close()
    
    for key in sorted(cnts.keys()):
        print(key, " -> ", cnts[key])
        
except Exception as e:
    print("An error occured", e)
    file.close()
