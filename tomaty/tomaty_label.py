"""
tomaty_label.py
~~~~~~~~

label classes for the tomaty application.


As of now, nothing differentiates the two.

:copyright: @ 2018
:author: elias julian marko garcia
:license: MIT, see LICENSE
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GLib, Gdk


class TimerLabel(Gtk.Label):
    """the label object inherents from Gtk.Label and reflects the status
        of the users' tomatoro progression. """

    TOMA_RESTART_MSG = """
<span font='16'>Start Tomatoro?</span>"""

    def __init__(self,
                 label="",
                 smargin=0,
                 emargin=0,
                 tmargin=0,
                 bmargin=0,
                 justify=Gtk.Justification.CENTER):

        super(TimerLabel, self).__init__()

        self.set_markup(label)
        self.set_margin_start(smargin)
        self.set_margin_end(emargin)
        self.set_margin_top(tmargin)
        self.set_margin_bottom(bmargin)
        self.set_justify(justify)


class StatsLabel(Gtk.Label):
    def __init__(self,
                 label="",
                 smargin=0,
                 emargin=0,
                 tmargin=0,
                 bmargin=0,
                 justify=Gtk.Justification.CENTER):
        super(StatsLabel, self).__init__()
        self.set_markup(label)
        self.set_margin_start(smargin)
        self.set_margin_end(emargin)
        self.set_margin_top(tmargin)
        self.set_margin_bottom(bmargin)
        self.set_justify(justify)
