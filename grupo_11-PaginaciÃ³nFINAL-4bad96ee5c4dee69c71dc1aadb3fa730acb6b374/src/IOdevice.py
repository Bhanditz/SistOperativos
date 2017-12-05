from queue import Queue
from src.interruptionHandlers.IRQ import IRQ
from src.interruptionHandlers.IRQVector import IRQTypes


class IOdevice:

    def __init__(self, irqVector):
        self._runtime = 5
        self._tickCount = 0
        self._waitingQueue = Queue()
        self._currentPcb = None
        self._irqVector = irqVector


    def tick(self):
        if (self._currentPcb):
            self.keepRunning()
        else:
            self.loadFromWaitingQueue()


    def keepRunning(self):
        self._tickCount += 1
        if (self._runtime < self._tickCount):
            irq = IRQ(IRQTypes.IO_OUT)
            self._tickCount = 0
            print('IO_OUT_interruption')
            self._irqVector.handle(irq)


    def loadFromWaitingQueue(self):
        if (not self._waitingQueue.empty()):
            self._currentPcb = self._waitingQueue.get()
            self._tickCount += 1

    def getCurrentPCB(self):
        pcb = self._currentPcb
        self._currentPcb = None
        return pcb

    def getWaitingQueue(self):
        return self._waitingQueue

    def addToWaitingQueue(self, pcb):
        self._waitingQueue.put(pcb)