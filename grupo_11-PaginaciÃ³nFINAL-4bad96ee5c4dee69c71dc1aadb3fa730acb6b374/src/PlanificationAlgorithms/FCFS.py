from queue import Queue

class FCFS():

    def __init__(self):
        self._readyQueue = Queue()

    def mustExpropiate(self, a_pcb, another_pcb):
        return False

    def addPCB(self, pcb):
        self._readyQueue.put(pcb)

    def empty(self):
        return self._readyQueue.empty()

    def getNext(self):
        return self._readyQueue.get()

    def getReadyQueue(self):
        return self._readyQueue









