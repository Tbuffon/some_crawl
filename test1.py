import requests
from bs4 import BeautifulSoup
import csv
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
url = 'https://edfjzxt.xmu.edu.cn/alumni/donate/xmuDonatePublic/listForWeb'

response = requests.get(url='https://edfjzxt.xmu.edu.cn/website/page/Information/xxgk.html', headers=headers).content
soup = BeautifulSoup(response, 'html.parser')
table = soup.find('table')
thead = table.find('thead')
# 获取表头
header = []
for th in thead.find_all('th'):
    header.append(th.text.strip())

csvfile = open('donation_records.csv', 'w', newline='')
writer = csv.writer(csvfile)
writer.writerow(header)

for i in range(1, 10):
    response = requests.get(url='https://edfjzxt.xmu.edu.cn/alumni/donate/xmuDonatePublic/listForWeb?pageNo='+ str(i) +'&pageSize=10', headers=headers).json()

    records = response['result']['records']

    # 获取表格内容
    rows = []
    for data in records:
        row = []
        row.append(data['donateTime'])  # 捐赠时间
        row.append(data['donor'])       # 捐赠人 
        row.append(data['major'])       # 院系专业
        row.append(data['alumniAssoc']) # 校友会
        row.append(data['projName'])    # 捐赠项目
        row.append(data['donateAmt'])   # 捐赠金额
        rows.append(row)
    writer.writerows(rows)

# 存储表格数据
# with open('donation_records.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(header)
#     writer.writerows(rows)


# print(soup.tr)
# print(soup.find('tr', class_ = 'active'))
# print(soup.select('table'))
# print(soup.find('tr', class_ = 'listInfo'))


# tbody = table.find('thead', id="listInfo")
# # tbody = table.find('tbody')



# # 获取表格内容
# rows = []
# for tr in tbody.find_all('tr'):
#     row = []
#     for td in tr.find_all('td'):
#         row.append(td.text.strip())
#     rows.append(row)



# with open('output.txt', 'w', encoding='utf-8') as f:
#             f.write(str(response))