class AirQualityReading:
    def __init__(self, co2, temperature, humidity, timestamp):
        self.co2 = co2
        self.temperature = temperature
        self.humidity = humidity
        self.timestamp = timestamp

    def __str__(self):
        return f"[{self.timestamp}] - CO2: {self.co2} ppm; Temperature: {self.temperature} degrees C; Humidity: {self.humidity} %rH"