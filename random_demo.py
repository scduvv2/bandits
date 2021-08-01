#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 13:20:25 2021

@author: eshasharma
"""#
# import csv and random libraries

import csv
import random

# for random example 
from datetime import datetime

          
# Introductin to csv library and dict reader       
with open('BanditsData.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
           print(row)
           print(row['Sample A'])

with open('homes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
           print(row)
  
# Introduction to random library and seed  

from random import seed
from random import random
from random import sample
# seed random number generator - this will be used to generate the random 
# numbers 
seed(1)
# generate some random numbers
print(random(), random(), random())
# reset the seed
seed(2)
# generate some random numbers
print(random(), random(), random()) 
# generate some random numbers based on current date    
seed(datetime.now())
# Generate 10 random numbers 
print(random(), random(), random())           
s = sample(range(1000), k=10)
print(s)