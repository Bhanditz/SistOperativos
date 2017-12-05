from time import sleep
from src.DummyTimer import DummyTimer


class Clock:

    def __init__(self, cpu, IOdevice):
        self._cpu = cpu
        self._IOdevice = IOdevice
        self._timer = DummyTimer()

    # ticks puede ser infinito o un nro pasado x parametro
    def run(self, ticks):
        i = 0
        while i < ticks:
            self._IOdevice.tick()
            self._timer.tick()
            self._cpu.tick()
            i+=1
            sleep(1)

    def setTimer(self, timer):
        self._timer = timer

    def timer(self):
        return self._timer