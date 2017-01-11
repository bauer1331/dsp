#Rejected code for regex

def histogram_simple(s):#page 103
	d = dict()
	for c in s:
		if not c in d:
			d[c] = 1
		else:
			d[c] += 1
	print d	
print"    "



def mymethod():
    return [[1,2,3,4],
            [1,2,3,4],
            [1,2,3,4],
            [1,2,3,4]]

mylist = mymethod()

for thing in (i[1] for i in mylist):
    print thing

# this bit is meant to be outside the for loop, 
# I mean it to represent the last value thing was in the for
#if thing:
 #   print thing

"""
test5 = dict()
import string 
def process_line(line, hist):
	for word in line:
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower

		hist[word] = hist.get(word, 0) + 1
		return hist
print "   "
print process_line(test4, test5)
#print test 
"""



"""









L1 = []
for elem in test3:
	L1.extend(elem.strip().split(','))
print L1



    updated = [s[0]]
    for char in s[1:]:
        if char == s[0]:
            updated.append('*')
        else:
            updated.append(char)
    return ''.join(updated)


#def process_set(x):
#	hist = dict()
#	for line in x:
#		process_line(line,hist)
#	print hist
import string

test2 = dict()
def process_line(line, hist):
	for word in line.split():
		word = line.strip(string.punctuation + string.whitespace)
		word = line.lower

		hist[word] = hist.get(word, 0) + 1




print process_line(test,test2)


def get_unique(x):
	import pandas as pd
	x = set(x.iloc[:,0])
	x_list = list(x)
	print x_list

print get_unique(test)






import csv

def get_col(filename, col_num, delim):
	file = csv.reader(open(filename,"rb"),delimiter=delim)
	degree = []
	for row in file:
		degree.append(row[col_num])

degree = get_col('faculty.csv',1,',')

print degree

#count_degree = {x:degree.count(x) for x in degree}
#print count_degree


#	def process_file(filename):
#	hist = dict()
#	fp = open(filename)
	
#	for word in word:
#		hist[word] = word + 1
#index_not = s.find('not')

"""