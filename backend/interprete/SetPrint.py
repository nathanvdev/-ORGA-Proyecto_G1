class SetPrint():
    def __init__(self, printType, Fila, Columna, Color):
        self.printType = printType
        self.Fila = Fila
        self.Columna = Columna
        self.Color = Color

    def execute(self):
        output = f'{self.printType};{self.Fila};{self.Columna};{self.Color}'
        return output