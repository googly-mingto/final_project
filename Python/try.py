import pandas as pd
import numpy as np 
from node import *
file = pd.read_csv("data/small_maze.csv")
value = file.values
title = file.columns

nd_array = np.array([Node(i+1) for i in range(np.shape(value)[0])])

for i in range(np.shape(file)[0]):
	for element in value[i][1:5]:
		if not np.isnan(element):
			for index in np.where(value[i][1:5] == element):
				nd_array[i].setSuccessor(int(element), index+1, 2)

print(type(nd_array[1].Successors[0][1].name))
