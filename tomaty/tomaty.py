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

POMO_MINUTES = 1
BREAK_MINUTES = 5


class Tomaty(Gtk.Window):
    def __init__(self):
        """init for main class Tomaty, runs tomaty app"""

        super(Tomaty, self).__init__(title="tomaty :: focus!")
        self.set_border_width(100)
        self.pomo_time = 10
        self.rem_time = self.pomo_time
        self.running = False

        # setup main box for labels
        self.vbox = Gtk.VBox(spacing=10)
        self.add(self.vbox)

        # make the label with timer
        self.timer_label = Gtk.Label(label="{}".format(self.rem_time))

        # add into hbox
        self.vbox.pack_start(self.timer_label, True, True, 0)

        button = Gtk.Button.new_with_label(label="start")
        button.connect("clicked", self.click_start)

        self.vbox.pack_start(button, True, True, 0)

    def click_start(self, button):
        # begin counting!
        if self.running is False:
            self.running = True
            GLib.timeout_add_seconds(1, self.count_down)

    def count_down(self):
        # check to make sure countdown is not done
        if self.rem_time == 0:
            self.timer_label.set_text(str="Pomodoro Done!")
            self.rem_time = self.pomo_time
            self.running = False
            return GLib.SOURCE_REMOVE

        self.timer_label.set_text(str="{}".format(self.tick_tock()))
        # signal to continue countdown within main loop
        return GLib.SOURCE_CONTINUE

    def tick_tock(self):
        self.rem_time = self.rem_time - 1

        return self.rem_time


def run():
    t = Tomaty()
    t.connect('delete-event', Gtk.main_quit)
    t.show_all()
    Gtk.main()
