from src.instructions.Instruction import Instruction
import logging

class CPUInstruction(Instruction):

    def __repr__(self):
        if self._count:
            return "CPU({count})".format(count=self._count)
        else:
            return "CPU"

    def isCpu(self):
        return True

    def run(self, pc, ir, pcb):
        print("Exec: {op}, PC={pc}, PCB={pcb}".format(op=ir, pc=pc, pcb = pcb._pid))