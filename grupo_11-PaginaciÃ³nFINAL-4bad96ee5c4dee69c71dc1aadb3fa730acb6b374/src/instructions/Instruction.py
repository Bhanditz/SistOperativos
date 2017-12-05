class Instruction():

    def __init__(self, count):
        self._count = count

    def isExit(self):
        return False

    def isIo(self):
        return False

    def isCpu(self):
        return False

    @property
    def count(self):
        return self._count

    def expand(self):
        expanded = []

        for _ in range(self._count):
            expanded.append(self.__class__(0))

        return expanded