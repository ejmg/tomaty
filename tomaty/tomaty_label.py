"""
tomaty_label.py
~~~~~~~~

label class for the tomaty application

:copyright: @ 2018
:author: elias julian marko garcia
:license: MIT, see LICENSE
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GLib, Gdk


class TomatyLabel(Gtk.Label):
    """the label object inherents from Gtk.Label and reflects the status
        of the users' tomatoro progression. """

    def __init__(self,
                 label="",
                 smargin=0,
                 emargin=0,
                 tmargin=0,
                 bmargin=0,
                 justify=Gtk.Justification.CENTER):

        super(TomatyLabel, self).__init__()

        self.set_markup(label)
        self.set_margin_start(smargin)
        self.set_margin_end(emargin)
        self.set_margin_top(tmargin)
        self.set_margin_bottom(bmargin)
        self.set_justify(justify)
