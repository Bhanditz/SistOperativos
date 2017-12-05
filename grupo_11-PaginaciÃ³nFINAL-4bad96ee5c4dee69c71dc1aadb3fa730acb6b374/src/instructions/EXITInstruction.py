from src.instructions.Instruction import Instruction


class EXITInstruction(Instruction):

    def isExit(self):
        return True

    def __repr__(self):
        return "EXIT"

    def run(self, pc, ir, pcb):
        print("Exec: {op}, PC={pc}, PCB={pcb}".format(op=ir, pc=pc, pcb= pcb._pid))