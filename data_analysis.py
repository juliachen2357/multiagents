# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 12:45:47 2023

@author: czyji
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import math
# Specify the path to your CSV file
csv_file_path = 'C:/Users/czyji/Downloads/example_109V1_20231202233215.csv'

# Open the CSV file
locations={}
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Each row is a list of values
        split_string = row[0].split()
        
        for agent_num in range(int(len(split_string)/2)):
            for index in range(0,2):
                locations[agent_num,index]=[]
        break
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Each row is a list of values
        split_string = row[0].split()                
        for agent_num in range(int(len(split_string)/2)):
            for index in range(0,2):
                locations[agent_num,index].append(float(split_string[agent_num*2+index]))
                
                
# Sample list of values
data_summary={}
plt_colors = []
plt_colors.append([0.8500, 0.3250, 0.0980])  # orange0
plt_colors.append([0.0, 0.4470, 0.7410])  # blue1
plt_colors.append([0.4660, 0.6740, 0.1880])  # green2
plt_colors.append([0.4940, 0.1840, 0.5560])  # purple3
plt_colors.append([0.9290, 0.6940, 0.1250])  # yellow4
plt_colors.append([0.3010, 0.7450, 0.9330])  # cyan5
plt_colors.append([0.6350, 0.0780, 0.1840])  # chocolate6

plt_colors.append([0.8500, 0, 0])  # red7
plt_colors.append([0.0, 0.4470, 0.])  # blue8
plt_colors.append([0, 0, 0.8])  # green9

plt_colors.append([0.2, 0.2, 0.2])    # dark gray 10
plt_colors.append([0.8, 0.8, 0.8])    # light gray 11
plt_colors.append([1.0, 0.0, 0.0])    # pure red 12
plt_colors.append([0.0, 1.0, 0.0])    # pure green 13 
plt_colors.append([0.0, 0.0, 1.0])    # pure blue 14
plt_colors.append([1.0, 1.0, 0.0])    # pure yellow 15
plt_colors.append([1.0, 0.5, 0.0])    # orange 16
plt_colors.append([0.5, 0.0, 0.5])    # magenta 17
plt_colors.append([0.0, 0.5, 0.5])    # teal 18
plt_colors.append([0.5, 0.5, 0.0])    # olive 19
for agent_num in range(int(len(split_string)/2)):
    for index in range(0,2):
        
        values=locations[agent_num,index]
        differences = [abs(values[i] - values[i - 1]) for i in range(1, len(values))]
        data_summary[agent_num,index]=[np.mean(differences),np.var(differences)]
    plt.plot(locations[agent_num,0], locations[agent_num,1], label='Line 1',color=plt_colors[agent_num])
plt.show()
closest_distance_each_agent={}
for agent1 in range(int(len(split_string)/2)):
    closest_distance_each_agent[agent1]=[]
for row in range(len(locations[agent1,0])): 
    for agent1 in range(int(len(split_string)/2)):
        x1, y1 = locations[agent1,0][row], locations[agent1,1][row]
        closet_distance=999
        for agent2 in range(int(len(split_string)/2)):
            if agent1 != agent2:  # Avoid comparing an agent to itself
                x2, y2 = locations[agent2,0][row], locations[agent2,1][row]
                distance_12 = calculate_distance(x1, y1, x2, y2)
                if closet_distance>distance_12:
                    closet_distance=distance_12 
        closest_distance_each_agent[agent1].append(distance_12)

for agent_num in range(int(len(split_string)/2)):
    plt.plot(closest_distance_each_agent[agent_num],'*',color=plt_colors[agent_num])
        

























  
        
