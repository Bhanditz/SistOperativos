
class PageTable():

    def __init__(self, freeFrames, cantPages):
        self._pageTable = self.initPageTable(freeFrames, cantPages)


    def initPageTable(self, freeFrames, cantPages):
        ret = []
        for i in range(0, int(cantPages)):
            ret.append(freeFrames[i])
        return ret

    def getFrame(self, pag):
        return self._pageTable[pag]

    def getFrames(self):
        return self._pageTable

