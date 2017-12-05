import unittest
from src.Hardware import Hardware
from src.Kernel import Kernel
from src.PlanificationAlgorithms.RoundRobin import RoundRobin
from src.Program import Program
from src.instructions.CPUInstruction import CPUInstruction
from src.instructions.IOInstruction import IOInstruction
from src.pagedMemory.Pagination import Pagination


class RoundRobin_Test(unittest.TestCase):

    def setUp(self):
        self.program0 = Program("t.exe", [CPUInstruction(10)])
        self.program1 = Program("p.exe", [CPUInstruction(5)])
        self.program2 = Program("t.exe", [IOInstruction(1),
                                           CPUInstruction(2),
                                           ])


        self.hardware = Hardware(memorySize = 32)
        self.kernel = Kernel(self.hardware, RoundRobin(3, self.hardware.clock(), self.hardware.irqVector()),
                             Pagination(self.hardware.memory(), self.hardware.mmu(), frameSize=2))
        self.fileSystem = self.kernel.fileSystem()

        # Load programs
        self.fileSystem.save("home/nicolas/program0", self.program0)
        self.fileSystem.save("home/nicolas/program1", self.program1)
        self.fileSystem.save("home/nicolas/program2", self.program2)


        self.scheduler = self.kernel.scheduler()
        self.pcbTable = self.kernel.pcbTable()
        self.cpu = self.kernel.hardware().cpu()
        self.waitingQueue = self.kernel.hardware().IOdevice().getWaitingQueue()


    def RR_Test(self):
        self.kernel.execute("home/nicolas/program0")
        self.kernel.execute("home/nicolas/program1")
        self.kernel.start_running(3) # Ejecuto 3 ticks, el quantum
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 1)  # La cola de listos tiene el pcb de program1
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 0) # el pid de program0
        self.assertEqual(self.cpu.getPCB().getPid(), 0)
        self.kernel.start_running(3) # cambia de proceso, debe ejecutar program1
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 1)  # La cola de listos tiene el pcb de program0
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 1) # el pid de program1
        self.assertEqual(self.cpu.getPCB().getPid(), 1)
        self.kernel.start_running(3)
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 1)
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 0)
        self.assertEqual(self.cpu.getPCB().getPid(), 0)
        self.kernel.start_running(2) # los ticks que le quedan a program 1
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 1)
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 1)
        self.assertEqual(self.cpu.getPCB().getPid(), 1)
        self.kernel.start_running(1)
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 0) # ya no esta program1
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 0)
        self.assertEqual(self.cpu.getPCB().getPid(), 0)
        print(self.kernel.hardware().memory())


    def RR_IO_Test(self):
        self.kernel.execute("home/nicolas/program2")
        self.kernel.execute("home/nicolas/program0")
        self.kernel.start_running(1)
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 0)
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 1)
        self.assertEqual(self.cpu.getPCB().getPid(), 1)
        self.assertEqual(self.waitingQueue.qsize(), 1)
        self.kernel.start_running(2)
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 0)
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 1)
        self.assertEqual(self.cpu.getPCB().getPid(), 1)
        self.assertEqual(self.waitingQueue.qsize(), 0)
        self.kernel.start_running(3)
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 0)
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 1)
        self.assertEqual(self.cpu.getPCB().getPid(), 1)
        self.kernel.start_running(3)
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 1)
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 0)
        self.assertEqual(self.cpu.getPCB().getPid(), 0)
        self.kernel.start_running(3)
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 0)
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 1)
        self.assertEqual(self.cpu.getPCB().getPid(), 1)
        print(self.kernel.hardware().memory())