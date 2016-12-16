# -*- coding: utf-8 -*-
# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
import numpy



football = csv.reader(open('football.csv',"rb"),delimiter=',')
name = []
for row in football:
	name.append(row[0])

football = csv.reader(open('football.csv',"rb"),delimiter=',')
#csv_foot = csv.reader(football, delimiter = ',')
goals = []
for row in football:
	goals.append(row[5])

goals = numpy.matrix(map(int, goals[1:]))
#print goals

import csv
football = open('football.csv')
csv_foot = csv.reader(football)

goals_against = []
for row in csv_foot:
	goals_against.append(row[6])

goals_against = numpy.matrix(map(int, goals_against[1:]))
goals_against1 = goals_against[0]
#print goals_against

diff= abs(goals - goals_against)

#print diff.index(diff.min())
index_two = numpy.unravel_index(diff.argmin(), diff.shape)


print name[index_two[1]+1]

