from gi.repository import Gtk

class MainWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="gra")

		# box
		self.box = Gtk.Box(spacing=110)
		self.add(self.box)

				# Button
		self.button = Gtk.Button(label="Click")
		self.button.connect("clicked", self.button_clicked)
		self.box.pack_start(self.button, True, True, 0)

		self.bacon = Gtk.Button(label="bacon")
		self.bacon.connect("clicked", self.bacon_clicked)
		self.box.pack_start(self.bacon, True, True, 0)


	def bacon_clicked(self, widget):

		print("you clicked bacon")

	# User clicks button
	def button_clicked(self, widget):
		print("you clicked buton")
    




   

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()