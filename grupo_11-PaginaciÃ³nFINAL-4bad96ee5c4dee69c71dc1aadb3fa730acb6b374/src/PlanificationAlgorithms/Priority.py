from queue import Queue


class Priority():

    def __init__(self, maxPriority):
        self._readyQueue = self.generateReadyQueue(maxPriority)


    def generateReadyQueue(self, max):
        list = []
        for i in range(0, max):
            list.append(Queue())
        return list

    def addPCB(self, pcb):
        self._readyQueue[pcb.getPriority()].put(pcb)

    def mustExpropiate(self, aPcb, anotherPcb):
        return False

    def getNext(self):
        for queue in self._readyQueue:
            if not queue.empty():
                return queue.get()

    def empty(self):
        ret = True
        for queue in self._readyQueue:
            ret = ret and queue.empty()
        return ret

    def getReadyQueue(self):
        return self._readyQueue





