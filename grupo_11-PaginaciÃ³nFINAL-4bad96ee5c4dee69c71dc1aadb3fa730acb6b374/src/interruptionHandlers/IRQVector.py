from src.DummyTimer import DummyTimer
from src.interruptionHandlers.IRQTypes import IRQTypes
from src.interruptionHandlers.IoInIRQHandler import IoInIRQHandler
from src.interruptionHandlers.IoOutIRQHandler import IoOutIRQHandler
from src.interruptionHandlers.KillIRQHandler import KillIRQHandler
from src.interruptionHandlers.NewIRQHandler import NewIRQHandler
from src.interruptionHandlers.TimeOutIRQHandler import TimeOutIRQHandler


class IRQVector():

    def __init__(self):
        self._allHandlers = {}
        self.register(IRQTypes.NEW, NewIRQHandler())
        self.register(IRQTypes.IO_IN, IoInIRQHandler())
        self.register(IRQTypes.IO_OUT, IoOutIRQHandler())
        self.register(IRQTypes.KILL, KillIRQHandler())
        self.register(IRQTypes.TIMEOUT, TimeOutIRQHandler())

    def handle(self, irq):
        handler = self._allHandlers[irq.getIrqType()]
        if(handler != None):
            irq.setUp(self._kernel.pcbTable(), self._kernel.scheduler(), self._kernel.dispatcher(), self._kernel.loader(),
                      self._kernel.hardware().IOdevice(), self._kernel.hardware().clock().timer(), self._kernel.memoryManager())
            handler.execute(irq)

    def register(self, irqType, handler):
        self._allHandlers[irqType] = handler


    def kernel(self, aKernel):
        self._kernel = aKernel


