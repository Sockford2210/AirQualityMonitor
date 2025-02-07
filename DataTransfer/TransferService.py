import requests

class DataTransferService:
    def __init__(self, url, device_id, logger):
        self.__url = url
        self.__device_id = device_id
        self.__logger = logger

    def submit_reading(self, reading):
        formatted_timestamp_str = reading.get_timestamp().strftime("%m/%d/%Y, %H:%M:%S")

        json_data = {
            "deviceId": self.__device_id,
            "timestamp": formatted_timestamp_str,
            "humidityPercentage": reading.get_humidity(),
            "temperatureCelcius": reading.get_temperature(),
            "co2ppm": reading.get_co2()
        }

        self.__logger.info(f"DataService: {self.__url}, Device Id: {self.__device_id}")

        try:
            self.__logger.info(f"Sending data: {json_data}")
            response = requests.post(self.url, json=json_data, verify=False)
            self.__logger.info(f"Data transfer status code: {response.status_code}")
        except:
            self.__logger.exception("Error sending data")
        finally:
            self.__logger.info("Terminating data transfer")