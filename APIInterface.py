import requests

class DataService:
    def __init__(self, url, device_id):
        self.url = url
        self.device_id = device_id

    def submit_reading(self, reading):
        jsonData = {
            "deviceId": self.device_id,
            "timestamp": reading.timestamp.strftime("%m/%d/%Y, %H:%M:%S"),
            "humidityPercentage": reading.humidity,
            "temperatureCelcius": reading.temperature,
            "co2ppm": reading.co2
        }

        print(f"DataService: {self.url}, Device Id: {self.device_id}\n")
        print(f"Sending Data: {jsonData}\n")
        response = requests.post(self.url, json=jsonData, verify=False)
        print(f"Data transfer status code: {response.status_code}\n")