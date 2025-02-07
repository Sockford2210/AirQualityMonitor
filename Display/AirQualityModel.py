class AirQualityDisplayModel:
    def __init__(self, co2, temperature, humidity):
        self.__co2 = round(float(co2), 2)
        self.__temperature = round(float(temperature), 2)
        self.__humidity = round(float(humidity), 2)

    def get_co2_display(self):
        return f"{str(self.__co2)} ppm"

    def get_temperature_display(self):
        return f"{str(self.__temperature)} degC"

    def get_humidity_display(self):
        return f"{str(self.__humidity)} %rH"