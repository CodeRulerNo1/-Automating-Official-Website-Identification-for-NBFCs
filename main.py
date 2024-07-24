import pandas as pd
from googlesearch import search
import os
def load(a,i):
    print("Loading"+'.'*(i%3+1)+' '*(3-(i%3)),int(i/a*100),'%')
def find_websites(FileName):
    if not FileName.endswith(".xlsx"):
        raise ValueError("Enter a file with extension .xlsx")
    df = pd.read_excel(FileName)
    n=df.shape[0]
    lro,ln,lad,lemid,lj=[],[],[],[],[]
    for i in range(n):
        query = df.iloc[i]["NBFC Name"]
        if query=='':
            raise ValueError("No value at index",i,"for the NBFC name")
        ro=df.iloc[i]["Regional Office"]
        ad=df.iloc[i]["Address"]
        emid=df.iloc[i]["Email ID"]
        load(n+1,i+1)
        for j in search(query, tld="co.in", num=1, stop=1, pause=1.5):
            if j.startswith("https://www.zaubacorp") or j.startswith("https://in.linkedin" or j.endswith(".pdf")) or j.startswith("https://www.icra") or j.startswith("https://trendlyne") or j.startswith("https://www.crisil") or j.startswith("www.tofler"):
                os.system('cls')
                continue
            lro.append(ro)
            ln.append(query)
            lad.append(ad)
            lemid.append(emid)
            lj.append(j)
            os.system('cls')
    D={"Regional Office":lro,"NBFC Name":ln,"Address":lad,"Email ID":lemid,"Official Website":lj}
    dfo=pd.DataFrame(D)
    dfo.to_excel('Output.xlsx')
