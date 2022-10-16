"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    

    def __init__(self, start=0):
        "Create serial number starting at specified start number"
        self.start = start
        self.count = 0
        
    def __repr__(self):
        "Show representation"
        return f'<SerialGenerator start={self.start} next={self.start + 1}>'
    
    def generate(self):
        "Generate a new serial number"
        self.counter = self.start + self.count;
        self.count += 1
        return self.counter

    def reset(self):
        "Reset the count and go back to original start point"
        self.count = 0;