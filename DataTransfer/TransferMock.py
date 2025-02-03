class DataTransferService:
    def __init__(self, url, device_id, logger):
        self.url = url
        self.device_id = device_id
        self.logger = logger

    def submit_reading(self, reading):
        json_data = {
            "deviceId": self.device_id,
            "timestamp": reading.timestamp.strftime("%m/%d/%Y, %H:%M:%S"),
            "humidityPercentage": reading.humidity,
            "temperatureCelcius": reading.temperature,
            "co2ppm": reading.co2
        }

        self.logger.info(f"DataService: {self.url}, Device Id: {self.device_id}")
        self.logger.info(f"Sending data: {json_data}")
        self.logger.info(f"Data transfer status code: {response.status_code}")
        self.logger.info("Terminating data transfer")