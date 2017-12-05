from src.States import State
from src.interruptionHandlers.IRQHandler import IRQHandler


class IoInIRQHandler(IRQHandler):


    def execute(self, irq):
        self.deallocate(irq, State.WAITING)
        ##self._IOdeviceController.add(pcb) --> hay q crear el IOdeviceController y reemp por IOdevice
        pcb = irq.pcbTable().runningPcb()
        irq.IOdevice().addToWaitingQueue(pcb)
        irq.timer().resetTimer()
        irq.pcbTable().setRunningPid(None)
        if(not irq.scheduler().isEmpty()):
            pcb = irq.scheduler().getNext()
            self.allocate(irq, pcb)


