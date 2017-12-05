
import unittest
from src.Hardware import Hardware
from src.Kernel import Kernel
from src.PlanificationAlgorithms.Priority import Priority
from src.Program import Program
from src.instructions.CPUInstruction import CPUInstruction
from src.pagedMemory.Pagination import Pagination


class Priority_Test(unittest.TestCase):

    def setUp(self):
        self.program0 = Program("t.exe", [CPUInstruction(9)])
        self.program1 = Program("p.exe", [CPUInstruction(2)])
        self.program2 = Program("x.exe", [CPUInstruction(5)])
        self.program3 = Program("e.exe", [CPUInstruction(10)])

        self.hardware = Hardware(memorySize = 64)
        self.kernel = Kernel(self.hardware, Priority(5), Pagination(self.hardware.memory(), self.hardware.mmu(), frameSize=2))
        self.fileSystem = self.kernel.fileSystem()

        # Load programs
        self.fileSystem.save("home/nicolas/program0", self.program0)
        self.fileSystem.save("home/nicolas/program1", self.program1)
        self.fileSystem.save("home/nicolas/program2", self.program2)
        self.fileSystem.save("home/nicolas/program3", self.program3)

    def prioridad_Test(self):
        self.kernel.execute("home/nicolas/program2", 3) # 1 porque cpu esta ociosa
        self.kernel.execute("home/nicolas/program1", 2) # 4
        self.kernel.execute("home/nicolas/program0", 1) # 3
        self.kernel.execute("home/nicolas/program3", 0) # 2
        self.kernel.start_running()