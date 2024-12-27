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
        t.penup()
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
        disk.newpos(self.x, self.y + disk.dheight * len(self.stack))
        self.stack.append(disk)
        disk.showdisk()

    def pop_disk(self):
        disk = self.stack.pop()
        t.penup()
        t.goto(self.x, self.y + disk.dheight * len(self.stack))
        disk.cleardisk()
        t.penup()
        t.pencolor("black")
        self.show_pole()
        return disk

class Hanoi(object):
    def __init__(self,n=3,start="A",workspace="B",destination="C"):
        self.startup = Pole(start,0,0)
        self.workspacep = Pole(workspace,150,0)
        self.destinationp = Pole(destination,300,0)
        self.startup.show_pole()
        self.workspacep.show_pole()
        self.destinationp.show_pole()
        for i in range(n):
            self.startup.push_disk(Disk("d"+str(i),0,i*150,20,(n-i)*30))
    
    def move_disk(self,start,destination):
        disk = start.pop_disk()
        destination.push_disk(disk)

    def move_tower(self,n,s,d,w):
        if n ==1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)

    def solve(self):
        self.move_tower(3,self.startup,self.destinationp,self.workspacep)

h = Hanoi()
h.solve()


t.done()