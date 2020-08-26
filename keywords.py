# extract keywords for s&p 500 components
from pytrends.request import TrendReq
import pandas as pd
import time
import pytrends

startTime = time.time()
pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25)) 
trends = pytrends.related_queries()
colnames = ["keywords"]
df = pd.read_csv("~/downloads/ra_paper/keyword_list_2.csv")
df2 = df["keywords"].values.tolist()
print(df2)

for x in range(0, len(df2)):
    keywords = [df2[x]]
    print(keywords)

keyword_data = pd.DataFrame()
print(keyword_data)

for x in range(0, len(df2)):
    startTime = time.time()
    pytrends.build_payload(kw_list=[df2[x]], cat=0, timeframe='2020-01-01 2020-07-30', geo='US')
    related_queries = pytrend.related_queries()
    trends_value = related_queries[df2[x]]['top'].head(25)
    keyword_data = keyword_data.append(trends_value)

print(keyword_data)
keyword_data.shape

keyword_data.to_csv('allkeywords.csv') 
