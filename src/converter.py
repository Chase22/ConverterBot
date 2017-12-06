import pint, os

ureg = pint.UnitRegistry();

class Converter:
    def __init__(self):
        self.conversions = {}  
        path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'config', 'convert.txt')
        with open(path) as file:
            for line in file:
                name, var = line.partition("=")[::2]
                self.conversions[name.strip()] = var.strip()
                self.conversions[var.strip()] = name.strip()
                
        print(self.conversions)
    
    def convert(self, measurement):
        newunit = self.conversions[str(measurement.units)]
        print(newunit)
        return measurement.to(newunit)