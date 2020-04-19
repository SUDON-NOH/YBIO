import pandas as pd
import os
import openpyxl

class excel_pd:

    def __init__(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n', ' '*50, 'EXCEL', ' '*50, '\n\n\n\n\n\n\n\n\n\n\n\n' )
        self.folder = ''
        self.load = ''
        self.path = ''
        self.file_list = ''


    # 폴더 읽어서 파일 이름 모두 저장
    def read_folder(self):

        self.folder = input('불러올 폴더명을 입력하세요.')
        self.load = input('불러올 폴더의 경로를 입력하세요.')
        # 경로 설정 필요
        self.path = self.load + self.folder
        print('\n\n\n\n\n입력한 폴더의 파일들을 불러오는 중입니다.\n\n\n\n')
        self.file_list = os.listdir(self.path)
        print(self.folder,' 폴더에 있는 파일 목록입니다.\n', self.file_list)
        return self.file_list

    # 파일읽기: CSV 파일을 DF 형태로 변환하기
    def change_toDF(self):
        file_name = input('불러올 파일명을 입력하세요.')
        self.df = pd.read_csv(file_name)
        print('========================상위 데이터를 보여줍니다.========================\n', self.df.head(),
              '\n=====================================================================')
        print('========================테이블의 열을 보여줍니다.========================\n', self.df.columns,
              '\n=====================================================================')
        print('========================         DATA         ========================\n', self.df,
              '\n=====================================================================')
        return self.df

    #