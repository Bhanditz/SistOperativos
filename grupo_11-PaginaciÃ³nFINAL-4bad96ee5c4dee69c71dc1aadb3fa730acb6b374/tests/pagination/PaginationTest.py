
import unittest
from src.Exceptions.NotEnoughSpaceInMemoryException import NotEnoughSpaceInMemoryException
from src.Exceptions.ProgramNotAvailableException import ProgramNotAvailableException
from src.Hardware import Hardware
from src.Kernel import Kernel
from src.PlanificationAlgorithms.FCFS import FCFS
from src.Program import Program
from src.instructions.CPUInstruction import CPUInstruction
from src.instructions.EXITInstruction import EXITInstruction
from src.instructions.IOInstruction import IOInstruction
from src.pagedMemory.Pagination import Pagination


class PaginationTest(unittest.TestCase):

    def setUp(self):
        self.program0 = Program("t.exe", [CPUInstruction(10)])
        self.program2 = Program("x.exe", [IOInstruction(1),
                                           CPUInstruction(60),
                                           ])

        self.program3 = Program("f.exe", [CPUInstruction(65)]) # Programa demasiado grande para la memoria disponible


        self.hardware = Hardware(memorySize=64)
        self.kernel = Kernel(self.hardware, FCFS(), Pagination(self.hardware.memory(), self.hardware.mmu(), frameSize=2))
        self.fileSystem = self.kernel.fileSystem()

        # Load programs
        self.fileSystem.save("home/nicolas/program0", self.program0)
        self.fileSystem.save("home/nicolas/program2", self.program2)
        self.fileSystem.save("home/nicolas/program3", self.program3)


        self.scheduler = self.kernel.scheduler()
        self.pcbTable = self.kernel.pcbTable()
        self.cpu = self.kernel.hardware().cpu()
        self.waitingQueue = self.kernel.hardware().IOdevice().getWaitingQueue()


    def load_program_Test(self):
        self.assertEqual(self.fileSystem.get("home/nicolas/program0"), self.program0)
        program0 = self.fileSystem.get("home/nicolas/program0")
        self.assertEqual(self.kernel.memoryManager().freeFramesLength(), 32)
        self.assertEqual(self.kernel.memoryManager().cantPages(program0), 6)
        self.assertEqual(self.kernel.memoryManager().freeFrames(), [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                                                                    21,22,23,24,25,26,27,28,29,30,31])
        self.assertEqual(self.kernel.memoryManager().generatePageTable([26,27,28,29,30,31], program0).getFrames(), [26,27,28,
                                                                                                                    29,30,31])
        self.kernel.execute("home/nicolas/program0")
        self.kernel.start_running(1) # Ejecuto 1 tick
        self.assertEqual(self.kernel.memoryManager().freeFramesLength(), 26)
        self.assertEqual(self.kernel.memoryManager().freeFrames(),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
        self.assertEqual(self.pcbTable.runningPcb().pageTable().getFrames(), [31,30,29,28,27,26])

    def pagination_memory_Test(self):
        self.kernel.execute("home/nicolas/program0") # El programa tiene 11 instrucciones, 10 de Cpu y una de Exit
        self.assertEqual(type(self.kernel.hardware().memory().get(62)).__name__, type(CPUInstruction(0)).__name__)
        self.assertEqual(type(self.kernel.hardware().memory().get(63)).__name__, type(CPUInstruction(0)).__name__)
        self.assertEqual(type(self.kernel.hardware().memory().get(60)).__name__, type(CPUInstruction(0)).__name__)
        self.assertEqual(type(self.kernel.hardware().memory().get(61)).__name__, type(CPUInstruction(0)).__name__)
        self.assertEqual(type(self.kernel.hardware().memory().get(58)).__name__, type(CPUInstruction(0)).__name__)
        self.assertEqual(type(self.kernel.hardware().memory().get(59)).__name__, type(CPUInstruction(0)).__name__)
        self.assertEqual(type(self.kernel.hardware().memory().get(56)).__name__, type(CPUInstruction(0)).__name__)
        self.assertEqual(type(self.kernel.hardware().memory().get(57)).__name__, type(CPUInstruction(0)).__name__)
        self.assertEqual(type(self.kernel.hardware().memory().get(54)).__name__, type(CPUInstruction(0)).__name__)
        self.assertEqual(type(self.kernel.hardware().memory().get(55)).__name__, type(CPUInstruction(0)).__name__)
        self.assertEqual(type(self.kernel.hardware().memory().get(52)).__name__, type(EXITInstruction(0)).__name__)
        for x in range(0, 52): # 52 no incluye
            self.assertEqual(self.kernel.hardware().memory().get(x), 'trash')
        self.assertEqual(self.kernel.hardware().memory().get(53), 'trash')


    def no_enough_memory_Test(self):
        with self.assertRaises(NotEnoughSpaceInMemoryException):
            self.kernel.execute("home/nicolas/program3")

    def no_program_available_Test(self):
        with self.assertRaises(ProgramNotAvailableException):
            self.kernel.execute("home/nicolas/programNoHay")

    def put_one_program_try_put_another_but_there_is_no_memory_Test(self):
        self.kernel.execute("home/nicolas/program0") # program0 tiene 11 instrucciones
        self.kernel.start_running(3) # ejecuto 3 ticks, program0 no libero su memoria
        with self.assertRaises(NotEnoughSpaceInMemoryException): # Llega un programa de 62 instrucciones
            self.kernel.execute("home/nicolas/program2") # como la memoria disp es 64 pero ambos progs ocupan 62 + 11 inst, no hay mem suficiente


    # Ahora pongo los mismos progs. que antes pero como program0 termina libera su memoria y program3 tiene suficiente para ejecutarse
    def put_one_program_try_put_another_Test(self):
        self.kernel.execute("home/nicolas/program0") # program0 tiene 11 instrucciones
        self.kernel.start_running(11) # ejecuto 11 ticks, program0 termina, libera su mem y puede cargarse program3
        self.kernel.execute("home/nicolas/program2") # Llega un programa de 62 instrucciones como program0 termino libero 11 lugares en mem
                                                     # suficientes para que program3 pueda ejecutar
