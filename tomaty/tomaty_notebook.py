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
    def __init__(self):
        super(TomatyNotebook, self).__init__()

        self.set_size_request(250, 150)


class TomatyPage(Gtk.VBox):
    def __init__(self):
        "docstring"
        super(TomatyPage, self).__init__()
        self.spacing = 0
        self.set_homogeneous(False)
