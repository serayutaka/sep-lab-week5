import turtle as t

class Disk(object):
    def __init__(self,name="", xpos=0, ypos=0, height=20,width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        t.penup()
        t.goto(self.dxpos, self.dypos)
        t.pendown()
        t.setheading(0)

        t.fillcolor('grey')
        t.begin_fill()
        t.fd(self.dwidth / 2)
        t.left(90)
        t.fd(self.dheight)
        t.left(90)
        t.fd(self.dwidth)
        t.left(90)
        t.fd(self.dheight)
        t.left(90)
        t.fd(self.dwidth / 2)
        t.end_fill()
    
    def newpos(self, new_x, new_y):
        self.dxpos = new_x
        self.dypos = new_y

    def cleardisk(self):
        t.penup()
        t.goto(self.dxpos, self.dypos)
        t.pendown()
        t.setheading(0)

        t.pencolor('white')
        t.fillcolor('white')
        t.begin_fill()
        t.fd(self.dwidth / 2)
        t.left(90)
        t.fd(self.dheight)
        t.left(90)
        t.fd(self.dwidth)
        t.left(90)
        t.fd(self.dheight)
        t.left(90)
        t.fd(self.dwidth / 2)
        t.end_fill()

class Pole():
    def __init__(self, n="", x=0, y=0, width=10, height=100):
        self.name = n
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.stack = []
        self.top = 0

    def show_pole(self):
        t.goto(self.x, self.y)
        t.pendown()
        t.forward(self.width / 2)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width / 2)
        t.penup()

    def push_disk(self, disk):
        self.stack.append(disk)
        disk.newpos(self.x + self.width / 2, self.y + disk.dheight * len(self.stack))
        disk.showdisk()

    def pop_disk(self):
        disk = self.stack.pop()
        disk.cleardisk()

p1 = Pole("p1", 20, 20)
p1.show_pole()
p1.push_disk(Disk(20,20))
p1.push_disk(Disk(20,20))
p1.push_disk(Disk(20,20))

t.done()