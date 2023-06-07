from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import re

browser = webdriver.Chrome(executable_path='chromedriver.exe')
browser.get('http://em100.edaptivedocs.net/Login.aspx')

browser.implicitly_wait(1)
idGuestAccess = browser.find_element(By.ID, 'idGuestAccess')
idGuestAccess.click()

browser.implicitly_wait(1)
clsi_m100_ed33_2023 = browser.find_element(By.LINK_TEXT, 'CLSI M100 ED33:2023')
clsi_m100_ed33_2023.click()

# # 初始化数据列表
data = {
 '抗生素':[],
 '抗生素上标':[],
 '抗生素说明':[],
 '分级':[],
 '分级说明':[],
 '尿检':[],
 '所在表格':[],
 '表格名称':[],
 '表格名称上标':[]}

letters = [chr(i) for i in range(ord('A'), ord('P') + 1)]

browser.implicitly_wait(1)

for i, letter in enumerate(letters):
    toc = browser.find_element(By.ID, 'idLPTOC')
    toc.click()

    browser.implicitly_wait(1)
    table = browser.find_element(By.XPATH, f'//*[@id="idTOCInner"]/div[{15 + i}]/div/a')
    table.click()

    browser.implicitly_wait(3)








    title = browser.find_element(By.XPATH, f'//*[@id="CLSI M100 ED33:2023 TABLE 1{letter}"]/h1')
    try: 
        sup = title.find_element(By.TAG_NAME, 'sup').text
    except NoSuchElementException:
        sup = ''

    # print(sup)
    if title.text.endswith(sup):
        title = title.text.rstrip(sup)
    title = title.split('. ')
    # print(title)

    # 找到表格元素
    table = browser.find_element(By.XPATH, f'//*[@id="CLSI M100 ED33:2023 TABLE 1{letter} [Table Data]"]/div/table/tbody')


    # 获取表格所有行
    rows = table.find_elements(By.TAG_NAME, 'tr')

    classfication = []
    classfication_description = []
    urine_only = None

    # # 遍历表格行,获取每个单元格的数据
    for i, row in enumerate(rows):

        # 获取行中的所有单元格
        cols = row.find_elements(By.TAG_NAME, 'td') 
        # 初始化单行的数据
        row_data = []
        # 遍历单元格
        for j, col in enumerate(cols):
            # 获取单元格内容
            text = col.text
            if i == 0:
                text = text.split(': ')
                classfication.append(text[0])
                classfication_description.append(text[1])
                continue

            if text == 'Urine Only':
                urine_only = text
                continue

            if text == ' ':
                continue

            cli = re.sub(r'\([^)]*\)', '', text)
            cli_description = re.findall(r'\([^)]*\)', text)
            cli_description = ''.join(cli_description).replace('(', '').replace(')', '')

            try:
                cli_sup = col.find_element(By.TAG_NAME, 'sup').text
                if cli.endswith(cli_sup):
                    cli = cli.rstrip(cli_sup)  
            except NoSuchElementException:
                cli_sup = None
            print(i,j)
            
            
            data['所在表格'].append(title[0])
            data['表格名称上标'].append(sup)
            data['表格名称'].append(title[1])
            data['抗生素'].append(cli)
            data['抗生素上标'].append(cli_sup)
            data['抗生素说明'].append(cli_description)
            data['分级'].append(classfication[j])
            data['分级说明'].append(classfication_description[j])
            data['尿检'].append(urine_only)

            # 添加到单行数据中
            # row_data.append(text)
        # # 添加单行数据到总的数据中
        # data.append(row_data)











# # 关闭浏览器    
# browser.close()

# 使用pandas转换为DataFrame
df = pd.DataFrame(data)

# # 将行索引设置为列
# df = df.transpose()

df.to_csv("table", sep='\t', encoding='utf-8', index=False)
# df.to_csv("table.csv", encoding='utf-8-sig', index=False)


# print(browser.current_url)

# with open('output.txt', 'w', encoding='utf-8') as f:
#             f.write(str(browser.page_source))



# df = pd.DataFrame(data)
# filename = 'my_table.csv'
# df.to_csv(filename, sep='\t', encoding='utf-8', index=False)

