import os
import numpy as np
# excel read
import xlrd



print('Enter your statename:')
statename = input()

loc = ("data/trunk_"+statename+"_rate.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

totlist = list()

currlist = list()
collist = list()
for i in range(sheet.nrows):
    rowname = sheet.cell_value(i,0)
    if(rowname == "Footnotes:"):
        break
    if(rowname != ''):
        if(rowname[-1]==':'):
            probsum = 0
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
            sec1 = sheet.cell_value(i,1)
            if sec1 == '–' or sec1 == '':
                sec1 = 0;
            rowlist.append(sec1)
            currlist.append(rowlist)


sumprob = 0.0;
print('Enter your gender:')
print('1) Male')
print('2) Female')
a1 = input()
sumprob = sumprob + totlist[1][int(a1)-1][1]
print('Enter your age:')
print('1) Under 14')
print('2) 14 to 15')
print('3) 16 to 19')
print('4) 20 to 24')
print('5) 25 to 34')
print('6) 35 to 44')
print('7) 45 to 54')
print('8) 55 to 64')
print('9) 65 and over')
a1 = input()
sumprob = sumprob + totlist[2][int(a1)-1][1]
print('Enter your occupation:')
print('1) Management, business, financial')
print('2) Computer, engineering, and science')
print('3) Education, legal, community service, arts, and media')
print('4) Healthcare practitioners and technical')
print('5) Service')
print('6) Sales and related')
print('7) Office and administrative support')
print('8) Farming, fishing, and forestry')
print('9) Construction and extraction')
print('10) Installation, maintenance, and repair')
print('11) Production')
print('12) Transportation and material moving')
a1 = input()
sumprob = sumprob + totlist[3][int(a1)-1][1]
print('Enter your occupation Industry sector:')
print('1) Goods producing industries')
print('2) Natural resources and mining')
print('3) Agriculture, forestry, fishing and hunting')
print('4) Mining(5)')
print('5) Construction')
print('6) Manufacturing')
print('7) Service providing industries')
print('8) Trade, Transportation and utilities')
print('9) Wholesale trade')
print('10) Retail trade')
print('11) Transportation and warehousing')
print('12) Utilities')
print('13) Information')
print('14) Financial activities')
print('15) Finance and insurance')
print('16) Real estate and rental and leasing')
print('17) Professional and business services')
print('18) Professional, scientific, and technical services')
print('19) Management of companies and enterprises')
print('20) Administrative and support and waste management and remediation services')
print('21) Education and health services')
print('22) Educational services')
print('23) Health care and social assistance')
print('24) Leisure and hospitality')
print('25) Arts, entertainment, and recreation')
print('26) Accommodation and food services')
print('27) Other services')
print('28) Other services, except public administration')
print('29) Public administration')
a1 = input()
sumprob = sumprob + totlist[5][int(a1)-1][1]

print('For the following options, enter 1 for things you had/exposed to in the past and 0 if not')
print('Musculoskeletal disorders')
a3 = input()
sumprob = sumprob + int(a3)*totlist[6][0][1]

print('Violence and other injuries by persons or animal')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][0][1]
print('Intentional injury by other person')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][1][1]
print('Injury by person unintentional or intent unknown')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][2][1]
print('Animal and insect related incidents')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][3][1]
print('Transportation incidents')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][4][1]
print('Roadway incidents involving motorized land vehicles')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][5][1]
print('Fires, explosions')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][6][1]
print('Falls, slips, trips')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][7][1]
print('Slips, trips without fall')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][8][1]
print('Fall on same level')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][9][1]
print('Fall to lower level')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][10][1]
print('Exposure to harmful substances or environments')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][11][1]
print('Contact with object, equipment')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][12][1]
print('Struck by object')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][13][1]
print('Struck against object')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][14][1]
print('Caught in object, equipment, material')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][15][1]
print('Overexertion and bodily reaction')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][16][1]
print('Overexertion in lifting or lowering')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][17][1]
print('Repetitive motion involving microtasks')
a3 = input()
sumprob = sumprob + int(a3)*totlist[7][18][1]


print('Fractures')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][0][1]
print('Sprains, strains, tears')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][1][1]
print('Amputations')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][2][1]
print('Cuts, lacerations, punctures')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][3][1]
print('Cuts, lacerations')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][4][1]
print('Punctures (except gunshot wounds)')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][5][1]
print('Bruises, contusions')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][6][1]
print('Chemical burns and corrosions')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][7][1]
print('Heat (thermal) burns')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][8][1]
print('Multiple traumatic injuries')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][9][1]
print('With sprains and other injuries')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][10][1]
print('With fractures and other injuries')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][11][1]
print('Soreness, pain')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][12][1]
print('Carpal tunnel syndrome')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][13][1]
print('Tendonitis')
a3 = input()
sumprob = sumprob + int(a3)*totlist[8][14][1]


print('Chemicals, chemical products')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][0][1]
print('Containers')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][1][1]
print('Furniture, fixtures')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][2][1]
print('Machinery')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][3][1]
print('Parts and materials')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][4][1]
print('Person, injured or ill worker')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][5][1]
print('Worker motion or position')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][6][1]
print('Person, other than injured or ill workers')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][7][1]
print('Health care patient')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][8][1]
print('Floors, walkways, ground surfaces')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][9][1]
print('Handtools')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][10][1]
print('Ladders')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][11][1]
print('Vehicles')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][12][1]
print('Trucks')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][13][1]
print('Cart, dolly, hand truck--nonpowered')
a3 = input()
sumprob = sumprob + int(a3)*totlist[9][14][1]


print('Containers, furniture, and fixtures')
a3 = input()
sumprob = sumprob + int(a3)*totlist[10][0][1]
print('Machinery')
a3 = input()
sumprob = sumprob + int(a3)*totlist[10][1][1]
print('Computers and peripheral equipment')
a3 = input()
sumprob = sumprob + int(a3)*totlist[10][2][1]
print('Tools, instruments, and equipment')
a3 = input()
sumprob = sumprob + int(a3)*totlist[10][3][1]
print('Firearms, law enforcement, and other self-defense equipment')
a3 = input()
sumprob = sumprob + int(a3)*totlist[10][4][1]
print('Vehicles')
a3 = input()
sumprob = sumprob + int(a3)*totlist[10][5][1]
print('Highway vehicle, motorized')
a3 = input()
sumprob = sumprob + int(a3)*totlist[10][6][1]
print('Ice, sleet, snow')
a3 = input()
sumprob = sumprob + int(a3)*totlist[10][7][1]
print('Liquids-nonchemical')
a3 = input()
sumprob = sumprob + int(a3)*totlist[10][8][1]

counter = 0
emr = 1.0
while(True):
    print("Enter your previous company's EMR:")
    print("Enter 0 if N/A")
    a4 = input()
    if(a4 == '0'):
        break
    counter = counter + 1
    emr = emr * float(a4)

emr = emr**(1/counter)
sumprob = sumprob * emr

print("===================")
print("your previous company's average EMR is: ",emr)
sumprob = sumprob/100
print("your probability is:",sumprob,"%")
print("Suggested investment on Backpain is:",60.96*sumprob)



