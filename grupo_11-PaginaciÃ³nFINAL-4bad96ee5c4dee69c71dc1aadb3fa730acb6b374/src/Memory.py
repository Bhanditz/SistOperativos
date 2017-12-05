#!/usr/bin/env python3

from tabulate import tabulate

class Memory():

    def __init__(self, size):
        self._size = size
        self._memory = ["trash"] * self._size


    def __repr__(self):
        return tabulate(enumerate(self._memory), tablefmt='psql')

    def get(self, i):
        return self._memory.__getitem__(i)

    def put(self, i, instr):
        self._memory[i] = instr


    def isEmpty(self):
        return not self._memory

    def size(self):
        return self._size







