"""
This defines the helper functions
"""

class Logger:

    @staticmethod
    def getlogger(name="unknown"):
        return Logger(name)
    
    def __init__(self, name):
        self._name = name

    def log(self, msg=None):
        print("[%s] : ... %s  ..." % (self._name, msg))

