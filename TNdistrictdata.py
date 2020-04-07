# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:08:51 2020

@author: Ramya Aravind
"""

import tabula
import camelot
from datetime import date
import PyPDF2, io, requests
import pandas as pd

from bs4 import BeautifulSoup

today = date.today()
tdate = today.strftime("%d-%m")
url=("https://stopcorona.tn.gov.in/wp-content/uploads/2020/03/Media-Bulletin-"+tdate+"-20-COVID-19-6-PM.pdf")

response = requests.get(url)
pdf_file = io.BytesIO(response.content) # response being a requests Response object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
num_pages = pdf_reader.numPages

newdf1 = tabula.read_pdf(url, pages=str(num_pages))
df = (pd.DataFrame(newdf1[0])).fillna(0)
new_df = df.drop(df.columns[[0,2,3]], axis = 1)
new_df.rename(columns={ new_df.columns[1]: "New Cases", new_df.columns[2]: "Total Cases"  }, inplace = True)
new_df = new_df[:-1]


new_df.to_json('tndistrict.json', orient = 'index')
new_df.to_json('tndistrict1.json', orient = 'records')



url2 = 'https://www.mohfw.gov.in/'
response = requests.get(url2)
soup = BeautifulSoup(response.content, 'html5lib')
table = soup.find_all('table', attrs={'class':'data-table table-responsive'})
print(table)

#df = pd.DataFrame(newdf1)

# df = newdf1.replace('NaN', 0)
# newdf1.fillna(0)