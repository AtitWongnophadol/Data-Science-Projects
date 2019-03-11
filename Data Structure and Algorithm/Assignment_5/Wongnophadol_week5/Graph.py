# Assignment 5 by Atit Wongnophadol
# Dec 25, 2018

import os
import numpy as np
import networkx as nx

# set my workspace
path="/Users/plodium2000/Dropbox/MIDS program/Courses/Data Structure and Algorithm/1B_assignments_2016_11_10/Assignment_5/Assignment_5 submission/"
os.chdir(path)

# use numpy to convert data into matrix
adjMatrix = np.loadtxt("adj.txt", dtype=int)

# use networkx to convert a matrix into a graph
g = nx.Graph(adjMatrix)

# function to calculate total number of nodes
def equidistant (g, n1, n2):

    j = 0
    count = 0
    
    for j in g.node():
    
        # for any given node, if it has the same length to target, count it
        length_1 = nx.dijkstra_path_length(g, source=j, target=n1)
        length_2 = nx.dijkstra_path_length(g, source=j, target=n2)
        
        if length_1 == length_2:
            count+=1
        
    return (count)

# Specify output file path and filename
input_file_path = "input.txt"

# Specify output file path and filename
output_file_path = "output.txt"

# Read the input file and write out scrambled message of each line into the output file.
with open(input_file_path,'rt') as input_file, open(output_file_path,'wt') as output_file:
    for line in input_file:
        # Print statements to quickly test the accuracy of the program.
        param = line.rstrip().replace(" ","")
        output_file.write(str(equidistant(g, int(param[0]), int(param[1])))+"\n")
