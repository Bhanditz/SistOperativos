import unittest
from src.Hardware import Hardware
from src.Kernel import Kernel
from src.PlanificationAlgorithms.PreemptivePriority import PreemptivePriority
from src.Program import Program
from src.instructions.CPUInstruction import CPUInstruction
from src.pagedMemory.Pagination import Pagination


class PreemptivePriority_Algorithm_Test(unittest.TestCase):

    def setUp(self):
        self.program0 = Program("t.exe", [CPUInstruction(3)])
        self.program1 = Program("p.exe", [CPUInstruction(5)])

        self.hardware = Hardware(memorySize = 32)
        self.kernel = Kernel(self.hardware, PreemptivePriority(5), Pagination(self.hardware.memory(), self.hardware.mmu(), frameSize=2))
        self.fileSystem = self.kernel.fileSystem()

        # Load programs
        self.fileSystem.save("home/nicolas/program0", self.program0)
        self.fileSystem.save("home/nicolas/program1", self.program1)

        self.scheduler = self.kernel.scheduler()
        self.pcbTable = self.kernel.pcbTable()
        self.cpu = self.kernel.hardware().cpu()


    # Agrego un prog le ejecuto 2 ticks, agrego otro con mayor prioridad el cual expropia Cpu, este termina y se vuelve a ejecutar
    # el primer programa
    def prioridadExp_Test(self):
        self.kernel.execute("home/nicolas/program0", 3) # CPU esta ociosa y llega program0 primero
        self.kernel.start_running(2)  # Ejecuta por 2 ticks
        self.assertTrue(self.scheduler.isEmpty()) # la cola de listos pasa a estar vacia, program0 esta en Cpu
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 0)
        self.assertEqual(self.cpu.getPCB().getPid(), 0)
        self.kernel.execute("home/nicolas/program1", 2) # llega program1 y expropia Cpu
        self.kernel.start_running(2) # Ejecuta 2 ticks
        self.assertTrue(len(self.scheduler.getReadyQueue()), 1)  # la cola de listos tiene el pcb de program0
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 1)
        self.assertEqual(self.cpu.getPCB().getPid(), 1)
        self.kernel.start_running(4) # Despues de 6 ticks program1 termina, y vuelve a ejecutar program0
        self.assertTrue(len(self.scheduler.getReadyQueue()), 0)
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 0)
        self.assertEqual(self.cpu.getPCB().getPid(), 0)
        print(self.kernel.hardware().memory())
