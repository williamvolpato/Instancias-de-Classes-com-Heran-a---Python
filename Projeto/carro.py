from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        estado = "ligado" if self._ligado else "desligado"
        return f"Carro {self.marca} {self.modelo} com {self.portas} portas está {estado}."
