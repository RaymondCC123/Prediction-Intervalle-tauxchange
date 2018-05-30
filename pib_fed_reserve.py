import requests
import json
import csv

### API : PIB of the US

url = "https://api.stlouisfed.org/fred/series/observations?" \
      "series_id=GDP&api_key=09cefe3ef92e58d279f3d34f776aa262&" \
      "file_type=json&" \
      "observation_start=1999-01-01&" \
      "observation_end=2017-12-31&" \
      "frequency=q"
r = requests.get(url)

print(json.dumps(r.json()["observations"], indent=4, sort_keys=True))

with open('/Users/laurence/devisePIB/pib_US_Billions of Dollars_fed_reserve.csv', 'w') as csvfile:
    f = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # Write CSV Header, If you dont need that, remove this line
    f.writerow(["date", "pib_US"])
    for x in r.json()["observations"]:
        f.writerow([x["date"],
                    x["value"]])

###
###
###
###
###
###


### API : PIB of the EuroArea

url = "https://api.stlouisfed.org/fred/series/observations?" \
      "series_id=EUNNGDP&" \
      "api_key=09cefe3ef92e58d279f3d34f776aa262&" \
      "file_type=json&" \
      "observation_start=1999-01-01&" \
      "observation_end=2017-12-31&" \
      "frequency=q"
r = requests.get(url)

print(json.dumps(r.json()["observations"], indent=4, sort_keys=True))

with open('/Users/laurence/devisePIB/pib_EuroArea_Millions of Euros_fed_reserve.csv', 'w') as csvfile:
    f = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # Write CSV Header, If you dont need that, remove this line
    f.writerow(["date", "pib_EuroArea"])
    for x in r.json()["observations"]:
        f.writerow([x["date"],
                    x["value"]])

### method alternative

# from fredapi import Fred
# from pprint import pprint
#
# fr = Fred(api_key='09cefe3ef92e58d279f3d34f776aa262')  ### insert api key here
#
# data = fr.get_series_latest_release(series_id='GDP')
# pprint(data)
# # pprint(data.index)
# # pprint(data.values)
# # pprint(type(data))
# data.to_csv('/Users/laurence/devisePIB/pib_US_Billions of Dollars.csv', mode='w', sep=';', decimal='.')
#
# data = fr.get_series_latest_release(series_id='EUNNGDP')
# pprint(data)
# data.to_csv('/Users/laurence/devisePIB/pib_EuroArea_Millions of Euros.csv', mode='w', sep=';', decimal='.')
#
# data = fr.get_series_latest_release(series_id='CHNGDPNQDSMEI')
# pprint(data)
# data.to_csv('/Users/laurence/devisePIB/pib_China_Billions of Chinese Yuans.csv', mode='w', sep=';', decimal='.')
