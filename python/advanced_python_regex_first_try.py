"""Part 1 Regular expressions"""

def get_csv(filename, col):
	import pandas as pd
	fp = pd.read_csv(filename)
	#print fp

	#x = set(fp.iloc[:,col])
	x_list = list(fp[col])
	return x_list




#print test
#print test

def getDegrees(filename):
	update = []
	for line in filename:
		x = line.split(" ")
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
print"    "

degrees = get_csv('faculty.csv',1)
degrees2 = getDegrees(degrees)
degrees3 = list(traverse(degrees2))
print histogram(degrees3)

titles = get_csv('faculty.csv',2)
print '     '
print titles
#titles2 = getDegrees(titles)
print '     '
#print titles2
#titles3 = list(traverse(titles2))
#print '     '
#print titles3
#print '     '
print histogram(titles)

