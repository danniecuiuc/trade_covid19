from pytrends.request import TrendReq
import pandas as pd
import time
import pytrends


startTime = time.time()
pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25))
df = pd.read_csv("allkeywords10.csv")
keylist = df["query"].values.tolist()

print(keylist)

dataset = []

for x in range(0, len(keylist)):
    keywords = [keylist[x]]
    pytrends.build_payload(kw_list=keylist, cat=8, timeframe='2020-01-01 2020-07-31', geo='US')
    data = pytrends.interest_over_time()
    if not data.empty:
        data = data.drop(labels=['isPartial'], axis='columns') 
        dataset.append(data)

result = pd.concat(dataset, axis=1)
result.to_csv('search_result_10.csv')

