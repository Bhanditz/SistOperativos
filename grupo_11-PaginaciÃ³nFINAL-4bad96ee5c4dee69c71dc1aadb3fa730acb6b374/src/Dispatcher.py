
class Dispatcher:

    def __init__(self, cpu, mmu):
        self._cpu = cpu
        self._mmu = mmu

    def load(self, pcb):
        self._cpu.setPC(pcb.getPC())
        self._cpu.setPCB(pcb)
        self._mmu.pcb(pcb)

    def save(self, pcb):
        pcb.setPC(self._cpu.getPC())
        self._cpu.setPC(-1)




