from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        estado = "ligado" if self._ligado else "desligado"
        return f"Moto {self.marca} {self.modelo} do tipo {self.tipo} está {estado}."
