# -*- coding: utf-8 -*-
import  string, time, copy
import Tkinter as tk
from PIL import Image, ImageTk
import socket



# comunicating with server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8007
s.connect((host, port))

# down.
# leave.
# up, leave, enter.

class CanvasDnD(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.loc = self.dragged = 0
        tk.Frame.__init__(self, master)

        canv = tk.Canvas(root, width=512, height=512)


        squads = []
        side = 64
        tup = tuple((x, y) for y in (i * side for i in range(8))\
                    for x in (i * side for i in range(8)))
        count = 0

        for x1, y1 in tup:
            x2, y2 = x1 + side, y1 + side
            if count % 9 == 0:
                count += 1
            if count % 2 == 0:
                squads.append(canv.create_rectangle(x1, y1, x2, y2, width=3, fill="brown"))
            else:
                squads.append(canv.create_rectangle(x1, y1, x2, y2, width=3, fill="white"))
            count += 1
        path1 = 'C:/Users/User/PycharmProjects/chess/img/blackp.png'
        path2 = 'C:/Users/User/PycharmProjects/chess/img/whitep.png'
        path3 = 'C:/Users/User/PycharmProjects/chess/img/blackr.png'
        path4 = 'C:/Users/User/PycharmProjects/chess/img/whiter.png'
        path5 = 'C:/Users/User/PycharmProjects/chess/img/blackn.png'
        path6 = 'C:/Users/User/PycharmProjects/chess/img/whiten.png'
        path7 = 'C:/Users/User/PycharmProjects/chess/img/blackb.png'
        path8 = 'C:/Users/User/PycharmProjects/chess/img/whiteb.png'
        path9 = 'C:/Users/User/PycharmProjects/chess/img/blackq.png'
        path10 = 'C:/Users/User/PycharmProjects/chess/img/whiteq.png'
        path11 = 'C:/Users/User/PycharmProjects/chess/img/blackk.png'
        path12 = 'C:/Users/User/PycharmProjects/chess/img/whitek.png'

        coord = []
        figures = []
        white1 = []
        black1 = []
        self.imgb1 = ImageTk.PhotoImage(Image.open(path1))
        self.imgw1 = ImageTk.PhotoImage(Image.open(path2))
        y = 32.
        while y <= 480.:
            figures.append(canv.create_image(96., y, image=self.imgb1, tag="DnD"))
            figures.append(canv.create_image(480. - 64., y, image=self.imgw1, tag="DnD"))
            black1.append([96.,y])
            coord.append([96.,y])
            white1.append([480. - 64., y])
            coord.append([480.-64., y])
            y += 64.
        self.imgb2 = ImageTk.PhotoImage(Image.open(path3))
        self.imgw2 = ImageTk.PhotoImage(Image.open(path4))

        figuresx1 = 32.
        figuresx2 = 512. - 32.

        coord.append([32., figuresx1])
        coord.append([32., figuresx2])
        coord.append([512.-32., figuresx1])
        coord.append([512. - 32., figuresx2])

        black1.append([32., figuresx1])
        black1.append([32., figuresx2])
        white1.append([512.-32., figuresx1])
        white1.append([512. - 32., figuresx2])

        figures.append(canv.create_image(32., figuresx1, image=self.imgb2, tag="DnD"))
        figures.append(canv.create_image(32., figuresx2, image=self.imgb2, tag="DnD"))
        figures.append(canv.create_image(512. - 32., figuresx1, image=self.imgw2, tag="DnD"))
        figures.append(canv.create_image(512. - 32., figuresx2, image=self.imgw2, tag="DnD"))

        self.imgb3 = ImageTk.PhotoImage(Image.open(path5))
        self.imgw3 = ImageTk.PhotoImage(Image.open(path6))

        figuresx1 += 64.
        figuresx2 -= 64.

        coord.append([32., figuresx1])
        coord.append([32., figuresx2])
        coord.append([512. - 32., figuresx1])
        coord.append([512. - 32., figuresx2])

        black1.append([32., figuresx1])
        black1.append([32., figuresx2])
        white1.append([512.-32., figuresx1])
        white1.append([512. - 32., figuresx2])


        figures.append(canv.create_image(32., figuresx1, image=self.imgb3, tag="DnD"))
        figures.append(canv.create_image(32., figuresx2, image=self.imgb3, tag="DnD"))
        figures.append(canv.create_image(512. - 32., figuresx1, image=self.imgw3, tag="DnD"))
        figures.append(canv.create_image(512. - 32., figuresx2, image=self.imgw3, tag="DnD"))
        '''слоны'''
        self.imgb4 = ImageTk.PhotoImage(Image.open(path7))
        self.imgw4 = ImageTk.PhotoImage(Image.open(path8))

        figuresx1 += 64.
        figuresx2 -= 64.

        coord.append([32., figuresx1])
        coord.append([32., figuresx2])
        coord.append([512. - 32., figuresx1])
        coord.append([512. - 32., figuresx2])

        black1.append([32., figuresx1])
        black1.append([32., figuresx2])
        white1.append([512.-32., figuresx1])
        white1.append([512. - 32., figuresx2])

        figures.append(canv.create_image(32., figuresx1, image=self.imgb4, tag="DnD"))
        figures.append(canv.create_image(32., figuresx2, image=self.imgb4, tag="DnD"))
        figures.append(canv.create_image(512. - 32., figuresx1, image=self.imgw4, tag="DnD"))
        figures.append(canv.create_image(512. - 32., figuresx2, image=self.imgw4, tag="DnD"))

        self.imgb5 = ImageTk.PhotoImage(Image.open(path9))
        self.imgw5 = ImageTk.PhotoImage(Image.open(path10))

        self.imgb6 = ImageTk.PhotoImage(Image.open(path11))
        self.imgw6 = ImageTk.PhotoImage(Image.open(path12))

        figuresx1 += 64.
        figuresx2 -= 64.

        coord.append([32., figuresx1])
        coord.append([32., figuresx2])
        coord.append([512. - 32., figuresx1])
        coord.append([512. - 32., figuresx2])

        black1.append([32., figuresx1])
        black1.append([32., figuresx2])
        white1.append([512.-32., figuresx1])
        white1.append([512. - 32., figuresx2])

        figures.append(canv.create_image(32., figuresx1, image=self.imgb5, tag="DnD"))
        figures.append(canv.create_image(32., figuresx2, image=self.imgb6, tag="DnD"))
        figures.append(canv.create_image(512. - 32., figuresx1, image=self.imgw5, tag="DnD"))
        figures.append(canv.create_image(512. - 32., figuresx2, image=self.imgw6, tag="DnD"))
        self.kingbl = 29
        self.kingwh = 31
        canv.pack(expand=1, fill=tk.BOTH)

        canv.tag_bind("DnD", "<ButtonPress-1>", self.down)
        canv.tag_bind("DnD", "<ButtonRelease-1>", self.chkup)
        canv.tag_bind("DnD", "<Enter>", self.enter)
        canv.tag_bind("DnD", "<Leave>", self.leave)
        self.coord = coord

        self.white1 = white1
        self.black1 = black1

        self.figures = figures

        self.canv = canv
    def down(self, event):
        self.arr = event.widget.coords(tk.CURRENT)
        if (self.arr in self.white1):
            self.ind = 0
            for i in range(0, 32, 1):
                if event.widget.coords(tk.CURRENT) == self.coord[i]:
                    self.ind = i

            self.loc = 1
            self.dragged = 0
            event.widget.bind("<Motion>", self.motion)
            self.movement = True
        else:
            self.movement = False

    def motion(self, event):
        root.config(cursor="exchange")
        cnv = event.widget

        xy = cnv.canvasx(event.x), cnv.canvasy(event.y)
        points = event.widget.coords(tk.CURRENT)
        anchors = copy.copy(points[:2])

        for idx in range(len(points)):
            mouse = xy[idx % 2]
            zone = anchors[idx % 2]
            points[idx] = points[idx] - zone + mouse
        apply(event.widget.coords, [tk.CURRENT] + points)

    def leave(self, event):
        self.loc = 0

    def enter(self, event):
        self.loc = 1
        if self.dragged == event.time:
            self.up(event)

    def chkup(self, event):
        event.widget.unbind("<Motion>")
        if self.movement:
            root.config(cursor="")

            up = event.widget.coords(tk.CURRENT)[1]
            down = event.widget.coords(tk.CURRENT)[1]
            left = event.widget.coords(tk.CURRENT)[0]
            right = event.widget.coords(tk.CURRENT)[0]
            a = False
            b = False
            while not (a and b):
                up -= 1.
                down += 1.
                left -= 1.
                right += 1.
                if (up % 64 == 0) and (a == False):
                    self.coord[self.ind][1] = up + 32.
                    a = True
                if (down % 64 == 0) and (a == False):
                    self.coord[self.ind][1] = down - 32.
                    a = True
                if (left % 64 == 0) and (b == False):
                    self.coord[self.ind][0] = left + 32.
                    b = True
                if (right % 64 == 0) and (b == False):
                    self.coord[self.ind][0] = right - 32.
                    b = True
            OK = False
            left_move = (self.coord[self.ind][0] - self.arr[0])/64.
            updown_move = abs(self.coord[self.ind][1] - self.arr[1])/64.
            if((self.ind<=15)and((left_move==-2.)or (left_move==-1.) or(left_move == updown_move == 1))):
                OK = True
            if(((self.ind==18)or(self.ind==19))and (((left_move != 0)and(updown_move==0))or((left_move == 0)and(updown_move != 0)))):
                OK = True
            if ((self.ind==22)or(self.ind==23))and(((abs(left_move) == 2)and(updown_move==1))or((abs(left_move) == 1)and(updown_move==2))):
                OK = True
            if ((self.ind==26)or(self.ind==27))and(abs(left_move)==abs(updown_move)):
                OK = True
            if ((self.ind == 31)) and ((abs(left_move) == 1)or (updown_move == 1)):
                OK = True
            if ((self.ind == 30)) and (((abs(left_move)==abs(updown_move)))or (((left_move != 0)and(updown_move==0))or((left_move == 0)and(updown_move != 0)))):
                OK = True
            check = 0
            for i in range(0,16,1):
                if(self.coord[self.ind] == self.white1[i]):
                    check += 1
            if (check>1):
                OK = False
            if self.coord[self.ind] ==  self.arr:
                OK = False
            if (OK):
                apply(event.widget.coords, [tk.CURRENT] + self.coord[self.ind])
                for i in range(0, 32, 1):
                    if (self.coord[self.ind] == self.coord[i]) and (self.ind != i):
                        self.canv.delete(self.figures[i])
                        self.coord[i] = [-100, -100]

                self.target = event.widget.find_withtag(tk.CURRENT)
                if self.loc:  # is button released in same widget as pressed?
                    self.up(event)
                else:
                    self.dragged = event.time

                full = ''
                for i in range(0, len(self.coord), 1):
                    buf = ','.join(str(v) for v in self.coord[i])
                    buf += ' '
                    full += buf

                s.send(full)
                data = s.recv(10000)
                if data == '0':
                    self.canv.create_rectangle(0, 0, 512, 512, fill="green")

                if data == '1':
                    self.canv.create_rectangle(0, 0, 512, 512, fill="red")

                dataa = data.split(' ')
                for i in range(0, len(dataa), 1):
                    dataa[i] = dataa[i].split(',')
                del dataa[len(dataa) - 1]

                for i in range(0, len(dataa), 1):
                    for j in range(0, len(dataa[i]), 1):
                        dataa[i][j] = float(dataa[i][j])
                self.coord = dataa

                for i in range(len(self.coord)):
                    self.canv.coords(self.figures[i], self.coord[i][0], self.coord[i][1])

                self.white1[0] = self.coord[1]
                self.white1[1] = self.coord[3]
                self.white1[2] = self.coord[5]
                self.white1[3] = self.coord[7]
                self.white1[4] = self.coord[9]
                self.white1[5] = self.coord[11]
                self.white1[6] = self.coord[13]
                self.white1[7] = self.coord[15]
                self.white1[8] = self.coord[18]
                self.white1[9] = self.coord[19]
                self.white1[10] = self.coord[22]
                self.white1[11] = self.coord[23]
                self.white1[12] = self.coord[26]
                self.white1[13] = self.coord[27]
                self.white1[14] = self.coord[30]
                self.white1[15] = self.coord[31]
            else:
                self.coord[self.ind] = self.arr

                if (self.ind <= 15):
                    self.white1[(self.ind - 1) / 2] = self.arr
                ind = 0
                if self.ind == 18:
                    ind = 8
                if self.ind == 19:
                    ind = 9
                if self.ind == 22:
                    ind = 10
                if self.ind == 23:
                    ind = 11
                if self.ind == 26:
                    ind = 12
                if self.ind == 27:
                    ind = 13
                if self.ind == 30:
                    ind = 14
                if self.ind == 31:
                    ind = 15
                if ind != 0:
                    self.white1[ind] = self.arr
                apply(event.widget.coords, [tk.CURRENT] + self.arr)



    def up(self, event=None):
        event.widget.unbind("<Motion>")



#main window
root = tk.Tk()
root.title("white")
root.resizable(width=False, height=False)

CanvasDnD(root).pack()
root.mainloop()
s.close()
