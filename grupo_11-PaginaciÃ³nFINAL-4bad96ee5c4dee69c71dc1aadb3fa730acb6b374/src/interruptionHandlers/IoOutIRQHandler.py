from src.States import State
from src.interruptionHandlers.IRQHandler import IRQHandler


class IoOutIRQHandler(IRQHandler):


    def execute(self, irq):
        pcb = irq.IOdevice().getCurrentPCB()
        if (irq.pcbTable().getRunningPid() != None):  # Hay uno corriendo
            if irq.scheduler().mustExpropiate(irq.pcbTable().runningPcb(), pcb):  # Si es expropiado, pcb en cpu va a cola de ready y el otro a cpu
                running = irq.pcbTable().runningPcb()
                self.deallocate(irq, State.READY)
                irq.scheduler().add(running)
                self.allocate(irq, pcb)
                print("EXPROPRIATED")
            else:  # No obtuvo cpu en la expropiacion, pasa a la cola de ready
                pcb._state = State.READY
                irq.scheduler().add(pcb)

        else:  # No habia nada en CPU
            self.allocate(irq, pcb)
