from Bio import Medline
from Bio import Entrez
import pandas as pd

Entrez.email = "sdnoh@ybiologics.com"

# 찾고 싶은 검색어를 입력
TERM = 'COVID 19, rbd'


handle_1 = Entrez.egquery(term=TERM)
record = Entrez.read(handle_1)
# 아래의 과정은 모든 데이터베이스를 검색 후 검색어와 일치하는 항목이 몇 가지인지 확인
for row in record['eGQueryResult']:
    if row["DbName"]=="pubmed":
        x = row["Count"]
        x = int(x)

# retmax: 검색할 양
handle_2 = Entrez.esearch(db='pubmed', term=TERM, retmax=x)
record_2 = Entrez.read(handle_2)
handle_2.close()

# PUBMED 에서 검색한 리스트의 id를 불러옴
idlist = record_2["IdList"]


handle = Entrez.efetch(db="pubmed", id=idlist, rettype ="medline", retmode = 'text')
# handle = Entrez.efetch(db="pubmed", id=idlist, retmode = 'text')
record = Medline.parse(handle)
records = list(record)


P = []
TOTAL = []

count = 1
for record in records:
    P = []
    # print(record)
    X = record.get("PMID", "")
    # print("X\n", X)
    Y = record.get("TI", "")
    # print("Y\n", Y)
    Z = record.get("AB", "")
    # print("Z\n", Z)
    P.append(X)
    P.append(Y)
    P.append(Z)
    TOTAL.append(P)


handle.close()

# help(record)

df = pd.DataFrame(TOTAL)
df.columns = ["PMID", "Title", "Abstract"]
print(df)


file_name = "PUBMED_" + TERM + ".xlsx"

# 저장할 경로를 설정
file_load = "C:/Users/SD NOH/PycharmProjects/" + file_name
df.to_excel(file_load)