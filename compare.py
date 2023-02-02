from pylab import *
import csv
from numpy import linspace
import sys

frequence1=30
frequence2=30

duree=10
ord1=[]
ord2=[]

with open ('csv/'+str(sys.argv[1])+'.csv', newline='') as csvfile :
	reader=csv.reader(csvfile,quoting=csv.QUOTE_NONNUMERIC)
	for row in reader :
		ord1=row[:frequence1*duree]
		break

with open ('csv/'+str(sys.argv[2])+'.csv', newline='') as csvfile :
	reader=csv.reader(csvfile,quoting=csv.QUOTE_NONNUMERIC)
	for row in reader :
		ord2=row[:frequence2*duree]
		break




abs1=linspace(0,duree,len(ord1))
abs2=linspace(0,duree,len(ord2))

plot(abs1,ord1)
plot(abs2,ord2)

plt.show()



