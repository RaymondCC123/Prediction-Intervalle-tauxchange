import requests
import json
import csv

# API : PIB US
url = "https://api.stlouisfed.org/fred/series/observations?" \
      "series_id=GDP&api_key=09cefe3ef92e58d279f3d34f776aa262&" \
      "file_type=json&" \
      "observation_start=1999-01-01&" \
      "observation_end=2017-12-31&" \
      "frequency=q"
r = requests.get(url)

# print(json.dumps(r.json()["observations"], indent=4, sort_keys=True))

with open('/Users/laurence/devisePIB/pib_US_Billions of Dollars_fed_reserve.csv', 'w') as csvfile:
    f = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # Write CSV Header, If you dont need that, remove this line
    f.writerow(["date", "pib_US"])
    for x in r.json()["observations"]:
        f.writerow([x["date"],
                    x["value"]])


def dernier_pib_us():
    url1 = "https://api.stlouisfed.org/fred/series/observations?" \
           "series_id=GDP&api_key=09cefe3ef92e58d279f3d34f776aa262&" \
           "file_type=json&" \
           "observation_start=2018-01-01&" \
           "frequency=q"
    r1 = requests.get(url1)
    date1 = r1.json()["observations"][0]["date"]
    value1 = r1.json()["observations"][0]["value"]
    return value1


###
###
###
###
###
###


# API : PIB of the EuroArea
url = "https://api.stlouisfed.org/fred/series/observations?" \
      "series_id=EUNNGDP&" \
      "api_key=09cefe3ef92e58d279f3d34f776aa262&" \
      "file_type=json&" \
      "observation_start=1999-01-01&" \
      "observation_end=2017-12-31&" \
      "frequency=q"
r = requests.get(url)

# print(json.dumps(r.json()["observations"], indent=4, sort_keys=True))

with open('/Users/laurence/devisePIB/pib_EuroArea_Millions of Euros_fed_reserve.csv', 'w') as csvfile:
    f = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # Write CSV Header, If you dont need that, remove this line
    f.writerow(["date", "pib_EuroArea"])
    for x in r.json()["observations"]:
        f.writerow([x["date"],
                    x["value"]])


def dernier_pib_euro():
    url2 = "https://api.stlouisfed.org/fred/series/observations?" \
           "series_id=CLVMEURSCAB1GQEA19&" \
           "api_key=09cefe3ef92e58d279f3d34f776aa262&" \
           "file_type=json&" \
           "observation_start=2018-01-01&" \
           "frequency=q"
    r2 = requests.get(url2)
    date2 = r2.json()["observations"][0]["date"]
    value2 = r2.json()["observations"][0]["value"]
    return value2
