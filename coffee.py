import csv
import plotly.express as px
import numpy as np
def getDataSource(dataPath):
    coffee = []
    sleep = []
    with open(dataPath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            coffee.append(float(row['sleep in hours']))
            sleep.append(float(row['Coffee in ml']))
    return{'x':coffee,'y':sleep}
def findCorelations(dataSources):
    corelations = np.corrcoef(dataSources['x'],dataSources['y'])
    print(corelations[0,1])
def setup():
    dataPath = './cups of coffee vs hours of sleep.csv'
    dataSource = getDataSource(dataPath)
    findCorelations(dataSource)
setup()