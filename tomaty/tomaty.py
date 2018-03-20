"""
tomaty.py
~~~~~~~~

stub code for tomaty.py


TODO: everything

:copyright: @ 2018
:author: elias julian marko garcia
:license: MIT, see LICENSE
"""
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
        self.hbox = Gtk.Box(spacing=10)
        self.add(self.hbox)

        # make the label with timer
        self.timer_label = Gtk.Label("{}".format(self.time))

        # add into hbox
        self.hbox.pack_start(self.timer_label, True, True, 0)

        # begin counting!
        GLib.timeout_add_seconds(1, self.count_down)

    def count_down(self):
        self.timer_label.set_text("{}".format(self.tick_tock()))

        # signal to main loop to continue
        return GLib.SOURCE_CONTINUE

    def tick_tock(self):
        self.time = self.time - 1

        return self.time


def tomaty():
    t = Tomaty()
    t.connect('delete-event', Gtk.main_quit)
    t.show_all()
    Gtk.main()


if __name__ == '__main__':
    tomaty()
