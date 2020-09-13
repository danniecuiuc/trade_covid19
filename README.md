# trade_covid19

- quantitative trading algorithms development  amid covid19 
- factor modeling and alternative data analytics

Google Trends data for all components in S&P 500 index, from 2020-01-01 to 2020-07-30 (including both pre-covid19 and post-covid19)
Alternative Data:
1. obtain the company name list of all the components in the S&P 500 index.
2. use Google trends API to obtain the top 25 popular keywords for each company (e.g. the top 25 keywords that are most frequently searched for Amazon includes Amazon Prime, Amazon Video, and Amazon Stock, etc.)
3. obtain the search count for each keyword(topic).
4. sum up the search counts of the 25 keywords for each company to get the aggregated popularity score for each company.
5. use the popularity score as alternative data factor, build multi-factor models, and analyze its relationship with daily stock prices.
