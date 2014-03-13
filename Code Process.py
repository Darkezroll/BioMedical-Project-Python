#!/usr/bin/env python

f = open("input.txt", "r")

dna = f.readlines()

a = dna[0]
b = dna[1]

mutation = 0

transitions = set([('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')])
ratio = {True: 0.0, False: 0.0}


for i in zip(a,b):
    
    if i[0] != i[1] :
        
        mutation = mutation + 1
        
        ratio[i in transitions] += 1
    
    
print ("Counting Point Mutations : " ,mutation)
print ("Transition : " ,ratio[True])
print ("Transversion : " ,ratio[False])
print ("Transition/Transversion Ratio : " ,ratio[True] / ratio[False])
