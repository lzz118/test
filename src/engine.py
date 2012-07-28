"""
The engine class that does everything...
"""

from helper import Logger

class Engine:
    def __init__(self):
        self._logger = Logger.getlogger("Engine")
        self._logger.log("Engine has inited")

    def __del__(self):
        self._logger.log("Engine has destroied")
