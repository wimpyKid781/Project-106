import csv
import plotly.express as px
import numpy as np
def getDataSource(dataPath):
    grade = []
    days = []
    with open(dataPath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            grade.append(float(row['Marks In Percentage']))
            days.append(float(row['Days Present']))
    return{'x':grade,'y':days}
def findCorelations(dataSources):
    corelations = np.corrcoef(dataSources['x'],dataSources['y'])
    print(corelations[0,1])
def setup():
    dataPath = './Student Marks vs Days Present.csv'
    dataSource = getDataSource(dataPath)
    findCorelations(dataSource)
setup()