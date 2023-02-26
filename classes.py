class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie one is', cookie_two.get_color())

cookie_two.set_color('yellow')

print('\nCookie one is still', cookie_one.get_color())
print('\nCookie one is now', cookie_two.get_color())