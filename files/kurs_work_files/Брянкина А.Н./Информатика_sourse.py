#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk
import math

class Gausa:

	# Этот callback завершает программу
	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		return False

	def gauss_jordan(self, eps = 1.0/(10**10)):
		"""Puts given matrix (2D array) into the Reduced Row Echelon Form.
		 Returns True if successful, False if 'm' is singular.
		 NOTE: make sure all the matrix items support fractions! Int matrix will NOT work!
		 Written by Jarno Elonen in April 2005, released into Public Domain"""

		(h, w) = (len(self.matrix), len(self.matrix))
		for y in range(0,h):
			maxrow = y
			for y2 in range(y+1, h):		# Find max pivot
				if abs(self.matrix[y2][y]) > abs(self.matrix[maxrow][y]):
					maxrow = y2
			(self.matrix[y], self.matrix[maxrow]) = (self.matrix[maxrow], self.matrix[y])
			#if abs(m[y][y]) <= eps:		 # Singular?
				#return False
			for y2 in range(y+1, h):		# Eliminate column y
				c = self.matrix[y2][y] / self.matrix[y][y]
				for x in range(y, w):
					self.matrix[y2][x] -= self.matrix[y][x] * c
		for y in range(h-1, 0-1, -1): # Backsubstitute
			c	= self.matrix[y][y]
			for y2 in range(0,y):
				for x in range(w-1, y-1, -1):
					self.matrix[y2][x] -=	self.matrix[y][x] * self.matrix[y2][y] / c
			self.matrix[y][y] /= c
			for x in range(h, w):			 # Normalize row y
			 self.matrix[y][x] /= c
		#return True

	def start_program (self):
		# Создаём новое окно
		self.window_start = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window_start.set_position(gtk.WIN_POS_CENTER)
		self.window_start.set_default_size(100,100)
		# Устанавливаем заголовок окна
		self.window_start.set_title("Метод Гаусса")

		# Устанавливаем обработчик для delete_event, который немедленно
		# Завершает работу GTK.
		self.window_start.connect("delete_event", self.delete_event)

		# Устанавливаем границу для окна
		self.window_start.set_border_width(5)
		
		# Создаём таблицу 3х4
		table = gtk.Table(3, 3, True)

		# Размещаем таблицу в главном окне
		self.window_start.add(table)

		# Создаём первую кнопку
		button = gtk.Button("ok")
		
		self.entry_1 = gtk.Entry(max=0)
		table.attach(self.entry_1, 0, 3, 1, 2, gtk.SHRINK, gtk.SHRINK)
		self.entry_1.show()
		
		# По нажатии кнопки мы вызываем метод "callback"
		# с указателем на "ok" в виде аргумента
		button.connect("clicked", self.create_matrix, None)
		# Вставляем ok в верхнюю левую ячейку таблицы
		table.attach(button, 2, 3, 2, 3, gtk.SHRINK, gtk.SHRINK, 1, 1)
		button.show()
		
		label = gtk.Label("Введите размерность матрицы")
		table.attach(label, 0, 3, 0, 1)
		label.show()
		table.show()
		self.window_start.show()

	
	def create_matrix (self, widget, data=None):
		# Создаём новое окно
		self.window_matrix = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window_matrix.set_position(gtk.WIN_POS_CENTER)
		self.window_matrix.set_default_size(150,150)
		# Устанавливаем заголовок окна
		self.window_matrix.set_title("Метод Гаусса")

		# Устанавливаем обработчик для delete_event, который немедленно
		# Завершает работу GTK.
		self.window_matrix.connect("delete_event", self.delete_event)

		# Устанавливаем границу для окна
		self.window_matrix.set_border_width(5)
		self.N = int(self.entry_1.get_text())
		# Создаём таблицу 3х4
		table = gtk.Table(self.N + 1, self.N + 2, True)

		# Размещаем таблицу в главном окне
		self.window_matrix.add(table)

		# Создаём первую кнопку
		button = gtk.Button("ok")

		# По нажатии кнопки мы вызываем метод "callback"
		# с указателем на "ok" в виде аргумента
		button.connect("clicked", self.solver, None )
		# Вставляем ok в верхнюю левую ячейку таблицы
		table.attach(button, self.N, self.N + 1, self.N + 1, self.N + 2, gtk.SHRINK, gtk.SHRINK, 1, 1)
		button.show()
		
		label = gtk.Label("Введите коэффициенты матрицы")
		table.attach(label, 0, self.N +1, 0, 1)
		label.show()
		
		self.entry = {}
		for i in xrange(self.N):
			for j in xrange(self.N):
				self.entry[str(i) + "," + str(j)] = gtk.Entry(max=0)
				table.attach(self.entry[str(i) + "," + str(j)] , i, i + 1, j +1, j +2, gtk.SHRINK, gtk.SHRINK)
				self.entry[str(i) + "," + str(j)] .show()
		       
		table.show()
		self.window_matrix.show()
	
	def solver (self, widget, data=None):
		self.matrix = []
		for i in xrange(self.N):
			row = []
			for j in xrange(self.N):
				row.append(int(self.entry[str(j) + "," + str(i)].get_text()))
			self.matrix.append(row)
		self.gauss_jordan()
		
		# Создаём новое окно
		self.window_matrix_res = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window_matrix_res.set_position(gtk.WIN_POS_CENTER)
		self.window_matrix_res.set_default_size(150,150)
		# Устанавливаем заголовок окна
		self.window_matrix_res.set_title("Метод Гаусса")

		# Устанавливаем обработчик для delete_event, который немедленно
		# Завершает работу GTK.
		self.window_matrix_res.connect("delete_event", self.delete_event)

		# Устанавливаем границу для окна
		self.window_matrix_res.set_border_width(5)

		# Создаём таблицу 3х4
		table = gtk.Table(self.N + 1, self.N + 2, True)

		# Размещаем таблицу в главном окне
		self.window_matrix_res.add(table)

		# Создаём первую кнопку
		button = gtk.Button("ok")

		# По нажатии кнопки мы вызываем метод "callback"
		# с указателем на "ok" в виде аргумента
		button.connect("clicked", lambda w: gtk.main_quit())
		# Вставляем ok в верхнюю левую ячейку таблицы
		table.attach(button, self.N, self.N + 1, self.N + 1, self.N + 2, gtk.SHRINK, gtk.SHRINK, 1, 1)
		button.show()
		
		label = gtk.Label("Результирующая матрица")
		table.attach(label, 0, self.N +1, 0, 1)
		label.show()
		
		print self.matrix
		for i in xrange(self.N):
			for j in xrange(self.N):
				label = gtk.Label(str(self.matrix[j][i]))
				table.attach(label , i, i + 1, j +1, j +2, gtk.SHRINK, gtk.SHRINK)
				label.show()
		       
		table.show()
		self.window_matrix_res.show()
		
	def __init__(self):
		self.start_program()

def main():
	gtk.main()
	return 0		 

if __name__ == "__main__":
	Gausa()
	main()
