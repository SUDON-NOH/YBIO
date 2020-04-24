import pandas as pd
import openpyxl

# 마지막 행의 번호를 알기 위한 과정
excel_1 = pd.read_excel("C:/test/MREGI008OR(2.0).xlsx")
x = excel_1[['Unnamed: 2']][-1:].values.tolist()
x = x[0][0]
insert_sn = x + 1
last = x + 8 # 마지막 행

# REGI008OR(2.0).xlsx 파일 읽기
file = pd.read_excel('C:/test/REGI008OR(2.0).xlsx')
# 필요없는 행 삭제
file_1 = file.drop(file.index[0:6])
# 필요없는 열 제거
file_2 = file_1.drop(file_1.columns[[0, 1]], axis = 'columns')
# NEW 값만 추출
file_3 = file_2[file_2['Unnamed: 24'] == 'NEW']
# 다시 한번 필요없는 열 제거
file_4 = file_3.drop(file_3.columns[[0, 21, 22]], axis = 'columns')
# 첨부하기 위한 리스트 작성
list = file_4.values.tolist()
for a in range(len(list)):
    list[a].insert(0, insert_sn)
    insert_sn += 1

wb = openpyxl.load_workbook("C:/test/MREGI008OR(2.0).xlsx")
w_sheet = wb["M"]

# columns
columns = ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']

# row
last = str(last)


for k in list:
    for m, i in zip(columns, k):
        z = m + last
        w_sheet[z] = i
        if m == 'w':
            last = int(last)
            last += 1
            last = str(last)


wb.save('C:/test/MREGI008OR(2.0)_1.xlsx')