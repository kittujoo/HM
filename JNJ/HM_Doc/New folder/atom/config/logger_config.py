import os


def get_log_config(results_path: str) -> dict:
    atom_log = os.path.join(results_path, "atom.log")
    atom_error = os.path.join(results_path, "atom_error.log")
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "file_formatter": {
                "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
            }
        },
        "handlers": {
            "debug_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "file_formatter",
                "filename": atom_log,
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8"
            },
            "error_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "file_formatter",
                "filename": atom_error,
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8"
            }
        },
        "root": {
            "level": "DEBUG",
            "handlers": [
                "debug_file_handler",
                "error_file_handler"
            ]
        }
    }
