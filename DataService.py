import requests

class DataService:
    def __init__(self, url):
        sefl.URL = url

    def SubmitReading(self, json):
        response = requests.post