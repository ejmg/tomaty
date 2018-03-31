"""
tomaty_button.py
~~~~~~~~~~~~~

button class for tomaty window application


:copyright: @ 2018
:author: elias julian marko garcia
:license: MIT, see LICENSE
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GLib, Gdk


class TomatyButton(Gtk.Button):
    def __init__(self,
                 smargin=0,
                 emargin=0,
                 tmargin=0,
                 bmargin=0,
                 halign=Gtk.Align.CENTER):
        super(TomatyButton, self).__init__()
        self.set_label("start")
        self.set_margin_start(smargin)
        self.set_margin_end(emargin)
        self.set_margin_top(tmargin)
        self.set_margin_bottom(bmargin)
        self.set_halign(halign)

    def updateButton(self):
        """updates the text of the button label"""
        if self.get_label() == "start":
            self.set_label("restart")
        else:
            self.set_label("start")
