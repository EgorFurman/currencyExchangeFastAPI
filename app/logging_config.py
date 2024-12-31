import logging
from logging.config import dictConfig

from app.config import app_settings


def setup_logging():
    log_dir = app_settings.ROOT_DIR / 'app'

    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'DEBUG',
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'level': 'WARNING',
                'filename': str(log_dir / 'logs.log')
            }
        },
        'loggers': {
            'logger': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': False,
            }
        }
    }
    dictConfig(logging_config)

