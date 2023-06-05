from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
browser = webdriver.Chrome(executable_path='chromedriver.exe')
browser.get('http://em100.edaptivedocs.net/Login.aspx')

browser.implicitly_wait(1)
idGuestAccess = browser.find_element(By.ID, 'idGuestAccess')
idGuestAccess.click()

browser.implicitly_wait(1)
clsi_m100_ed33_2023 = browser.find_element(By.LINK_TEXT, 'CLSI M100 ED33:2023')
clsi_m100_ed33_2023.click()

browser.implicitly_wait(1)
toc = browser.find_element(By.ID, 'idLPTOC')
toc.click()

browser.implicitly_wait(1)
table_1a = browser.find_element(By.XPATH, '//*[@id="idTOCInner"]/div[15]/div/a')
table_1a.click()

browser.implicitly_wait(3)

# title = browser.find_element(By.XPATH, '//*[@id="CLSI M100 ED33:2023 TABLE 1A"]/h1/b/span').text
# sup = browser.find_element(By.XPATH, '//*[@id="CLSI M100 ED33:2023 TABLE 1A"]/h1/b/span/sup').text
# print(sup)
# if title.endswith(sup):
#     title = title.rstrip(sup)
# title = title.split('.')

# 找到表格元素
table = browser.find_element(By.XPATH, '//*[@id="CLSI M100 ED33:2023 TABLE 1A [Table Data]"]/div/table/tbody')

# 获取表格所有行
rows = table.find_elements(By.TAG_NAME, 'tr')

# # 初始化数据列表
data = []

# # 遍历表格行,获取每个单元格的数据
for row in rows:
    # 获取行中的所有单元格
    cols = row.find_elements(By.TAG_NAME, 'td') 
    # 初始化单行的数据
    row_data = []
    # 遍历单元格
    for col in cols:
        # 获取单元格内容
        text = col.text
        # 添加到单行数据中
        row_data.append(text)
    # 添加单行数据到总的数据中
    data.append(row_data)

# 关闭浏览器    
browser.close()

# 使用pandas转换为DataFrame
df = pd.DataFrame(data)

# 将行索引设置为列
df = df.transpose()

df.to_csv("table", sep='\t', encoding='utf-8', index=False)

# print(browser.current_url)

# with open('output.txt', 'w', encoding='utf-8') as f:
#             f.write(str(browser.page_source))


# data = {
#  '抗生素':[],
#  '抗生素上标':[],
#  '抗生素说明':[],
#  '分级':[],
#  '分级说明':[],
#  '尿检':[],
#  '所在表格':[],
#  '表格名称':[],
#  '表格名称上标':[]}
# df = pd.DataFrame(data)
# filename = 'my_table.csv'
# df.to_csv(filename, sep='\t', encoding='utf-8', index=False)

