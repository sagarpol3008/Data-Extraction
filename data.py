# import csv
# import pandas as pd
# file = open('list_of_real_usa_addresses.csv')
# csvreader = csv.reader(file)

# rows = []
# for row in csvreader:
#     rows.append(row)

# data = pd.read_csv("list_of_real_usa_addresses.csv")

# add1 = data.address[0]
# print(add1)

import PyPDF2
import re
from pdfminer.high_level import extract_pages, extract_text

file = PyPDF2.PdfFileReader('Property_Paper.pdf')

page1 = file.getPage(0)  # get the dat of first page

page1_text = page1.extractText()
# print(page1_text)


# print(file.getPage(0).extractText())

#text = extract_text("Property_Paper.pdf")
# print(text)


# extract the exact address
pattern = re.compile(r"Protierty Address: (\d{5} [^\n]+)")
matches = pattern.findall(page1_text)
# print(matches)         #print all string in list format
str1 = matches[0]
print(str1)
