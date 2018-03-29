"""
tomaty.py
~~~~~~~~

tomaty is a gtk based application that implements the Pomodoro technique to
help users focus better on their work and encourage healthy lifestyle habits.

This continues to be a work in progress. Expect many changes between 0.9.0dev
and 2.0.0!

:copyright: @ 2018
:author: elias julian marko garcia
:license: MIT, see LICENSE
"""

import pathlib
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GLib, Gdk
from datetime import timedelta
from simpleaudio import WaveObject
from os import path
from tomaty.tomaty_notebook import TomatyNotebook, TomatyPage
from tomaty.tomaty_label import TimerLabel, StatsLabel
from tomaty.tomaty_button import TomatyButton

TOMA_MINUTES = 25
BREAK_MINUTES = 5

TIMER_FRMT = """
<span font='34'>{}</span>
"""

TOMA_MSG = """
<span font='16'>Tomatoro Done!\nStart Break?</span>"""

BREAK_MSG = """
<span font='16'>Break Over!\nStart Tomatoro?</span>"""

TOMA_RESTART_MSG = """
<span font='16'>Start Tomatoro?</span>"""

BREAK_RESTART_MSG = """
<span font='16'>Start Break?</span>"""

COUNT = """
<span font='11'><tt>Tomatoros Completed: {}</tt></span>"""

TOTAL_TIME = """
<span font='11'><tt>Total Time: {}</tt></span>"""


class Tomaty(Gtk.Window):
    def __init__(self):
        """init for main class Tomaty, runs tomaty app"""

        super(Tomaty, self).__init__(title="tomaty :: focus!")

        # attributes
        self.set_border_width(5)
        self.set_resizable(False)
        self.tomatosCompleted = 0
        self.running = False
        self.breakPeriod = False
        self.tomaTime = timedelta(minutes=TOMA_MINUTES)
        self.breakTime = timedelta(minutes=BREAK_MINUTES)
        self.remTime = self.tomaTime
        self.tomatoroLength = self.tomaTime + self.breakTime

        # create notebook, add as main and sole child widget of window
        self.notebook = TomatyNotebook()
        self.add(self.notebook)

        # TODO: properly convert to minutes when no longer dev'ing

        # timer page setup
        self.timerPage = TomatyPage()
        self.timerLabel = TimerLabel(
            label=TIMER_FRMT.format(str(self.remTime)[2:]))
        self.timerPage.pack_start(self.timerLabel, True, True, 0)

        # start button
        self.tomatyButton = TomatyButton(tmargin=5, bmargin=5)
        self.tomatyButton.connect("clicked", self.click_start)
        self.timerPage.pack_start(self.tomatyButton, False, False, 0)
        self.notebook.append_page(
            child=self.timerPage, tab_label=Gtk.Label(label='tomatoro'))

        # statistics page setup
        self.statsPage = TomatyPage()
        self.countLabel = StatsLabel(
            label=COUNT.format(self.tomatosCompleted), smargin=10, emargin=10)

        total = str(self.tomatoroLength * self.tomatosCompleted)
        self.totalLabel = StatsLabel(
            label=TOTAL_TIME.format(total),
            emargin=25,
            justify=Gtk.Justification.LEFT)

        self.statsPage.pack_start(self.countLabel, False, False, 0)
        self.statsPage.pack_start(self.totalLabel, False, False, 0)
        self.notebook.append_page(
            child=self.statsPage, tab_label=Gtk.Label(label="stats"))

    def click_start(self, tomatyButton):
        # begin counting!
        if self.running is False:
            self.running = True
            self.tomatyButton.updateButton()
            if self.breakPeriod is False:
                self.remTime = self.tomaTime
                GLib.timeout_add_seconds(1, self.countDown)
            else:
                self.remTime = self.breakTime
                GLib.timeout_add_seconds(1, self.countDown)
        else:
            self.running = False
            self.tomatyButton.updateButton()
            if self.breakPeriod is False:
                self.timerLabel.set_markup(str=TOMA_RESTART_MSG)
                self.remTime = self.tomaTime
                GLib.SOURCE_REMOVE
            else:
                self.timerLabel.set_markup(str=BREAK_RESTART_MSG)
                self.remTime = self.breakTime
                GLib.SOURCE_REMOVE

    def countDown(self):
        # check to make sure countdown is not done if it is done, then we need
        # to reset a lot of things before going forward
        if self.remTime == timedelta(seconds=0):
            alarm()
            self.running = False
            self.tomatyButton.updateButton()
            if self.breakPeriod is False:
                self.tomatosCompleted += 1
                self.countLabel.set_markup(
                    str=COUNT.format(self.tomatosCompleted))

                total = str(self.tomatoroLength * self.tomatosCompleted)
                self.totalLabel.set_markup(str=TOTAL_TIME.format(total))
                self.timerLabel.set_markup(str=TOMA_MSG)
                self.breakPeriod = True
            else:
                self.timerLabel.set_markup(str=BREAK_MSG)
                self.breakPeriod = False

            return GLib.SOURCE_REMOVE

        if self.running is False:
            return GLib.SOURCE_REMOVE

        self.timerLabel.set_markup(str=TIMER_FRMT.format(self.tickTock()))
        # signal to continue countdown within main loop
        return GLib.SOURCE_CONTINUE

    def tickTock(self):
        # TODO: change to minutes format when done dev'ing
        self.remTime = self.remTime - timedelta(seconds=1)

        return str(self.remTime)[2:]


def alarm():

    # really need to find a cleaner, non-hack, way of getting to resources/
    resourcePath = path.join(path.split(__file__)[0], 'resources')
    alarmPath = path.join(path.join(resourcePath, 'audio'), 'alarm.wav')
    wav_obj = WaveObject.from_wave_file(alarmPath)
    wav_obj.play()


def run():
    t = Tomaty()
    t.connect('delete-event', Gtk.main_quit)
    t.show_all()
    Gtk.main()
