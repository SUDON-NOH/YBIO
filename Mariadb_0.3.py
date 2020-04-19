import pymysql
# SQL Table 에 있는 데이터를 PANDAS의 데이터프레임으로 불러오는 모듈
from sqlalchemy import create_engine
import pandas as pd
pymysql.install_as_MySQLdb()
import MySQLdb


class Mariadb_SD:
    def __init__(self):
        print("MariaDB를 실행합니다")
        self.password = ''
        self.username = ''
        self.db = ''
        self.login_info = ''

        # 로그인
    def DB_login(self):
        x = ''
        while True:
            self.username = input("UserID를 입력하세요.")
            self.password = input("Password를 입력하세요.")

            try:
                # 접속을 위한 정보입력
                self.connect = pymysql.connect(
                    host='localhost',
                    user=self.username,
                    password=self.password,
                    db='ybio',
                    charset='utf8'
                     )
                self.cur = self.connect.cursor()
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n접속을 성공했습니다.")
                break
            except pymysql.err.OperationalError:
                print('\n\n\n\n\n\n\n\n\n\n\n\n=============ID와 PW를 확인하세요===============\n\n\n')
                x = input('종료 입력시 접속 종료, 접속시도를 게속하려면 아무 키나 눌러주세요.')
                if x == '종료':
                    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n종료되었습니다.')
                    break
                continue

    # 접속 종료
    # 전체를 묶어서 언제든 종료할 수 있게 해야함.
    def DB_close(self):
        while True:
            x = input("종료하시려면 '종료'를 입력하세요.")
            if x == '종료':

                self.connect.close()
                print("접속이 종료되었습니다.")
                break
            else:
                print("접속 상태를 유지합니다.")
                break

    def query_sql(self):
        while True:
            try:
                print('\n\n\n\n')
                sql = input('명령문 입력(종료 입력시 Query 종료)')

                if sql == '종료':
                    print('명령문 입력이 종료되었습니다.')
                    break
                else:
                    print('명령문을 실행합니다.')
                    self.cur.execute(sql)
                    # 명령문을 데이터베이스에 전송
                    print("명령문을 데이터베이스에 전송합니다.")
                    self.connect.commit()

            except pymysql.err.ProgrammingError or pymysql.err.ProgrammingError:
                print('입력오류 다시 시도해주세요.')
                continue

    def load_mariaDB(self):
        # 데이터베이스의 table 을 불러 Pandas 데이터프레임 형태로 저장한다.
        self.login_info = 'mysql+mysqldb://' + self.username + ':' + self.password + '@localhost/ybio'
        engine = create_engine(self.login_info, encoding = 'utf-8')
        conn = engine.connect()
        x = ''

        while True:
            table_name = input('저장할 Table 명을 입력하세요.')
            try:
                data = pd.read_sql_table(table_name, conn)
                print('========================상위 데이터를 보여줍니다.========================\n', data.head(),
                      '\n================================================')
                print('========================테이블의 열을 보여줍니다.========================\n', data.columns,
                      '\n================================================')
                print('========================         DATA         ========================\n', data,
                      '\n================================================')
                return data
            except ValueError:
                print('Table ', table_name, ' not found\nPlease try again')
                x = input('종료하시려면 "종료"를 입력하세요.')
                if x == '종료':
                    print('불러오기를 종료합니다.')
                    break
                continue

    def insert_sql(self, dataframe_name):
        self.login_info = 'mysql+mysqldb://' + self.username + ':' + self.password + '@localhost/ybio'
        engine = create_engine(self.login_info, encoding = 'utf-8')
        x = ''

        while True:

            table = input('\n\n\n\n\n\n저장할 Table명을 입력하세요.\n\n\n\n\n\n')

            try:
                dataframe_name.to_sql(name= table, con=engine, if_exists='append')
                print('해당 내용이 ', table, '에 추가되었습니다.')
                break

            except ValueError:
                print('Table ', table, ' not found\nPlease try again')
                x = input('종료하시려면 "종료"를 입력하세요.')
                if x == '종료':
                    print('불러오기를 종료합니다.')
                    break
                continue


