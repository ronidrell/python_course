class ComplexNumbers:
    def __init__(self, realpart=0, imagpart=0):
        self.real = realpart
        self.imag = imagpart
    def __repr__(self):
        if self.imag >= 0:
            return "{} + {}i".format(self.real, self.imag)
        else:
            return "{} - {}i".format(self.real, self.imag * (-1))
    def __add__(self, other_complex_number):
        return ComplexNumbers(self.real + other_complex_number.real,
                              self.imag + other_complex_number.real)
    def __sub__(self, other_complex_number):
         return ComplexNumbers(self.real - other_complex_number.real,
                               self.imag - other_complex_number.real)
    def __mul__(self, other_complex_number):
        return ComplexNumbers(self.real * other_complex_number.real - self.imag * other_complex_number.imag,
                              self.imag * other_complex_number.real + self.real * other_complex_number.imag)


x = ComplexNumbers(5, -4)
y = ComplexNumbers(3)
