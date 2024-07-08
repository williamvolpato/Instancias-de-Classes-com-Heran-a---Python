class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        estado = "ligado" if self._ligado else "desligado"
        return f"Veiculo {self.marca} {self.modelo} está {estado}."
