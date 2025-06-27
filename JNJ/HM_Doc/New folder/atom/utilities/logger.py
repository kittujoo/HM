import logging


class Logger:

    def __init__(self, logger_instance_name):
        self.logger = logging.getLogger(logger_instance_name)

    def info(self, msg, *args, **kwargs):
        """
        Delegate an info call to the underlying logger
        """
        self.logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        """

       Delegate a debug call to the underlying logger
        """
        self.logger.debug(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """

       Delegate an error call to the underlying logger
        """
        self.logger.error(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """

       Delegate an warning call to the underlying logger
        """
        self.logger.warning(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        """
       Delegate an exception call to the underlying logger
        """
        self.logger.exception(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        """
        Delegate an exception call to the underlying logger
        """
        self.logger.log(level=level, msg=msg, *args, **kwargs)


