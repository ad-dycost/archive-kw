# -*- coding: utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk

class XO_Field:
    list = [[' ',' ',' '], 
            [' ',' ',' '],
            [' ',' ',' ']]
    win = False
    chr = ' '

    def check(self):
        a = self.list
        for i in range(3):
            if (a[i][0] == a[i][1] == a[i][2]):
                return a[i][0]
            
        for i in range(3):
            if (a[0][i] == a[1][i] == a[2][i]):
                return a[0][i]
            
        if (a[0][0] == a[1][1] == a[2][2]):
            return a[1][1]
        if (a[0][2] == a[1][1] == a[2][0]):
            return a[1][1]
        
        return False
        
    def post(self,symbol,x,y):
        self.list[y][x] = symbol
        self.chr = self.check()
        if ((self.chr != False) & (self.chr!=' ')):
            self.win = True

class XO_Win:
    
    def create_button(self,box):
        button = gtk.Button(self.field.chr)
        box.pack_start(button,True,True,0)
        button.show()
        return button
    
    def __init__(self):        
        self.field = XO_Field()
        self.set = True
        self.boxes = []
        self.buttons = [[],[],[]]
    
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.window.set_title("Крестики-Нолики.py!")
        self.window.set_border_width(10)
        self.window.set_size_request(400,400)
        
        self.vbox = gtk.VBox(False,0)
        self.window.add(self.vbox)
        
        for i in range(3):
            box = gtk.HBox(False,0)
            self.boxes.append(box)
            for j in range(3):
                self.buttons[i].append(self.create_button(box))
                self.buttons[i][j].connect("clicked",self.on_btn_click,i,j)
            self.vbox.pack_start(box,True,True,0)
            box.show()
                
        self.vbox.show()
        self.window.show()
        
    def main(self):
        gtk.main()

    def destroy(self, widget, data=None):
        gtk.main_quit()
        
    def postgui(self,chr,i,j):
        self.buttons[i][j].set_label(chr)
        
    def on_btn_click(self,button,i,j):
        if self.field.win == True:
            return

        if self.field.list[i][j] == ' ':
            if self.set == True:	
				self.field.post('X',j,i)
				self.buttons[i][j].set_label("X")
				map = button.get_colormap()
				color = map.alloc_color("red")
				style = button.get_style().copy()
				style.bg[gtk.STATE_NORMAL] = color
				self.buttons[i][j].set_style(style)
				self.set = False
            else:
				self.field.post('O',j,i)
				self.buttons[i][j].set_label('O')
				map = button.get_colormap()
				color = map.alloc_color("green")
				style = button.get_style().copy()
				style.bg[gtk.STATE_NORMAL] = color
				self.buttons[i][j].set_style(style)
				self.set = True
        
        both = 0
        if self.field.win == True:
            self.window.set_title("Выиграл: " + self.field.chr + '!')
        else:
            for i in range(3):
                for j in range(3):
                    both = both + 1
            if both == 0:
                self.window.set_title("Ничья!")
            
win = XO_Win()
win.main()
