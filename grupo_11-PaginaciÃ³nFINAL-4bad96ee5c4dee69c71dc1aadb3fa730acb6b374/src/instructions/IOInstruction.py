from src.instructions.Instruction import Instruction

class IOInstruction(Instruction):

    def __repr__(self):
        if self._count:
            return "IO({count})".format(count=self._count)
        else:
            return "IO"

    def isIo(self):
        return True

    def run(self, pc, ir, pcb):
        print("Exec: {op}, PC={pc}, PCB={pcb}".format(op=ir, pc=pc, pcb = pcb._pid))