"""Part 1 Regular expressions"""

import csv

def get_col(filename, col_num):
	files = csv.reader(open(filename,"rb"),delimiter=',')
	next(files)
	degree = []
	for row in files:
		degree.append(row[col_num])
	return degree

#print get_col('faculty.csv',1)



#print test
#print test

def getDegrees(filename, split_on):
	update = []
	for line in filename:
		x = line.split(split_on)
		update.append(x)
	return update
		#print x


#print getDegrees(test)



def traverse(o, tree_types=(list,tuple)):
	if isinstance(o, tree_types):
		for value in o:
			for subvalue in traverse(value, tree_types):
				yield subvalue
	else:
		yield o

#print list(traverse(test))
#print "    "



import string
def histogram(s):
	d = dict()
	for c in traverse(s):
		c = c.translate(None, string.punctuation)
		c = c.lower()
		if c != '':
			if not c in d:
				d[c] = 1
			else:
				d[c] += 1
	print d



def get_column ( array, column_number ):
    #try:
    return [row[column_number] for row in array]
    





degrees = get_col('faculty.csv',1)
degrees2 = getDegrees(degrees, ' ')
degrees3 = list(traverse(degrees2))
print histogram(degrees3)

titles = get_col('faculty.csv',2)
print '     '
print histogram(titles)

email = get_col('faculty.csv',3)
print "     "
print email

domains = getDegrees(email, '@')
domains2 = get_column(domains, 1)
print '     '
print set(domains2)