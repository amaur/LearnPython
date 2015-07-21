import abc
from abc import *

class PluginBase(metaclass=ABCMeta):


    @abc.abstractmethod
    def load(self, input):
        """ Retrieve data from the input source and return an object"""
        return

    @abc.abstractmethod
    def save(self, output,data):
        """Save the data object to the output"""
        return