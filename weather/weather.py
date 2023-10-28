import requests
class Weather():

    def __init__(self,city):

        self.city=city
        self.params={
            'access_key':'be23673cd6f87cc2dccf313a17854817', #Use your Weather Stack api
            'query':city
        }
    def weather(self):
        try:
            api_result=requests.get('http://api.weatherstack.com/current',self.params)
            api_response=api_result.json()
            return api_response
        except ConnectionError:
            return "No internet connection"

