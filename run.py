import socket
import pandas as pd
import xlsxwriter

#Constants
excel_path = 'example.xlsx'
column_name = 'Domain'

# Instance of result
workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()

# Putting the headers
worksheet.write("A1", "DOMAIN")
worksheet.write("B1", "IP")

# Reading data from excel
data = pd.read_excel (excel_path)
rows = pd.DataFrame(data, columns= [column_name])

# Gambi :(
row = 1

for domain in rows['Domain']:
    result = ''
    try:
        result = socket.gethostbyname(domain)
    except Exception as exc:
        result = exc
    finally:
        row = row + 1
        worksheet.write("{}{}".format("A", row), domain)
        worksheet.write("{}{}".format("B", row), str(result))


workbook.close()
