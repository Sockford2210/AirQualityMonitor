class AirQualityReading:
    def __init__(self, co2, temperature, humidity, timestamp):
        self.__co2 = co2
        self.__temperature = temperature
        self.__humidity = humidity
        self.__timestamp = timestamp

    def __str__(self):
        return f"[{self.__timestamp}] - CO2: {self.__co2} ppm; Temperature: {self.__temperature} degrees C; Humidity: {self.__humidity} %rH"

    def get_co2(self):
        return self.__co2

    def get_temperature(self):
        return self.__temperature

    def get_humidity(self):
        return self.__humidity

    def get_timestamp(self):
        return self.__timestamp