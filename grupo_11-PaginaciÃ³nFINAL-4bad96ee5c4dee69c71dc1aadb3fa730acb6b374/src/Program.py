from src.instructions.EXITInstruction import EXITInstruction

class Program:

    def __init__(self, name, instructions):
        self._name = name
        self._instructions = instructions

    @property
    def name(self):
        return self._name

    @property
    def instructions(self):
        return self._instructions

    def expand(self):
        expanded = []

        for instr in self._instructions:
            expanded.extend(instr.expand())

        if not expanded[-1].isExit():
            expanded.append(EXITInstruction(1))

        self._instructions = expanded
        return self

    def size(self):
        return len(self._instructions)

    # permitido, se usa solo en loader
    def copy(self):
        instructions = []
        for instr in self._instructions:
            instructions.append(instr)
        return Program(self._name, instructions)



    def __repr__(self):
        return "Program({name}, {instructions})".format(name=self._name, instructions=self._instructions)