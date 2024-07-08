from carro import Carro
from moto import Moto

def main():
    # Criando instâncias de Carro
    carro1 = Carro("Toyota", "Corolla", 4)
    carro2 = Carro("Ford", "Mustang", 2)
    carro3 = Carro("Honda", "Civic", 4)

    # Criando instâncias de Moto
    moto1 = Moto("Yamaha", "YZF-R3", "esportiva")
    moto2 = Moto("Honda", "CB500X", "casual")
    moto3 = Moto("Ducati", "Panigale V4", "esportiva")

    # Imprimindo as informações
    print(carro1)
    print(carro2)
    print(carro3)
    print(moto1)
    print(moto2)
    print(moto3)

if __name__ == "__main__":
    main()
