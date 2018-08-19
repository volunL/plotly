import pandas as pd
import datetime

#excel_path = 'excel/Shibor2018.xls'
excel_path='excel/2018hs300.xlsx'
data=pd.read_excel(excel_path,header=[0],usecols=[0,2])
print(data)
# for i in data['日期']:
#    print(i.strftime('%Y-%m-%d '))

#for i in data:
head=list(data)
print(len(head))
for i in range(0,len(head)):
    print(head[i]," ",i)
