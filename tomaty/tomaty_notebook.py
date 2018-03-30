"""
tomaty_notebook.py
~~~~~~~~~~~~~

notebook class for the main tomaty window application


:copyright: @ 2018
:author: elias julian marko garcia
:license: MIT, see LICENSE
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GLib, Gdk


class TomatyNotebook(Gtk.Notebook):
    def __init__(self, width=0, height=0):
        super(TomatyNotebook, self).__init__()
        self.set_size_request(width, height)


class TomatyPage(Gtk.VBox):
    def __init__(self, spacing=0, homogeneous=False):
        "docstring"
        super(TomatyPage, self).__init__()
        self.set_spacing(spacing)
        self.set_homogeneous(homogeneous)
