#mask.py
#https://github.com/lucas7234/covidanalyze
#analyze csv file and draw graph by numpy, matplotlib

#see readme.md to use matplotlib and python
import csv
import numpy as np
from matplotlib.pyplot as plt

#path setting and read files
path = input('File Path(C://..., Must be CSV): ')
f = open(path, 'r', encoding = 'utf-8')
lines = csv.reader(f)

header = next(lines)

#print as text
print()
print('=' * 50)
#print header
for i in header:
  print(i, end = ' ')
print()
for line in lines:
  print(line, end = ' ')
print()
print('=' * 50)

#print as matplotlib graph
###Developing
###
###

#close csv file
f.close()
