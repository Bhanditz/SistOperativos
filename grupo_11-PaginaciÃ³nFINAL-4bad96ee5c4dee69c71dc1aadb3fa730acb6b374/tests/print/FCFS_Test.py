
import unittest
from src.Hardware import Hardware
from src.Kernel import Kernel
from src.PlanificationAlgorithms.FCFS import FCFS
from src.Program import Program
from src.instructions.CPUInstruction import CPUInstruction
from src.instructions.IOInstruction import IOInstruction
from src.pagedMemory.Pagination import Pagination


class FCFS_Test(unittest.TestCase):

    def setUp(self):
        self.program0 = Program("t.exe", [CPUInstruction(9)])
        self.program1 = Program("p.exe", [CPUInstruction(5)])
        self.program2 = Program("f.exe", [CPUInstruction(5), IOInstruction(1)])

        self.hardware = Hardware(memorySize = 32)
        self.kernel = Kernel(self.hardware, FCFS(), Pagination(self.hardware.memory(), self.hardware.mmu(), frameSize=2))
        self.fileSystem = self.kernel.fileSystem()


        # Load programs
        self.fileSystem.save("home/nicolas/program0", self.program0)
        self.fileSystem.save("home/nicolas/program1", self.program1)
        self.fileSystem.save("home/nicolas/program2", self.program2)


    def FCFS_Test(self):
        self.kernel.execute("home/nicolas/program0")
        self.kernel.execute("home/nicolas/program1")
        self.kernel.start_running()

    def FCFS_IO_Test(self):
        self.kernel.execute("home/nicolas/program0")
        self.kernel.execute("home/nicolas/program2")
        self.kernel.execute("home/nicolas/program1")
        self.kernel.start_running()
