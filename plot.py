import plotly
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
import plotly.io as pio

import os
import numpy as np
# excel read
import xlrd

import xlrd

loc = ("data/trunk_cal_data_rate.xlsx") 
loc2 = ("data/trunk_cal_data_number.xlsx")

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

wb2 = xlrd.open_workbook(loc2) 
sheet2 = wb2.sheet_by_index(0) 

totlist = list()
currlist = list()

collist = list()

probsum = 0;
problist = list()

for i in range(sheet.nrows):
 rowname = sheet.cell_value(i,0)
 if(rowname == "Footnotes:"):
  break;
 if(rowname != ''):
  if(rowname[-1]==':'):
   probsum = 0;
   collist.append(rowname)
   newlist = list()
   currlist = newlist
   totlist.append(currlist)
  else:
   rowlist = list()
   sec1 = sheet.cell_value(i,0)
   sec2 = sheet.cell_value(i,8)
   sec3 = sheet2.cell_value(i,8)
   if sec2 == '–' or sec2=='':
    sec2 = 0;
   if sec3 == '–' or sec3=='':
    sec3 = 0;
   rowlist.append(sec1)
   rowlist.append(sec2)
   rowlist.append(sec3)
   currlist.append(rowlist)
print(totlist)

# totlist = [[], [['Men', 25.4, 128960.0], ['Women', 18.7, 71010.0]], [['Under 14', '-', '-'], ['14 to 15', '-', '-'], ['16 to 19', 16.7, 3470.0], ['20 to 24', 24.7, 15850.0], ['25 to 34', 21.9, 43630.0], ['35 to 44', 23.5, 44710.0], ['45 to 54', 25.4, 45140.0], ['55 to 64', 21.0, 36480.0], ['65 and over', 23.1, 7960.0]]]
# collist = ['', 'Sex','Age']

x = []
y = []
sizes = []
print(totlist[1])
count = 0

for i in range(1, len(totlist)):
	for j in range(0,len(totlist[i])):
		x.append(collist[i])
		temp = totlist[i][j][1]
		if  temp == '-':
			temp = 0;
		y.append(temp)
		if totlist[i][j][2] == '-':
			# print(totlist[i][j][2])
			sizes.append(0)
		else:
			# print(totlist[i][j][2])
			sizes.append(totlist[i][j][2]/500)
		count+=1
	



# N = 10
# x = np.random.rand(N)
# x = ['giraffes', 'orangutans', 'monkeys', 'giraffes','giraffes', 'orangutans', 'monkeys', 'giraffes','giraffes', 'orangutans']
# y = np.random.rand(N)
colors = np.random.rand(count)
# sz = np.random.rand(N)*30+20

fig = go.Figure()
fig.add_scatter(x=x,
                y=y,
                mode='markers',
                marker={'size': sizes,
                        'color': colors,
                        'opacity': 0.6,
                        'colorscale': 'Viridis'
                       });
plotly.offline.plot(fig)