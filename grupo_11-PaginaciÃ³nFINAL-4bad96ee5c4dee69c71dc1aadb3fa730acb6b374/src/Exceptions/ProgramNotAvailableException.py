class ProgramNotAvailableException(Exception):

    def __init__(self):
        super(ProgramNotAvailableException, self).__init__("program not available on disk")