from Display.OLEDInterface import FourRowOLEDDisplay
from Display.LEDInterface import LEDInterface

class AirQualityDisplay:
    def __init__(self, logger):
        self.__logger = logger
        self.__display = FourRowOLEDDisplay()
        self.__led_interface = LEDInterface(logger)
        self.__led_interface.turn_green_on()

    def __del__(self):
        self.__led_interface.turn_green_off()
        del self.__display
        del self.__led_interface

    def update_air_quality_values(self, air_quality):
        self.__logger.info("Updating air quality display")

        try:
            self.__display.reset()
            
            self.__display.set_row_one(f"CO2: {air_quality.get_co2_display()}")
            self.__display.set_row_two(f"Hum: {air_quality.get_humidity_display()}")
            self.__display.set_row_three(f"Temp: {air_quality.get_temperature_display()}")

            self.__display.show()

            self.__logger.info("Updated air quality display")
        except:
            self.__logger.error("Error updating air quality display")

    def set_high_co2_alert_light(self):
        self.__led_interface.turn_red_on()

    def unset_high_co2_alert_light(self):
        self.__led_interface.turn_red_off()
