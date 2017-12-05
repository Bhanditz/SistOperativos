
class MMU:

    def __init__(self, mem):
        self._memory = mem
        self._pcb = None
        self._frameSize = None # No necesario pero usado por ahora

    def fetch(self, pc):
        pag = int(pc / self._frameSize)
        offset = pc % self._frameSize
        frame = self._pcb.pageTable().getFrame(pag)
        return self._memory.get(frame * self._frameSize + offset)


    def setFrameSize(self, frameSize):
        self._frameSize = frameSize

    def pcb(self, pcb):
        self._pcb = pcb

