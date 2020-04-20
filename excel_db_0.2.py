import pandas as pd
import os
import openpyxl
import xlrd
import numpy as np

class excel_pd:

    def __init__(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n', ' '*50, 'EXCEL', ' '*50, '\n\n\n\n\n\n\n\n\n\n\n\n' )
        self.folder = ''
        self.load = ''
        self.path = ''
        self.file_list = ''
        self.excel_add = ''




    # 폴더 읽어서 파일 이름 모두 저장
    def read_folder(self):
        print('\n\n\n\n\n\n', "=" * 50, '파일 목록을 저장합니다.', '=' * 50, '\n\n')
        self.folder = input('불러올 폴더명을 입력하세요.')
        self.load = input('불러올 폴더의 경로를 입력하세요.')
        # 경로 설정 필요
        self.path = self.load + self.folder
        print('\n\n\n\n\n입력한 폴더의 파일들을 불러오는 중입니다.\n\n\n\n')
        self.file_list = os.listdir(self.path)
        print(self.folder,' 폴더에 있는 파일 목록입니다.\n', self.file_list)
        return self.file_list

    # 파일읽기: CSV 파일을 DF 형태로 변환하기
    def csv_toDF(self):
        file_name = input('불러올 파일명을 입력하세요.\n 주소입력이 필요할 경우 주소를 입력해야합니다.')
        self.df = pd.read_csv(file_name)
        print('========================상위 데이터를 보여줍니다.========================\n', self.df.head(),
              '\n=====================================================================')
        print('========================테이블의 열을 보여줍니다.========================\n', self.df.columns,
              '\n=====================================================================')
        print('========================         DATA         ========================\n', self.df,
              '\n=====================================================================')
        return self.df

    # 파일읽기: excel 파일 읽기
    def excel_toDF(self):
        print('\n\n\n\n\n\n', "=" * 50, 'Excel 파일을 불러 Dataframe으로 저장합니다.', '=' * 50, '\n\n')
        print(self.file_list)
        file_name = input('불러올 파일의 이름을 입력해주세요.')
        file_name_add = self.path + "\\" + file_name
        workbook = xlrd.open_workbook(file_name_add)
        sheet_names = workbook.sheet_names()
        print(sheet_names)
        sheet_name = input('불러올 시트의 이름를 입력하세요')
        self.df = pd.read_excel(file_name_add, sheet_name = sheet_name)

        self.df = self.df.drop(self.df.index[0:7])
        self.df = self.df.drop(self.df.columns[[0, 1, 2, 26, 27, 28, 29]], axis='columns')
        print(self.df.columns)
        self.df = self.df.reset_index()
        self.df.rename = self.df.rename(columns = {
                                    'Unnamed: 3':'UID',
                                    'Unnamed: 4':'ID',
                                    'Unnamed: 5':'PDATE',
                                    'Unnamed: 6':'DATE',
                                    'Unnamed: 7':'CollaboType',
                                    'Unnamed: 8':'Researcher',
                                    'Unnamed: 9':'Helper',
                                    'Unnamed: 10':'Helper_Ratio',
                                    'Unnamed: 11':'Project_ID',
                                    'Unnamed: 12':'Project',
                                    'Unnamed: 13':'Target',
                                    'Unnamed: 14':'RID',
                                    'Unnamed: 15':'TITLE',
                                    'Unnamed: 16':'Detail',
                                    'Unnamed: 17':'Purpose',
                                    'Unnamed: 18':'EQID',
                                    'Unnamed: 19':'KITID',
                                    'Unnamed: 20':'EQNAME',
                                    'Unnamed: 21':'KITNAME',
                                    'Unnamed: 22':'NSUB',
                                    'Unnamed: 23':'Sample_Num',
                                    'Unnamed: 24':'EVENT_',
                                    'Unnamed: 25':'REAPEAT_'},
                                    inplace = True)
        self.df = self.df.dropna(subset=['UID'])
        self.df = self.df.replace(np.nan, 'NULL')
        # self.df['num'] = 'NULL'
        # columns = self.df.columns.tolist()
        # columns.insert(0, 'num')
        # columns.pop()
        # self.df = self.df[columns]
        self.df = self.df.drop(self.df.columns[0], axis = 'columns')

        print('========================상위 데이터를 보여줍니다.========================\n', self.df.head(),
              '\n=====================================================================')
        print('========================테이블의 열을 보여줍니다.========================\n', self.df.columns,
              '\n=====================================================================')
        print('========================         DATA         ========================\n', self.df,
              '\n=====================================================================')

        return self.df




 

