from enum import Enum


class IRQTypes(Enum):

    NEW     = 1
    IO_IN   = 2
    IO_OUT  = 3
    KILL    = 4
    TIMEOUT = 5







