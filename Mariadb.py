import pymysql
import os
import pandas as pd
import openpyxl

class Mariadb_SD:

    def __init__(self):
        print("MariaDB를 실행합니다")
        self.password = ''
        self.username = ''
        self.db = ''

    # 로그인
    def login_db(self):
        self.username = input("UserID를 입력하세요.")
        self.password = input("Password를 입력하세요.")


        self.connect = pymysql.connect(
            host='localhost',
            user=self.username,
            password=self.password,
            db='ybio',
            charset='utf8'
             )
        self.cur = self.connect.cursor()
        print("접속을 성공했습니다.")

    # 접속 종료
    def DB_close(self):
        while True:
            x = input("종료하시려면 'Yes'를 입력하세요.")
            if x == 'Yes':
                self.connect.close()
                print("접속이 종료되었습니다.")
                break
            else:
                break

    def query_sql(self):
        while True:
            print('/n/n/n/n/n/n/n')
            sql = input('명령문 입력')

            if sql == '종료':
                break
            else:
                self.cur.execute()


class excel_pd:

    def __init__(self):
        print(' '*50, 'EXCEL', ' '*50)

    def read_folder(self):

        self.load = input('폴더 이름을 입력하세요.')
        # 경로 설정 필요
        self.path = './' + self.load
        self.file_list = os.listdir(self.path)
        print(self.load,' 폴더에 있는 파일 목록입니다./n', self.file_list)
        return self.file_list

