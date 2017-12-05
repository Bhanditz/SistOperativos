
class Scheduler:

    def __init__(self, planner):
        self._planner = planner

    def add(self, pcb):
        self._planner.addPCB(pcb)

    def getNext(self):
        return self._planner.getNext()

    def mustExpropiate(self, pcb_current, pcb_candidate):
        return self._planner.mustExpropiate(pcb_current, pcb_candidate)

    def isEmpty(self):
        return self._planner.empty()


    # Se usa solo para test
    def getReadyQueue(self):
        return self._planner.getReadyQueue()




