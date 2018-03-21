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


class TomatyLabel(Gtk.Label):
    def __init__(self):
        """init the TomatyLabel used for the countdown"""

        super(TomatyLabel, self).__init__("Hello")


class TomatyWindow(Gtk.Window):
    def __init__(self, args):
        """init te TomatyWindow used for the tomaty app"""

        super(TomatyWindow, self).__init__(title="Tomaty :: Focus!")
        self.set_border_width(75)
        self.hbox = Gtk.Box(spacing=10)
        self.add(self.hbox)


class Tomaty(TomatyWindow, TomatyLabel):
    def __init__(self, args):
        """init for main class of the tomaty app"""
        super(Tomaty, self).__init__()


def tomaty():
    print("Coming soon!")
