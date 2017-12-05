import unittest
from src.Hardware import Hardware
from src.Kernel import Kernel
from src.PlanificationAlgorithms.RoundRobin import RoundRobin
from src.Program import Program
from src.instructions.CPUInstruction import CPUInstruction
from src.instructions.IOInstruction import IOInstruction
from src.pagedMemory.Pagination import Pagination


class SO_Test(unittest.TestCase):

    def setUp(self):
        self.program0 = Program("p.exe", [CPUInstruction(3)])
        self.program1 = Program("t.exe", [CPUInstruction(5)])
        self.program2 = Program("t.exe", [ IOInstruction(1),
                                            CPUInstruction(5),
                                           ])
        self.program3 = Program("f.exe", [CPUInstruction(3),
                                           IOInstruction(1),
                                           ])


        self.hardware = Hardware(memorySize = 32)
        self.kernel = Kernel(self.hardware, RoundRobin(3, self.hardware.clock(), self.hardware.irqVector()),
                             Pagination(self.hardware.memory(), self.hardware.mmu(), frameSize=2))
        self.fileSystem = self.kernel.fileSystem()

        # Load programs
        self.fileSystem.save("home/nicolas/program0", self.program0)
        self.fileSystem.save("home/nicolas/program1", self.program1)
        self.fileSystem.save("home/nicolas/program2", self.program2)
        self.fileSystem.save("home/nicolas/program3", self.program3)

    def test_RR(self):
        self.kernel.execute("home/nicolas/program0")
        self.kernel.execute("home/nicolas/program1")
        self.kernel.start_running()

    def test_RR_IO(self):
        self.kernel.execute("home/nicolas/program2")
        self.kernel.execute("home/nicolas/program1")
        self.kernel.execute("home/nicolas/program3")
        self.kernel.start_running()