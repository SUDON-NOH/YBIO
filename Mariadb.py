import pymysql

class Mariadb_SD:

    def __init__(self):
        print("MariaDB를 실행합니다")
        self.password = ''
        self.username = ''
        self.db = ''

    def DB_Login(self):
        self.username = input("UserID를 입력하세요.")
        self.paswword = input("Password를 입력하세요.")


        self.connect = pymysql.connect(
            host='localhost',
            userid=self.username,
            password=self.password,
            db='ybio',
            charset = 'utf8'
             )
        cur = self.connect.cursor()
        print("접속을 성공했습니다.")

    def DB_close(self):
        while True:
            x = input("종료하시려면 'Yes'를 입력하세요.")
            if x == 'Yes':
                self.connect.close()
                print("접속이 종료되었습니다.")
            else:
                break

    def query_sql(self):
        while True:


"""

sql_drop = "drop table if exists test"
cur.execute(sql_drop)
sql = "create table test(" \
      "userid char(8))"
cur.execute(sql)


sql = "drop table test"
cur.execute(sql)

"""