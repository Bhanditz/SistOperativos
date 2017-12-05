from src.States import State


class IRQHandler():

    def allocate(self, irq, pcb):
        pcb.setState(State.RUNNING)
        irq.pcbTable().setRunningPid(pcb.getPid())
        irq.dispatcher().load(pcb)

    def deallocate(self, irq, state):
        pcb = irq.pcbTable().runningPcb()
        irq.dispatcher().save(pcb)
        pcb.setState(state)

