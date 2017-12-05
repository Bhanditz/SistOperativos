from src.States import State
from src.interruptionHandlers.IRQHandler import IRQHandler


class KillIRQHandler(IRQHandler):


    def execute(self, irq):
        self.deallocate(irq, State.TERMINATED)
        self.takeOutBusyFrames(irq)
        irq.pcbTable().setRunningPid(None)
        irq.timer().resetTimer()
        if not irq.scheduler().isEmpty():
            pcb = irq.scheduler().getNext()
            self.allocate(irq, pcb)
        else:
            print("NOOP")


    # desocupar los frames usados
    def takeOutBusyFrames(self, irq):
        pcb = irq.pcbTable().runningPcb()
        if pcb.pageTable(): # pregunto porq en bajo demando pageTable no esta en Pcb
            frames = pcb.pageTable().getFrames()
            irq.memoryManager().restoreFramesUsed(frames)




