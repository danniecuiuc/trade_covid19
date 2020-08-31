from pytrends.request import TrendReq
import pandas as pd
import time
import pytrends

startTime = time.time()
pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25))

df_split = pd.read_csv("~/downloads/ra_paper/keyword_list_2.csv",encoding = "ISO-8859-1")
df_split_test = df_split["keywords"].values.tolist()[300:311]   #0-301 DONE

for x in range(0, len(df_split_test)): 
    keywords = [df_split_test[x]]
    print(keywords)

keyword_data = pd.DataFrame()

for x in range(0, len(df_split_test)): 
    startTime = time.time()
    pytrends.build_payload(kw_list=[df_split_test[x]], cat=0, timeframe='2020-01-01 2020-07-30', geo='US')
    related_queries = pytrends.related_queries()
    trends_value = related_queries[df_split_test[x]]['top'].head(25)
    keyword_data = keyword_data.append(trends_value)

print(keyword_data)
