# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:14:55 2019

@author: kdoyl
"""

state_data = {'State':['Alabama','Alaska','Arizona','Arkansas'],'PostCode':['AL','AK','AZ','AR'],'Area':['52,423','656,424','*','53,182'],'Pop':['4,040,587','550,043','3,665,228','2,350,750']}
import pandas as pd
import numpy as np
state_data =  {'State':['Alabama','Alaska','Arizona','Arkansas'],'PostCode':['AL','AK','AZ','AR'],'Area':['52,423','656,424','*','53,182'],'Pop':['4,040,587','550,043','3,665,228','2,350,750']}
state_data
stdf = pd.DataFrame(state_data,columns=['State','PostCode','Area','Pop'])
stdf
stdf['Area']
stdf.Area
stdf['Area'][0]
stdf = stdf.set_index('State')
stdf
stdf =stdf.replace('*','0')
stdf
def item_replace(xstr):
    return xstr.replace(',','')
stdf['Area'] = stdf['Area'].map(item_replace)
stdf
stdf['Pop'] = stdf['Pop'].map(item_replace)
stdf
stdf[['Area','Pop']] = stdf[['Area','Pop']].astype(float)
stdf
mean_area = stdf['Area'].mean()
mean_area
stdf['Area'] = stdf.Area.mask(stdf.Area == 0, mean_area)
stdf


persondict = {'person':['Bob','Alice','Steve'], 'age':[32, 24, 64], 'weight':[128, 86, 95]}
persontable = pd.DataFrame(persondict, columns=['person','age','weight'])
persontable
persontable = persontable.set_index('person')
persontable
persontable.shape
persontable.dtypes
result = persontable.stack()
result
result.shape
result.index
persontall = result.reset_index()
persontall
persontall.columns=['person','attribute','value']
persontall
result.unstack()
persontall.pivot('person','attribute','value')

PROGRAM:  report_ALbb_csv.py
import csv
infile = 'ALbb.salaries.2003.tsv'
playersList = []
with open(infile, 'rU') as csvfile:
    ALReader = csv.reader(csvfile,  dialect='excel', delimiter='\t')
    for line in ALReader:
        if line[0] == '' or line[0].startswith('American') or line[0].startswith('Team')\
        or line[0].startswith('Source'):
            continue
        else:
            try:
                player = {}
                player['team'] = line[0]
                player['name'] = line[1]
                player['sal'] = int(line[2].replace(',',''))
                player['position'] = line[3]
                playersList.append(player)
            except IndexError:
                print ('Error: ', line)
csvfile.close()
print ("Read", len(playersList), "player data")
outfile1 = infile.replace('tsv', '') + 'report.txt'
fout1 = open(outfile1, 'w')
fout1.write("American League Baseball players average salary in 2003\n\n")
total_salary = 0.0
for player in playersList:
    total_salary += player['sal']
average_salary = total_salary / len(playersList)
fout1.write('Average salary = ${:,.2f}'.format(average_salary))
fout1.close()
outfile2 = infile.replace('tsv','') + 'million.csv'
with open(outfile2, 'w', newline='') as csvfileout:
    ALwriter = csv.writer(csvfileout, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    ALwriter.writerow(['Player', 'Team', 'Salary'])
    for player in playersList:
        if (player['sal'] > 310000):
            ALwriter.writerow([player['name'], player['team'], player['sal']])
csvfileout.close()

            
