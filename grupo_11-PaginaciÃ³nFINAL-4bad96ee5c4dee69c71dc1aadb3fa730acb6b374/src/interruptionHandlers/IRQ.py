

class IRQ():

    def __init__(self, irq_type):
        self._irq_type  = irq_type

    def getIrqType(self):
        return self._irq_type

    def setUp(self, pcbTable, scheduler, dispatcher, loader, IOdevice, timer, memoryManager):
        self._pcbTable      = pcbTable
        self._scheduler     = scheduler
        self._dispatcher    = dispatcher
        self._loader        = loader
        self._IOdevice      = IOdevice
        self._timer         = timer
        self._memoryManager = memoryManager


    def pcbTable(self):
        return self._pcbTable

    def dispatcher(self):
        return self._dispatcher

    def IOdevice(self):
        return self._IOdevice

    def scheduler(self):
        return self._scheduler

    def timer(self):
        return self._timer

    def path(self):
        return self._path

    def loader(self):
        return self._loader

    def priority(self):
        return self._priority

    def memoryManager(self):
        return self._memoryManager