from DataTransfer.TransferMock import DataTransferService
from AirQuality.ReaderMock import AirQualityReader
from Display.LEDMock import LEDInterface
from Logging.SystemLogging import file_logger as logger
from Monitoring.Monitor import Monitor

API_URL = "https://mock.com"
DEVICE_ID = "1"

data_transfer_service = DataTransferService(API_URL, DEVICE_ID, logger)
air_quality_reader = AirQualityReader(logger)
led_interface = LEDInterface(logger)

if __name__ == '__main__':
    monitor = Monitor(logger, air_quality_reader, led_interface, data_transfer_service)
    monitor.execute()

    del data_transfer_service
    del air_quality_reader
    del led_interface
    del monitor