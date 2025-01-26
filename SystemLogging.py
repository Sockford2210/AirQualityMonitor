import sys
import logging.config

LOGGING_CONFIG = { 
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': { 
        'default': { 
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            'datefmt': "%d/%m/%Y %H:%M:%S"
        },
    },
    'handlers': { 
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': logging.DEBUG,
            'stream': sys.stdout,
        },
        'file-logger': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'level': logging.DEBUG,
            'filename': 'Logs/logfile.txt',
            'maxBytes': 52428800,
            'backupCount': 7
        },
    },
    'loggers': { 
        'file-logger': {
            'handlers': ['file-logger', 'console'],
            'level': logging.DEBUG
        },
        'console': {
            'handlers': ['console'],
            'level': logging.DEBUG
        }
    } 
}

logging.config.dictConfig(LOGGING_CONFIG)

console_logger = logging.getLogger('console')
file_logger = logging.getLogger('file-logger')