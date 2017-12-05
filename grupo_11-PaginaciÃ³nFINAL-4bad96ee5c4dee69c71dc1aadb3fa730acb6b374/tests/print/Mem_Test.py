
import unittest
from src.Hardware import Hardware
from src.Kernel import Kernel
from src.PlanificationAlgorithms.FCFS import FCFS
from src.Program import Program
from src.instructions.CPUInstruction import CPUInstruction
from src.instructions.IOInstruction import IOInstruction
from src.pagedMemory.Pagination import Pagination


class Mem_Test(unittest.TestCase):

    def setUp(self):
        self.program0 = Program("t.exe", [CPUInstruction(9)])
        self.program2 = Program("s.exe", [CPUInstruction(5), IOInstruction(1)])

        self.hardware = Hardware(memorySize = 32)
        self.kernel = Kernel(self.hardware, FCFS(), Pagination(self.hardware.memory(), self.hardware.mmu(), frameSize=2))
        self.fileSystem = self.kernel.fileSystem()

        # Load programs
        self.fileSystem.save("home/nicolas/program0", self.program0)
        self.fileSystem.save("home/nicolas/program2", self.program2)


    # frameSize = 2
    # GetFramesForProgram0 --> frames[15,14,13,12,11]
    # pag = pc = 0 / frameSize (2)
    # offset = pc = 0 % frameSize
    # DirFisic = frame * FrameSize (2) + offset
    # Dirs Fisicas --> # PAg0 --> 30, 31 # PAg1 --> 28, 29 # PAg2 --> 26, 27 # etc
    def load_a_Program_Test(self):
        self.kernel.execute("home/nicolas/program0")
        self.kernel.start_running(11)
        print(self.kernel.hardware().memory())


    def load_two_programs_Test(self):
        self.kernel.execute("home/nicolas/program0")
        self.kernel.execute("home/nicolas/program2")
        self.kernel.start_running(25)
        print(self.kernel.hardware().memory())