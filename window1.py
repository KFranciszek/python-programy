import pygtk
pygtk.require('2.0')
import gtk


window = gtk.Window()

label = gtk.Label()
label.set_label("OMG I think thenewboston is awesome!")
label.set_angle(50)
window.add(label)

print(label.get_properties("angle"))

window.connect("delete-event", gtk.main_quit) # zamykanie programu za pomoca wyjscia z okienka
window.show_all()
gtk.main()