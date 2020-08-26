from pytrends.request import TrendReq
import pandas as pd
import time

pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25))
startTime = time.time()
pytrends.build_payload(kw_list=['foundation'], geo = 'US', timeframe = 'today 1-y', cat = 0)
related_queries= pytrends.related_queries()
print(related_queries)

startTime = time.time()
pytrends.build_payload(kw_list=['foundation'], geo = 'US', timeframe = "2019-01-01 2020-07-28", cat = 0)
related_queries= pytrend.related_queries()
print(related_queries)

pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25))
trends = pytrends.related_queries()
df = pd.read_csv("keyword_list_1.csv")
print(related_queries)
df2 = df["keywords"].values.tolist()
print(trends)

dataset = []
for x in range(0, len(df2)):
    print(df2[x])
    trends_value = trends[df2[x]]['top'].value.tolist().head(50)
    pytrends.build_payload(kw_list=trends_keywords, cat=0, timeframe='2019-01-01 2020-07-28', geo='US')
    data = pytrends.interest_over_time()
    if not data.empty:
        data = data.drop(labels=['isPartial'], axis='columns')
        dataset.append(data)

result = pd.concat(dataset, axis=1)
result.to_csv('search_result.csv')
