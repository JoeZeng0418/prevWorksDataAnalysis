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

from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

  
def random_colors():
  r = int(randint(0,255))
  g = int(randint(0,255))
  b = int(randint(0,255))
  return (r,g,b)
def makeGraph(state1, state2, category):
  rtn = ""
  # statename = [
  # "All_U.S.",
  # "Alabama",
  # "Alaska",
  # "Arizona",
  # "Arkansas",
  # "California",
  # "Connecticut",
  # "Delaware",
  # "District of Columbia",
  # "Georgia",
  # "Hawaii",
  # "Illinois",
  # "Indiana",
  # "Iowa",
  # "Kansas",
  # "Kentucky",
  # "Louisiana",
  # "Maine",
  # "Maryland",
  # "Massachusetts",
  # "Michigan",
  # "Minnesota",
  # "Missouri",
  # "Montana",
  # "Nebraska",
  # "Nevada",
  # "New Jersey",
  # "New Mexico",
  # "New York",
  # "North Carolina",
  # "Ohio",
  # "Oregon",
  # "Pennsylvania",
  # "Puerto Rico",
  # "South Carolina",
  # "Tennessee",
  # "Texas",
  # "Utah",
  # "Vermont",
  # "Virginia",
  # "Virgin Islands",
  # "Washington",
  # "West Virginia",
  # "Wisconsin",
  # "Wyoming",
  # "Guam"]

  for i in range(1):
  # for i in range(len(statename)):
    # contry 2
    sn2 = state2.replace(" ","_")
    loc_ = ("data/trunk_"+sn2+"_rate.xlsx") 
    loc2_ = ("data/trunk_"+sn2+"_case.xlsx")
    state_name2 = sn2
    wb_ = xlrd.open_workbook(loc_) 
    sheet_ = wb_.sheet_by_index(0) 
    wb2_ = xlrd.open_workbook(loc2_) 
    sheet2_ = wb2_.sheet_by_index(0)

    # contry 1
    sn = state1.replace(" ","_")
    loc = ("data/trunk_"+sn+"_rate.xlsx") 
    loc2 = ("data/trunk_"+sn+"_case.xlsx")
    state_name = sn
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0)
    wb2 = xlrd.open_workbook(loc2) 
    sheet2 = wb2.sheet_by_index(0) 



    # get totlist for country 1
    totlist_1 = list()
    currlist_1 = list()
    collist_1 = list()
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
        collist_1.append(rowname)
        newlist = list()
        currlist_1 = newlist
        totlist_1.append(currlist_1)
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
        currlist_1.append(rowlist)


    # get totlist for country 2
    totlist_2 = list()
    currlist_2 = list()
    collist_2 = list()
    for i in range(sheet_.nrows):
     rowname = sheet_.cell_value(i,0)
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
        collist_2.append(rowname)
        newlist = list()
        currlist_2 = newlist
        totlist_2.append(currlist_2)
      else:
        rowlist = list()
        sec = sheet_.cell_value(i,0)
        if sec == '–' or sec == '':
          sec = 0;
        rowlist.append(sec)
        for index in range(2,9):
          sec = sheet_.cell_value(i,index)
          if sec == '–' or sec == '':
            sec = 0;
          rowlist.append(sec)
        for index in range(2,9):
          sec = sheet2_.cell_value(i,index)
          if sec == '–' or sec == '':
            sec = 0;
          rowlist.append(sec)
        currlist_2.append(rowlist)

    # print(totlist_2)




    # create a single plot for two country 
    year = [2011,2012,2013,2014,2015,2016,2017]
    # for i in range(1,2):
    for i in range(1,len(totlist_1)):
      if collist_1[i]!=category:
        continue
      data = []
      for j in range(len(totlist_1[i])):

        # country 1
        datalist  = list()
        for z in range(1,8):
          datalist.append(totlist_1[i][j][z])
        trace = go.Scatter(
            x = year,
            y = datalist,
            name = totlist_1[i][j][0]+"_"+state_name,
            line = dict(
                color = ("rgb" + str(random_colors())),
                width = 1)
        )
        data.append(trace)

        # country 2
        datalist  = list()
        for z in range(1,8):
          datalist.append(totlist_2[i][j][z])
        trace = go.Scatter(
            x = year,
            y = datalist,
            name = totlist_1[i][j][0]+"_"+state_name2,
            line = dict(
                color = ("rgb" + str(random_colors())),
                width = 1)
        )
        data.append(trace)
      
      layout = dict(title = collist_1[i],
                  xaxis = dict(title = 'year'),
                  yaxis = dict(title = 'percentage'),
                  )

      fig = dict(data=data, layout=layout)

      filen = 'public/graphs/'+state_name+"_"+state_name2+'_Line_' + collist_1[i] +'.html' 
      rtn = 'graphs/'+state_name+"_"+state_name2+'_Line_' + collist_1[i] +'.html' 
      plotly.offline.plot(fig, filename=filen)
  return rtn



@app.route("/")
def home():
    return "hi"
@app.route("/index")
def index():
    return "this is index"

@app.route('/getGraph', methods=['GET', 'POST'])
def getGraph():
  if request.method == 'GET':
    print("generating graph\n\n\n\n\n")
    # print(request.form)
    print("\n\n\n\n\n")
    state1 = request.args.get('state1')
    state2 = request.args.get('state2')
    category = request.args.get('category')
    # resp = make_response('{"response": '+result+'}')
    # resp.headers['Content-Type'] = "application/json"
    return makeGraph(state1, state2, category)
      # return render_template('login.html', message='')

if __name__ == "__main__":
  app.run(debug = True)
