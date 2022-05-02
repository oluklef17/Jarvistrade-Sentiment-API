from datetime import datetime
from getdata import getdata
import time
import os
import pandas as pd

'''while True:
 date = datetime.now()
 fTime = date.strftime("%H:%M:%S")
 print(fTime)
 time.sleep(10)'''

date = datetime.now()
fDate = date.strftime("%Y%m%d")

def write():
 if(os.path.exists(f'Sentiment_{fDate}.csv') == False):
    with open(f'Sentiment_{fDate}.csv', 'w', encoding='utf-8') as f:
        f.write(str(getdata()))
