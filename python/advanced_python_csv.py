import csv

def get_col(filename, col_num):
	files = csv.reader(open(filename,"rb"),delimiter=',')
	next(files)
	degree = []
	for row in files:
		degree.append(row[col_num])
	return degree

email = get_col('faculty.csv',3)

#print email

with open('emails.csv', 'w') as csvfile:
	wr = csv.writer(csvfile)
	for i in email:
		wr.writerow([i])

