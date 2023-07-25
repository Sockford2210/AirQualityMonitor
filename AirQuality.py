import board
import busio
import adafruit_scd30

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
FREQUENCY = 50000

class AirQualityReading:
    def __init__(self, reading):
        self.CO2 = reading["CO2"]
        self.Temperature = reading["Temperature"]
        self.Humidity = reading["Humidity"]

    def __str__(self):
        return f"CO2: {self.CO2} ppm\nTemperature: {self.Temperature} degrees C\nHumidity: {self.Humidity} %%rH"


class Monitor:
    def __init__(self, dataService):
        i2c = busio.I2C(board.SCL, board.SDA, frequency=FREQUENCY)
        self.scd = adafruit_scd30.SCD30(i2c)

    def TakeReading()
        if self.scd.data_available:
            print("Data Available\n")
            newReading = AirQualityReading('CO2' : scd.CO2, 'Temperature' : scd.temperature, 'Humidity' : scd.Humidity)
            print(newReading)
            print("")

        else:
            print("ERROR: Data Not Available!\n")