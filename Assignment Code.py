"""

Name:		Pratham Gupta
Roll No:	2018072
Section:	A
Group:		8

"""

import csv

filename1 = "Journal.csv"

data = []		#list which will collect data
hindex = []		#list which contains the h-index of the data
ifactor = []	#list which contains the i-factor of the data

#Extracting data from csv file
with open(filename1, 'r') as cfile:
	creader = csv.reader(cfile)

	for row in creader:
		data.append(row)

	for row in data:
		hindex.append(float(row[1]))
		ifactor.append(float(row[2]))

cfile.close();

#Finding out the correlation coefficient between H-Index and Impact Factor
#Finding mean of each variable
himean = sum(hindex)/len(hindex)	#mean of h-index
ifmean = sum(ifactor)/len(ifactor)	#mean of i-factor
	


#Finding variance of each variable
if_sq = 0
hi_sq = 0
term = 0
	
for i, j in zip(hindex, ifactor) :
	hi_sq += i*i
	if_sq += j*j
	term += (i-himean)*(j-ifmean)  

sd_hi = (hi_sq/len(hindex)-(himean**2))**0.5	#standard deviation of h-index
sd_if = (if_sq/len(ifactor)-(ifmean**2))**0.5	#standard deviation of i-factor
numerator = term/len(hindex)					#covariance 

cor = numerator/(sd_if*sd_hi)					#correlation of the h-index and i-factor of journals in computer science

print("\n\n\nCorrelation Coefficient : " + str(cor))




#Finding regression line for training data
thindex=hindex[:497]
tifactor=ifactor[:497]

#Finding mean of each variable for training data
himean = sum(thindex)/len(thindex)
ifmean = sum(tifactor)/len(tifactor)
	
#Finding variance of each variable for training data
tif_sq = 0
thi_sq = 0
term_t = 0
	
for i, j in zip(thindex, tifactor) :
	thi_sq += i*i
	tif_sq += j*j
	term_t += (i-himean)*(j-ifmean)  

sd_hi = (thi_sq/len(thindex)-(himean**2))**0.5
sd_if = (tif_sq/len(tifactor)-(ifmean**2))**0.5
cov = term_t/len(thindex)

print("\n\n\nCorrelation : " + str(cov/(sd_hi*sd_if)))



#Plotting the data points on a graph
import matplotlib.pyplot as plt
import tkinter
plt.scatter(hindex, ifactor, c='r')


#Finding the regression line
coeff_a = round(cov/(sd_hi**2), 3)

coeff_b = round(ifmean - coeff_a*himean, 3)

print("\n\n\nRegression Line : y = " + str(coeff_a) + "x + " + str(coeff_b))

#Plotting the Regression Line
y_func=[]
for i in range(len(hindex)):
	y_func.append(coeff_a*hindex[i]+coeff_b)

plt.plot(hindex, y_func)
plt.show()


#Predicting Impact Factor of test data and error 
test_hi = hindex[497:]
test_if = ifactor[497:]
error = []

for i, j, k in zip(thindex, tifactor, data) :
	p_if = coeff_a*i + coeff_b
	k.append(p_if)
	error.append((p_if-j)/j)

rms_error = 0
for e in error:
	rms_error+=e*e
rms_error=rms_error/len(error)

print("\n\n\nError between Predicted and Actual Impact Factor : " + str(rms_error))

#Predicting Impact Factor for Conferences 
filename2 = 'Conferences.csv'

write_if = []
read_hi = []
data = []

with open(filename2, 'r') as csvfile:
	csvreader = csv.reader(csvfile)

	for row in csvreader:
		data.append(row)

	for row in data:
		read_hi.append(float(row[1]))


csvfile.close();

for i, j in zip(read_hi, data):
	write_if.append(round(coeff_a*i+coeff_b,3))
	j.append(round(coeff_a*i+coeff_b,3))

with open(filename2, 'w') as csvfile:
	csvwriter = csv.writer(csvfile) 
	csvwriter.writerows(data)

csvfile.close();


	












			

