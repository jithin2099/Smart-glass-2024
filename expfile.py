import os

f = open('datasetnames.txt', 'r+')
names = f.read()
names = names.split("\n")
length = len(names)
print(length)
f.close

g = open('datasetnames.txt', 'a')
g.write('\nAkshara')
g.close()

f = open('datasetnames.txt', 'r+')
names = f.read()
names = names.split("\n")
print(names)
length = len(names)
print(length)
f.close