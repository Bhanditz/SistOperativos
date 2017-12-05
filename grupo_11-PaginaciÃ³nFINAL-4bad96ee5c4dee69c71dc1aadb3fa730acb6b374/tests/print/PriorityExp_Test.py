
import unittest
from src.Hardware import Hardware
from src.Kernel import Kernel
from src.PlanificationAlgorithms.PreemptivePriority import PreemptivePriority
from src.Program import Program
from src.instructions.CPUInstruction import CPUInstruction
from src.pagedMemory.Pagination import Pagination


class PriorityExp_Test(unittest.TestCase):

    def setUp(self):
        self.program0 = Program("t.exe", [CPUInstruction(3)])
        self.program1 = Program("p.exe", [CPUInstruction(5)])
        self.program2 = Program("t.exe", [CPUInstruction(7)])


        self.hardware = Hardware(memorySize = 64)
        self.kernel = Kernel(self.hardware, PreemptivePriority(5), Pagination(self.hardware.memory(), self.hardware.mmu(), frameSize=2))
        self.fileSystem = self.kernel.fileSystem()

        # Load programs
        self.fileSystem.save("home/nicolas/program0", self.program0)
        self.fileSystem.save("home/nicolas/program1", self.program1)
        self.fileSystem.save("home/nicolas/program2", self.program2)

    def prioridadExp_Simple_Test(self):
        self.kernel.execute("home/nicolas/program0", 3) # 2 CPU esta ociosa y llega program0 primero
        self.kernel.execute("home/nicolas/program1", 2) # 1 # pero luego llega a la cola de listos program1 con una prioridad mayor
        self.kernel.start_running()

    def prioridadExp_Test(self):
        self.kernel.execute("home/nicolas/program0", 3) # 3
        self.kernel.execute("home/nicolas/program1", 2) # 1
        self.kernel.start_running(3) # Ejecuta por 3 ticks
        self.kernel.execute("home/nicolas/program2", 1) # 2 Se agrega el prog2 y toma CPU por expropiacion
        self.kernel.start_running() # Termina de correr todos los progs.