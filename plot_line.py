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

statename = [
"All_U.S.",
"Alabama",
"Alaska",
"Arizona",
"Arkansas",
"California",
"Connecticut",
"Delaware",
"District of Columbia",
"Georgia",
"Hawaii",
"Illinois",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Maryland",
"Massachusetts",
"Michigan",
"Minnesota",
"Missouri",
"Montana",
"Nebraska",
"Nevada",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"Ohio",
"Oregon",
"Pennsylvania",
"Puerto Rico",
"South Carolina",
"Tennessee",
"Texas",
"Utah",
"Vermont",
"Virginia",
"Virgin Islands",
"Washington",
"West Virginia",
"Wisconsin",
"Wyoming",
"Guam"]

for i in range(1):
# for i in range(len(statename)):
  sn = statename[i].replace(" ","_")

  loc = ("data/trunk_"+sn+"_rate.xlsx") 
  loc2 = ("data/trunk_"+sn+"_case.xlsx")

  state_name = sn

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
      rowname = rowname[0:-1]
      rownamelist = rowname.split("(")
      rowname = rownamelist[0]
      rowname = rowname.replace(' ','_')
      rowname = rowname.replace(',','')


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

  # print(collist)
  # print(rowlist)
  # year = [2011,2012,2013,2014,2015,2016,2017]
  # for i in range(1,len(totlist)):
  #   data = []
  #   for j in range(len(totlist[i])):
  #     datalist  = list()
  #     for z in range(1,8):
  #       datalist.append(totlist[i][j][z])

  #     # print(datalist)
  #     trace = go.Scatter(
  #         x = year,
  #         y = datalist,
  #         name = totlist[i][j][0],
  #         line = dict(
  #             color = ("rgb" + str(random_colors())),
  #             width = 1)
  #     )
  #     data.append(trace)
    
  #   layout = dict(title = collist[i],
  #               xaxis = dict(title = 'year'),
  #               yaxis = dict(title = 'percentage'),
  #               )

  #   fig = dict(data=data, layout=layout)

  #   filen = 'public/graphs/'+state_name+'_Line_' + collist[i] +'.html' 
  #   plotly.offline.plot(fig, filename=filen)
