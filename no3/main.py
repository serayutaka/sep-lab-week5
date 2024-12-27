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

d = Disk()
d.showdisk()
d.cleardisk()