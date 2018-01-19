from tkinter import *
from collections import namedtuple

point = namedtuple('point', ['x', 'y'])

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
        self.polygon_closed = False

    def reset(self):
        self.setup()
        self.c.delete("all")

    def click(self, event):
        if self.polygon_closed:
            self.reset()
        else:
            pt = point(event.x, event.y)
            self.points.append(pt)
            if len(self.points) > 1:
                self.draw_line(*self.points[-2:])

    def close_polygon(self, event):
        self.click(event)
        self.draw_line(self.points[0], self.points[-1])
        self.polygon_closed = True

    def draw_line(self, p1, p2):
        self.c.create_line(*p1, *p2, width=self.line_width, fill=self.color)

if __name__ == '__main__':
    sketch_window()
