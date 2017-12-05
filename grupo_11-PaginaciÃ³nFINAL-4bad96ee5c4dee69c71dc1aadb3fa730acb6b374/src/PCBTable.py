from src.PCB import PCB

class PCBTable:

    def __init__(self):
        self._table = {}
        self._nextPid = 0
        self._runningPid = None

    # se podria crear un pcb con PageTable None, ya que si es Pag. bajo demanda no se pasa la page Table aca, sino a mmu
    def createPcb(self, priority, pageTable = None):
        newPcb = PCB(priority, pageTable)
        newPcb._pid = self.newPid()
        self._table[newPcb._pid] = newPcb
        return newPcb


    def newPid(self):
        current = self._nextPid
        self._nextPid += 1
        return current

    def getRunningPid(self):
        return self._runningPid

    def isRunningPcb(self):
        return self._runningPid != None

    def runningPcb(self):
        return self._table[self._runningPid]

    def getTable(self):
        return self._table

    def getNextPid(self):
        return self._nextPid

    def setRunningPid(self, pid):
        self._runningPid = pid

