from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=True)

        self.__running = False

    def redraw(self):
        self.__canvas.update_idletasks()
        self.__canvas.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Application closed.")

    def draw_line(self, line, fill="Red"):
        line.draw(self.__canvas, fill)

    def close(self):
        self.__running = False

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill="Red"):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill, width=2)
        canvas.pack(fill=BOTH,expand=1)