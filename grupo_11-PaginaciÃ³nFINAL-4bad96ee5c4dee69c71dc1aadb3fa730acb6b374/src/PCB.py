from src.States import State

class PCB:
    # pcb con None en PageTable si es pag. bajo demanda
    def __init__(self, priority, pageTable = None):
        self._ir = None
        self._pid = None
        self._state = State.NEW
        self._pc = 0
        self._path = ""
        self._baseDir = None
        self._priority = priority
        self._pageTable = pageTable


    def setPid(self, pid):
        self._pid = pid

    def getPriority(self):
        return self._priority

    def setBaseDir(self, bd):
        self._baseDir = bd

    def getBaseDir(self):
        return self._baseDir

    def getPC(self):
        return self._pc

    def setPC(self, addr):
        self._pc = addr

    def getIr(self):
        return self._ir

    def setIr(self, ins):
        self._ir = ins

    def getPid(self):
        return self._pid

    def setState(self, state):
        self._state = state

    def getState(self):
        return self._state

    def pageTable(self):
        return self._pageTable