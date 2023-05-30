class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width (self, new_width):
        self.width = new_width

    def set_height (self, new_height):
        self.height = new_height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            line = ''
            for draw in range(0, self.height):
                line += '*' * (int(self.width)) +'\n'
        return line

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())

class Square(Rectangle):

    def __init__(self, length):
        super().__init__(width=length, height=length)
        self.length = length
     
    def set_side(self, new_length):
        self.height = new_length
        self.width = new_length
        self.length = new_length

    def set_width (self, new_length):
        self.length = new_length

    def __str__(self):
        return f"Square(side={self.length})"
