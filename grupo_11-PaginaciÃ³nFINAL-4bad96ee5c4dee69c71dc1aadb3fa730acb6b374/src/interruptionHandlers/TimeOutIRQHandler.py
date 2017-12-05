from src.States import State
from src.interruptionHandlers.IRQHandler import IRQHandler


class TimeOutIRQHandler(IRQHandler):


    def execute(self, irq):
        if (irq.pcbTable().getRunningPid() != None):
            self.deallocate(irq, State.READY)
            pcb = irq.pcbTable().runningPcb()
            irq.scheduler().add(pcb)
            irq.pcbTable().setRunningPid(None)
            pcb = irq.scheduler().getNext()
            self.allocate(irq, pcb)
            print('TIMEOUT')
