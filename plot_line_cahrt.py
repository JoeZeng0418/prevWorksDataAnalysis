import plotly
from plotly import tools
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
import plotly.io as pio

import os
import numpy as np
# excel read
import xlrd
from random import randint

def random_colors():
  r = int(randint(0,255))
  g = int(randint(0,255))
  b = int(randint(0,255))
  return (r,g,b)

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
    sec = sheet.cell_value(i,0)
    if sec == '–' or sec == '':
      sec = 0;
    rowlist.append(sec)
     
    for index in range(2,9):
      sec = sheet.cell_value(i,index)
      if sec == '–' or sec == '':
        sec = 0;
      rowlist.append(sec)

    for index in range(2,9):
      sec = sheet2.cell_value(i,index)
      if sec == '–' or sec == '':
        sec = 0;
      rowlist.append(sec)

    currlist.append(rowlist)
# print(totlist)

# totlist = [[], [['Men', 25.4, 128960.0], ['Women', 18.7, 71010.0]], [['Under 14', '-', '-'], ['14 to 15', '-', '-'], ['16 to 19', 16.7, 3470.0], ['20 to 24', 24.7, 15850.0], ['25 to 34', 21.9, 43630.0], ['35 to 44', 23.5, 44710.0], ['45 to 54', 25.4, 45140.0], ['55 to 64', 21.0, 36480.0], ['65 and over', 23.1, 7960.0]]]
# collist = ['', 'Sex','Age']



year = [2011,2012,2013,2014,2015,2016,2017]

# print(totlist)

# fig = tools.make_subplots(rows=len(totlist), cols=1, subplot_titles=collist)

for i in range(1,len(totlist)):
  data = []
  for j in range(len(totlist[i])):
    datalist  = list()
    for z in range(1,8):
      datalist.append(totlist[i][j][z])

    # print(datalist)
    trace = go.Scatter(
        x = year,
        y = datalist,
        name = totlist[i][j][0],
        line = dict(
            color = ("rgb" + str(random_colors())),
            width = 1)
    )
    # fig.append_trace(trace,i,1)
    data.append(trace)
  
  layout = dict(title = collist[i],
              xaxis = dict(title = 'year'),
              yaxis = dict(title = 'percentage'),
              )

  fig = dict(data=data, layout=layout)
  plotly.offline.plot(fig, filename='styled-line')

# print(data)
# layout = dict(title = 'percentage among people in each year',
#               xaxis = dict(title = 'year'),
#               yaxis = dict(title = 'percentage'),
#               )


# fig = dict(data=data, layout=layout)




# fig = go.Figure()
# fig.add_scatter(x=x,
#                 y=y,
#                 mode='markers',
#                 marker={'size': sizes,
#                         'color': colors,
#                         'opacity': 0.6,
#                         'colorscale': 'Viridis'
#                        });
# plotly.offline.plot(fig)