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
        self.program0 = Program("t.exe", [CPUInstruction(10)])
        self.program1 = Program("p.exe", [CPUInstruction(5)])
        self.program2 = Program("x.exe", [IOInstruction(1),
                                           CPUInstruction(2),
                                           ])


        self.hardware = Hardware(memorySize = 64)
        self.kernel = Kernel(self.hardware, FCFS(), Pagination(self.hardware.memory(), self.hardware.mmu(), frameSize=2))
        self.fileSystem = self.kernel.fileSystem()


        # Load programs
        self.fileSystem.save("home/nicolas/program0", self.program0)
        self.fileSystem.save("home/nicolas/program1", self.program1)
        self.fileSystem.save("home/nicolas/program2", self.program2)


        self.scheduler = self.kernel.scheduler()
        self.pcbTable = self.kernel.pcbTable()
        self.cpu = self.kernel.hardware().cpu()
        self.waitingQueue = self.kernel.hardware().IOdevice().getWaitingQueue()



    def FCFS_Test(self):
        self.kernel.execute("home/nicolas/program0")
        self.kernel.execute("home/nicolas/program1")
        self.kernel.start_running(2) # Ejecuto 2 ticks
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 1)  # La cola de listos tiene el pcb de program1
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 0) # el pid de program0
        self.assertEqual(self.cpu.getPCB().getPid(), 0)
        self.kernel.start_running(9) # debe cambiar de contexto a program1, program0 termino
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 0) # Program1 termino, program0 esta en Cpu
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 1) # el pid de program1
        self.assertEqual(self.cpu.getPCB().getPid(), 1)
        self.kernel.start_running(3) # ejecuto tres instrucciones de program1
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 0)
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 1)
        self.assertEqual(self.cpu.getPCB().getPid(), 1)
        self.kernel.start_running(3) # ejecuto las instrucciones que quedan de program1
        self.assertEqual(self.cpu.getPC(), -1) # Cpu esta ociosa [en realidad deberia ser pc = -1]
        print(self.kernel.hardware().memory())


    def FCFS_IO_Test(self):
        self.kernel.execute("home/nicolas/program2")
        self.kernel.execute("home/nicolas/program0")
        self.kernel.start_running(1) # ejecuto un tick, program 2 tira una interrupcion de IO
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 0) # vacia, program2 esta haciendo IO, program0 en Cpu
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 1) # el pid de program0
        self.assertEqual(self.cpu.getPCB().getPid(), 1)
        self.assertEqual(self.waitingQueue.qsize(), 1) # el pcb de program2
        self.kernel.start_running(6) # program2 termina IO y pasa a readyQueue
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 1) # program0 sigue ejecutando
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 1)
        self.assertEqual(self.cpu.getPCB().getPid(), 1)
        self.kernel.start_running(5) # program0 termina
        self.assertEqual(self.scheduler.getReadyQueue().qsize(), 0) # program2 esta en Cpu
        self.assertEqual(self.pcbTable.runningPcb().getPid(), 0) # el pid de program2
        self.assertEqual(self.cpu.getPCB().getPid(), 0)
        self.kernel.start_running(3) # termina program2
        print(self.kernel.hardware().memory())
