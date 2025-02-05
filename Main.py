from DataTransfer.TransferMock import DataTransferService
from AirQuality.ReaderSCD30 import AirQualityReader
from Display.LEDInterface import LEDInterface
from Display.DisplayModule import AirQualityDisplay
from Logging.SystemLogging import console_logger as logger
from Monitoring.Monitor import Monitor

API_URL = "https://LAPTOP-DQ2OSHGS:32768/api/AirData"
DEVICE_ID = "1"

data_transfer_service = DataTransferService(API_URL, DEVICE_ID, logger)
air_quality_reader = AirQualityReader(logger)
led_interface = LEDInterface(logger)
display = AirQualityDisplay(logger)

if __name__ == '__main__':
    monitor = Monitor(logger, air_quality_reader, led_interface, data_transfer_service, display)
    monitor.execute()

    del data_transfer_service
    del air_quality_reader
    del led_interface
    del display
    del monitor