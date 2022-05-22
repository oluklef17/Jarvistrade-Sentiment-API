'''from bs4 import BeautifulSoup
import requests

url = requests.get('https://www.forexfactory.com/calendar').text

with open('ff.html','r') as f:
    site = BeautifulSoup(f,'html.parser')

dates = site.find_all('span', class_='date')
symbols =  site.find_all('td')


for symbol in symbols:
    print(symbol)

for date in dates:
    day = list(date.text)
    day.insert(3,', ')
    d = ''.join(day)
    print(d)'''

from bs4 import BeautifulSoup
import os
import requests
import pandas as pd

#'https://www.dailyfx.com/sentiment'
#'https://fxssi.com/tools/current-ratio?filter=AUDJPY'



'''f = request.urlopen(url)
content = f.read()'''

'''with open('ff.html','r') as f:
    site = BeautifulSoup(f,'html.parser')'''

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
url = 'https://www.dailyfx.com/sentiment-report'
content = requests.get(url, headers=headers).text

path = r"C:\Users\user\AppData\Roaming\MetaQuotes\Terminal\B9AB1781CD4361C9C32CAAC85492E650\MQL4\Files"


all = list()
symbol = list()
long = list()
short = list()
dLong = list()
dShort = list()

soup = BeautifulSoup(content,'html.parser')


for s in soup.find_all('td'):
    value = s.span.text
    all.append(value)

all = all[7:len(all)]
symbol = all[0:len(all):7]
long = all[2:len(all):7]
short = all[3:len(all):7]
dLong = all[4:len(all):7]
dShort = all[5:len(all):7]

def getdata():
 table = {'SYMBOLS':symbol, 'LONGS':long, 'SHORTS':short, 'CHANGE IN LONGS':dLong, 'CHANGE IN SHORTS':dShort}
 data = pd.DataFrame(table)
 return table

'''print(symbol)
print(long)
print(short)'''

for sym in symbol:
    sym.replace(" ","")

filename = 'sentiment.csv'
location = os.path.join(path,filename)

with open(filename, 'w') as f:
    for i in range(len(symbol)):
        f.write(symbol[i]+","+long[i]+","+short[i]+"\n")




