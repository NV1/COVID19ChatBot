import requests
import json
class Api:
    def __init__(self):
        pass

    def makeApiRequestForCounrty(self, country_name):
        url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"
        querystring = {"country": "Canada"}
        headers = {
            'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
            'x-rapidapi-key': "7322d59420msh74980c259f39287p1bc789jsncd3218e4a174"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('response')[0]
        print(result.get('cases'))
        print("*" * 20)
        return result.get('cases') , result.get('deaths'),result.get('tests')


    def makeApiRequestForIndianStates(self):
        url = "https://covid19-data.p.rapidapi.com/india"
        headers = {
            'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
            'x-rapidapi-key': "7322d59420msh74980c259f39287p1bc789jsncd3218e4a174"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        #result = js.get('list')
        return js


    def makeApiWorldwide(self):
        url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
        headers = {
            'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
            'x-rapidapi-key': "7322d59420msh74980c259f39287p1bc789jsncd3218e4a174"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('data')

        return result

