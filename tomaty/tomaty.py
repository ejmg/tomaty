"""
tomaty.py
~~~~~~~~

stub code for tomaty.py


TODO: everything

:copyright: @ 2018
:author: elias julian marko garcia
:license: MIT, see LICENSE
"""
import inspect
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GLib

POMO_MINUTES = 25
BREAK_MINUTES = 5


class Tomaty(Gtk.Window):
    def __init__(self):
        """init for main class Tomaty, runs tomaty app"""

        super(Tomaty, self).__init__(title="tomaty :: focus!")
        self.set_border_width(100)
        self.time = 60 * POMO_MINUTES

        # setup main box for labels
        self.vbox = Gtk.VBox(spacing=10)
        self.add(self.vbox)

        # make the label with timer
        self.timer_label = Gtk.Label(label="{}".format(self.time))

        # add into hbox
        self.vbox.pack_start(self.timer_label, True, True, 0)

        button = Gtk.Button.new_with_label(label="start")
        button.connect("clicked", self.click_start)

        self.vbox.pack_start(button, True, True, 0)

    def click_start(self, button):
        # begin counting!

        GLib.timeout_add_seconds(1, self.count_down)

    def count_down(self):
        self.timer_label.set_text(str="{}".format(self.tick_tock()))

        # signal to main loop to continue
        return GLib.SOURCE_CONTINUE

    def tick_tock(self):
        self.time = self.time - 1

        return self.time


def run():
    t = Tomaty()
    t.connect('delete-event', Gtk.main_quit)
    t.show_all()
    Gtk.main()
