class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self,color):
        self.color = color

cookie_one = Cookie("green")
cookie_two = Cookie("Red")

print("1", cookie_one.get_color())

print("1", cookie_two.get_color())