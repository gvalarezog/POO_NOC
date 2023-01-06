from rectangulo import Rectangulo


class RectanguloEspecial(Rectangulo):
    def __init__(self, base:float=0, altura:float=0):
        self._base=base
        self._altura=altura

    def __str__(self):
        return f'Rectangulo Especial [base: {self._base}, altura: {self._altura}]'

if __name__ == '__main__':
    r=RectanguloEspecial(5,6)
    print(r)
    print(f'__name__: {__name__}')
