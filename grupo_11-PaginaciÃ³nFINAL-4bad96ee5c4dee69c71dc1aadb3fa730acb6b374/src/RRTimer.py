from src.interruptionHandlers.IRQ import IRQ
from src.interruptionHandlers.IRQTypes import IRQTypes


class RRTimer:

    def __init__(self, quantum, irqVector):
        self._quantum = quantum
        self._irqVector = irqVector
        self._tickCount = 0


    def tick(self):
        if(self._tickCount >= self._quantum):
            self._tickCount = 0
            irq = IRQ(IRQTypes.TIMEOUT)
            self._irqVector.handle(irq)
        self._tickCount += 1


    def resetTimer(self):
        self._tickCount = 0

