from src.CPU import CPU
from src.Clock import Clock
from src.DummyTimer import DummyTimer
from src.IOdevice import IOdevice
from src.MMU import MMU
from src.Memory import Memory
from src.interruptionHandlers.IRQVector import IRQVector


class Hardware:

    def __init__(self, memorySize):
        self._memory = Memory(memorySize)
        self._mmu = MMU(self._memory)
        self._irqVector = IRQVector()
        self._cpu = CPU(self._mmu, self._irqVector)
        self._IOdevice = IOdevice(self._irqVector)
        self._clock = Clock(self._cpu, self._IOdevice)
        self._timer = DummyTimer()



    def irqVector(self):
        return self._irqVector

    def clock(self):
        return self._clock

    def IOdevice(self):
        return self._IOdevice

    def timer(self):
        return self._timer

    def setTimer(self, aTimer):
        self._timer = aTimer

    def mmu(self):
        return self._mmu

    def cpu(self):
        return self._cpu

    def memory(self):
        return self._memory