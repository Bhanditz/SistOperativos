from src.States import State
from src.interruptionHandlers.IRQHandler import IRQHandler


class NewIRQHandler(IRQHandler):


    def execute(self, irq):
        pageTable = irq.loader().load(irq.path())
        pcb = irq.pcbTable().createPcb(irq.priority(), pageTable)
        if (irq.pcbTable().getRunningPid() != None): #Hay uno corriendo
            if (irq.scheduler().mustExpropiate(irq.pcbTable().runningPcb(), pcb)):
                current = irq.pcbTable().runningPcb()
                self.deallocate(irq, State.READY)
                irq.scheduler().add(current)
                self.allocate(irq, pcb)
                print("EXPROPRIATED")
            else: # No obtuvo cpu en la expropiacion, pasa a la cola de ready
                pcb.setState(State.READY)
                irq.scheduler().add(pcb)

        else: # Como no habia nada en Cpu alojo el proceso en la misma
            self.allocate(irq, pcb)

