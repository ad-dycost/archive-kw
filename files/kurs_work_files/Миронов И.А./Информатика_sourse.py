#!/usr/bin/python
# -*- coding: utf-8 -*-
import pylab
import matplotlib
from math import *
import numpy as np  
import matplotlib.pyplot as plt
# Используем графическую библеотеку Tkinter
import Tkinter
import ttk
# Создаем форму(окно)
tk=Tkinter.Tk()
tk.title("Кур.работа")
# Создаем GUI элементы ввода данных
lbla=Tkinter.Label(tk)
lbla["text"]="A= "
lbla.pack()
# Создаем поле ввода
a=Tkinter.Entry(tk)
a.pack()
lblb=Tkinter.Label(tk)
lblb["text"]="B= "
lblb.pack()
# Создаем поле ввода
b=Tkinter.Entry(tk,width=20,bd=3)
b.pack()
lblc=Tkinter.Label(tk)
lblc["text"]="C= "
lblc.pack()
# Создаем поле ввода
c=Tkinter.Entry(tk,width=20,bd=3)
c.pack()
# Определяем функцию-обработчик события нажатия на конпку 
def solve():
  a1=float(a.get())
  b1=float(b.get())
  c1=float(c.get())
  d=b1**2-4*a1*c1
  
  if d<0: 
# Создание объект Label(Надпись)
	lbl0=Tkinter.Label(tk)
	lbl0["text"]="Корней нет, D меньше нуля"
	lbl0.pack()
  if d>0:
    x1=(-1*b1+d**0.5)/2*a1
    x2=(-1*b1-d**0.5)/2*a1
    
# Создание объект Label(Надпись)
    lbl1=Tkinter.Label(tk)
    lbl1["text"]="X1= ", x1
    lbl1.pack()
# Создание объект Label(Надпись)
    lbl2=Tkinter.Label(tk)
    lbl2["text"]="X2= ", x2
    lbl2.pack()
    matplotlib.rcParams["axes.grid"] = True
    xmin=-100
    xmax=100
    
    x = pylab.arange (xmin, xmax, 1)
    y=a1*(x-x1)*(x-x2)
    pylab.clf()
    plt.plot(x,y,x1,x2)
    plt.show()
  if d==0:
    x=(-1*b1)/(2*a1)
# Создание объект Label(Надпись)
    lbl=Tkinter.Label(tk)
    lbl["text"]="X1=X2= ", x
    lbl.pack()
    matplotlib.rcParams["axes.grid"] = True
    x = pylab.arange (-20.0, 20.1, 0.1)
    y=a1*x**2+b1*x+c1
    pylab.clf()
    plt.plot(x,y)
    plt.show()
# Создаем кнопку @РЕШИТЬ
btn=Tkinter.Button(tk)
btn["text"]="График и результат"
# Привязываем функцию-обработчик к событию нажатия
btn["command"]=solve
btn.pack()

# Создаем кнопку выхода их приложения
button=Tkinter.Button(tk)
button["text"]="Закрыть"
button["command"]=tk.quit
button.pack()  


# Запуск
tk.mainloop()
  

