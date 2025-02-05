class AirQualityDisplayModel:
    def __init__(self, co2, temperature, humidity):
        self.co2 = round(float(co2), 2)
        self.temperature = round(float(temperature), 2)
        self.humidity = round(float(humidity), 2)
    
    def set_co2_value(self, co2):
        self.co2 = round(co2, 2)
        
    def set_temperature_value(self, temperature):
        self.temperature = round(temperature, 2)

    def set_humidity_value(self, humidity):
        self.humidity = round(humidity, 2)

    def get_co2_display(self):
        return f"{self.co2} ppm"

    def get_temperature_display(self):
        return f"{self.temperature} degrees C"

    def get_humidity_display(self):
        return f"{self.humidity} %rH"