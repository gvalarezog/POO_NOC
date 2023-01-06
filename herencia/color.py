
class Color:
    def __init__(self, color=None):
        self._color = color

    def __str__(self):
        return f'Color [color={self._color}]'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

if __name__ == '__main__':
    c = Color(color='Celeste')
    print(c)
