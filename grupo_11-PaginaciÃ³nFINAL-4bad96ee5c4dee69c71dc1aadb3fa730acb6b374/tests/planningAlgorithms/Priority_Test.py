import unittest
from src.Hardware import Hardware
from src.Kernel import Kernel
from src.PlanificationAlgorithms.Priority import Priority
from src.Program import Program
from src.instructions.CPUInstruction import CPUInstruction
from src.pagedMemory.Pagination import Pagination


class Priority_Test(unittest.TestCase):

    def setUp(self):
        self.program0 = Program("t.exe", [CPUInstruction(3)])
        self.program1 = Program("p.exe", [CPUInstruction(5)])
        self.program2 = Program("e.exe", [CPUInstruction(10)])

        self.hardware = Hardware(memorySize = 32)
        self.kernel = Kernel(self.hardware, Priority(5), Pagination(self.hardware.memory(), self.hardware.mmu(), frameSize=2))
        self.fileSystem = self.kernel.fileSystem()

        # Load programs
        self.fileSystem.save("home/nicolas/program0", self.program0)
        self.fileSystem.save("home/nicolas/program1", self.program1)
        self.fileSystem.save("home/nicolas/program2", self.program2)

        self.scheduler = self.kernel.scheduler()
        self.pcbTable = self.kernel.pcbTable()
        self.cpu = self.kernel.hardware().cpu()


    def priority_Test(self):
        self.kernel.execute("home/nicolas/program0", 3) # CPU esta ociosa y llega program0 primero, se ejecuta primero
        self.kernel.execute("home/nicolas/program1", 2) # Llega program1 1 pero se ejecuta ultimo
        self.kernel.execute("home/nicolas/program2", 1) # Llega program2 y se ejecuta segundo
        self.kernel.start_running(2) # Ejecuto 2 ticks
        self.assertTrue(len(self.scheduler.getReadyQueue()), 2)  # La cola de listos tiene 2 pcbs, de program1 y 2
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 0) # verifico que tiene el pid para program0
        self.assertEqual(self.cpu.getPCB().getPid(), 0)
        self.kernel.start_running(2) # Ejecuta los ticks necesarios para terminar program0
        self.assertTrue(len(self.scheduler.getReadyQueue()), 1)  # La cola de listos tiene solo un pcb, el de program1
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 2) # el pid de program2, que tiene mayor prioridad
        self.assertEqual(self.cpu.getPCB().getPid(), 2)
        self.kernel.start_running(11)  # Ejecuta los ticks necesarios para terminar program2
        self.assertTrue(len(self.scheduler.getReadyQueue()), 0)  # La cola de listos ya no tiene pcbs
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 1) # el pid de program1
        self.assertEqual(self.cpu.getPCB().getPid(), 1)
        print(self.kernel.hardware().memory())
