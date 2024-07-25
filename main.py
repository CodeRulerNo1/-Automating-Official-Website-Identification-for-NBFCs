import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd
import threading
import os
from test import search
def load(a,i):
    print("Loading"+'.'*(i%3+1)+' '*(3-(i%3)),int(i/a*100),'%')
def get_company_website(df,L):
    n=df.shape[0]
    lro,ln,lad,lemid,lj=[],[],[],[],[]
    for i in range(n):  
        load(n,i)
        query = df.iloc[i]["NBFC Name"]
        query.replace(' ','+')
        if query=='':
            raise ValueError("No value at index",i,"for the NBFC name")
        ro=df.iloc[i]["Regional Office"]
        ad=df.iloc[i]["Address"]
        emid=df.iloc[i]["Email ID"]
        j=search(query)
        if j == None:
            continue
        lro.append(ro)
        ln.append(query)
        lad.append(ad)
        lemid.append(emid)
        lj.append(j)
    D={"Regional Office":lro,"NBFC Name":ln,"Address":lad,"Email ID":lemid,"Official Website":lj}
    dfo=pd.DataFrame(D)
    L.append(dfo)
start_time=time.time()
FileName='NBFC.xlsx'
if not FileName.endswith(".xlsx"):
        raise ValueError("Enter a file with extension .xlsx")
df = pd.read_excel(FileName,sheet_name="List of NBFCs")
ldf,t,L=[],[],[]  
n=df.shape[0]
for i in range(0,n//100+1):
    s_df=df.iloc[i*100:100*(i+1),:]
    t.append(threading.Thread(target=get_company_website,args=(s_df,L)))
    t[i].start()
for j in range(0,n//100+1):
    t[j].join()
output=pd.concat(L)
output.to_excel('Output.xlsx')
end_time=time.time()
exe=end_time- start_time
print("Execution Time:",exe)
