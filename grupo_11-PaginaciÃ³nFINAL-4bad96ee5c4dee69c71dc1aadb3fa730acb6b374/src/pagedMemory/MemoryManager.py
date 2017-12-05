from src.PageTable import PageTable


class MemoryManager:

    def __init__(self, memory, frameSize):
        self._memory = memory
        self._frameSize = frameSize
        self._freeFrames = self.initFrames() # [0,1,2,3,4, etc]


    def freeFramesLength(self):
        return len(self._freeFrames)

    def initFrames(self):
        freeFrames = []
        for i in range(0, int(self._memory.size() / self._frameSize)):
            freeFrames.append(i)
        return freeFrames

    def cantPages(self, program):
        cantPages = int(program.size() / self._frameSize)
        if program.size() % self._frameSize > 0:
            cantPages += 1
        return cantPages


    def getFreeFrames(self, cantFrames):
        framesRet = []
        for i in range(0, cantFrames):
            frame = self._freeFrames.pop()
            framesRet.append(frame)
        return framesRet

    def generatePageTable(self, freeFrames, program):
        return PageTable(freeFrames, self.cantPages(program))

    def frameSize(self):
        return self._frameSize

    def restoreFramesUsed(self, frames):
        for frame in frames:
            self._freeFrames.append(frame)


    def freeFrames(self):
        return self._freeFrames