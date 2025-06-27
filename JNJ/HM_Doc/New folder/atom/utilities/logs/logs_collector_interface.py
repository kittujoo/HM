"""
File_Name: logs_collector_interface.py
Desc: Formal interface for handling logs collection on different environments.

Raises NotImplementedError:
    Classes implementing the interface need to have the below abstractmethod implemented.

__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Ionel Luca" Initial check-in - Jan 12, 2023
"""

import abc


class LogsCollectorInterface(metaclass=abc.ABCMeta):
    """Interface for enforcing logs collection functionality on any environment."""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, "stop_logging") and
                callable(subclass.stop_logging) or
                NotImplemented)

    @abc.abstractmethod
    def start_logging(self):
        """Set current log last entry from the current environment, for furure log cropping"""
        raise NotImplementedError

    @abc.abstractmethod
    def stop_logging(self):
        """Collects new logs from the current environment"""
        raise NotImplementedError
