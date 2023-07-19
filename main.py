class Tom: 
    name: str = 'Tom'   # Tom's name is Tom
    money: float = 0.0  # Tom has no money
    
    def __str__(self):
        return f'Tom is called {self.name} and he has ${self.money}'

    def __repr__(self):
        return f'Tom(\'{self.name}\', {self.money})'

if __name__ == '__main__':
    tom = Tom()
    print(f'{repr(tom)} was created!')
    print(str(tom))
