from Display.OLEDInterface import FourRowOLEDDisplay

class AirQualityDisplay:
    def __init__(self, logger):
        self.logger = logger
        self.display = FourRowOLEDDisplay()

    def update_air_quality_values(self, air_quality):
        self.logger.info("Updating air quality display")

        try:
            self.display.reset()
            
            self.display.set_row_one(f"CO2: {air_quality.get_co2_display()}")
            self.display.set_row_two(f"Humidity: {air_quality.get_humidity_display()}")
            self.display.set_row_three(f"Temperature: {air_quality.get_temperature_display()}")

            self.display.show()

            self.logger.info("Updated air quality display")
        except:
            self.logger.error("Error updating air quality display")