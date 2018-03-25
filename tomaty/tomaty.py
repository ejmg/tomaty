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
from gi.repository import Gtk, GObject, GLib, Gdk
from datetime import timedelta

POMO_MINUTES = 10
BREAK_MINUTES = 5

TIMER_FRMT = """
<span font='34'>{}</span>
"""

POMO_MSG = """
<span font='16'>Pomodoro Done!\nStart Break?</span>"""

BREAK_MSG = """
<span font='16'>Break Over!\nStart Pomodoro?</span>"""

POMO_RESTART_MSG = """
<span font='16'>Start Pomodoro?</span>"""

BREAK_RESTART_MSG = """
<span font='16'>Start Break?</span>"""


class Tomaty(Gtk.Window):
    def __init__(self):
        """init for main class Tomaty, runs tomaty app"""

        super(Tomaty, self).__init__(title="tomaty :: focus!")
        self.set_border_width(5)
        self.set_default_size(250, 135)
        self.set_resizable(False)
        self.set_size_request(250, 135)

        self.notebook = Gtk.Notebook()
        self.notebook.set_size_request(250, 150)

        self.add(self.notebook)

        # TODO: properly convert to minutes when no longer dev'ing
        self.pomo_time = timedelta(seconds=POMO_MINUTES)
        self.break_time = timedelta(seconds=BREAK_MINUTES)
        self.rem_time = self.pomo_time
        self.running = False
        self.break_period = False

        # setup main box for labels
        self.vbox = Gtk.VBox(spacing=0)
        self.vbox.set_homogeneous(False)

        # make the label with timer
        self.timer_label = Gtk.Label()
        self.timer_label.set_markup(TIMER_FRMT.format(str(self.rem_time)[2:]))
        # set text, not label, to center align.
        self.timer_label.set_justify(2)
        self.timer_label.set_margin_top(0)
        self.timer_label.set_margin_bottom(0)

        # add into hbox
        self.vbox.pack_start(self.timer_label, True, True, 0)

        self.button = Gtk.Button.new_with_label(label="start")
        self.button.connect("clicked", self.click_start)
        # self.button.set_border_width(50)
        self.button.set_margin_top(5)
        self.button.set_margin_bottom(5)
        self.button.set_halign(Gtk.Align.CENTER)

        self.vbox.pack_start(self.button, False, False, 0)

        self.notebook.append_page(
            child=self.vbox, tab_label=Gtk.Label(label='tomatoro'))

    def click_start(self, button):
        # begin counting!
        if self.running is False:
            self.running = True
            self.button.set_label("restart")
            if self.break_period is False:
                self.rem_time = self.pomo_time
                GLib.timeout_add_seconds(1, self.countDown)
            else:
                self.rem_time = self.break_time
                GLib.timeout_add_seconds(1, self.countDown)
        else:
            self.running = False
            self.button.set_label("start")
            if self.break_period is False:
                self.timer_label.set_markup(str=POMO_RESTART_MSG)
                self.rem_time = self.pomo_time
                GLib.SOURCE_REMOVE
            else:
                self.timer_label.set_markup(str=BREAK_RESTART_MSG)
                self.rem_time = self.break_time
                GLib.SOURCE_REMOVE

    def countDown(self):
        # check to make sure countdown is not done if it is done, then we need
        # to reset a lot of things before going forward
        if self.rem_time == timedelta(seconds=0):
            self.running = False
            self.button.set_label("start")
            if self.break_period is False:
                self.timer_label.set_markup(str=POMO_MSG)
                self.break_period = True
            else:
                self.timer_label.set_markup(str=BREAK_MSG)
                self.break_period = False

            return GLib.SOURCE_REMOVE

        if self.running is False:
            return GLib.SOURCE_REMOVE

        self.timer_label.set_markup(str=TIMER_FRMT.format(self.tickTock()))
        # signal to continue countdown within main loop
        return GLib.SOURCE_CONTINUE

    def tickTock(self):
        # TODO: change to minutes format when done dev'ing
        self.rem_time = self.rem_time - timedelta(seconds=1)

        return str(self.rem_time)[2:]


def run():
    t = Tomaty()
    t.connect('delete-event', Gtk.main_quit)
    t.show_all()
    Gtk.main()
