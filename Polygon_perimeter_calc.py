from tkinter import *
from collections import namedtuple
from sympy.geometry import *


class sketch_window(object):

    def __init__(self):
        self.root = Tk()

        self.reset_button = Button(self.root, text='reset', command=self.reset)
        self.reset_button.grid(row=0, column=0)
        
        self.c = Canvas(self.root, bg='black', width=600, height=600)
        self.c.grid(row=1, columnspan=3)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.line_width = 1
        self.color = 'white'
        self.c.bind('<Button-1>', self.click)
        self.c.bind('<Double-Button-1>', self.close_polygon)
        self.points = []
        self.polygon = None

    def reset(self):
        self.setup()
        self.c.delete("all")

    def click(self, event):
        if self.polygon:
            self.reset()
        else:
            pt = Point(event.x, event.y)
            self.points.append(pt)
            if len(self.points) > 1:
                self.draw_line(*self.points[-2:])

    def close_polygon(self, event):
        self.click(event)
        self.draw_line(self.points[0], self.points[-1])
        self.polygon = Polygon(*self.points)
        self.show_perimeter()

    def draw_line(self, p1, p2):
        self.c.create_line(*p1, *p2, width=self.line_width, fill=self.color)

    def show_perimeter(self):
        perimeter = self.polygon.perimeter.evalf()
        area = abs(self.polygon.area.evalf())
        msg = 'Perimeter: {:.2f}'.format(perimeter)
        msg += '\n Area: {:.2f}'.format(area)

        self.c.create_text(*self.polygon.centroid.evalf(), text=msg, fill='white')

if __name__ == '__main__':
    sketch_window()
