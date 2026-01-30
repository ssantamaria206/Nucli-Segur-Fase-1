import abc
class Vehicle:


    # TASCA: Fes el Getter per llegir els kms (ja que és privat)
    def llegir_kms(self):
        return self.__kms

    # TASCA: Fes el Setter amb seguretat anti-frau
    def actualitzar_kms(self, nous_kms):
        # Si nous_kms és més petit que self.__kms, retorna False.
        # Si és correcte, actualitza i retorna True.
        if nous_kms < self.__kms:
            return False
        else:
            self.__kms = nous_kms
            return True
class Esportiu(Vehicle):
    def __init__(self, matricula, model, kms_inicials):
        self.matricula = matricula
        self._model = model       # Protegit (un guió)
        self.__kms = kms_inicials # Privat (dos guions)
    def calcular_preu(self, dies):
        PreuDiaEsportiu = 100
        preu = dies * PreuDiaEsportiu
        return preu 

class Camio(Vehicle):
    def __init__(self, matricula, model, kms_inicials, tones):
        self.matricula = matricula
        self._model = model       # Protegit (un guió)
        self.__kms = kms_inicials # Privat (dos guions)
        self.tones = tones
    def calcular_preu(self, dies):
        PreuDiaCamio = 50
        preu = dies * PreuDiaCamio + self.tones *  20
        return preu



# (2 dies * 50) + (10 tones * 20) = 100 + 200 = 300€
#self.assertEqual(volvo.calcular_preu(2), 300)