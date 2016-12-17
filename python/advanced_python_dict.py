import csv
import pandas as pd

faculty = pd.read_csv('faculty.csv')
#print faculty
namesFL = faculty.name



faculty1 = pd.read_csv('faculty.csv')
dte = faculty[[' degree', ' title',' email']]


def get_col(filename, col_num):
	files = csv.reader(open(filename,"rb"),delimiter=',')
	next(files)
	degree = []
	for row in files:
		degree.append(row[col_num])
	return degree


def makeSplit(filename, split_on):
	update = []
	for line in filename:
		x = line.split(split_on)
		update.append(x)
	return update

def get_column ( array, column_number ):
    #try:
    return [row[column_number] for row in array]

#def makeDict(names, )

#names = get_col('faculty.csv',0)
split_names = makeSplit(namesFL, ' ')
last_names = get_column(split_names,-1)
first_names = get_column(split_names,0)
namesTlf = pd.Series(zip(last_names, first_names))
namesTfl = pd.Series(zip(first_names, last_names))

pd_last_names = pd.Series(last_names)

last_names_df = pd.concat([pd_last_names.reset_index(drop=True), dte], axis=1)
last_names_df.columns = ['name','degree','title','email']
#headers = last_names_df.dtypes.index
#print headers
#print last_names_df
#print type(last_names_df)


#dict_last_name = last_names_df.set_index('name').to_dict()
#print dict_last_name
from collections import defaultdict
faculty_dict = {k: g[['degree', 'title', 'email']].values.tolist() for k,g in last_names_df.groupby("name")}



fl_names_df = pd.concat([namesTfl.reset_index(drop=True), dte], axis=1)
fl_names_df.columns = ['name','degree','title','email']
dict_fl_name = fl_names_df.set_index('name').T.to_dict('list')
print dict_fl_name


lf_names_df = pd.concat([namesTlf.reset_index(drop=True), dte], axis=1)
lf_names_df.columns = ['name','degree','title','email']
dict_lf_name = lf_names_df.set_index('name').T.to_dict('list')
print "    "
print dict_lf_name


#dictLN = {}
#for x in range(len(last_names_df)):
#	currentid = last_names_df.iloc[x,0]
#	currentvalue = last_names_df.iloc[x,1:]
#	dictLN.setdefault(currentid, [])
#	dictLN[currentid].append(currentvalue)
#print faculty_dict
print "   "
first3_fac = {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}
print first3_fac
print "   "
first3_fl_name = {k: dict_fl_name[k] for k in dict_fl_name.keys()[:3]}
print first3_fl_name
print '    '
first3_lf_name = {k: dict_lf_name[k] for k in dict_lf_name.keys()[:3]}
print first3_lf_name
#



