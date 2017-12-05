from src.Exceptions.ProgramNotAvailableException import ProgramNotAvailableException


class FileSystem:

    def __init__(self):
        self._dictionary = {}


    def save(self, path, program):
        self._dictionary[path] = program.expand()

    def get(self, path):
        try:
            return self._dictionary[path]
        except KeyError:
            raise ProgramNotAvailableException
