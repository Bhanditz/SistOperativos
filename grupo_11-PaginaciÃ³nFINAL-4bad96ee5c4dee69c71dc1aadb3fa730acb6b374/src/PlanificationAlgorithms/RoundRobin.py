from queue import Queue
from src.RRTimer import RRTimer


class RoundRobin():

    def __init__(self, quantum, clock, irqVector):
        self._readyQueue = Queue()
        clock.setTimer(RRTimer(quantum, irqVector))

    def empty(self):
        return self._readyQueue.empty()

    # No hace nada porque RR solo setea el Timer del sist (cambiar Dummy x RR_Timer) una vez echo esto RR_Timer se encarga de la expropiacion
    # por la forma en que ejecuta clock primero le tira el tick a Timer
    def mustExpropiate(self, pcbInCpu, newPcb):
        pass

    def addPCB(self, pcb):
        self._readyQueue.put(pcb)

    def getNext(self):
        return self._readyQueue.get()

    def getReadyQueue(self):
        return self._readyQueue
