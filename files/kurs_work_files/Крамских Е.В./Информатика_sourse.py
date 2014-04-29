# -*- coding: utf-8 -*-
import pygtk, gtk, operator,time,string
pygtk.require('2.0')

class DrawingAreaExample:
	def __init__(self):
		event_box = gtk.EventBox()
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("Пример Drawing Area")
		window.connect("destroy", lambda w: gtk.main_quit())
		window.set_default_size(800,600)
		self.X = 100
		self.Y = 110
		self.area = gtk.DrawingArea()
		self.area.set_size_request(400, 300)
		self.pangolayout = self.area.create_pango_layout("")
		self.sw = gtk.ScrolledWindow()
		self.sw.add_with_viewport(self.area)
		self.table = gtk.Table(2,2)
		self.hruler = gtk.HRuler()
		self.vruler = gtk.VRuler()
		self.hruler.set_range(0, 400, 0, 400)
		self.vruler.set_range(0, 300, 0, 300)
		self.table.attach(self.hruler, 1, 2, 0, 1, yoptions=0)
		self.table.attach(self.vruler, 0, 1, 1, 2, xoptions=0)
		self.table.attach(self.sw, 1, 2, 1, 2)
		window.add(self.table)
		self.area.set_events(gtk.gdk.POINTER_MOTION_MASK |
							gtk.gdk.POINTER_MOTION_HINT_MASK )
		self.area.connect("expose-event", self.area_expose_cb)
		window.connect('key_press_event', self.area_expose_cb)
		event_box.add(self.area)
		def motion_notify(ruler, event):
			return ruler.emit("motion_notify_event", event)
		self.area.connect_object("motion_notify_event", motion_notify,
								self.hruler)
		self.area.connect_object("motion_notify_event", motion_notify,
								self.vruler)
		self.hadj = self.sw.get_hadjustment()
		self.vadj = self.sw.get_vadjustment()
		def val_cb(adj, ruler, horiz):
			if horiz:
				span = self.sw.get_allocation()[3]
			else:
				span = self.sw.get_allocation()[2]
			l,u,p,m = ruler.get_range()
			v = adj.value
			ruler.set_range(v, v+span, p, m)
			while gtk.events_pending():
				gtk.main_iteration()
		self.hadj.connect('value-changed', val_cb, self.hruler, True)
		self.vadj.connect('value-changed', val_cb, self.vruler, False)
		def size_allocate_cb(wid, allocation):
			x, y, w, h = allocation
			l,u,p,m = self.hruler.get_range()
			m = max(m, w)
			self.hruler.set_range(l, l+w, p, m)
			l,u,p,m = self.vruler.get_range()
			m = max(m, h)
			self.vruler.set_range(l, l+h, p, m)
		self.sw.connect('size-allocate', size_allocate_cb)
		self.area.show()
		self.hruler.show()
		self.vruler.show()
		self.sw.show()
		self.table.show()
		window.show()
	
	def area_expose_cb(self, area, event):
		self.style = self.area.get_style()
		self.gc = self.style.fg_gc[gtk.STATE_NORMAL]
		self.draw_rectangles()
		key = gtk.gdk.keyval_name(event.keyval)
		if key == "Left":
			self.X = self.X - 1
			return True
		elif key == "Right":
			self.X = self.X + 1
			return True
		elif key == "Up":
			self.Y = self.Y - 1
			return True
		elif key == "Down":
			self.Y = self.Y + 1
			return True
		return True
   
	def draw_rectangles(self):
		self.area.window.draw_rectangle(self.gc, True, self.X + 20, self.Y + 50, 40, 40)
		self.area.window.draw_layout(self.gc, self.X + 5, self.Y + 80, self.pangolayout)
		return

   
def main():
   gtk.main()
   return 0

if __name__ == "__main__":
   DrawingAreaExample()
   main()
