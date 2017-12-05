#!/usr/bin/env python3
import math

from src.Dispatcher import Dispatcher
from src.PCBTable import PCBTable
from src.Scheduler import Scheduler
from src.interruptionHandlers.IRQ import IRQ
from src.interruptionHandlers.IRQVector import IRQTypes


class Kernel:

    def __init__(self, hardware, schedulerAlgorithm, memoryType):
        self._hardware      = hardware
        self._dispatcher    = Dispatcher(hardware.cpu(), hardware.mmu())
        self._scheduler     = Scheduler(schedulerAlgorithm)
        self._pcbTable      = PCBTable()
        self._fileSystem    = memoryType.fileSystem()
        self._memoryManager = memoryType.memoryManager()
        self._loader        = memoryType.loader()

    def execute(self, path, priority = 0):
        irq = IRQ(IRQTypes.NEW)
        irq._path = path
        irq._priority = priority
        self._hardware.irqVector().kernel(self)
        self._hardware.irqVector().handle(irq)

    def start_running(self, ticks = math.inf):
        self._hardware.clock().run(ticks)



    def hardware(self):
        return self._hardware

    def pcbTable(self):
        return self._pcbTable

    def scheduler(self):
        return self._scheduler

    def dispatcher(self):
        return self._dispatcher

    def loader(self):
        return self._loader

    def fileSystem(self):
        return self._fileSystem

    def memoryManager(self):
        return self._memoryManager