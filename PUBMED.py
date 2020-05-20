from Bio import Medline
from Bio import Entrez
import pandas as pd

Entrez.email = "sdnoh@ybiologics.com"

# 찾고 싶은 검색어를 입력
TERM = 'COVID-19, RBD'


handle_1 = Entrez.egquery(term=TERM)
record = Entrez.read(handle_1)
for row in record['eGQueryResult']:
    if row["DbName"]=="pubmed":
        x = row["Count"]
        x = int(x)

handle_2 = Entrez.esearch(db='pubmed', term=TERM, retmax=x)
record_2 = Entrez.read(handle_2)
handle_2.close()
idlist = record_2["IdList"]


handle = Entrez.efetch(db="pubmed", id=idlist, rettype ="medline", retmode = 'text')
record = Medline.parse(handle)
records = list(record)


P = []
TOTAL = []

count = 1
for record in records:
    P = []
    # print(record)
    X = record.get("PMID", "?")
    # print("X\n", X)
    Y = record.get("TI", "?")
    # print("Y\n", Y)
    Z = record.get("AB", "?")
    # print("Z\n", Z)
    P.append(X)
    P.append(Y)
    P.append(Z)
    TOTAL.append(P)


handle.close()

df = pd.DataFrame(TOTAL)
df.columns = ["PMID", "Title", "Abstract"]

file_name = "PUBMED_" + TERM + ".xlsx"

# 저장할 경로를 설정
file_load = "C:/Users/SD NOH/PycharmProjects/" + file_name
df.to_excel(file_load)