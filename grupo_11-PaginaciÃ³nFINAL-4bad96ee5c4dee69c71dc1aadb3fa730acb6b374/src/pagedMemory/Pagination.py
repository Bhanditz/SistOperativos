from src.pagedMemory.FileSystem import FileSystem
from src.pagedMemory.Loader import Loader
from src.pagedMemory.MemoryManager import MemoryManager


class Pagination:

    def __init__(self, memory, mmu, frameSize):
        self._fileSystem = FileSystem()
        self._memoryManager = MemoryManager(memory, frameSize)
        self._loader = Loader(self._fileSystem, self._memoryManager, memory)
        mmu.setFrameSize(frameSize)

    def fileSystem(self):
        return self._fileSystem

    def memoryManager(self):
        return self._memoryManager

    def loader(self):
        return self._loader