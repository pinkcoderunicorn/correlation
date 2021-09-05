import csv
import numpy as np
 
def getDataSource():
 
 with open ("coffeesleepdata", newline = "") as f:
 file_data = csv.DictReader(f)
 
 #returning the data_source
 
 Coffee in ml = []
 sleep in hours = []
 
 for row in file_data:
 sleep in hours.append(float(row['sleep in hours']))
 Coffee in ml.append(float(row['Coffee in ml']))
 
 return{'x': sleep in hours, 'y': Coffee in ml}
 
#data_source is our key name
def findCorrelation(data_source):
 correlation = np.corrcoef(data_source['x'], data_source['y'])
 print(correlation[0,1])
 
gds = getDataSource()
findCorrelation(gds)