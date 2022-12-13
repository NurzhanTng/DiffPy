class F():
    def __init__(self, data:int=0) -> None:
        self.data = data

    def __add__(self, other):
        if type(other) == type(self):
            return F(self.data + other.data)
        if type(other) == type(1):
            return F(self.data + other)
        raise Exception(f'Incorrect type of {other}: {type(other)}. It can be {int} or {self}')

    def __sub__(self, other):
        if type(other) == type(self):
            return F(self.data - other.data)
        if type(other) == type(1):
            return F(self.data - other)
        raise Exception(f'Incorrect type of {other}: {type(other)}. It can be {int} or {self}')
    
    def __mul__(self, other):
        if type(other) == type(self):
            return F(self.data * other.data)
        if type(other) == type(1):
            return F(self.data * other)
        raise Exception(f'Incorrect type of {other}: {type(other)}. It can be {int} or {self}')

    def return_data(self):
        return self.data

# err = F(2) + 'a'

a = F(5)
b = F(7)
c = a + 5
c2 = a - b
d = a * b

print(f'A: {a.return_data()}          ||| {a} ')
print(f'B: {b.return_data()}          ||| {b}')
print(f'A + B: {c.return_data()}     ||| {c}')
print(f'A - B: {c2.return_data()}     ||| {c2}')
print(f'A * B: {d.return_data()}     ||| {d}')


x = F(1)
eq = x*5-6
print( eq.return_data() )
