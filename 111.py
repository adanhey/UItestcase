import requests
import os
import openpyxl

headers = {"Cookie": "%s;%s" % ("sid=pc-7ab5cf40-db7e-4cca-8a5c-36bb751b7938",
                                "uwebJwt=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJpbm92YW5jZSIsImNvbXBhbnlJZCI6ImEzYzA0ZTcwLTQyY2QtNGNmYy04NmNjLWY3MjI5Y2FkODAyZiIsImNvbXBhbnlJZHMiOiIxX2EzYzA0ZTcwLTQyY2QtNGNmYy04NmNjLWY3MjI5Y2FkODAyZl8iLCJjdXN0b21lckNvZGUiOiIwMDAwMTAyMDc1IiwidXNlck5hbWUiOiJzeXNhZG1pbiIsImV4cCI6MTcwODEyOTgwNCwidXNlcklkIjoiOTA1ODllMGItYTM0NC00ZDczLWE2M2QtOGE4MDEwNWM5MjIyIiwiaWF0IjoxNjc2NTkzODA0LCJqdGkiOiJlMzk1NjZjYy04ZjczLTQ4MTctYjAzNy00NDRmYjY4YzU1Y2UifQ.-hnjNk66QYIXNnhoKWpdxBvdKMyycnHKCy6jNDqyiQM")}
host = 'https://huiservertest2.iotdataserver.net'
strc = 'dlwmfwFumMOJKobXGwtv'
url = '%s/es/productModel/exportTemplateExcel' % host
url2 = '%s/es/productModel/importExcel' % host
result = requests.Session().get(url=url, headers=headers)
with open("./%s.xlsx" % strc, "wb") as f:
    f.write(result.content)
    f.close()
xlx = openpyxl.load_workbook("./%s.xlsx" % strc)
sheet = xlx['sheet1']
sheet['A2'] = "ADWQjQfUaFxLFGCwZyTm"
sheet['B2'] = "可删除PDcJfVrCzRWbWXwlwLrT"
sheet['C2'] = "三边封制袋机"
sheet['D2'] = "220V/50HZ"
sheet['E2'] = "906"
sheet['F2'] = "QBgrSWHKZqTLjRZrXyCy"
xlx.save("./%s.xlsx" % strc)
fic = open("./%s.xlsx" % strc, "rb")
data = {}
data2 = {"file": fic}
result = requests.Session().post(url=url2, headers=headers, data=data,
                                 files=data2)
fic.close()
os.remove("./%s.xlsx" % strc)

