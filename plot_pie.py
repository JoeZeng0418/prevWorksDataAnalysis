import plotly
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
import plotly.io as pio

import os
import numpy as np# excel read
import xlrd

import xlrd

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
  # statename = 'California'
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
  # print(collist)
  # print(totlist)

  # totlist = [
  #     [],
  #     [
  #         ['Men', 25.4, 128960.0],
  #         ['Women', 18.7, 71010.0]
  #     ],
  #     [
  #         ['Under 14', '-', '-'],
  #         ['14 to 15', '-', '-'],
  #         ['16 to 19', 16.7, 3470.0],
  #         ['20 to 24', 24.7, 15850.0],
  #         ['25 to 34', 21.9, 43630.0],
  #         ['35 to 44', 23.5, 44710.0],
  #         ['45 to 54', 25.4, 45140.0],
  #         ['55 to 64', 21.0, 36480.0],
  #         ['65 and over', 23.1, 7960.0]
  #     ]
  # ]# collist = ['', 'Sex', 'Age']

  figures = []

  for i in range(1, len(totlist)): # for every category
    labels = []
    values_rate = []
    values_number = []
    for j in range(0, len(totlist[i])):
      labels.append(totlist[i][j][0])
      values_rate.append(totlist[i][j][1])
      values_number.append(totlist[i][j][2])
    trace = go.Pie(labels=labels, values=values_number)
    # print(labels)
    # print(values_number)
    plotly.offline.plot([trace], filename="public/graphs/" + states[l].replace(" ","_") + "_2017" + '_Pie_' + collist[i]+".html")



















