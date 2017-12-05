from src.interruptionHandlers.IRQ import IRQ
from src.interruptionHandlers.IRQVector import IRQTypes


class CPU():

    def __init__(self, mmu, irqVector):
        self._mmu = mmu
        self._pcb = None
        self._pc = -1
        self._ir = None
        self._irqVector = irqVector

    def tick(self):
        if (self._pc != -1):
            self.fetch()
            self.decode()
            self.execute()

    def decode(self): {}

    def fetch(self):
        self._ir = self._mmu.fetch(self._pc)
        self._pc += 1

    def execute(self):
        if (self._ir.isCpu()):
            self._ir.run(self._pc, self._ir, self._pcb) # self._ir parametro demás

        elif (self._ir.isIo()):
            self._ir.run(self._pc, self._ir, self._pcb)
            print('IO_IN_interruption')
            irq = IRQ(IRQTypes.IO_IN)
            self._irqVector.handle(irq)

        elif (self._ir.isExit()):
            self._ir.run(self._pc, self._ir, self._pcb)
            irq = IRQ(IRQTypes.KILL)
            self._irqVector.handle(irq)


    def setPCB(self,pcb):
        self._pcb = pcb

    def getPCB(self):
        return self._pcb

    def setPC(self,pc):
        self._pc = pc

    def getPC(self):
        return self._pc

    # No se usa
    def __repr__(self):
        return "CPU(PC={pc})".format(pc=self._pcb._pc)
