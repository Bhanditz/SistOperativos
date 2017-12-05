from src.Exceptions.NotEnoughSpaceInMemoryException import NotEnoughSpaceInMemoryException


class Loader:

    def __init__(self, fileSystem, memoryManager, memory):
        self._fileSystem = fileSystem
        self._memoryManager = memoryManager
        self._memory = memory

    def load(self, path):
        program = self._fileSystem.get(path)
        if self._memoryManager.freeFramesLength() >= self._memoryManager.cantPages(program) :
            free_frames = self._memoryManager.getFreeFrames(self._memoryManager.cantPages(program))
            self.loadToMemory(free_frames, program)
            return self._memoryManager.generatePageTable(free_frames, program)
        else:
            raise NotEnoughSpaceInMemoryException


    def loadToMemory(self, freeFrames, program):
        instructions = program.copy().instructions # permitido para que no sea list instructions destructiva
        offset = 0
        for frame in freeFrames:
            for instr in instructions:
                if offset < self._memoryManager.frameSize():
                    basedir = self._memoryManager.frameSize() * frame
                    self._memory.put(basedir + offset, instr)
                    offset += 1
                else:
                    offset = 0
                    del instructions[:self._memoryManager.frameSize()]
                    break



