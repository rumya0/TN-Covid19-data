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

