import socket
import pandas as pd
import xlsxwriter

excelPath = 'example.xlsx'

workbook = xlsxwriter.Workbook(excelPath)
worksheet = workbook.add_worksheet()

data = pd.read_excel (excelPath)
rows = pd.DataFrame(data, columns= ['Domain'])

row = 0
#print(domains)
for domain in rows['Domain']:
    result = ''
    try:
        row = row + 1
        result = socket.gethostbyname(domain)
    except Exception as exc:
        result = exc
    finally:
        worksheet.write("{}{}".format("B", row), str(result))


workbook.close()
