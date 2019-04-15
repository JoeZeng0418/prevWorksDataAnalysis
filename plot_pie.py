import plotly
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
import plotly.io as pio

import os
import numpy as np# excel read
import xlrd

import xlrd

if not os.path.exists('images'):
  os.mkdir('images')

states = [
  "All U.S.",
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
  "Guam",
];

for l in range(0,1):
  filename1 = "data/trunk_" + states[l].replace(" ","_") + "_rate.xlsx"

  filename2 = "data/trunk_" + states[l].replace(" ","_") + "_case.xlsx"
  loc = (filename1)
  loc2 = (filename2)
  
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
    rowname = sheet.cell_value(i, 0)
    if (rowname == "Footnotes:"):
      break;
    if (rowname != ''):
      if (rowname[-1] == ':'):
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
      else :
        rowlist = list()
        sec1 = sheet.cell_value(i, 0)
        sec2 = sheet.cell_value(i, 8)
        sec3 = sheet2.cell_value(i, 8)
        if sec2 == '–' or sec2 == '':
          sec2 = 0;
        if sec3 == '–' or sec3 == '':
          sec3 = 0;
        rowlist.append(sec1)
        rowlist.append(sec2)
        rowlist.append(sec3)
        currlist.append(rowlist)

  figures = []

  for i in range(1, len(totlist)): # for every category
  # for i in range(3,4): # just for occupation
    pass
    labels = []
    values_rate = []
    values_number = []
    for j in range(0, len(totlist[i])):
      labels.append(totlist[i][j][0])
      values_rate.append(totlist[i][j][1])
      values_number.append(totlist[i][j][2])
    trace = go.Pie(labels=labels, values=values_number)
    plotly.offline.plot([trace], filename="public/graphs/" + states[l].replace(" ","_") + "_2017" + '_Pie_' + collist[i]+".html")
    # for image output
    # data = go.Data([trace])
    # layout=go.Layout(title="Occupation")
    # figure=go.Figure(data=data,layout=layout)
    # pio.write_image(figure, 'images/fig1.png')




















