import requests
import pandas as pandas

###
###
###
###
###
# API : Taux-Change trimestriel EUR/USD
url = "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/Q.USD.EUR.SP00.A?startPeriod=1999-Q2&endPeriod=2018-Q1"
r = requests.get(url, headers={'Accept': 'text/csv'})
# print(r.headers['Content-Type'])
# print(r.text)

with open('/Users/laurence/devisePIB/taux_EURUSD_ECB.csv', 'w') as file:
    file.write(r.text)

data = pandas.read_csv('/Users/laurence/devisePIB/taux_EURUSD_ECB.csv', usecols=[6, 7])
print(data)
data.to_csv('/Users/laurence/devisePIB/taux_EURUSD_ECB.csv', mode='w', sep=';', decimal='.',
            header=["date", "taux_EURUSD"])

###
###
###
###
###
###
# merge csvfiles
dfs = [data]
to_merge = ["/Users/laurence/devisePIB/pib_US_Billions of Dollars_fed_reserve.csv",
            "/Users/laurence/devisePIB/pib_EuroArea_Millions of Euros_fed_reserve.csv"]  # type: List[str]

for filename in to_merge:
    # read the csv, making sure the first two columns are str
    df = pandas.read_csv(filename, header=0, converters={0: str, 1: float}, sep=';', decimal='.')
    # throw away all but the first two columns
    df = df.iloc[:, [-1]]
    print(df)
    # df = df.drop(["date"], axis=1)
    # change the column names so they won't collide during concatenation
    # df.columns = [filename + str(cname) for cname in df.columns]
    dfs.append(df)
# print(dfs)
# concatenate them horizontally
merged = pandas.concat(dfs, axis=1)
# write it out
merged.to_csv("/Users/laurence/devisePIB/merged.csv",
              header=['date(quarterly)', 'taux_EURUSD', 'pib_US(Billions of Dollars)',
                      'pib_EuroArea(Millions of Euros)'],
              index=None, sep=';', decimal='.')
