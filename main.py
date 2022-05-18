class Asiento:

    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro

    def cambiarColor(self,color):
        colors = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        if color in colors:
            self.color = color


class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self,registro):
        self.registro=registro   

    def asignarTipo(self,tipo):

        if tipo=="gasolina" or tipo=="electrico" :
            self.tipo=tipo

class Auto:

    cantidadCreados=0

    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):
        numeroasientos =0
        for asiento in self.asientos:
            if(asiento != None):
                numeroasientos +=1   
        return numeroasientos                    

    def verificarIntegridad(self):

        if self.motor.registro != self.registro:
            return "Las piezas no son originales"

        for asiento in self.asientos:
            if asiento != None:
                if asiento.registro != self.registro:
                    return "Las piezas no son originales"
        return "Auto original"
