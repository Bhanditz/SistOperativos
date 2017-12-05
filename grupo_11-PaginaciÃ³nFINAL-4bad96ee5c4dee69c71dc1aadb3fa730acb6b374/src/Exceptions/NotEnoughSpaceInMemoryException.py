class NotEnoughSpaceInMemoryException(Exception):

    def __init__(self):
        super(NotEnoughSpaceInMemoryException, self).__init__("there is no space to allocate program ")